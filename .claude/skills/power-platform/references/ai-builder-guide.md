# AI Builder Reference Guide

## Overview

AI Builder is a Power Platform capability for adding AI to apps and automations without code. Consumption is metered via AI Builder credits (add-on license).

**Workflow**: Choose model type -> Connect data -> Configure -> Train (custom only) -> Publish -> Use in apps/flows.

**Integration points**: Power Apps (canvas and model-driven), Power Automate (cloud flows), Copilot Studio (agent tools).

---

## Model Categories

### Prebuilt Models

Ready to use immediately, no training required.

| Model | Template Name | Data Type |
|---|---|---|
| Sentiment analysis | SentimentAnalysis | Text |
| Key phrase extraction | KeyPhraseExtraction | Text |
| Entity extraction | EntityExtraction | Text |
| Language detection | LanguageDetection | Text |
| Text translation | TextTranslation | Text |
| Category classification | TextClassificationV2 | Text |
| Text recognition (OCR) | TextRecognition | Documents |
| Receipt processing | ReceiptScanning | Documents |
| Invoice processing | InvoiceProcessing | Documents |
| Business card reader | BusinessCard | Documents |
| ID reader | IdentityDocument | Documents |
| Contract processing (preview) | ContractDocument | Documents |
| Image description (preview) | ImageDescription | Images |

### Custom Models

Trained on your own data, then published.

| Model | Template Name | Data Type |
|---|---|---|
| Document processing | DocumentScanning | Documents |
| Prediction | BinaryPrediction / GenericPrediction | Structured data |
| Category classification | TextClassificationV2 | Text |
| Entity extraction | EntityExtraction | Text |
| Object detection | ObjectDetection | Images |

---

## Prebuilt Models Detail

### Sentiment Analysis

Detects positive, negative, neutral, or mixed sentiment at sentence and document level. Returns label + confidence score (0-1). Supports 14 languages. Limit: 5,120 chars per document, 400 calls/60s.

### Key Phrase Extraction

Identifies main talking points from text. Returns list of key phrases. Supports 30+ languages. Limit: 5,120 chars per document, 400 calls/60s.

### Entity Extraction (Prebuilt)

Recognizes data elements: Age, Boolean, City, Color, Country/Region, Date/Time, Duration, Email, Event, Money, Number, Organization, Person name, Phone number, URL, Zip code, and more. Supports 7 languages. Limit: 5,000 chars per document.

### Text Recognition (OCR)

Extracts printed and handwritten text from images/documents. Returns text lines with bounding boxes. Print: 200+ languages. Handwritten: 9 languages. Formats: JPG, PNG, BMP, PDF (up to 2,000 pages). Max 20 MB. Limit: 480 calls/60s.

### Receipt Processing

Extracts: MerchantName, TransactionDate/Time, PurchasedItems, Subtotal, Tax, Tip, Total. Supports 100+ languages. Single-page receipts only. Max 20 MB. Limit: 360 calls/60s (shared with invoice).

**Extracted field details**:

| Field | Type | Notes |
|---|---|---|
| MerchantName | String | Store/vendor name |
| MerchantAddress | String | Full address |
| MerchantPhoneNumber | String | Contact number |
| TransactionDate | Date | Purchase date |
| TransactionTime | Time | Purchase time |
| PurchasedItems | Array | Name, quantity, price per item |
| Subtotal | Number | Pre-tax amount |
| Tax | Number | Tax amount |
| Tip | Number | Gratuity |
| Total | Number | Final amount |

Each field includes a confidence score. Use threshold of 0.7+ for automated processing; route lower-confidence results to human review.

### Invoice Processing

Extracts: CustomerName, InvoiceId, InvoiceDate, DueDate, VendorName, addresses, SubTotal, TotalTax, InvoiceTotal, line items with Amount/Description/Quantity/UnitPrice, payment details (IBAN/SWIFT). All fields include confidence scores. Supports key-value pair extraction for unlisted fields. 30+ languages. Can augment with custom model for specific layouts. Limit: 360 calls/60s.

### Business Card Reader

Extracts: Name, Company, JobTitle, Email, Phone numbers, Address, Website. English and Japanese only. Limit: 24 calls/60s.

### Other Prebuilt

- **Language detection**: Identifies language of input text.
- **Text translation**: Translates between supported languages.
- **ID reader**: Extracts from passports, driver licenses.
- **Contract processing (preview)**: Extracts clauses from contracts.
- **Image description (preview)**: Generates natural language image descriptions.

---

## Custom Models Detail

### Document Processing (Deep Dive)

Reads information from structured/semi-structured documents (invoices, tax forms, purchase orders). Minimum 5 sample documents to train. Used via form processor component (canvas apps) or document processing action (flows).

#### Layout vs Template Method

| Aspect | Template (Fixed layout) | Neural (Variable layout) |
|---|---|---|
| Document structure | Fixed positions (scanned forms) | Variable positions (different vendors) |
| Training samples needed | Minimum 5 per layout | Minimum 5, recommended 15+ |
| Field detection | Position-based | Semantic understanding |
| Best for | Single-template forms | Multi-vendor invoices, varied layouts |

#### Supported Field Types

| Type | Description | Example |
|---|---|---|
| Single-line text | Short text fields | Invoice number, name |
| Multi-line text | Paragraph blocks | Description, notes |
| Number | Numeric values | Amount, quantity |
| Date | Date values | Invoice date, due date |
| Checkbox | Selected/unselected | Approval checkbox |
| Selection mark | Radio buttons | Payment method selection |
| Signature | Presence of signature | Signed/unsigned |
| Table | Row/column structured data | Line items |

#### Table Extraction

Tables are extracted as structured collections. Each table contains rows, and each row contains cell values mapped to column headers.

Power Automate reference for table extraction:
```
Action: "Process and save information from documents"
Output path: {result}.tables[0].rows[*].cells[*].text
```

Power Fx reference for table data in canvas apps:
```
ForAll(
    FormProcessor1.Tables,
    ForAll(
        ThisRecord.Rows,
        {
            Column1: ThisRecord.Cells.Column1,
            Column2: ThisRecord.Cells.Column2
        }
    )
)
```

#### Training Requirements

- Minimum 5 documents per document type; 15-50 recommended for accuracy.
- Documents must be PDF, JPG, PNG, or BMP format.
- Max file size: 20 MB per document.
- For PDFs: up to 2,000 pages supported.
- Tag at least one instance of each field across your training set.
- For tables: tag at least 2 rows per table across documents.
- Use consistent labeling; avoid overlapping field boundaries.

### Prediction

Analyzes historical data patterns to predict outcomes. Data source: Dataverse tables.

| Type | Description | Example |
|---|---|---|
| Binary | Two outcomes (yes/no) | Is this transaction fraudulent? |
| Multiple outcome | More than two outcomes | Early/on-time/late shipment? |
| Numerical | Answer is a number | Days until arrival? |

**Training requirements for prediction models**:
- Minimum 50 rows with outcome values; recommended 1,000+ for reliable results.
- At least 10 rows per outcome category for classification models.
- Data must be in a Dataverse table with a target column (the value to predict).
- Historical data quality directly impacts model accuracy.
- Avoid columns that leak future information into training data.

**Performance metrics returned after training**:
- **Accuracy**: Percentage of correct predictions on test data.
- **Precision/Recall**: Per-class metrics for classification models.
- **Feature importance**: Ranked list of columns most influencing predictions.

### Category Classification (Custom)

Classifies text into business-specific categories. Learns from labeled text in Dataverse. Use cases: spam detection, request routing.

### Entity Extraction (Custom)

Recognizes business-specific entities beyond prebuilt types. Requires labeled training data with custom entity definitions.

### Object Detection (Deep Dive)

Detects custom objects in images. Use cases: inventory management, equipment identification, shelf auditing. Requires labeled images with bounding boxes.

#### Image Requirements

| Requirement | Value |
|---|---|
| Minimum images | 15 per object tag |
| Recommended images | 50+ per object tag for accuracy |
| Supported formats | JPG, PNG, BMP |
| Min resolution | 256 x 256 pixels |
| Max file size | 6 MB per image |
| Objects per image | Multiple objects can be tagged |
| Max tags per model | 500 distinct object tags |

#### Training Labels

- Each image must have at least one bounding box drawn around a target object.
- Bounding boxes should tightly fit the object without excessive padding.
- Include variety: different angles, lighting, backgrounds, sizes.
- Tag each object instance separately (if 3 items appear, draw 3 boxes).
- Minimum 15 tagged instances per object type across all images.

#### Confidence Thresholds for Object Detection

| Threshold | Use Case |
|---|---|
| 0.9+ | High-precision scenarios (safety, compliance) |
| 0.7 - 0.9 | Standard detection (inventory counting) |
| 0.5 - 0.7 | Exploratory / flagging for review |
| Below 0.5 | Generally discard or send to human review |

Power Fx for object detection in canvas apps:
```
// Display detected objects above threshold
Filter(
    ObjectDetector1.GroupedResults,
    Confidence >= 0.7
)

// Count specific objects
CountRows(
    Filter(
        ObjectDetector1.Results,
        TagName = "ProductA" && Confidence >= 0.7
    )
)
```

---

## AI Prompts (Prompt Builder)

Reusable generative AI prompts powered by Azure OpenAI (GPT-4o / GPT-4o mini). Managed through Copilot Studio.

**Core concepts**: Instruction (what to do) + Context (information needed) + Input variables (dynamic content) + Knowledge objects (Dataverse data).

**Creation workflow**: AI hub -> Prompts -> Build your own prompt -> Write instruction -> Add input variables with `/` -> Attach knowledge source -> Test -> Save.

**Power Automate actions**: "Create text with GPT using a prompt" (GPT-4o or GPT-4o mini).

**Power Apps usage**: Add AI model as data source, bind to control event:
```
Set(TextCompletionResult, 'Create text with GPT'.Predict(TextInput1.Text));
```

Supports 21 languages including English, French, German, Spanish, Japanese, Chinese, Arabic, Korean.

### Custom Prompts Deep Dive

#### Prompt Engineering Best Practices

1. **Be specific with instructions**: Instead of "summarize this", use "summarize the following customer complaint in 2-3 sentences, highlighting the main issue and desired resolution."
2. **Define output format**: Specify whether you want JSON, bullet points, a table, or plain text. Example: "Return the result as a JSON object with keys: category, urgency, summary."
3. **Provide examples (few-shot)**: Include 1-3 examples of input/output pairs directly in the prompt instruction to guide the model.
4. **Set constraints**: Define what the model should NOT do. Example: "Do not include personal opinions. Only use information from the provided context."
5. **Use system-level framing**: Start with a role definition. Example: "You are a customer service analyst who classifies support tickets."

#### Input Variables

Input variables make prompts reusable by injecting dynamic content at runtime.

**Defining variables**: In the prompt editor, type `/` to insert a variable placeholder. Name variables descriptively (e.g., `/CustomerEmail`, `/OrderDetails`).

**Variable types**:
- **Text**: Free-form string input (default).
- **Number**: Numeric values passed as text.
- **File**: Document or image content (for multimodal prompts).

**Example prompt with variables**:
```
Classify the following support ticket into one of these categories:
Billing, Technical, Shipping, General Inquiry.

Ticket subject: /TicketSubject
Ticket body: /TicketBody
Customer tier: /CustomerTier

Return a JSON object with: category, priority (1-5), suggestedResponse
```

#### Knowledge Grounding

Knowledge sources let prompts reference your organization's data stored in Dataverse.

**Supported knowledge sources**:
- Dataverse tables (structured data)
- Dataverse file columns (uploaded documents)
- SharePoint sites (document libraries)

**How grounding works**: The prompt engine retrieves relevant chunks from your knowledge source and includes them as context alongside the user instruction. This is a form of RAG (Retrieval-Augmented Generation).

**Configuration**: In the prompt editor, select "Add knowledge" -> Choose source -> Select table/site -> Map columns for search/retrieval.

#### Testing Prompts

- Use the **Test** panel in the prompt editor to run prompts with sample inputs before saving.
- Check output quality, format adherence, and edge cases.
- Test with varied input lengths and languages if your prompt must handle multilingual content.
- Monitor token usage in the test panel to estimate credit consumption.

#### Prompt Versioning

- Each save creates a new version of the prompt.
- Published prompts are referenced by apps/flows; updating requires re-publishing.
- Use descriptive prompt names with version indicators for tracking (e.g., "TicketClassifier_v2").
- Roll back by re-publishing a previous version from the version history.

---

## Using AI Builder in Power Apps

### Power Fx Formula Bar (Preview)

Models callable directly via Power Fx: Sentiment analysis, Entity extraction, Key phrase extraction, Language detection, Category classification.

**Sentiment analysis example**:
```
Set(
    SentimentResult,
    AIBuilder.SentimentAnalysis(TextInput1.Text)
);
// Access: SentimentResult.sentiment, SentimentResult.confidenceScores
```

**Entity extraction example**:
```
Set(
    Entities,
    AIBuilder.EntityExtraction(TextInput1.Text)
);
// Returns collection of {category, text, confidenceScore}
```

### Canvas App Components

**Prebuilt**: Business card reader, Receipt processor, Text recognizer.
**Custom**: Form processor (document processing), Object detector.

### Component Properties

| Component | Property | Format |
|---|---|---|
| Form processor | Fields | `{Control}.Fields` |
| Form processor | Tables | `{Control}.Tables` |
| Form processor | Confidence | `{Control}.Fields.{FieldName}.Confidence` |
| Text recognizer | Selected text | `{Control}.Selected.Text` |
| Text recognizer | All results | `{Control}.Results.Text` |
| Object detector | Tag info | `{Control}.GroupedResults.TagId/TagName/ObjectCount` |
| Object detector | Per-result | `{Control}.Results.TagName/Confidence/BoundingBox` |

### Model-Driven App Integration

In model-driven apps, AI Builder models are used through:
- **Embedded canvas apps**: Insert a canvas app with AI Builder components into a model-driven form.
- **Business process flows**: Trigger AI Builder actions at specific stages.
- **Custom pages**: Build custom pages with AI Builder controls within model-driven apps.

---

## Using AI Builder in Power Automate

### Prebuilt Actions

- Analyze positive or negative sentiment in text
- Classify text into categories with standard model
- Create text with GPT using a prompt (GPT-4o / GPT-4o mini)
- Detect the language being used in the text
- Extract entities from text with standard model
- Extract information from business cards / invoices / receipts / identity documents / documents
- Generate key phrases from text
- Generate description of an image (preview)
- Predict by field / by record ID
- Recognize text in an image or PDF
- Translate text into another language

### Custom Model Actions

- Classify text with custom category classification model
- Extract entities with custom entity extraction model
- Process documents with custom document processing model
- Detect objects with custom object detection model
- Predict with custom prediction model

### Configuration

Always leave **Asynchronous Pattern** set to **On** for AI Builder actions in cloud flows. Use the **Predict** action for generic model invocation.

### Error Handling for AI Builder Actions

AI Builder actions can fail due to rate limits, service outages, or invalid input. Implement defensive patterns:

1. **Configure run-after on failed actions**: Set downstream actions to run after the AI Builder action even if it fails.
2. **Use Scope blocks**: Wrap AI Builder calls in a Scope, then add a parallel Scope that runs on failure.
3. **Retry policy**: Set retry policy to "Fixed interval" with 3 retries at 30-second intervals for transient failures.
4. **Input validation**: Check file size and format before sending to AI Builder to avoid wasting credits on guaranteed failures.

Example pattern:
```
Scope: "AI Processing"
  ├── Action: "Extract information from invoices"
  └── Action: "Create Dataverse row" (run after: succeeded)

Scope: "Error Handling" (run after: "AI Processing" has failed)
  ├── Action: "Create Dataverse row" (error log)
  └── Action: "Send email notification"
```

---

## Document Automation Pipeline

End-to-end pattern for processing documents at scale using AI Builder in Power Automate.

### Pipeline Architecture

```
Trigger (new document arrives)
  → Pre-validate (file type, size)
  → Extract with AI Builder
  → Evaluate confidence scores
  → Branch: High confidence → auto-process
  → Branch: Low confidence → human review queue
  → Store results in Dataverse
  → Archive source document
```

### Step-by-Step Flow Design

**1. Trigger**: Use "When a file is created" (SharePoint), "When a new email arrives" (Outlook), or "When a row is added" (Dataverse) depending on document source.

**2. Pre-validation**:
```
Condition: File size <= 20 MB AND file extension in [pdf, jpg, png, bmp]
  Yes → Continue to extraction
  No → Log error, notify sender
```

**3. Extraction**: Use the appropriate AI Builder action:
- Invoices: "Extract information from invoices"
- Receipts: "Extract information from receipts"
- Custom forms: "Process and save information from documents" (select custom model)

**4. Confidence Score Evaluation**:
```
Condition: Minimum field confidence >= 0.8
  Yes → Auto-process (create Dataverse record)
  No → Route to review queue
```

**5. Human-in-the-Loop Pattern**:
- Create an approval request using the Approvals connector.
- Include extracted data and the original document as attachments.
- Display low-confidence fields highlighted for reviewer attention.
- On approval, update the Dataverse record with reviewer corrections.
- Feed corrections back to retrain custom models periodically.

**6. Store Results**:
```
Action: "Create a new row" in Dataverse
  Table: ProcessedDocuments
  Fields mapped from AI Builder output:
    - VendorName: outputs('Extract_Invoice')?['body/responsev2/predictionOutput/result/fields/VendorName/value']
    - InvoiceTotal: outputs('Extract_Invoice')?['body/responsev2/predictionOutput/result/fields/InvoiceTotal/value']
    - ConfidenceScore: outputs('Extract_Invoice')?['body/responsev2/predictionOutput/result/fields/InvoiceTotal/confidence']
```

### Batch Processing

For bulk document processing, use a combination of:
1. Scheduled flow that queries a SharePoint folder or Dataverse table for unprocessed documents.
2. "Apply to each" loop with concurrency set to 1 (to respect rate limits).
3. Delay action between iterations if approaching rate limits (360 calls/60s for invoice/receipt).

---

## Confidence Scores

### Interpreting Scores per Model Type

Every AI Builder model returns confidence scores (0.0 to 1.0) indicating the model's certainty about its prediction.

| Model Type | Score Meaning | Typical Range |
|---|---|---|
| Sentiment analysis | Certainty of detected sentiment | 0.6 - 1.0 |
| Entity extraction | Certainty an entity was correctly identified | 0.5 - 1.0 |
| Document processing | Per-field extraction confidence | 0.3 - 1.0 (varies by field clarity) |
| Invoice/Receipt | Per-field extraction confidence | 0.7 - 1.0 (printed text) |
| Object detection | Certainty an object was correctly identified and located | 0.1 - 1.0 |
| Prediction | Probability of predicted outcome | 0.5 - 1.0 |
| Category classification | Certainty of assigned category | 0.4 - 1.0 |

### Threshold Recommendations

| Scenario | Recommended Threshold | Rationale |
|---|---|---|
| Financial data (amounts, totals) | 0.90+ | Errors have monetary impact |
| Identity fields (names, IDs) | 0.85+ | Must be accurate for compliance |
| General text extraction | 0.70+ | Acceptable for informational use |
| Categorization/routing | 0.65+ | Moderate impact if misrouted |
| Exploratory/analytics | 0.50+ | Low stakes, reviewing trends |

### Fallback Strategies

When confidence falls below threshold:

1. **Human review queue**: Route to a manual review task (Approvals connector or custom Dataverse queue).
2. **Secondary model**: Try an alternative model (e.g., custom document model when prebuilt invoice model gives low confidence).
3. **Field-level fallback**: Accept high-confidence fields, flag only low-confidence fields for review.
4. **Reject and notify**: Return document to sender with request for clearer image/scan.

Example Power Automate expression for field-level confidence check:
```
if(
  greater(
    outputs('Extract_Invoice')?['body/responsev2/predictionOutput/result/fields/InvoiceTotal/confidence'],
    0.85
  ),
  outputs('Extract_Invoice')?['body/responsev2/predictionOutput/result/fields/InvoiceTotal/value'],
  'NEEDS_REVIEW'
)
```

---

## Model Lifecycle Management

### Training

1. **Prepare data**: Collect and label training samples in the required format.
2. **Create model**: AI Builder > Explore > Select model type > Configure.
3. **Upload training data**: Provide labeled documents/images/text or select Dataverse table.
4. **Tag/label**: For document and object detection models, tag fields or draw bounding boxes in the labeling UI.
5. **Train**: Click "Train" to start model training. Training time varies by model type and data volume (minutes to hours).

### Publishing

- After training completes, review the model performance summary.
- Click "Publish" to make the model available for use in apps and flows.
- Only published models can be referenced in production apps and flows.
- Publishing creates a snapshot; the model continues to serve this version until re-published.

### Versioning

- Each publish creates a new version of the model.
- Apps and flows reference the latest published version automatically.
- Previous versions are retained and can be viewed in the model's version history.
- To roll back: re-train with previous training data and re-publish, or use solution export/import for version management.

### Retraining Schedules

| Trigger | Action |
|---|---|
| Accuracy drift detected | Retrain with updated data |
| New document layouts appear | Add samples of new layouts, retrain |
| Quarterly review | Evaluate model metrics, retrain if accuracy drops below target |
| Business process change | Update labels/categories, retrain |
| After significant data correction | Incorporate corrected data into training set |

**Monitoring performance**:
- Track extraction accuracy by comparing AI Builder output to verified human-reviewed values.
- Log confidence score distributions over time; a downward trend indicates model drift.
- Use Power BI dashboards connected to your Dataverse logging table to visualize trends.
- Set up alerts when average confidence drops below your threshold.

### Model Status Lifecycle

```
Draft → Training → Trained → Published → (Retrain cycle)
                      ↓
                  Training Failed (review data quality)
```

---

## Administration

### AI Builder Credits

AI Builder consumption is metered using credits. Each action consumes a specific number of credits.

**Credit consumption per action (approximate)**:

| Action | Credits per Call |
|---|---|
| Prebuilt text models (sentiment, entities, etc.) | 1 |
| Text recognition (OCR) | 1 per page |
| Invoice processing | 1 per page |
| Receipt processing | 1 |
| Business card reader | 1 |
| Document processing (custom) | 1 per page |
| Object detection | 1 |
| Prediction | 1 |
| AI Prompts (GPT) | Varies by token usage |

**Credit allocation**:
- Credits are pooled at the tenant level and shared across all environments.
- Purchased via AI Builder add-on capacity packs (per-user or per-app licensing).
- Trial environments get a limited credit allocation.
- Credits refresh monthly.

### Capacity Management

**Checking credit usage**: Power Platform admin center > Resources > Capacity > AI Builder.

**Usage monitoring**:
- View consumption by environment, model type, and time period.
- Set up notifications when approaching capacity limits.
- Allocate credits to specific environments if needed.

**Overage behavior**: When credits are exhausted, AI Builder actions in flows will fail with a capacity error. Prebuilt models in apps may continue to work in limited capacity (grace period behavior varies).

### Environment Settings

Admins can control AI Builder at the environment level:

**Enable/Disable AI Builder per environment**:
1. Go to Power Platform admin center.
2. Select the environment.
3. Settings > Features.
4. Toggle "AI Builder" on or off.

**Restrict model creation**: Use security roles to control who can create, train, and publish models.

| Security Role | Permissions |
|---|---|
| System Administrator | Full access to all AI Builder features |
| Environment Maker | Create and manage own models |
| AI Builder (custom role) | Configurable per-model-type access |
| Basic User | Use published models only (in apps/flows) |

### Data Loss Prevention (DLP) Policies

AI Builder connectors can be categorized in DLP policies:
- Group AI Builder actions as "Business" or "Non-business" data.
- Block AI Builder usage in specific environments via DLP.
- The "AI Builder" connector appears in DLP policy configuration alongside other connectors.

### Disabling AI Builder Tenant-Wide

To disable AI Builder across the entire tenant:
1. Power Platform admin center > Settings > Tenant settings.
2. Turn off "Allow users to create AI Builder models."
3. This prevents new model creation but does not delete existing models.
4. Published models continue to function until manually unpublished.

---

## Advanced Integration Patterns

### Multi-Model Chains

Chain multiple AI Builder models in sequence for complex processing.

**Example: Intelligent Email Processing**
```
1. Trigger: "When a new email arrives"
2. Language Detection → determine email language
3. Text Translation → translate to English if needed
4. Sentiment Analysis → classify urgency
5. Entity Extraction → pull dates, amounts, names
6. AI Prompt (GPT) → generate suggested response
7. Category Classification → route to correct team
8. Create Dataverse row with all extracted intelligence
```

**Example: Document Intelligence Pipeline**
```
1. Trigger: "When a file is created in SharePoint"
2. Condition: Check file type
   - PDF/Image → Invoice Processing (prebuilt)
   - If confidence < 0.7 → Custom Document Processing model
3. Entity Extraction on extracted text for additional data points
4. AI Prompt → summarize document contents
5. Prediction model → predict approval likelihood
6. Create Dataverse row + attach original document
```

### AI Builder + Power Automate + Dataverse Patterns

**Pattern: Enriched Data Entry**
- User creates a Dataverse row (e.g., new Contact).
- Automated flow triggers on row creation.
- AI Builder extracts entities from the "Notes" field.
- Flow updates the row with extracted phone, email, address.

**Pattern: Continuous Document Processing**
- SharePoint document library receives documents throughout the day.
- Scheduled flow runs every 15 minutes.
- Queries for unprocessed files (status column = "New").
- Processes each file with AI Builder, updates status to "Processed" or "Review Needed."
- Dataverse table stores extraction results linked to the source file.

**Pattern: Feedback Loop for Model Improvement**
- AI Builder extracts data, stores results with confidence scores.
- Low-confidence items go to human review (model-driven app).
- Reviewer corrects values, marks as "Verified."
- Monthly process: export verified corrections as new training data.
- Retrain custom model with augmented dataset.

### Power Fx + AI Builder Combined Patterns

**In-app document scanner with validation**:
```
// Trigger extraction
Set(InvoiceData, FormProcessor1.Fields);

// Validate confidence
If(
    InvoiceData.InvoiceTotal.Confidence >= 0.85,
    // Auto-accept
    Patch(
        Invoices,
        Defaults(Invoices),
        {
            VendorName: InvoiceData.VendorName.Value,
            Total: Value(InvoiceData.InvoiceTotal.Value),
            Status: "Auto-Approved"
        }
    ),
    // Flag for review
    Patch(
        Invoices,
        Defaults(Invoices),
        {
            VendorName: InvoiceData.VendorName.Value,
            Total: Value(InvoiceData.InvoiceTotal.Value),
            Status: "Needs Review",
            ConfidenceFlag: "Low confidence on total"
        }
    )
);
```

**Sentiment-driven UI**:
```
// Change UI based on detected sentiment
Set(
    CustomerSentiment,
    AIBuilder.SentimentAnalysis(CustomerMessage.Text)
);

// Dynamic styling
If(
    CustomerSentiment.sentiment = "negative",
    Set(UrgencyColor, Color.Red),
    CustomerSentiment.sentiment = "positive",
    Set(UrgencyColor, Color.Green),
    Set(UrgencyColor, Color.Gray)
);
```

---

## Rate Limits

| Model Group | Calls/Environment | Period |
|---|---|---|
| Receipt + Invoice processing | 360 | 60 seconds |
| Language detection + Sentiment + Key phrase | 400 | 60 seconds |
| Text recognition (OCR) | 480 | 60 seconds |
| Business card reader | 24 | 60 seconds |
| AI Prompts (GPT) | Varies by model/token | Per minute |
| Custom document processing | 360 | 60 seconds |
| Object detection | 480 | 60 seconds |

**Rate limit handling in flows**:
- Use "Delay" actions between iterations when processing batches.
- Set concurrency control on "Apply to each" loops (limit to 1-5 concurrent iterations).
- Implement exponential backoff: if action fails with 429, wait 30s, retry, then 60s, then 120s.
- Distribute processing across off-peak hours for large batches.

---

## Common Patterns

**Document automation**: Trigger on new document -> Extract with AI Builder -> Check confidence (~0.65 threshold) -> Fall back to custom model if low -> Save to Dataverse.

**Multi-model fallback**: Prebuilt invoice model as primary; custom document model for specific layouts when confidence is low.

**Text analytics flow**: New email -> Sentiment analysis (route negative to escalation) -> Key phrase extraction (tag/categorize) -> Entity extraction (dates, amounts, organizations).

**AI prompts in automation**: Create reusable prompt with variables -> Use "Create text with GPT" action -> Pass dynamic content -> Use output for summarization, classification, or response generation.

**Hybrid human-AI processing**: AI Builder processes documents automatically -> Low-confidence results enter approval queue -> Human reviewer corrects and approves -> Corrections feed back into model retraining pipeline.

**Cross-environment deployment**: Export AI Builder models as part of a solution -> Import to target environment -> Re-publish models -> Verify credit allocation in target environment.

---

## Quick Reference: Action Names in Power Automate

| Scenario | Action Name |
|---|---|
| Extract invoice data | Extract information from invoices |
| Extract receipt data | Extract information from receipts |
| Process custom form | Process and save information from documents |
| Analyze sentiment | Analyze positive or negative sentiment in text |
| Extract entities | Extract entities from text with standard model |
| Detect language | Detect the language being used in the text |
| Translate text | Translate text into another language |
| OCR | Recognize text in an image or a PDF document |
| Generate text (GPT) | Create text with GPT using a prompt |
| Detect objects | Detect and count objects in images |
| Classify text | Classify text into categories with one of the standard models |
| Read business card | Extract information from business cards |
| Read ID document | Extract information from identity documents |
