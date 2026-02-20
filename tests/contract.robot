*** Settings ***
Documentation    OKW Web Selenium Contract
...              This test enforces the public keyword contract.
Library          OkwWebSelenium

*** Variables ***
@{KW}
# --- Actions (no input) ---
...    ClickOn
...    DoubleClickOn
...    SetFocus

# --- Actions (with input) ---
...    SetValue
...    Select
...    TypeKey

# --- Verify: Value ---
...    VerifyValue
...    VerifyValueWCM
...    VerifyValueREGX

# --- Verify: Placeholder ---
...    VerifyPlaceholder
...    VerifyPlaceholderWCM
...    VerifyPlaceholderREGX

# --- Verify: Tooltip ---
...    VerifyTooltip
...    VerifyTooltipWCM
...    VerifyTooltipREGX

# --- Verify: Label ---
...    VerifyLabel
...    VerifyLabelWCM
...    VerifyLabelREGX

# --- Verify: Caption ---
...    VerifyCaption
...    VerifyCaptionWCM
...    VerifyCaptionREGX

# --- Verify: Attribute ---
...    VerifyAttribute
...    VerifyAttributeWCM
...    VerifyAttributeREGX

# --- Verify: Generic / Focus ---
...    VerifyExist
...    VerifyHasFocus

# --- Lists ---
...    VerifyListCount
...    VerifySelectedCount

# --- Memorize ---
...    MemorizeValue
...    MemorizeTooltip
...    MemorizeLabel
...    MemorizeCaption
...    MemorizeAttribute

# --- Log ---
...    LogValue
...    LogTooltip
...    LogLabel
...    LogCaption
...    LogAttribute

# --- Tables (Web) ---
...    VerifyTableCellValue
...    VerifyTableRowContent
...    VerifyTableColumnContent
...    VerifyTableRowCount
...    VerifyTableColumnCount
...    VerifyTableHasRow
...    VerifyTableContent
...    VerifyTableCellValueByHeaders
...    VerifyTableRowContentByHeader
...    VerifyTableColumnContentByHeader
...    VerifyTableCellValueByHeadersREGX
...    VerifyTableRowContentByHeaderREGX
...    VerifyTableColumnContentByHeaderREGX

*** Test Cases ***
All Web Selenium Keywords Must Exist
    FOR    ${kw}    IN    @{KW}
        Keyword Should Exist    ${kw}
    END

