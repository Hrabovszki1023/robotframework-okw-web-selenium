*** Settings ***
Library    Collections

*** Variables ***
${TAB_TOKEN}           $TAB
${LF_TOKEN}            $LF
${EMPTY_TOKEN}         $EMPTY
${EMPTYCOL_TOKEN}      $EMPTYCOL
${EMPTYTABLE_TOKEN}    $EMPTYTABLE

*** Test Cases ***
Parse Row Pattern Basic
    ${tt}=    Evaluate    __import__('okw4robot.utils.table_tokens').utils.table_tokens
    ${row}=   Evaluate    ${tt}.parse_row_pattern('A${TAB_TOKEN}B${TAB_TOKEN}C')
    Length Should Be      ${row}    3
    Should Be Equal       ${row}[0]    A
    Should Be Equal       ${row}[1]    B
    Should Be Equal       ${row}[2]    C

Parse Column Pattern Basic
    ${tt}=    Evaluate    __import__('okw4robot.utils.table_tokens').utils.table_tokens
    ${col}=   Evaluate    ${tt}.parse_column_pattern('X${LF_TOKEN}Y${LF_TOKEN}Z')
    Length Should Be      ${col}    3
    Should Be Equal       ${col}[0]    X
    Should Be Equal       ${col}[1]    Y
    Should Be Equal       ${col}[2]    Z

Parse Table Pattern Basic 2x2
    ${tt}=    Evaluate    __import__('okw4robot.utils.table_tokens').utils.table_tokens
    ${tbl}=   Evaluate    ${tt}.parse_table_pattern('Z11${TAB_TOKEN}Z12${LF_TOKEN}Z21${TAB_TOKEN}Z22')
    Length Should Be      ${tbl}    2
    ${r0}=   Evaluate     ${tbl}[0]
    ${r1}=   Evaluate     ${tbl}[1]
    Length Should Be      ${r0}     2
    Length Should Be      ${r1}     2
    Should Be Equal       ${r0}[0]  Z11
    Should Be Equal       ${r0}[1]  Z12
    Should Be Equal       ${r1}[0]  Z21
    Should Be Equal       ${r1}[1]  Z22

Empty Tokens Handling
    ${tt}=    Evaluate    __import__('okw4robot.utils.table_tokens').utils.table_tokens
    ${row}=   Evaluate    ${tt}.parse_row_pattern('${EMPTY_TOKEN}')
    Length Should Be      ${row}    1
    Should Be Equal       ${row}[0]
    ${col}=   Evaluate    ${tt}.parse_column_pattern('${EMPTYCOL_TOKEN}')
    Length Should Be      ${col}    0
    ${tbl}=   Evaluate    ${tt}.parse_table_pattern('${EMPTYTABLE_TOKEN}')
    Length Should Be      ${tbl}    0


