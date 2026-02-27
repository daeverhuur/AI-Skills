# Testing & Monitoring Reference

## Test Studio for Canvas Apps

Test Studio is a built-in low-code testing tool for canvas apps in Power Apps. It enables makers to create, organize, and automate UI tests directly within the app editor.

### Core Concepts

| Concept | Description |
|---------|-------------|
| Test case | A set of test steps that validate a specific scenario |
| Test suite | A collection of test cases that run together |
| Test step | A single action or assertion within a test case |
| Test assertion | A check that a condition is true using `Assert()` |

### Creating Test Cases

1. Open the canvas app in Edit mode
2. Select **Advanced tools** > **Open tests** (or Tests pane)
3. Select **New test case** to create a case within the default suite
4. Each test case auto-records steps as you interact with the app in the authoring canvas
5. Add assertions between steps to validate expected outcomes

### Test Steps and Actions

Each test step captures a user interaction:

| Step Type | Example |
|-----------|---------|
| SetProperty | `SetProperty(TextInput1.Text, "Hello")` |
| Select | `Select(Button1)` |
| Assert | `Assert(Label1.Text = "Hello", "Label should display input text")` |
| Navigate | Navigating between screens triggers a step |

Steps can be manually edited after recording to refine values or add conditional logic.

### Assert Function

The `Assert` function is the primary validation mechanism:

```
Assert(condition, message)
```

- `condition` -- any boolean Power Fx expression
- `message` -- descriptive text shown when the assertion fails
- A test case **fails** if any assertion evaluates to false
- A test case **passes** if all assertions evaluate to true and no unhandled errors occur

Common assertion patterns:

```
// Verify label shows expected value
Assert(Label1.Text = "Welcome", "Welcome label not displayed")

// Verify visibility
Assert(Panel1.Visible = true, "Panel should be visible after login")

// Verify item count
Assert(CountRows(Gallery1.AllItems) > 0, "Gallery should have items")

// Verify navigation
Assert(App.ActiveScreen = Screen2, "Should navigate to Screen2")
```

### Test Suites

- Default suite is created automatically
- Create additional suites to organize by feature area or scenario type
- Each suite runs its test cases sequentially
- Suite-level setup: `OnTestSuiteStart` property runs once before all cases
- Case-level setup: `OnTestCaseStart` property runs before each case
- Use setup properties to initialize variables and navigate to starting screen

### Running Tests

| Method | Description |
|--------|-------------|
| Play button (studio) | Run interactively in the browser; see step-by-step results |
| Published app test URL | Run tests against the published version |
| Power Automate | Trigger test runs from a cloud flow for automation |
| PowerShell | Use `Microsoft.PowerApps.TestEngine` module for CI/CD |

### Test Results

- Each step shows pass/fail status with duration
- Failed assertions display the custom message
- Network trace available for debugging failures
- Results can be exported as `.trx` files for integration with Azure DevOps

### Limitations

- Only supports canvas apps (not model-driven or custom pages)
- Cannot test component libraries independently
- No support for testing camera, microphone, or GPS inputs
- External data sources must contain real data (no mock data support natively)
- Tests run in a single browser session; no parallel execution
- Responsive layout testing requires manual screen size changes
- Cannot test offline scenarios

## Monitor Tool

Monitor is a debugging tool that provides real-time visibility into app behavior by capturing events, network calls, formula evaluations, and performance data.

### Supported App Types

| App Type | Monitor Support |
|----------|----------------|
| Canvas apps | Full support: formulas, network, properties, data |
| Model-driven apps | Network requests, page navigation, command execution |
| Custom pages | Supported within model-driven app context |

### Launching Monitor

- **For canvas apps**: Open app in Edit mode > Advanced tools > Monitor (or play the app and connect via session link)
- **For model-driven apps**: Navigate to the app, append `&monitor=true` to the URL, or launch from Power Apps portal > Apps > select app > Monitor
- **For published apps**: Share a monitor link with a user to capture their session remotely

### Signal Types and Events

| Event Category | Examples |
|----------------|----------|
| Network | HTTP requests/responses, Dataverse API calls, connector calls |
| Property | Control property evaluations and changes |
| Data | Data source operations (create, read, update, delete) |
| Screen | Screen navigation events and OnVisible triggers |
| User interaction | Button clicks, input changes, gallery selection |
| Error | Unhandled errors, delegation warnings, permission failures |

### Network Tab

Captures all HTTP traffic between the app and backend services:

- Request URL, method, headers, and body
- Response status code, headers, and body (with JSON formatting)
- Duration in milliseconds for each call
- Filter by status code to isolate errors (4xx, 5xx)
- Identify redundant calls that can be consolidated with `Concurrent()`

### Formula Evaluation

Monitor traces formula execution for canvas apps:

- Shows which formulas trigger on each event
- Displays input values and output results
- Highlights delegation warnings in real-time
- Reveals evaluation order for complex expressions
- Useful for identifying formulas that evaluate more often than expected

### Performance Profiling

Key metrics captured by Monitor:

| Metric | What It Reveals |
|--------|-----------------|
| App load time | Time from launch to first interactive screen |
| Screen transition time | Duration of navigation between screens |
| Data call duration | Time for each data source request |
| Formula evaluation time | How long individual expressions take |
| Total network payload | Size of data transferred |

### Common Performance Patterns to Watch

- **Excessive OnStart calls**: Move non-critical logic to OnVisible on individual screens
- **Large gallery data loads**: Use delegation-compatible queries to limit records
- **Redundant data calls**: Cache results in collections instead of repeating lookups
- **Slow connector responses**: Consider implementing Power Automate flows for complex operations
- **Unthrottled timer controls**: Ensure Timer.Duration and Timer.Repeat are set appropriately

## Solution Checker (Power Apps Checker)

Solution Checker performs static analysis on Power Platform solutions to identify performance, reliability, accessibility, and design issues before deployment.

### Rule Categories

| Category | Focus |
|----------|-------|
| Performance | Inefficient patterns, excessive data calls, non-delegable queries on large datasets |
| Reliability | Error handling gaps, race conditions, deprecated API usage |
| Accessibility | Missing labels, insufficient contrast, keyboard navigation issues |
| Design | Naming conventions, unused variables, code maintainability |
| Security | Hardcoded credentials, insecure connection patterns |
| Supportability | Patterns that complicate future maintenance and upgrades |

### Running Solution Checker

**From Power Apps portal:**
1. Navigate to Solutions
2. Select the target solution
3. Select **Solution checker** > **Run**
4. Wait for analysis to complete (can take several minutes for large solutions)
5. Review results in the portal with severity levels

**From Power Platform CLI (pac):**
```bash
pac solution check --path ./MySolution.zip --geo unitedstates
```

**From Azure DevOps pipeline:**
```yaml
- task: microsoft-IsvExpTools.PowerPlatform-BuildTools.checker.PowerPlatformChecker@2
  inputs:
    authenticationType: PowerPlatformSPN
    PowerPlatformSPN: 'ServiceConnection'
    FilesToAnalyze: '$(Build.ArtifactStagingDirectory)/solution.zip'
    RuleSet: '0ad12346-e108-40b8-a956-9a8f95ea18c9'
```

### Interpreting Results

| Severity | Meaning | Action |
|----------|---------|--------|
| Critical | Likely to cause failures or data loss | Must fix before deployment |
| High | Significant performance or reliability risk | Should fix before deployment |
| Medium | Best practice violations that may cause future issues | Plan to fix |
| Low | Minor code quality suggestions | Fix when convenient |
| Informational | Awareness items | Review and acknowledge |

### Common Issues Flagged

- **web-use-global-context**: Use `Xrm.Utility.getGlobalContext()` instead of `window.parent.Xrm`
- **il-specify-column**: Always specify columns in Dataverse queries instead of retrieving all
- **web-avoid-crm2011-service-odata**: Use Web API instead of deprecated OData v2 endpoint
- **web-avoid-window-top**: Avoid `window.top` references that break in Unified Interface
- **meta-remove-dup-reg**: Remove duplicate plug-in step registrations
- **app-formula-issues-high-severity**: Complex formula patterns that cause reliability issues

### Managed Environment Enforcement

In managed environments, Solution Checker can be enforced as a gate:

- **Warn mode**: Show checker results to admins on import but allow proceed
- **Block mode**: Prevent solution import if critical or high severity issues exist
- Configure enforcement level per environment via Power Platform admin center

## Power Apps Test Engine (Open Source)

Power Apps Test Engine is an open-source tool for automated testing of canvas apps and model-driven apps, designed for CI/CD integration.

### Key Features

- Runs tests headlessly using Playwright browser automation
- Supports YAML-based test definitions
- Integrates with Azure DevOps, GitHub Actions, and other CI/CD platforms
- Supports authentication via Azure AD app registration
- Can run against multiple environments

### Test Definition Format (YAML)

```yaml
testSuite:
  testSuiteName: Expense Report Tests
  testSuiteDescription: Validates expense submission workflow
  persona: User1
  appLogicalName: cr7d8_expensereport_12345
  onTestSuiteComplete: |
    = Screenshot("final-state")

  testCases:
    - testCaseName: Submit New Expense
      testCaseDescription: Create and submit an expense report
      testSteps: |
        = Screenshot("start-screen");
          SetProperty(TextInput_Amount.Text, "150.00");
          SetProperty(Dropdown_Category.Selected, {Value: "Travel"});
          Select(Button_Submit);
          Assert(Label_Status.Text = "Submitted", "Status should show Submitted");
          Screenshot("after-submit");
```

### Running in CI/CD

**GitHub Actions example:**

```yaml
- name: Run Power Apps Tests
  uses: microsoft/powerplatform-actions/run-tests@v1
  with:
    environment-url: ${{ secrets.ENV_URL }}
    tenant-id: ${{ secrets.TENANT_ID }}
    app-id: ${{ secrets.CLIENT_ID }}
    client-secret: ${{ secrets.CLIENT_SECRET }}
    test-suite-path: ./tests/
```

**Azure DevOps example:**

```yaml
- task: PowerPlatformRunTests@0
  inputs:
    environmentUrl: $(EnvironmentUrl)
    tenantId: $(TenantId)
    appId: $(ClientId)
    clientSecret: $(ClientSecret)
    testSuitePath: '$(Build.SourcesDirectory)/tests/'
```

### Test Engine vs Test Studio

| Aspect | Test Studio | Test Engine |
|--------|-------------|-------------|
| Authoring | Low-code in browser | YAML files in source control |
| Execution | Manual or single flow trigger | CI/CD pipeline headless |
| App types | Canvas only | Canvas + model-driven |
| Source control | Not natively | YAML files version controlled |
| Parallel runs | No | Configurable |
| Screenshots | No | Built-in |

## Power Automate Testing

### Flow Checker

The built-in flow checker validates flow definitions before saving:

- Detects missing required inputs
- Identifies expression syntax errors
- Flags unreachable actions (dead code)
- Warns about deprecated connectors or actions
- Validates trigger configuration

### Manual Testing Patterns

**Testing with trigger conditions:**
1. Save the flow in test mode
2. Use **Test** button > **Manually** to trigger with sample data
3. Review the run history for each action's inputs and outputs
4. Check action durations to identify bottlenecks

**Testing with static data:**
1. Use **Test** > **With a recently used trigger** to replay previous trigger data
2. Select a specific trigger event from history
3. Flow runs with the same input data for reproducible testing

### Flow Run History Analysis

| Column | Purpose |
|--------|---------|
| Status | Succeeded, Failed, Cancelled, Running |
| Start time | When the run was triggered |
| Duration | Total execution time |
| Trigger | What initiated the run |

Each action in the run shows:
- Input/output data (JSON expandable)
- Duration in seconds
- Status code for HTTP actions
- Retry attempts if configured

### Mock Data Patterns

Power Automate does not have native mock support, but these patterns help:

- **Environment variables**: Switch data sources between test and production
- **Condition flags**: Add a "test mode" variable that routes to test data
- **Separate test flows**: Create parallel flows with hardcoded test inputs
- **Solution variables**: Use solution environment variables to toggle endpoints

```
// Pseudo-pattern for test mode routing
if @{variables('IsTestMode')} equals true
    -> Use SharePoint test list
    -> Use test email recipients
else
    -> Use production list
    -> Use real recipients
```

### Error Handling Patterns for Flows

- **Configure run-after**: Set actions to run after failure/timeout/skipped
- **Scope + try-catch**: Wrap actions in Scope, add parallel Scope with run-after = failed
- **Terminate action**: End flow with Failed/Succeeded/Cancelled status and custom message
- **Send failure notifications**: Use run-after to notify admins on critical flow failures

## Application Insights Integration

Power Platform can send telemetry data to Azure Application Insights for advanced monitoring and alerting.

### Setup for Canvas Apps

1. Create an Application Insights resource in Azure
2. Copy the **Instrumentation Key** (or Connection String)
3. In Power Apps admin center, navigate to the environment settings
4. Under **Product** > **Analytics**, paste the instrumentation key
5. Telemetry begins flowing within minutes

### Setup for Model-Driven Apps

1. Same Application Insights resource can be used
2. Navigate to environment settings in admin center
3. Enable Application Insights under **Analytics** section
4. Model-driven app page loads, form events, and API calls are captured

### Custom Telemetry with Trace()

Canvas apps can send custom telemetry using the `Trace()` function:

```
// Log a custom event
Trace("ExpenseSubmitted",
    TraceSeverity.Information,
    {
        Amount: TextInput_Amount.Text,
        Category: Dropdown_Category.Selected.Value,
        UserId: User().Email
    }
)

// Log a warning
Trace("LargeExpenseDetected",
    TraceSeverity.Warning,
    {
        Amount: TextInput_Amount.Text,
        Threshold: "5000"
    }
)

// Log an error
Trace("SubmissionFailed",
    TraceSeverity.Error,
    {
        ErrorMessage: "Dataverse connection timeout",
        Screen: App.ActiveScreen.Name
    }
)
```

### Trace Severity Levels

| Level | Use Case |
|-------|----------|
| TraceSeverity.Information | Normal operations, user actions, milestones |
| TraceSeverity.Warning | Unexpected but recoverable situations |
| TraceSeverity.Error | Failures that prevent normal operation |
| TraceSeverity.Critical | System-level failures requiring immediate attention |

### Querying Telemetry in Application Insights

Use Kusto Query Language (KQL) to analyze telemetry:

```kql
// Canvas app errors in the last 24 hours
traces
| where timestamp > ago(24h)
| where severityLevel >= 3
| project timestamp, message, customDimensions
| order by timestamp desc

// Average app load time by screen
customMetrics
| where name == "ScreenTransition"
| summarize avg(value) by tostring(customDimensions["ScreenName"])

// User session count over time
customEvents
| where name == "AppLaunch"
| summarize count() by bin(timestamp, 1h)
| render timechart
```

### Alerting

- Create alert rules in Application Insights based on custom queries
- Set thresholds for error rates, response times, or custom metric values
- Integrate with Action Groups to send email, SMS, Teams notification, or trigger Azure Functions
- Common alerts: app error spike, flow failure rate > threshold, slow API response

## Debugging Common Issues

### Canvas App Issues

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Slow app load | Too much logic in App.OnStart | Move non-critical code to screen OnVisible |
| Gallery shows no data | Delegation limit exceeded | Add filters that delegate; increase non-delegable limit (max 2000) |
| Blank screen | OnVisible error | Check Monitor for errors; simplify OnVisible logic |
| Controls not responsive | Circular references | Review formula dependencies in Monitor |
| Data not saving | Patch() errors | Check Errors() collection after Patch; validate data types |
| "Network error" banner | Connector throttling | Implement retry logic; reduce call frequency |
| Unexpected behavior after publish | Caching | Clear browser cache; re-publish app |

### Model-Driven App Issues

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Form not loading | JavaScript error | Check browser console (F12); review custom scripts |
| Business rule not firing | Scope misconfiguration | Verify rule scope (entity vs all forms vs specific form) |
| Slow form load | Too many custom scripts | Reduce script size; use async loading patterns |
| Plugin error | Unhandled exception in plugin | Check plugin trace logs in Dataverse settings |
| View shows wrong data | Security role filtering | Verify user has correct read permissions on table/columns |
| Ribbon button missing | Ribbon customization conflict | Check solution layers for command bar overrides |

### Power Automate Flow Issues

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Flow not triggering | Trigger condition not met | Verify trigger configuration; check connection health |
| "Action failed" | Expression error | Review action inputs in run history; validate expressions |
| Timeout errors | Long-running operations | Increase timeout; use async patterns with webhooks |
| Throttling (429) | Too many API calls | Add delays; implement exponential backoff; use batch operations |
| Missing data in outputs | Null/empty values | Add null checks with `coalesce()` or `if(empty(...))` |
| Flow turns off | Repeated failures | Fix root cause; resubmit failed runs; re-enable flow |
| Connector auth failure | Token expired | Reauthorize connection; check service principal expiry |

### General Debugging Workflow

1. **Reproduce** the issue consistently
2. **Monitor**: Attach Monitor tool to capture events and network calls
3. **Isolate**: Narrow down to specific screen, formula, action, or data source
4. **Trace**: Add `Trace()` statements or check run history for detailed state
5. **Fix**: Apply targeted fix
6. **Validate**: Re-test with Monitor attached to confirm resolution
7. **Regress**: Run Test Studio / Test Engine suite to ensure no regressions

## Testing Strategy Recommendations

### Test Pyramid for Power Platform

| Level | Tool | Scope | Speed |
|-------|------|-------|-------|
| Unit | Test Studio / Test Engine | Individual screen or formula behavior | Fast |
| Integration | Power Automate test runs | End-to-end flow with real connectors | Medium |
| System | Test Engine in CI/CD | Full app workflow across screens | Slow |
| Manual | Monitor + browser | Exploratory and edge case testing | Varies |

### Recommended Practices

- Write tests for critical business logic and calculations first
- Use Test Studio for iterative development testing
- Use Test Engine with CI/CD for regression testing on deployment
- Monitor production apps with Application Insights for proactive issue detection
- Review Solution Checker results before every deployment to higher environments
- Maintain a test data set in a dedicated test environment
- Document known issues and expected test failures in source control alongside test definitions
