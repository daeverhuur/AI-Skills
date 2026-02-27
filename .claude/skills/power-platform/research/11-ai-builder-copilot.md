# 11 - AI Builder & Copilot Features

> Research from Microsoft Learn documentation (learn.microsoft.com/en-us/ai-builder/ and related Power Platform docs).

---

## 1. AI Builder Overview

AI Builder is a Microsoft Power Platform capability that lets makers add AI to apps and automations without writing code or managing ML infrastructure. It provides two categories of models:

- **Prebuilt models** -- ready to use immediately, no training required, common business scenarios.
- **Custom models** -- you supply your own data, train the model, then publish it.

**Integration points**: Power Apps (canvas & model-driven), Power Automate (cloud flows), Copilot Studio (agent tools).

**Licensing**: AI Builder is an add-on to Power Apps/Power Automate licenses. Consumption is metered via AI Builder credits.

**Workflow**: Choose model type -> Connect data -> Tailor/configure -> Train (custom only) -> Publish -> Use in apps/flows.

---

## 2. Complete Model Type Reference

| Data Type | Model | Build Type | Template Name |
|---|---|---|---|
| Documents | Business card reader | Prebuilt | BusinessCard |
| Documents | Document processing | Custom | DocumentScanning |
| Documents | Text recognition (OCR) | Prebuilt | TextRecognition |
| Documents | Receipt processing | Prebuilt | ReceiptScanning |
| Documents | Invoice processing | Prebuilt | InvoiceProcessing |
| Documents | ID reader | Prebuilt | IdentityDocument |
| Documents | Contract processing (preview) | Prebuilt | ContractDocument |
| Text | Text generation (preview, deprecated) | Prebuilt | GptPowerPrompt |
| Text | Category classification | Prebuilt + Custom | TextClassificationV2 |
| Text | Entity extraction | Prebuilt + Custom | EntityExtraction |
| Text | Key phrase extraction | Prebuilt | KeyPhraseExtraction |
| Text | Language detection | Prebuilt | LanguageDetection |
| Text | Sentiment analysis | Prebuilt | SentimentAnalysis |
| Text | Text translation | Prebuilt | TextTranslation |
| Structured data | Prediction | Custom | BinaryPrediction / GenericPrediction |
| Images | Object detection | Custom | ObjectDetection |
| Images | Image description (preview) | Prebuilt | ImageDescription |

---

## 3. Prebuilt Models -- Detail

### 3.1 Sentiment Analysis

Detects positive, negative, neutral, or mixed sentiment at both sentence and document level.

- **Output**: Sentiment label + confidence score (0-1) per sentence and per document.
- **Languages**: German, Spanish, English, French, Hindi, Italian, Japanese, Korean, Dutch, Norwegian, Portuguese (BR/PT), Turkish, Chinese (Simplified/Traditional).
- **Limit**: 5,120 characters per document; 400 calls/60s per environment (shared with language detection and key phrase extraction).

### 3.2 Key Phrase Extraction

Identifies main talking points from unstructured text.

- **Output**: List of key phrases (strings).
- **Languages**: 30+ languages including English, French, German, Japanese, Korean, Chinese, Spanish, Portuguese, and more.
- **Limit**: 5,120 characters per document; 400 calls/60s per environment.

### 3.3 Entity Extraction (Prebuilt)

Recognizes and classifies specific data elements in text.

- **Supported entity types**: Age, Boolean, City, Color, Continent, Country/Region, Date/Time, Duration, Email, Event, Language, Money, Number, Ordinal, Organization, Percentage, Person name, Phone number, Speed, State, Street address, Temperature, URL, Weight, Zip code.
- **Languages**: English, Chinese-Simplified, French, German, Portuguese, Italian, Spanish.
- **Limit**: 5,000 characters per document.

### 3.4 Text Recognition (OCR)

Extracts printed and handwritten text from images and documents using state-of-the-art OCR.

- **Output**: List of detected text lines with bounding box coordinates.
- **Print text**: 200+ languages/scripts supported.
- **Handwritten text**: English, Chinese (Simplified), French, German, Italian, Japanese, Korean, Portuguese, Spanish.
- **Formats**: JPG, PNG, BMP, PDF (first 2,000 pages).
- **Size**: 20 MB max.
- **Limit**: 480 calls/60s per environment.

### 3.5 Receipt Processing

Extracts key data from sales receipts using OCR.

- **Output fields**: MerchantName, MerchantAddress, MerchantPhone, TransactionDate, TransactionTime, PurchasedItems (Name/Price/Quantity/TotalPrice), Subtotal, TaxDetails, Tip, Total, DetectedText, CountryRegion, ReceiptType.
- **Languages**: 100+ languages supported.
- **Formats**: JPEG, PNG, PDF; max 20 MB; 50x50 to 10,000x10,000 px.
- **Limit**: Single-page receipts only; 360 calls/60s per environment (shared with invoice processing).

### 3.6 Invoice Processing

Extracts key data from invoices with extensive field support.

- **Output fields**: CustomerName, CustomerId, PurchaseOrder, InvoiceId, InvoiceDate, DueDate, VendorName, VendorAddress, CustomerAddress, BillingAddress, ShippingAddress, SubTotal, TotalDiscount, TotalTax, InvoiceTotal, AmountDue, PreviousUnpaidBalance, RemittanceAddress, ServiceAddress, ServiceStartDate, ServiceEndDate, VendorTaxId, CustomerTaxId, PaymentTerm, KVKNumber, PaymentDetails (IBAN/SWIFT/BankAccountNumber), TaxDetails, Items (Amount/Date/Description/Quantity/ProductCode/Tax/UnitPrice).
- **All fields include confidence scores.**
- **Key-value pair extraction** for additional unlisted fields.
- **Languages**: 30+ languages.
- **Formats**: JPEG, PNG, PDF; max 20 MB; PDF up to 2,000 pages.
- **Limit**: 360 calls/60s per environment.
- **Customization**: Can augment with custom Invoices model to add fields or improve extraction for specific invoice layouts.

### 3.7 Business Card Reader

Extracts contact information from business card images.

- **Output fields**: FirstName, LastName, FullName, CompanyName, Department, JobTitle, Email, BusinessPhone, MobilePhone, Fax, FullAddress, AddressStreet/City/State/PostalCode/Country, Website, OriginalImage.
- **Languages**: English and Japanese only.
- **Formats**: JPG, PNG, BMP, PDF; max 50 MB.
- **Limit**: 24 calls/60s per environment.

### 3.8 Other Prebuilt Models

- **Language detection**: Identifies the language of input text.
- **Text translation**: Translates text between supported languages.
- **ID reader**: Extracts data from identity documents (passports, driver licenses).
- **Contract processing (preview)**: Extracts clauses and data points from contracts.
- **Image description (preview)**: Generates natural language descriptions of images.
- **Category classification (prebuilt, preview)**: Classifies text into predefined categories.

---

## 4. Custom Models -- Detail

### 4.1 Document Processing (formerly Form Processing)

Reads and saves information from structured/semi-structured documents.

- **Training**: Minimum 5 sample documents to get started.
- **Capabilities**: Extract fields and tables from invoices, tax forms, purchase orders, etc.
- **Workflow**: Train -> Publish -> Use in Power Automate cloud flows or Power Apps canvas apps.
- **Component**: Form processor component for canvas apps; document processing action for flows.

### 4.2 Prediction

Analyzes historical data patterns to predict future outcomes. Three prediction types:

| Type | Description | Example |
|---|---|---|
| Binary | Two possible outcomes (yes/no) | Is this transaction fraudulent? |
| Multiple outcome | More than two outcomes | Will shipment arrive early/on-time/late/very late? |
| Numerical | Answer is a number | How many days until shipment arrives? |

- **Data source**: Microsoft Dataverse tables with historical data.
- **Training**: Automatic; AI Builder learns patterns from historical outcomes.

### 4.3 Category Classification (Custom)

Classifies unstructured text into business-specific categories.

- **Use cases**: Sentiment analysis, spam detection, customer request routing.
- **Data**: Learns from previously labeled text items in Dataverse.
- **Output**: Tags/categories applied to new text entries.

### 4.4 Entity Extraction (Custom)

Recognizes business-specific data elements in text beyond the prebuilt entity types.

- **Training**: Requires labeled training data with custom entity definitions.
- **Output**: Extracted entities classified into your custom categories.

### 4.5 Object Detection

Detects and identifies custom objects in images.

- **Use cases**: Inventory management (retail), equipment identification (manufacturing), shelf auditing.
- **Training**: Requires labeled images with bounding boxes around target objects.
- **Integration**: Object detector component in Power Apps; object detection action in Power Automate.

---

## 5. AI Prompts (Prompt Builder)

Prompt builder (now managed through Copilot Studio) lets makers create reusable generative AI prompts powered by Azure OpenAI models.

### 5.1 Core Concepts

- A **prompt** is a natural language instruction telling a generative AI model to perform a task.
- Prompts consist of two parts: the **instruction** (what to do) and the **context** (information needed).
- **Input variables** allow dynamic content to be injected at runtime.
- **Knowledge objects** connect prompts to business data from Dataverse or other sources.

### 5.2 Supported Languages

Arabic, Chinese (Simplified), Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Italian, Japanese, Korean, Polish, Portuguese (Brazil), Russian, Spanish, Swedish, Thai, Turkish.

### 5.3 Prompt Creation Workflow

1. Sign in to Power Apps, Power Automate, or Copilot Studio.
2. Navigate to AI hub -> Prompts -> Build your own prompt.
3. Write the prompt instruction or choose from the prompt template library.
4. Add input variables (text or image/document) using `/` or the Add content button.
5. Optionally attach a knowledge source (Dataverse data).
6. Enter sample values and select Test to validate.
7. Save and use in flows, apps, or Copilot Studio agents.

### 5.4 Usage in Power Automate

Power Automate actions for prompts:
- **Create text with GPT using a prompt** (GPT-4o mini)
- **Create text with GPT using a prompt** (GPT-4o)

### 5.5 Text Generation in Power Apps (Preview)

- Add the AI model as a data source in canvas app (Data -> Add data -> AI models).
- Bind model prediction to a control event using Power Fx:
  ```
  Set(TextCompletionResult, 'Create text with GPT'.Predict(TextInput1.Text));
  ```
- Currently only available in US region.

---

## 6. AI Builder in Power Apps

### 6.1 Power Fx Formula Bar Integration (Preview)

Models usable directly via Power Fx expressions:

| Model | Build Type |
|---|---|
| Sentiment analysis | Prebuilt |
| Entity extraction | Prebuilt + Custom |
| Key phrase extraction | Prebuilt |
| Language detection | Prebuilt |
| Category classification | Prebuilt + Custom |

### 6.2 Canvas App Components

**Prebuilt model components** (Insert tab in Power Apps Studio):
- Business card reader (canvas + model-driven)
- Receipt processor
- Text recognizer

**Custom model components**:
- Form processor (document processing)
- Object detector

### 6.3 Component Property Names

| Component | Property | Format |
|---|---|---|
| Form processor | Fields | `{Control}.Fields` |
| Form processor | Tables | `{Control}.Tables` |
| Text recognizer | Selected text | `{Control}.Selected.Text` |
| Text recognizer | All results | `{Control}.Results.Text` |
| Object detector | Tag info | `{Control}.GroupedResults.TagId/TagName/ObjectCount` |

---

## 7. AI Builder in Power Automate

### 7.1 Available Prebuilt Actions

| Action Name | Capability |
|---|---|
| Analyze positive or negative sentiment in text | Sentiment analysis |
| Classify text into categories with standard model | Category classification |
| Create text with GPT using a prompt | AI prompts (GPT-4o / GPT-4o mini) |
| Detect the language being used in the text | Language detection |
| Extract entities from text with standard model | Entity extraction |
| Extract information from business cards | Business card analysis |
| Extract information from documents | Document processing |
| Extract information from identity documents | ID document analysis |
| Extract information from invoices | Invoice processing |
| Extract information from receipts | Receipt processing |
| Generate the key phrases from a text | Key phrase extraction |
| Generate description of an image | Image description (preview) |
| Predict by field / by record ID | Prediction |
| Recognize text in an image or PDF | Text recognition |
| Translate text into another language | Text translation |

### 7.2 Custom Model Actions

- Classify text with custom category classification model
- Extract entities with custom entity extraction model
- Process documents with custom document processing model
- Detect objects with custom object detection model
- Predict with custom prediction model

### 7.3 Important Configuration

- Always leave the **Asynchronous Pattern** setting to **On** for any AI Builder action in a cloud flow.
- Use the **Predict** action for generic model invocation across multiple model types.

---

## 8. Copilot in Power Apps

### 8.1 Overview

Copilot in Power Apps enables natural language app creation. Makers describe business needs and Copilot generates an app with a data model. Powered by Azure OpenAI Service.

### 8.2 Key Capabilities

- **Natural language app generation**: Describe what you need and get a working app + data model.
- **Copilot control for canvas apps (preview)**: An AI chat assistant embedded in canvas apps that lets end users ask questions about app data in natural language. Data source: Dataverse tables only.
- **Copilot for model-driven apps**: AI assistance within model-driven app experiences.
- **Copilot Studio integration**: Customize the copilot behavior through Copilot Studio (topics, actions, articles).

### 8.3 Copilot Control (Canvas Apps)

> Note: As of February 2, 2026, the Copilot control cannot be added to new canvas apps. Microsoft 365 Copilot Chat in canvas apps is the recommended replacement.

- **Setup**: Enable in Power Platform admin center + turn on Copilot component in app settings.
- **Data source**: Dataverse tables only.
- **Customization**: Use Copilot Studio to define topics, actions, and responses.
- **Feedback**: Thumbs up/down from app users; feedback sent to Microsoft.

### 8.4 Admin Controls

| Scope | Setting | Default |
|---|---|---|
| Environment | Copilot toggle (preview features) | On |
| Tenant | Copilot in Power Apps (preview) | On |
| GA features | Cannot be turned off by admin | On (contact Support to disable) |

---

## 9. Copilot in Power Automate

### 9.1 Copilot in Cloud Flows

Create automation using natural language descriptions through multi-step conversational experience.

- Describe what you need and Copilot generates flow steps.
- Edit and refine flows through continued conversation.
- Get contextual help from Microsoft Copilot Studio bot.
- Use flows as plugins in Copilot for Microsoft 365 (preview).

### 9.2 Copilot in Desktop Flows

- Create desktop flows using natural language.
- **Record with Copilot (preview)**: AI-assisted recording of desktop actions.
- **Natural language to script**: Convert plain language to automation scripts.
- **Error repair (preview)**: AI-powered fix suggestions for automation errors at runtime.
- **Activity analysis (preview)**: Analyze desktop flow runs with natural language queries.

### 9.3 Copilot in Process Mining

- **Ingestion**: Guides users through the data ingestion experience.
- **Process analytics**: Generate process insights through natural language; summarize findings quantitatively and qualitatively.

### 9.4 Copilot in Automation Center

Retrieve information about past flow runs, work queue performance, and product features by asking questions in natural language.

### 9.5 Admin Controls

- Regions with GPUs (UK, Australia, US, India): Copilot on by default; disable via tenant-level Support request.
- Regions without GPUs: Copilot on by default via cross-geo data sharing; disable by toggling off cross-geo sharing in Power Platform admin center at tenant level.

---

## 10. Rate Limits Summary

| Model/Group | Calls per Environment | Renewal Period |
|---|---|---|
| Receipt + Invoice processing | 360 | 60 seconds |
| Language detection + Sentiment + Key phrase | 400 | 60 seconds |
| Text recognition (OCR) | 480 | 60 seconds |
| Business card reader | 24 | 60 seconds |

---

## 11. Key Patterns

### Pattern: Document Automation Pipeline
1. Trigger: New document arrives in SharePoint/OneDrive.
2. AI Builder action: Extract information from invoice/receipt/document.
3. Condition: Check confidence score (threshold ~0.65).
4. If low confidence: Fall back to custom document processing model.
5. Output: Save extracted data to Dataverse/Excel/SharePoint.

### Pattern: Multi-Model Fallback
Use prebuilt invoice model as primary extractor. If confidence is low for specific fields, invoke a custom document processing model trained on those specific invoice layouts. Combine results for maximum accuracy.

### Pattern: Text Analytics Flow
1. Trigger: New email/form submission.
2. Sentiment analysis -> Route negative sentiment to escalation queue.
3. Key phrase extraction -> Tag and categorize the submission.
4. Entity extraction -> Pull out dates, amounts, organizations for structured storage.

### Pattern: AI Prompts in Automation
1. Create a reusable prompt in prompt builder with input variables.
2. Use "Create text with GPT using a prompt" action in Power Automate.
3. Pass dynamic content (email body, customer feedback, document text) as input.
4. Use GPT output for summarization, classification, response generation, or action item extraction.

### Pattern: Copilot-Enhanced App
1. Build canvas app with business data in Dataverse.
2. Add Copilot control (or migrate to Microsoft 365 Copilot Chat).
3. Connect to Dataverse tables as data source.
4. Customize copilot behavior in Copilot Studio for domain-specific responses.
5. End users interact with data through natural language chat.

### Pattern: Power Fx + AI Builder in Canvas Apps
Use the formula bar to call AI models directly:
```
// Sentiment analysis
Set(result, AIBuilder.SentimentAnalysis.Predict(TextInput1.Text));

// Entity extraction
Set(entities, AIBuilder.EntityExtraction.Predict(TextInput1.Text));
```
No component insertion required -- works with any control event.

---

## 12. Sources

- https://learn.microsoft.com/en-us/ai-builder/overview
- https://learn.microsoft.com/en-us/ai-builder/model-types
- https://learn.microsoft.com/en-us/ai-builder/prediction-overview
- https://learn.microsoft.com/en-us/ai-builder/text-classification-overview
- https://learn.microsoft.com/en-us/ai-builder/entity-extraction-overview
- https://learn.microsoft.com/en-us/ai-builder/form-processing-model-overview
- https://learn.microsoft.com/en-us/ai-builder/object-detection-overview
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-receipt-processing
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-business-card
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-overview
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-sentiment-analysis
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-key-phrase
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-text-recognition
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-entity-extraction
- https://learn.microsoft.com/en-us/ai-builder/prebuilt-invoice-processing
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/prompts-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/create-custom-prompt
- https://learn.microsoft.com/en-us/ai-builder/azure-openai-model-papp
- https://learn.microsoft.com/en-us/ai-builder/use-in-powerapps-overview
- https://learn.microsoft.com/en-us/ai-builder/use-in-flow-overview
- https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/ai-overview
- https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/add-ai-copilot
- https://learn.microsoft.com/en-us/power-automate/copilot-overview
