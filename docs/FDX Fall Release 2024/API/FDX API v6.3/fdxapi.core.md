openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Core API
  description: Financial Data Exchange V6.3.0 Core API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Core API
tags:
  - name: Account Information
    description: Search and view customer accounts
  - name: Account Statements
    description: Search and retrieve account statements
  - name: Account Transactions
    description: Search and view account transactions
  - name: Money Movement
    description: View account money movement details
  - name: Personal Information
    description: Search and view customer or customers
  - name: Reward Program Categories
    description: View categories of reward programs
  - name: Reward Program Information
    description: Search and view customer reward programs
paths:
  ############################################################
  #
  # Core paths
  #
  ############################################################

  /accounts:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: searchForAccounts
      tags:
        - Account Information
      summary: Search for accounts
      description: >-
        Return information for all of the customer's consented accounts or just
        those accounts identified in the `accountIds` request parameter.
        Use `ResultTypeQuery` parameter value of `lightweight` to retrieve minimal
        descriptive information and the `accountId` for each account.
        The `accountId` can then be used in the `getAccount` operation's path
        `/accounts/{accountId}` to retrieve full details about each account
      parameters:
        - name: accountIds
          in: query
          description: Comma separated list of account ids
          style: form
          explode: false
          schema:
            type: array
            items:
              type: string
        - name: startTime
          in: query
          description: Start time for use in retrieval of transactions
          schema:
            type: array
            items:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        - name: endTime
          in: query
          description: End time for use in retrieval of transactions
          schema:
            type: array
            items:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        - $ref: './fdxapi.components.yaml#/components/parameters/ResultTypeQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: >-
            Array of accounts (DepositAccount, LoanAccount, LineOfCreditAccount, InvestmentAccount,
            InsuranceAccount, AnnuityAccount, CommercialAccount, or DigitalWallet)
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Accounts'
              examples:
                Search for accounts success response:
                  value:
                    page:
                      nextOffset: '2'
                      total: 3
                    links:
                      next:
                        href: '/accounts?offSet=2&limit=10'
                    accounts:
                      - accountCategory: DEPOSIT_ACCOUNT
                        accountId: '10001'
                        nickname: My Checking Acc XXXX3223
                        status: OPEN
                        balanceAsOf: '2017-11-05T13:15:30.751Z'
                        currentBalance: 13300.35
                        openingDayBalance: 500
                      - accountCategory: DEPOSIT_ACCOUNT
                        accountId: '10002'
                        nickname: My Checking Acc XXXX4443
                        status: OPEN
                        balanceAsOf: '2017-11-05T13:15:30.751Z'
                        currentBalance: 332.22
                        openingDayBalance: 100.0
                      - accountCategory: LOAN_ACCOUNT
                        accountId: '20001'
                        nickname: My Mortgage Acc XXXX9979
                        status: OPEN
                        balanceAsOf: '2017-11-05T13:15:30.751Z'
                        principalBalance: 133000.35
                        loanTerm: 30
                        nextPaymentDate: '2017-12-01'
                        nextPaymentAmount: 2333.32
        '206':
          description: >-
            Partial success array of accounts (DepositAccount, LoanAccount, LineOfCreditAccount, InvestmentAccount,
            InsuranceAccount, AnnuityAccount, CommercialAccount, or DigitalWallet)
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Accounts'
        '400':
          description: Start or end date value is not in the ISO 8601 format
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Invalid start or end date:
                  value:
                    code: '702'
                    message: Invalid start or end date
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Invalid date range:
                  value:
                    code: '703'
                    message: Invalid date range
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '404':
          $ref: './fdxapi.components.yaml#/components/responses/404'
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /accounts/{accountId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getAccount
      tags:
        - Account Information
      summary: Retrieve account details
      description: >-
        Retrieve full details about the account identified by `{accountId}` parameter
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
      responses:
        '200':
          description: >-
            This can be one of LoanAccount, DepositAccount, LineOfCreditAccount, InvestmentAccount,
            InsuranceAccount, AnnuityAccount, CommercialAccount, or DigitalWallet
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountWithDetails'
              examples:
                Loan Account With Details:
                  value:
                    accountCategory: LOAN_ACCOUNT
                    accountId: '12345678'
                    accountType: LOAN
                    accountNumberDisplay: XXXXX4567
                    status: OPEN
                    description: 30 Year Mortgage
                    nickname: My Home Mortgage
                    currency:
                      currencyCode: USD
                    interestRate: 4
                    loanTerm: 0
                    totalNumberOfPayments: 0
        '404':
          description: Account with id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Account not found:
                  value:
                    code: '701'
                    message: Account not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /accounts/{accountId}/asset-transfer-networks:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getAccountAssetTransferNetworks
      tags:
        - Money Movement
      description: ...
      summary: Get asset transfer details for this account
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
      responses:
        '200':
          description: Information required to facilitate asset transfer from this account
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetTransferNetworkList'
              examples:
                ACATS:
                  value:
                    assetTransferNetworks:
                      - identifier: '121000358'
                        identifierType: "ACCOUNT_NUMBER"
                        institutionName: US Investments
                        institutionId: '1234567890'
                        type: 'US_ACATS'
                        jointAccount: true

  /accounts/{accountId}/contact:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getAccountContact
      tags:
        - Personal Information
      description: Get contact information on the account
      summary: Get an account's contact information
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
      responses:
        '200':
          description: >-
            Details used to verify an account
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountContact'
        '404':
          description: Account with id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Account not found:
                  value:
                    code: '701'
                    message: Account not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /accounts/{accountId}/payment-networks:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getAccountPaymentNetworks
      tags:
        - Money Movement
      description: Get payment networks supported by the account
      summary: Get payment networks supported by the account
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: Information required to execute a payment transaction against this account
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountPaymentNetworkList'
              examples:
                Account Number:
                  value:
                    page:
                      totalElements: 1
                    paymentNetworks:
                      - bankId: "121000358"
                        identifier: "1234567890"
                        identifierType: "ACCOUNT_NUMBER"
                        type: "US_ACH"
                        transferIn: true
                        transferOut: true
                        transferLimits:
                          out:
                            day:
                              resetsOn: "2023-08-09T00:00:00.000Z"
                              transferMaxAmount: 10000.0
                              transferRemainingAmount: 8356.0
                              maxOccurrence: 6
                              remainingOccurrence: 5
                            month:
                              resetsOn: "2023-09-01T00:00:00.000Z"
                              transferMaxAmount: 50000.0
                              transferRemainingAmount: 35200.0
                            transaction:
                              transferMaxAmount: 5000.0
                              transferRemainingAmount: 4990.0
                Tokenized Account Number:
                  value:
                    page:
                      totalElements: 1
                    paymentNetworks:
                      - bankId: "121000358"
                        identifier: "987654321"
                        identifierType: "TOKENIZED_ACCOUNT_NUMBER"
                        type: "US_ACH"
                        transferIn: true
                        transferOut: true
                Multiple Networks:
                  value:
                    page:
                      totalElements: 2
                    paymentNetworks:
                      - bankId: "121000358"
                        identifier: "1234567890"
                        identifierType: "ACCOUNT_NUMBER"
                        type: "US_ACH"
                        transferIn: true
                        transferOut: true
                      - bankId: "026009593"
                        identifier: "1234567890"
                        identifierType: "ACCOUNT_NUMBER"
                        type: "US_FEDWIRE" # Real-time payments
                        transferIn: true
                        transferOut: true
        '404':
          description: Account with id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Account not found:
                  value:
                    code: '701'
                    message: Account not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Source account not found:
                  value:
                    code: '901'
                    message: Source account not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Data not found for request parameters:
                  value:
                    code: '1107'
                    message: Data not found for request parameters
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /accounts/{accountId}/statements:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: searchForAccountStatements
      tags:
        - Account Statements
      description: >-
        Get account statements. Example: GET
        /accounts/{accountId}/statements?startTime=value1&endTime=value2
      summary: Search for statements
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
        - $ref: './fdxapi.components.yaml#/components/parameters/StartTimeQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/EndTimeQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: Paginated list of available statements
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Statements'
              examples:
                Search for statements success response:
                  value:
                    page:
                      nextOffset: '2'
                      total: 3
                    links:
                      next:
                        href: '/accounts/1111/statements?offSet=2&limit=10'
                    statements:
                      - accountId: '10001'
                        statementId: '40004'
        '206':
          description: Partial success paginated list of available statements
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Statements'
        '400':
          description: Start or end date value is not in the ISO 8601 format
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Invalid start or end date:
                  value:
                    code: '702'
                    message: Invalid start or end date
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Invalid date range:
                  value:
                    code: '703'
                    message: Invalid date range
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '404':
          description: Account with id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Account not found:
                  value:
                    code: '701'
                    message: Account not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Data not found for request parameters:
                  value:
                    code: '1107'
                    message: Data not found for request parameters
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /accounts/{accountId}/statements/{statementId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getAccountStatement
      tags:
        - Account Statements
      description: >-
        Gets an account statement image file. Use
        [HTTP Accept request-header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)
        to specify desired content types. See ContentTypes definition for typical values
      summary: Get an account statement
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
        - $ref: '#/components/parameters/StatementIdPath'
      responses:
        '200':
          description: An image of an account statement
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/pdf:
              schema:
                description: A pdf image of an account statement
                type: string
                format: binary
            image/gif:
              schema:
                description: A gif image of an account statement
                type: string
                format: binary
            image/jpeg:
              schema:
                description: A jpeg image of an account statement
                type: string
                format: binary
            image/tiff:
              schema:
                description: A tiff image of an account statement
                type: string
                format: binary
            image/png:
              schema:
                description: A png image of an account statement
                type: string
                format: binary
        '302':
          description: Statement is available at specified location. URL is returned via the `Location` HTTP header
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
        '400':
          description: Statement is processing and is not yet available
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Statement is Processing:
                  value:
                    code: '1300'
                    message: Statement is Processing
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '404':
          description: When account is present with no statements in it
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Statements not found for given Account:
                  value:
                    code: '1108'
                    message: Statements not found for given Account
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Statement id not found for Account:
                  value:
                    code: '1104'
                    message: Statement id not found for Account
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '406':
          $ref: './fdxapi.components.yaml#/components/responses/406'
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /accounts/{accountId}/transaction-images/{imageId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getAccountTransactionImages
      tags:
        - Account Transactions
      description: Get account transaction image
      summary: Get account transaction image
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
        - $ref: '#/components/parameters/ImageIdPath'
      responses:
        '200':
          description: An image of transaction (such as a scanned check)
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/pdf:
              schema:
                type: string
                format: binary
            image/gif:
              schema:
                type: string
                format: binary
            image/jpeg:
              schema:
                type: string
                format: binary
            image/tiff:
              schema:
                type: string
                format: binary
            image/png:
              schema:
                type: string
                format: binary
        '404':
          description: Account or image with id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Account not found:
                  value:
                    code: '701'
                    message: Account not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Image Id not found for Transaction:
                  value:
                    code: '1103'
                    message: Image Id not found for Transaction
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '406':
          $ref: './fdxapi.components.yaml#/components/responses/406'
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /accounts/{accountId}/transactions:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: searchForAccountTransactions
      tags:
        - Account Transactions
      description: >-
        Search for account transactions. Example:
        /accounts/{accountId}/transactions?startTime=value1&endTime=value2
      summary: Search for account transactions
      parameters:
        - $ref: '#/components/parameters/AccountIdPath'
        - $ref: './fdxapi.components.yaml#/components/parameters/StartTimeQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/EndTimeQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: >-
            Paginated collection of transactions, which can be one of DepositTransaction,
            LoanTransaction, LineOfCreditTransaction, InvestmentTransaction, InsuranceTransaction,
            CommercialTransaction, or DigitalWalletTransaction
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Transactions'
              examples:
                Paginated Transactions:
                  value:
                    page:
                      nextOffset: '2'
                      total: 3
                    links:
                      next:
                        href: '/accounts/33333/transactions?offSet=2&limit=10'
                    transactions:
                      - accountCategory: DEPOSIT_ACCOUNT
                        accountId: '10001'
                        transactionId: '20002'
                        postedTimestamp: '2017-11-05T13:15:30.751Z'
                        description: Direct deposit from XYZ Corp
                        debitCreditMemo: CREDIT
                        amount: 1200.42
                        payee: XYZ Corp
                      - accountCategory: DEPOSIT_ACCOUNT
                        accountId: '10001'
                        transactionId: '20002'
                        postedTimestamp: '2017-11-05T13:15:31.751Z'
                        description: Withdrawal from ATM
                        debitCreditMemo: DEBIT
                        amount: 1200.42
                        payee: Account Owner
                Transaction with Rewards:
                  summary: Example of single transaction with associated reward
                  value:
                    transactions:
                      - accountCategory: LOC_ACCOUNT
                        accountId: '10001'
                        transactionId: '20003'
                        postedTimestamp: '2017-11-05T13:15:30.751Z'
                        description: Hotel Stay
                        debitCreditMemo: DEBIT
                        amount: 236
                        reward:
                          accrued: 472
                          adjusted: 0
                          categoryId: '293'
        '206':
          description: >-
            Partial success paginated list of transactions, which can be one of DepositTransaction,
            LoanTransaction, LineOfCreditTransaction, InvestmentTransaction, InsuranceTransaction,
            CommercialTransaction, or DigitalWalletTransaction
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Transactions'
        '400':
          description: Start or end date value is not in the ISO 8601 format
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Invalid start or end date:
                  value:
                    code: '702'
                    message: Invalid start or end date
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Invalid date range:
                  value:
                    code: '703'
                    message: Invalid date range
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '404':
          description: Account with id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Account not found:
                  value:
                    code: '701'
                    message: Account not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Data not found for request parameters:
                  value:
                    code: '1107'
                    message: Data not found for request parameters
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /reward-programs:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: searchRewardPrograms
      tags:
        - Reward Program Information
      description: Query all reward programs
      summary: Search reward programs
      parameters:
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: Data describing reward programs associated with accounts
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RewardPrograms'
              examples:
                Multiple Reward Programs:
                  summary: Example showing multiple reward programs
                  value:
                    rewardPrograms:
                      - programName: Marriott Bonvoy
                        rewardProgramId: 4FRCCQvGW0GZEMtsOQWlkQ
                        programUrl: https://www.marriott.com/loyalty.mi
                        memberships:
                          - accountIds:
                              - af0f8e58-9649-4c29-bab2-0295d522cd6f
                              - e75e31eb-bf04-4d87-9f20-4554f63a639e
                            businessOrConsumer: CONSUMER
                            customerId: kBA5C3d7cBK9DuRngsQRwt6Ydo80bjYDR7n4O5yCKshizuS7hOZJ4cAevBne
                            memberId: 5ee28848b4f242a6b7a41e0daa03a824
                            memberNumber: '1783949940'
                            memberTier: Gold
                            balances:
                              - name: Points
                                type: POINTS
                                balance: 900
                                accruedYtd: 1000
                                redeemedYtd: 200
                                qualifying: false
                              - name: Promotional
                                type: POINTS
                                balance: 900
                                accrued: 1000
                                redeemed: 200
                                qualifying: false
                      - programName: United MileagePlus®
                        rewardProgramId: GY4cHWCPxkqgkY61h4BKdQ
                        programUrl: https://www.united.com/en/us/fly/mileageplus.html
                        memberships:
                          - accountIds:
                              - b4ef4572-452d-41bd-9d2d-1b29dafe63f0
                            businessOrConsumer: BUSINESS
                            customerId: kBA5C3d7cBK9DuRngsQRwt6Ydo80bjYDR7n4O5yCKshizuS7hOZJ4cAevBne
                            memberId: b6b319dd3e2c4592847ad6ee32d518bc
                            memberNumber: '9394970669'
                            balances:
                              - name: Miles
                                type: MILES
                                balance: 900
                                accrued: 1000
                                redeemed: 200
                                qualifying: false
                      - programName: Starbucks Rewards
                        rewardProgramId: iqOtPUEYb0Go6SCL8As4fQ
                        programUrl: https://www.starbucks.com/rewards
                        memberships:
                          - accountIds:
                              - 89cf3262-ff38-4f6a-afbc-aafc50cac751
                            businessOrConsumer: CONSUMER
                            customerId: kBA5C3d7cBK9DuRngsQRwt6Ydo80bjYDR7n4O5yCKshizuS7hOZJ4cAevBne
                            memberId: 95c1aeacd85e4783950a9c2d6e76efa9
                            memberNumber: '7417973194'
                            balances:
                              - name: Stars
                                type: POINTS
                                balance: 900
                                accrued: 1000
                                redeemed: 200
                                qualifying: false

  /reward-programs/{rewardProgramId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getRewardProgram
      tags:
        - Reward Program Information
      description: Get a specific reward program
      summary: Get reward program
      parameters:
        - $ref: '#/components/parameters/RewardProgramIdPath'
      responses:
        '200':
          description: Data describing reward programs associated with accounts
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RewardProgram'
              examples:
                Single Reward Program:
                  value:
                    programName: Discover Cashback Bonus
                    rewardProgramId: ywX9ME0FXUa6Mtj0xkOgtA
                    programUrl: https://www.discover.com/credit-cards/cashback-bonus/
                    memberships:
                      - accountIds:
                          - af0f8e58-9649-4c29-bab2-0295d522cd6f
                          - e75e31eb-bf04-4d87-9f20-4554f63a639e
                        businessOrConsumer: CONSUMER
                        customerId: kBA5C3d7cBK9DuRngsQRwt6Ydo80bjYDR7n4O5yCKshizuS7hOZJ4cAevBne
                        memberId: b0a853a278804e1694d3104709cbfb58
                        memberNumber: '6137299224'
                        memberTier: Gold
                        balances:
                          - name: Cashback
                            type: CASHBACK
                            balance: 101.95
                            accruedYtd: 4500.1
                            redeemedYtd: 234.45
                            qualifying: false
                          - name: Cashback Match
                            type: CASHBACK
                            balance: 401.95
                            accruedYtd: 500.1
                            redeemedYtd: 134.45
                            qualifying: false
        '404':
          description: Reward program Id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Reward program Id not found:
                  value:
                    code: '1101'
                    message: Reward program Id not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /reward-programs/{rewardProgramId}/categories:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getRewardProgramCategories
      tags:
        - Reward Program Categories
      description: Get reward categories
      summary: Get reward categories
      parameters:
        - $ref: '#/components/parameters/RewardProgramIdPath'
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: Data describing a reward program's categories
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RewardCategories'
              examples:
                Multiple Reward Categories:
                  summary: Example response with multiple reward categories
                  value:
                    categories:
                      - categoryName: Amusement Park
                        categoryId: 100
                        multiplier: 1
                        description: >-
                          The Amusement Park category, including zoos, circuses and aquariums, covers
                          establishments that operate parks or carnivals and offer mechanical rides
                          and games and/or live animal shows.
                      - categoryName: Dining/Restaurant
                        categoryId: 101
                        multiplier: 2
                        description: >-
                          Merchants in the Dining/Restaurant category range from fast food restaurants
                          to fine dining establishments. They fall into the Dining category if they
                          primarily prepare food and drinks for immediate consumption on the premises
                          or for take-out. Dining merchants include bars, cocktail lounges, nightclubs,
                          taverns and fast-food restaurants. Some merchants that sell food and drinks
                          are located within larger establishments that sell other goods and services
                          and may not be not included in this category. For example a department store
                          or hotel restaurant, theme park cafes or discount store food counter would
                          not be categorized under Dining.
                      - categoryName: Entertainment
                        categoryId: 102
                        multiplier: 2
                        description: >-
                          Entertainment includes purchases made at sports promoters, movie theaters,
                          theatrical promoters, amusement parks, tourist attractions, record stores
                          and video rentals.
                      - categoryName: Hotels
                        categoryId: 103
                        multiplier: 5
                        description: >-
                          Hotels include businesses that provide sleeping or meeting room accommodations.
                          Some goods and services that appear on a hotel bill are included. Often
                          restaurants in hotels are categorized as a hotel purchase.
        '404':
          description: Request is invalid
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Reward program Id not found:
                  value:
                    code: '1101'
                    message: Reward program Id not found
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Categories not found for the reward program:
                  value:
                    code: '1102'
                    message: Categories not found for the reward program
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

components:

  securitySchemes:
    ############################################################
    #
    # Security Schemes
    #
    ############################################################

    OAuthFapi1Advanced:
      $ref: './fdxapi.components.yaml#/components/securitySchemes/OAuthFapi1Advanced'

  parameters:
    ############################################################
    #
    # Core request parameters
    #
    ############################################################

    AccountIdPath:
      name: accountId
      in: path
      description: Account Identifier
      required: true
      schema:
        type: string

    ImageIdPath:
      name: imageId
      in: path
      description: Image Identifier
      required: true
      schema:
        type: string

    RewardProgramIdPath:
      name: rewardProgramId
      in: path
      description: Reward Program Identifier
      required: true
      schema:
        type: string

    StatementIdPath:
      name: statementId
      in: path
      description: Statement Identifier
      required: true
      schema:
        type: string

  schemas:
    ############################################################
    #
    # Core data entities
    #
    ############################################################

    Account:
      title: Account entity
      description: An abstract account entity that concrete account entities extend
      type: object
      allOf:
        - $ref: '#/components/schemas/AccountDescriptor'
        - type: object
          properties:
            parentAccountId:
              description: >-
                Long-term persistent identity of the parent account. This is
                used to group accounts
              $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
            lineOfBusiness:
              description: >-
                The line of business, such as consumer, consumer joint, small
                business, corporate, etc.
              type: string
            routingTransitNumber:
              type: string
              description: >-
                The routing transit number (RTN) associated with the account number at the owning institution.
                FDX v6.3 adds separate bankInstitutionId and bankTransitId properties and deprecates the prior
                approach to use this field for concatenated Canadian institution IDs
            balanceType:
              $ref: '#/components/schemas/BalanceType'
              description: >-
                ASSET (positive transaction amount increases balance), LIABILITY
                (positive transaction amount decreases balance)
            contact:
              $ref: '#/components/schemas/AccountContact'
              description: >-
                Contact information associated with this account.
                Provider has the option to return contact in the Contact endpoint
              required: false
            interestRate:
              type: number
              description: Interest Rate of Account
            interestRateType:
              $ref: '#/components/schemas/InterestRateType'
              description: FIXED or VARIABLE
            interestRateAsOf:
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
              description: Date of account's interest rate
            priorInterestRate:
              type: number
              description: Previous Interest Rate of Account
            interestRateIndex:
              type: string
              description: >-
                Variable rate index name such as
                EONIA, EURIBOR, EURREPO, FEFUND, LIBOR, PRIME, SOFR, SONIA, etc.
            earlyPenaltyFlag:
              type: boolean
              description: Flag that indicates if there is an early penalty for withdrawal/payoff
            transferIn:
              type: boolean
              description: Account is eligible for incoming transfers
            transferOut:
              type: boolean
              description: Account is eligible for outgoing transfers
            billPayStatus:
              $ref: '#/components/schemas/AccountBillPayStatus'
              description: Defines account's ability to participate in bill payments
            micrNumber:
              $ref: './fdxapi.components.yaml#/components/schemas/String64'
              description: MICR Number
            lastActivityDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Date that last transaction occurred on account
            rewardProgramId:
              $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
              description: Long-term persistent identity of rewards program associated with this account
            transactionsIncluded:
              type: boolean
              description: >-
                Default is false. If present and true, a call to retrieve
                transactions will not return any further details about this
                account. This is an optimization that allows an FDX API server
                to return transactions and account details in a single call
            domicile:
              $ref: './fdxapi.components.yaml#/components/schemas/Domicile'
              description: The country and region of the account's legal jurisdiction
            bankInstitutionId:
              type: string
              pattern: ^[0-9]{3}$
              description: >-
                The Canadian 3-digit Institution (FID) associated with the account number, including leading zeros
            bankTransitId:
              type: string
              pattern: ^[0-9]{5}$
              description: >-
                The Canadian 5-digit Transit number associated with the account number, including leading zeros

    AccountContact:
      title: Account Contact entity
      description: Contact information for the account
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/Contacts'
        - type: object
          properties:
            holders:
              type: array
              items:
                $ref: '#/components/schemas/AccountHolder'
              description: Owners of the account

    AccountDescriptor:
      title: Account Descriptor entity
      description: This descriptor provides minimal information about the account for use in lightweight arrays
      type: object
      required:
        - accountCategory
      discriminator:
        propertyName: accountCategory
      properties:
        accountCategory:
          $ref: '#/components/schemas/AccountCategory'
          description: The entity type of this Account
        accountId:
          description: >-
            Long-term persistent identity of the account, though not an account number.
            This identity must be unique to the owning institution
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        error:
          description: Present if an error was encountered while retrieving this account
          $ref: './fdxapi.components.yaml#/components/schemas/Error'
        accountType:
          $ref: './fdxapi.components.yaml#/components/schemas/AccountType'
          description: Account type
        accountNumber:
          description: >-
            Full account number for the end user for this account at the owning institution.
            If not masked this is sensitive data which should only be exchanged if encrypted.
            For detailed information on implementing encryption see "Part 4 End to End Encryption"
            of the FDX API Security Model document in the Security section of the latest
            FDX Release download
          type: string
        accountNumberDisplay:
          description: >-
            Account display number for the end user's handle at the owning
            institution. This is to be displayed by the Interface Provider
          type: string
        productName:
          type: string
          description: Marketed product name for this account. Used in UIs to assist in account selection
        nickname:
          description: Name given by the user. Used in UIs to assist in account selection
          type: string
        status:
          description: >-
            Account status. Suggested values are: OPEN, CLOSED, PENDINGOPEN, PENDINGCLOSE,
            PAID, DELINQUENT, NEGATIVECURRENTBALANCE, RESTRICTED
          $ref: '#/components/schemas/AccountStatus'
        description:
          type: string
          description: Description of account
        accountOpenDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Account opening date
        accountCloseDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Account closing date
        currency:
          $ref: '#/components/schemas/Currency'
          description: Account currency
        fiAttributes:
          type: array
          description: Array of Financial institution-specific attributes
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'

    AccountHolder:
      title: Account Holder entity
      description: >-
        Extends `Customer` and adds a `relationship` field to define the customer's
        relationship with an account
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/Customer'
        - type: object
          properties:
            relationship:
              $ref: './fdxapi.components.yaml#/components/schemas/AccountHolderRelationship'
              description: "Customer's relationship to the account"

    AccountPaymentNetwork:
      title: Payment Network Supported by Account
      description: This provides details required to execute a transaction against the account
        within the payment network
      type: object
      properties:
        bankId:
          type: string
          description: >-
            Bank identifier used by the payment network. Typically the 9-digit routing transit number (RTN)
            associated with the account number at a US institution. FDX v6.3 adds separate bankInstitutionId
            and bankTransitId properties and deprecates the prior approach to use this field for concatenated
            Canadian institution IDs
        identifier:
          type: string
          description: >-
            The number used to identify the account within the payment network.
            If identifierType is ACCOUNT_NUMBER, this is the account number;
            if identifierType is TOKENIZED_ACCOUNT_NUMBER, this is a tokenized account number
        identifierType:
          $ref: '#/components/schemas/PaymentNetworkIdentifierType'
          description: Type of identifier, ACCOUNT_NUMBER or TOKENIZED_ACCOUNT_NUMBER
        type:
          $ref: '#/components/schemas/PaymentNetworkType'
          description: Type of Canadian or U.S. payment network,
            CA_ACSS, CA_LVTS, US_ACH, US_CHIPS, US_FEDWIRE, US_RTP
        transferIn:
          type: boolean
          description: Can transfer funds to the account using this information
        transferOut:
          type: boolean
          description: Can transfer funds from the account using this information
        supportsRequestForPayment:
          type: boolean
          description: Can receive Request for Payments
        transferLimits:
          description: The amount limits for transfers
          $ref: '#/components/schemas/TransferLimits'
        bankInstitutionId:
          type: string
          pattern: ^[0-9]{3}$
          description: >-
            The Canadian 3-digit Institution (FID) associated with the account number, including leading zeros
        bankTransitId:
          type: string
          pattern: ^[0-9]{5}$
          description: >-
            The Canadian 5-digit Transit number associated with the account number, including leading zeros

    AccountPaymentNetworkList:
      title: Array of account payment networks
      description: An optionally paginated array of payment networks supported by the account
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            paymentNetworks:
              type: array
              items:
                $ref: '#/components/schemas/AccountPaymentNetwork'
              description: Array of payment networks

    Accounts:
      title: Accounts entity
      description: An optionally paginated array of accounts
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            accounts:
              type: array
              description: >-
                An array of accounts with entity types dependent on the
                account type (deposit, investment, loan, line of credit,
                annuity, insurance, commercial, or digital wallet)
              items:
                $ref: '#/components/schemas/AccountWithDetails'

    AccountWithDetails:
      title: Account With Details entity
      description: An instance of an account with full details
      type: object
      discriminator:
        propertyName: accountCategory
        mapping:
          ANNUITY_ACCOUNT: '#/components/schemas/AnnuityAccount'
          COMMERCIAL_ACCOUNT: '#/components/schemas/CommercialAccount'
          DEPOSIT_ACCOUNT: '#/components/schemas/DepositAccount'
          DIGITAL_WALLET: '#/components/schemas/DigitalWallet'
          INSURANCE_ACCOUNT: '#/components/schemas/InsuranceAccount'
          INVESTMENT_ACCOUNT: '#/components/schemas/InvestmentAccount'
          LOAN_ACCOUNT: '#/components/schemas/LoanAccount'
          LOC_ACCOUNT: '#/components/schemas/LineOfCreditAccount'
      oneOf:
        - $ref: '#/components/schemas/AnnuityAccount'
        - $ref: '#/components/schemas/CommercialAccount'
        - $ref: '#/components/schemas/DepositAccount'
        - $ref: '#/components/schemas/DigitalWallet'
        - $ref: '#/components/schemas/InsuranceAccount'
        - $ref: '#/components/schemas/InvestmentAccount'
        - $ref: '#/components/schemas/LineOfCreditAccount'
        - $ref: '#/components/schemas/LoanAccount'

    AnnuityAccount:
      title: Annuity Account entity
      description: An annuity account type
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            payoutType:
              $ref: '#/components/schemas/PayoutType'
              description: Indicates type of payout such as immediate or deferred
            policyProductType:
              $ref: '#/components/schemas/PolicyProductType'
              description: The type of annuity product, e.g. Fixed or Variable
            payoutAmount:
              type: number
              description: Amount paid out, based on mode frequency
            payoutMode:
              $ref: '#/components/schemas/PayoutMode'
              description: Frequency of annuity payments
            payoutStartDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Date the payout starts
            payoutEndDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Date the payout ends
            numberModalPayouts:
              type: integer
              description: Total number of payouts
            surrenderValue:
              type: number
              description: Cash surrender value (net) available if contract is surrendered
            payoutChangePercentage:
              type: number
              description: Percentage of the accumulated value to be paid to the payee each year; used exclusive of payoutChangeAmount
            payoutChangeAmount:
              type: number
              description: Incremental modal amount (positive or negative) by which the payout amount will be changed; used exclusive of payoutPercentage
            periodCertainType:
              $ref: '#/components/schemas/PeriodCertainType'
              description: The number of modal periods comprising the duration of the certain period of an annuity payout

    AssetTransferNetwork:
      title: Asset Transfer Network
      description: Information required to facilitate asset transfer from this account
      type: object
      properties:
        identifier:
          type: string
          description: >-
            The number used to identify the account within the asset transfer network.
            If identifierType is ACCOUNT_NUMBER, this is the account number;
            if identifierType is TOKENIZED_ACCOUNT_NUMBER, this is a tokenized account number
        identifierType:
          description: Type of identifier
          $ref: '#/components/schemas/PaymentNetworkIdentifierType'
        institutionName:
          description: The name of the institution holding the account
          type: string
        institutionId:
          description: >-
            Institution identifier used by the asset transfer network ie. the Depository Trust and
            Clearing Corporation code for the institution holding the account
          type: string
        type:
          description: Type of asset transfer
          $ref: '#/components/schemas/AssetTransferType'
        jointAccount:
          description: Whether this account has joint owners
          type: boolean

    AssetTransferNetworkList:
      title: Asset Transfer Network List
      description: An array of asset transfer network details for this account
      type: object
      properties:
        assetTransferNetworks:
          description: Array of asset transfer networks
          type: array
          items:
            $ref: '#/components/schemas/AssetTransferNetwork'

    Bills:
      title: Bills entity
      description: The payments due on an account
      type: object
      properties:
        totalPaymentDue:
          type: number
          description: >-
            Total payment due or next payment due.  Monthly payment due for loans
        minimumPaymentDue:
          type: number
          description: The minimum amount which is due
        dueDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: The date that the payment is due
        autoPayEnabled:
          type: boolean
          description: Whether the user's bill is paid automatically
        autoPayAmount:
          type: number
          description: The amount of money the user has set to autopay this bill
        autoPayDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: The date the autopayment is set to trigger for this bill
        pastDueAmount:
          type: number
          description: >-
            The amount that the user should have already paid. The value is negative if
            user owes money
        lastPaymentAmount:
          type: number
          description: The amount of the most recent payment
        lastPaymentDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: The date of most recent payment
        statementBalance:
          type: number
          description: >-
            The amount of the last statement.  The value is negative if the user owes money
        statementDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: The date the statement was issued

    CardArt:
      title: Card Art entity
      description: Art associated with the card
      type: object
      properties:
        label:
          type: string
          description: Display label for the specific image
        imageUri:
          type: string
          format: uri
          description: >-
            The [URI](https://datatracker.ietf.org/doc/html/rfc2397) link
            of a PNG, JPG or GIF image with proportions defined by
            [ISO 8710 ID-1](https://en.wikipedia.org/wiki/ISO/IEC_7810) with 340x210 ratio and
            width no greater than 512 pixels. The image at this URI must be accessible at all
            times, with no additional authentication headers. Typically this is an image resource
            located in the data provider's public web site or Content Delivery Network

    CommercialAccount:
      title: Commercial Account entity
      description: Information for a commercial account type
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            balanceAsOf:
              description: As-of date of balances
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
            openingLedgerBalance:
              type: number
              description: Opening ledger balance
            closingLedgerBalance:
              type: number
              description: Closing ledger balance
            currentLedgerBalance:
              type: number
              description: Current ledger balance
            openingAvailableBalance:
              type: number
              description: Opening available balance
            currentAvailableBalance:
              type: number
              description: Current available balance
            closingAvailableBalance:
              type: number
              description: Closing available balance
            nextDayAvailableBalance:
              type: number
              description: Next day's available balance
            twoDaysPlusAvailableBalance:
              type: number
              description: Two days out's available balance
            numberOfOutstandingCredits:
              type: integer
              description: Number of outstanding credit transactions
            outstandingCreditsAmount:
              type: number
              description: Total amount of outstanding credits
            numberOfOutstandingDebits:
              type: integer
              description: Number of outstanding debit transactions
            outstandingDebitsAmount:
              type: number
              description: Total amount of outstanding debits
            transactions:
              type: array
              description: >-
                Transactions on the commercial account.
                Provider has the option to return transactions in the Transactions endpoint
              required: false
              items:
                $ref: '#/components/schemas/CommercialTransaction'
            commercialBalances:
              type: array
              description: A list of specific treasury management defined balances
              items:
                $ref: '#/components/schemas/CommercialBalance'

    CommercialBalance:
      title: Commercial Balance entity
      description: A specific treasury management defined balance
      type: object
      properties:
        commercialCode:
          $ref: '#/components/schemas/CommercialCode'
          description: The code for a specific treasury management defined field
        amount:
          type: number
          description: The treasury management balance amount
        memo:
          type: string
          description: Memo field for the treasury management balance amount

    CommercialCode:
      title: Commercial Code entity
      description: >-
        The code for a specific treasury management defined field.

        The [X9 BTRS/BTR3 standard](https://x9.org/standards/btrs/) (formerly named BAI2)
        for corporate and treasury data elements is proposed to provide the basis of
        (or starting point for) representing summary, account, and transaction codes
        for the Corp/Treasury Entity, subject to any necessary modifications useful
        to the members of the FDX consortium and users of the API specification
      type: object
      properties:
        type:
          $ref: '#/components/schemas/TreasuryManagementType'
          description: The source of Treasury Management account definition; one of BAI, BTRS, ISO, SWIFT
        code:
          type: string
          description: The code of the Treasury Management defined field

    CommercialTransaction:
      title: Commercial Transaction entity
      description: A transaction on a commercial account type
      type: object
      allOf:
        - $ref: '#/components/schemas/Transaction'
        - type: object
          properties:
            immediateAvailableBalance:
              type: number
              description: Immediate available balance
            nextDayAvailableBalance:
              type: number
              description: Next day available balance
            twoDaysPlusAvailableBalance:
              type: number
              description: Two days plus available balance
            referenceBankId:
              type: string
              description: Reference bank id
            referenceBranchId:
              type: string
              description: Reference branch id
            referenceCustomerId:
              type: string
              description: Reference customer id
            commercialCode:
              $ref: '#/components/schemas/CommercialCode'
              description: The code for a specific treasury management defined field
            memo:
              type: string
              description: Memo field for the commercial transaction

    Contribution:
      title: Contribution entity
      description: Contribution information to an investment account
      type: object
      properties:
        securityId:
          type: string
          description: Unique identifier of security
        securityIdType:
          $ref: '#/components/schemas/SecurityIdType'
          description: CINS, CMC, CME, CUSIP, ISIN, ITSA, NASDAQ, SEDOL, SICC, VALOR, WKN
        employerMatchPercentage:
          type: number
          description: Employer contribution match percentage
        employerMatchAmount:
          type: number
          description: Employer contribution match amount
        employeePreTaxAmount:
          type: number
          description: Employee pre-tax contribution amount
        employeePreTaxPercentage:
          type: number
          description: Employee pre-tax contribution percentage
        employeeAfterTaxAmount:
          type: number
          description: Employee after tax contribution amount
        employeeAfterTaxPercentage:
          type: number
          description: Employee after tax contribution percentage
        employeeRothTaxAmount:
          type: number
          description: Employee Roth contribution amount
        employeeRothTaxPercentage:
          type: number
          description: Employee Roth contribution percentage
        employeeDeferPreTaxAmount:
          type: number
          description: Employee defer pre-tax contribution match amount
        employeeDeferPreTaxPercentage:
          type: number
          description: Employee defer pre-tax contribution match percentage
        employeeYearToDate:
          type: number
          description: Employee total year to date contribution
        employerYearToDate:
          type: number
          description: Employer total year to date contribution
        rolloverContributionPercentage:
          type: number
          description: Rollover contribution percentage
        rolloverContributionAmount:
          type: number
          description: Rollover contribution Amount
        catchUpContribution:
          type: boolean
          description: If true, indicates that this is a catch up contribution

    Currency:
      title: Currency entity
      description: Represents an international currency
      type: object
      properties:
        currencyRate:
          type: number
          description: Currency rate between original and converted currency
        currencyCode:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso4217CurrencyCode'
          description: ISO 4217 currency code
        originalCurrencyCode:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso4217CurrencyCode'
          description: Original ISO 4217 currency code

    DebtSecurity:
      title: Debt Security entity
      description: An investment in a debt security
      type: object
      allOf:
        - $ref: '#/components/schemas/Security'
        - type: object
          properties:
            parValue:
              type: number
              description: Par value amount
            debtType:
              $ref: '#/components/schemas/DebtType'
              description: Debt type. One of COUPON, ZERO
            debtClass:
              $ref: '#/components/schemas/DebtClass'
              description: Classification of debt. One of TREASURY, MUNICIPAL, CORPORATE, OTHER
            couponRate:
              type: number
              description: Bond coupon rate for next closest call date
            couponDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Maturity date for next coupon
            couponMatureFrequency:
              $ref: '#/components/schemas/CouponMatureFrequency'
              description: When coupons mature. One of MONTHLY, QUARTERLY,  SEMIANNUAL, ANNUAL, OTHER
            callPrice:
              type: number
              description: Bond call price
            yieldToCall:
              type: number
              description: Yield to next call
            callDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Next call date
            callType:
              $ref: '#/components/schemas/CallType'
              description: Type of next call. One of CALL, PUT, PREFUND, MATURITY
            yieldToMaturity:
              type: number
              description: Yield to maturity
            bondMaturityDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Bond maturity date

    DepositAccount:
      title: Deposit Account entity
      description: Information for a deposit account type
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            balanceAsOf:
              description: As-of date of balances
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
            currentBalance:
              type: number
              description: Balance of funds in account
            openingDayBalance:
              type: number
              description: Day's opening fund balance
            availableBalance:
              type: number
              description: Balance of funds available for use
            annualPercentageYield:
              type: number
              description: Annual Percentage Yield
            interestYtd:
              type: number
              description: YTD Interest
            term:
              type: integer
              description: Term of CD in months
            maturityDate:
              description: Maturity date for CDs
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            transactions:
              type: array
              description: >-
                Transactions on the deposit account.
                Provider has the option to return transactions in the Transactions endpoint
              required: false
              items:
                $ref: '#/components/schemas/DepositTransaction'

    DepositTransaction:
      title: Deposit Transaction entity
      description: A transaction on a deposit account type
      type: object
      allOf:
        - $ref: '#/components/schemas/Transaction'
        - type: object
          properties:
            transactionType:
              $ref: '#/components/schemas/DepositTransactionType'
              description: >-
                CHECK, WITHDRAWAL, TRANSFER, POSDEBIT, ATMWITHDRAWAL,
                BILLPAYMENT, FEE, DEPOSIT, ADJUSTMENT, INTEREST,
                DIVIDEND, DIRECTDEPOSIT, ATMDEPOSIT, POSCREDIT
            payee:
              $ref: './fdxapi.components.yaml#/components/schemas/String255'
              deprecated: true
              description: Payee name.
                This is deprecated and will be removed in a future major release in place of `transactionPayee`
                which provides detailed information of a payee's name and place of business on the `Transaction` entity
            checkNumber:
              type: integer
              description: Check number

    DigitalWallet:
      title: Digital Wallet account entity
      description: Information for a digital wallet account
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            balanceAsOf:
              description: As-of date of balances
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
            currentBalance:
              type: number
              description: Balance of funds in account
            openingDayBalance:
              type: number
              description: Day's opening fund balance
            availableBalance:
              type: number
              description: Balance of funds available for use
            annualPercentageYield:
              type: number
              description: Annual Percentage Yield
            interestYtd:
              type: number
              description: YTD Interest
            transactions:
              type: array
              description: >-
                Transactions on the digital wallet.
                Provider has the option to return transactions in the Transactions endpoint
              required: false
              items:
                $ref: '#/components/schemas/DigitalWalletTransaction'

    DigitalWalletTransaction:
      title: Digital Wallet Transaction entity
      description: A transaction on a digital wallet account
      type: object
      allOf:
        - $ref: '#/components/schemas/Transaction'
        - type: object
          properties:
            transactionType:
              $ref: '#/components/schemas/DigitalWalletTransactionType'
              description: >-
                ADJUSTMENT, BILL_PAYMENT, CREDIT, DEBIT, DEPOSIT, DIRECT_DEPOSIT, DIVIDEND, FEE,
                INTEREST, MERCHANT_PAYMENT, MERCHANT_REFUND, TRANSFER_IN, TRANSFER_OUT,
                WITHDRAWAL
            payee:
              $ref: './fdxapi.components.yaml#/components/schemas/String255'
              deprecated: true
              description: Payee name.
                This is deprecated and will be removed in a future major release in place of `transactionPayee`
                which provides detailed information of a payee's name and place of business on the `Transaction` entity

    FiPortion:
      title: FI Portion entity
      description: Financial Institution-specific asset allocation
      type: object
      properties:
        assetClass:
          type: string
          description: Financial Institution-specific asset class
        percent:
          type: number
          description: Percentage of asset class that falls under this asset

    Holding:
      title: Holding entity
      description: A holding in an investment account
      type: object
      properties:
        holdingId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long term persistent identity of the holding
        securityIds:
          description: Unique identifiers for the security
          type: array
          items:
            $ref: '#/components/schemas/SecurityId'
        holdingName:
          type: string
          description: Holding name or security name
        holdingType:
          $ref: '#/components/schemas/HoldingType'
          description: ANNUITY, BOND, CD, DIGITALASSET, MUTUALFUND, OPTION, OTHER, STOCK
        holdingSubType:
          $ref: '#/components/schemas/HoldingSubType'
          description: MONEYMARKET, CASH
        positionType:
          $ref: '#/components/schemas/PositionType'
          description: LONG, SHORT
        heldInAccount:
          $ref: '#/components/schemas/HeldInAccount'
          description: Sub-account CASH, MARGIN, SHORT, OTHER
        description:
          type: string
          description: The description of the holding
        symbol:
          type: string
          description: Ticker / Market symbol
        originalPurchaseDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date of original purchase
        purchasedPrice:
          type: number
          description: Price of holding at the time of purchase
        currentAmortizationFactor:
          type: number
          description: >-
            Ranges from 0.0 - 1.0 indicates the adjustment to the calculation of the market
            value. 'currentUnitPrice * quantity * currentAmortizationFactor =  marketValue'
          minimum: 0.0
          maximum: 1.0
          default: 1.0
        currentUnitPrice:
          type: number
          description: Current unit price
        changeInPrice:
          type: number
          description: Change in current price compared to previous day's close
        currentUnitPriceDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Current unit price as of date
        units:
          type: number
          description: Required for stock, mutual funds. Number of shares (with decimals)
        marketValue:
          type: number
          description: Market value at the time of data retrieved
        faceValue:
          type: number
          description: Required for bonds. Face value at the time of data retrieved
        averageCost:
          type: boolean
          description: Cost is average of all purchases for holding
        cashAccount:
          type: boolean
          description: >-
            If true, indicates that this holding is used to maintain proceeds
            from sales, dividends, and other cash postings to the investment account
        rate:
          type: number
          description: For CDs, bonds, and other rate based holdings
        expirationDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: For CDs, bonds, and other time-based holdings
        inv401kSource:
          $ref: '#/components/schemas/Inv401kSourceType'
          description: >-
            Source for money for this security. One of PRETAX, AFTERTAX, MATCH,
            PROFITSHARING, ROLLOVER, OTHERVEST, OTHERNONVEST
        currency:
          $ref: '#/components/schemas/Currency'
          description: Currency information if it is different from Account entity
        assetClasses:
          type: array
          description: Percent breakdown by asset class
          items:
            $ref: '#/components/schemas/Portion'
        fiAssetClasses:
          type: array
          description: Percent breakdown by FI-specific asset class percentage breakdown
          items:
            $ref: '#/components/schemas/FiPortion'
        fiAttributes:
          type: array
          description: Array of FI-specific attributes
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'
        taxLots:
          type: array
          description: Breakdown by tax lot
          items:
            $ref: '#/components/schemas/TaxLot'
        digitalUnits:
          type: string
          description: Specify units to full precision with unlimited digits after decimal point
        security:
          description: The security of the Holding; one of DebtSecurity, MutualFundSecurity
            OptionSecurity, OtherSecurity, StockSecurity or SweepSecurity
          discriminator:
            propertyName: securityCategory
            mapping:
              DEBT_SECURITY: '#/components/schemas/DebtSecurity'
              MUTUAL_FUND_SECURITY: '#/components/schemas/MutualFundSecurity'
              OPTION_SECURITY: '#/components/schemas/OptionSecurity'
              OTHER_SECURITY: '#/components/schemas/OtherSecurity'
              STOCK_SECURITY: '#/components/schemas/StockSecurity'
              SWEEP_SECURITY: '#/components/schemas/SweepSecurity'
          oneOf:
            - $ref: '#/components/schemas/DebtSecurity'
            - $ref: '#/components/schemas/MutualFundSecurity'
            - $ref: '#/components/schemas/OptionSecurity'
            - $ref: '#/components/schemas/OtherSecurity'
            - $ref: '#/components/schemas/StockSecurity'
            - $ref: '#/components/schemas/SweepSecurity'

    InsuranceAccount:
      title: Insurance Account entity
      description: An insurance account type and properties such as category, premium,
        and payment term information
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            policyPremium:
              type: number
              description: The amount of the user's premium
            policyPremiumTerm:
              description: The payment term for the premium
              $ref: '#/components/schemas/InsurancePremiumTerm'
            policyStartDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: The premium start date
            policyStatus:
              $ref: '#/components/schemas/PolicyStatus'
              description: The status of an insurance policy account
            policyEndDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: The premium end date
            policyCoverageAmount:
              type: number
              description: Total amount of money the user is insured for
            transactions:
              type: array
              description: >-
                Transactions on the insurance account.
                Provider has the option to return transactions in the Transactions endpoint
              required: false
              items:
                $ref: '#/components/schemas/InsuranceTransaction'
            bills:
              type: array
              description: Payments due on the insurance account
              items:
                $ref: '#/components/schemas/Bills'

    InsuranceTransaction:
      title: Insurance Transaction entity
      description: An insurance transaction type
      type: object
      allOf:
        - $ref: '#/components/schemas/Transaction'
        - type: object
          properties:
            transactionType:
              description: The type of an insurance transaction
              $ref: '#/components/schemas/InsuranceTransactionType'

    InvestmentAccount:
      title: Investment Account entity
      description: An investment account type and information such as balances, transactions,
        holdings and privileges
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            balanceAsOf:
              description: As-of date for balances
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
            allowedCheckWriting:
              type: boolean
              description: Check writing privileges
            allowedOptionTrade:
              type: boolean
              description: Allowed to trade options
            currentValue:
              type: number
              description: Total current value of all investments
            holdings:
              type: array
              description: Holdings in the investment account
              items:
                $ref: '#/components/schemas/Holding'
            openOrders:
              type: array
              description: Open orders in the investment account
              items:
                $ref: '#/components/schemas/OpenOrder'
            contribution:
              type: array
              description: >-
                Describes how new contributions are distributed among the
                available securities
              items:
                $ref: '#/components/schemas/Contribution'
            vesting:
              type: array
              description: >-
                Provides the past, present, and future vesting schedule and percentages
              items:
                $ref: '#/components/schemas/Vesting'
            investmentLoans:
              type: array
              description: Investment loans in the account
              items:
                $ref: '#/components/schemas/InvestmentLoan'
            availableCashBalance:
              description: >-
                Cash balance across all sub-accounts. Should include sweep funds
              type: number
            margin:
              type: boolean
              description: Margin trading is allowed
            marginBalance:
              type: number
              description: Margin balance
            shortBalance:
              type: number
              description: Short balance
            rolloverAmount:
              type: number
              description: Rollover amount
            employerName:
              type: string
              description: Name of the employer in investment 401k Plan
            brokerId:
              type: string
              description: Unique identifier FI
            planId:
              type: string
              description: Plan number for Investment 401k plan
            calendarYearFor401K:
              type: integer
              description: The calendar year for this 401k account
            balanceList:
              type: array
              description: List of balances. Aggregate of name value pairs
              items:
                $ref: '#/components/schemas/InvestmentBalance'
            dailyChange:
              type: number
              description: Daily change
            percentageChange:
              type: number
              description: Percentage change
            transactions:
              type: array
              description: >-
                Transactions on the investment account.
                Provider has the option to return transactions in the Transactions endpoint
              required: false
              items:
                $ref: '#/components/schemas/InvestmentTransaction'
            pensionSource:
              type: array
              description: Pension sources in the investment account
              items:
                $ref: '#/components/schemas/PensionSource'

    InvestmentBalance:
      title: Investment Balance entity
      description: A point-in-time balance of the investment account
      type: object
      properties:
        balanceName:
          type: string
          description: Name of the balance
        balanceDescription:
          type: string
          description: Description of balance
        balanceType:
          $ref: '#/components/schemas/InvestmentBalanceType'
          description: AMOUNT, PERCENTAGE
        balanceValue:
          type: number
          description: Value of named balance
        balanceDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date as of this balance
        currency:
          $ref: '#/components/schemas/Currency'
          description: Currency if different from that of account

    InvestmentLoan:
      title: Investment Loan entity
      description: Any loan information against an investment account
      type: object
      properties:
        loanId:
          type: string
          description: Unique identifier for this loan
        loanDescription:
          type: string
          description: Description of loan
        initialLoanBalance:
          type: number
          description: Initial loan balance amount
        loanStartDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Start date of the loan
        currentLoanBalance:
          type: number
          description: Current loan principal balance amount
        dateAsOf:
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
          description: Date and time of current loan balance
        loanRate:
          type: number
          description: Loan annual interest rate for the loan
        loanPaymentAmount:
          type: number
          description: Loan payment amount
        loanPaymentFrequency:
          $ref: '#/components/schemas/LoanPaymentFrequency'
          description: >-
            WEEKLY, BIWEEKLY, TWICEMONTHLY, MONTHLY, FOURWEEKS, BIMONTHLY,
            QUARTERLY, SEMIANNUALLY, ANNUALLY, OTHER
        loanPaymentInitial:
          type: number
          description: Initial number of loan payments
        loanPaymentsRemaining:
          type: integer
          description: Remaining number of loan payments
        loanMaturityDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Expected loan end date
        loanInterestToDate:
          type: number
          description: Total interest paid to date on this loan
        loanTotalProjectedInterest:
          type: number
          description: Total projected interest to be paid on this loan
        loanNextPaymentDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: The next payment date for the loan

    InvestmentTransaction:
      title: Investment Transaction entity
      description: Specific transaction information
      type: object
      allOf:
        - $ref: '#/components/schemas/Transaction'
        - type: object
          properties:
            transactionType:
              $ref: '#/components/schemas/InvestmentTransactionType'
              description: >-
                PURCHASED, SOLD, PURCHASEDTOCOVER, ADJUSTMENT, PURCHASETOOPEN, PURCHASETOCLOSE,
                SOLDTOOPEN, SOLDTOCLOSE, INTEREST, MARGININTEREST, REINVESTOFINCOME, RETURNOFCAPITAL,
                TRANSFER, CONTRIBUTION, FEE, OPTIONEXERCISE, OPTIONEXPIRATION, DIVIDEND, DIVIDENDREINVEST,
                SPLIT, CLOSURE, INCOME, EXPENSE, CLOSUREOPT, INVEXPENSE, JRNLSEC, JRNLFUND, OTHER, DIV,
                SRVCHG, DEP, DEPOSIT, ATM, POS, XFER, CHECK, PAYMENT, CASH, DIRECTDEP, DIRECTDEBIT, REPEATPMT
            shares:
              type: number
              description: >-
                Required for stock, mutual funds. Number of shares (with decimals).
                Negative numbers indicate securities are being removed from the account
            faceValue:
              type: number
              description: Cash value for bonds
            price:
              type: number
              description: Unit purchase price
            securityId:
              type: string
              description: Unique identifier of security
            securityIdType:
              $ref: '#/components/schemas/SecurityIdType'
              description: CINS, CMC, CME, CUSIP, ISIN, ITSA, NASDAQ, SEDOL, SICC, VALOR, WKN
            securityType:
              $ref: '#/components/schemas/SecurityType'
              description: BOND, DEBT, DIGITALASSET, MUTUALFUND, OPTION, OTHER, STOCK, SWEEP
            symbol:
              type: string
              description: Ticker symbol
            markup:
              type: number
              description: Portion of unit price that is attributed to the dealer markup
            commission:
              type: number
              description: Transaction commission
            taxes:
              type: number
              description: Taxes on the trade
            fees:
              type: number
              description: Fees applied to the trade
            load:
              type: number
              description: Load on the transaction
            inv401kSource:
              $ref: '#/components/schemas/Inv401kSourceType'
              description: >-
                Source of money. One of PRETAX, AFTERTAX, MATCH, PROFITSHARING, ROLLOVER,
                OTHERVEST, OTHERNONVEST
            confirmationNumber:
              type: string
              description: Confirmation number of the transaction
            fractionalCash:
              type: number
              description: Cash for fractional units (used for stock splits)
            incomeType:
              $ref: '#/components/schemas/IncomeType'
              description: >-
                Type of investment income. One of CGLONG (capital gains-long term),
                CGSHORT (capital gains-short term), MISC
            oldUnits:
              type: number
              description: Number of shares before split
            splitRatioNumerator:
              type: number
              description: Split ratio numerator
            splitRatioDenominator:
              type: number
              description: Split ratio denominator
            newUnits:
              type: number
              description: Number of shares after split
            subAccountSec:
              $ref: '#/components/schemas/SubAccountType'
              description: Sub-account security Type. One of CASH, MARGIN, SHORT, OTHERS
            subAccountFund:
              $ref: '#/components/schemas/SubAccountType'
              description: From which account money came in. One of CASH, MARGIN, SHORT, OTHERS
            loanId:
              type: string
              description: For 401k accounts only. This indicates the transaction was due to a loan or
                a loan repayment
            loanPrincipal:
              type: number
              description: How much loan pre-payment is principal
            loanInterest:
              type: number
              description: How much loan pre-payment is interest
            payrollDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: The date for the 401k transaction was obtained in payroll
            priorYearContrib:
              type: boolean
              description: Indicates this buy was made using prior year's contribution
            withholding:
              type: number
              description: Federal tax withholding
            taxExempt:
              type: boolean
              description: Tax-exempt transaction
            gain:
              type: number
              description: For sales
            stateWithholding:
              type: number
              description: State tax withholding
            penalty:
              type: number
              description: Indicates amount withheld due to a penalty
            runningBalance:
              type: number
              description: Running balance of the position
            unitPrice:
              type: number
              description: >-
                Price per commonly-quoted unit. Does not include
                markup/markdown, unitprice. Share price for stocks, mutual
                funds, and others. Percentage of par for bonds. Per share (not
                contract) for options
            units:
              type: number
              description: >-
                For security-based actions other than stock splits, quantity.
                Shares for stocks, mutual funds, and others. Face value for bonds.
                Contracts for options
            unitType:
              $ref: '#/components/schemas/UnitType'
              description: SHARES, CURRENCY
            transactionReason:
              $ref: '#/components/schemas/TransactionReason'
              description: >-
                Reason for this transaction; CALL (the debt was called), SELL
                (the debt was sold), MATURITY (the debt reached maturity)
            accruedInterest:
              type: number
              description: Accrued interest
            transferAction:
              description: Transfer direction
              $ref: '#/components/schemas/TransferDirection'
            positionType:
              $ref: '#/components/schemas/PositionType'
              description: LONG, SHORT
            digitalUnits:
              type: string
              description: Full precision unit number, unlimited digits after decimal point
            settlementTimestamp:
              description: When the trade settled
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'

    LineItem:
      title: Line Item entity
      description: A line item within a transaction
      type: object
      properties:
        description:
          type: string
          description: The description of the line item
        amount:
          type: number
          description: The amount of money attributable to this line item
        checkNumber:
          type: integer
          description: Check number
        memo:
          $ref: './fdxapi.components.yaml#/components/schemas/String255'
          description: Secondary item description
        reference:
          type: string
          description: A reference number
        imageIds:
          type: array
          description: >-
            Array of image identifiers (unique to transaction) used to retrieve
            images of check or transaction receipt
          items:
            type: string
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'
          description: >-
            Links (unique to this Transaction) used to retrieve images of
            checks or transaction receipts, or invoke other APIs

    LineOfCreditAccount:
      title: Line of Credit Account entity
      description: A line of credit account
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            balanceAsOf:
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
              description: As-of date for balances
            creditLine:
              type: number
              description: Credit limit
            availableCredit:
              type: number
              description: Available credit
            nextPaymentAmount:
              type: number
              description: Amount of next payment.
                May differ from minimumPaymentAmount if the customer pays more than their minimum or out of cycle
            nextPaymentDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Due date of next payment.
                May differ from statementAmountDueDate if the customer pays out of cycle
            principalBalance:
              type: number
              description: Principal balance
            currentBalance:
              type: number
              description: Current balance of the line of credit
            minimumPaymentAmount:
              type: number
              description: Minimum payment amount from last statement balance,
                which is due at `statementAmountDueDate`
            lastPaymentAmount:
              type: number
              description: Last payment amount
            lastPaymentDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Last payment date
            pastDueAmount:
              type: number
              description: Past Due Amount
            lastStmtBalance:
              type: number
              description: Final balance amount at end of last statement
            lastStmtDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Last Statement Date
            statementAmountDueDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: The payment due date listed for the statement balance
            purchasesApr:
              type: number
              description: Purchases APR
            advancesApr:
              type: number
              description: Advances APR
            cashAdvanceLimit:
              type: number
              description: Cash advance limit
            availableCash:
              type: number
              description: Available cash
            financeCharges:
              type: number
              description: Finance charges
            cardNetwork:
              type: string
              description: Card network, e.g. "VISA", "MASTERCARD", "AMERICAN_EXPRESS", "DISCOVER", "INTERLINK", "STAR" etc.
            cardArt:
              $ref: '#/components/schemas/CardArt'
              description: Any Art associated to the Card related to the account
            transactions:
              type: array
              description: >-
                Transactions on the line-of-credit account.
                Provider has the option to return transactions in the Transactions endpoint
              required: false
              items:
                $ref: '#/components/schemas/LineOfCreditTransaction'

    LineOfCreditTransaction:
      title: Line of Credit Transaction entity
      description: A line of credit transaction
      type: object
      allOf:
        - $ref: '#/components/schemas/Transaction'
        - type: object
          properties:
            transactionType:
              $ref: '#/components/schemas/LineOfCreditTransactionType'
              description: CHECK, WITHDRAWAL, PAYMENT, FEE, ADJUSTMENT, INTEREST, PURCHASE
            checkNumber:
              type: integer
              description: Check number
            paymentDetails:
              $ref: './fdxapi.components.yaml#/components/schemas/PaymentDetails'
              description: Breakdown of payment details

    LoanAccount:
      title: Loan Account entity
      description: A loan account type
      type: object
      allOf:
        - $ref: '#/components/schemas/Account'
        - type: object
          properties:
            balanceAsOf:
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
              description: As-of date for balances
            principalBalance:
              type: number
              description: Principal balance of loan
            escrowBalance:
              type: number
              description: Escrow balance of loan
            originalPrincipal:
              type: number
              description: Original principal of loan
            originatingDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Loan origination date
            loanTerm:
              type: integer
              description: Term of loan in months
            totalNumberOfPayments:
              type: integer
              description: Total number of payments
            nextPaymentAmount:
              type: number
              description: Amount of next payment
            nextPaymentDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Date of next payment
            paymentFrequency:
              $ref: '#/components/schemas/PaymentFrequency'
              description: DAILY, WEEKLY, BIWEEKLY, SEMIMONTHLY, MONTHLY, SEMIANNUALLY, ANNUALLY
            compoundingPeriod:
              $ref: '#/components/schemas/CompoundingPeriod'
              description: DAILY, WEEKLY, BIWEEKLY, SEMIMONTHLY, MONTHLY, SEMIANNUALLY, ANNUALLY
            payOffAmount:
              type: number
              description: Payoff amount
            lastPaymentAmount:
              type: number
              description: Last payment amount
            lastPaymentDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Last payment date
            maturityDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Maturity date
            interestPaidYearToDate:
              type: number
              description: Interest paid year to date
            currentSchool:
              type: string
              description: Current school the student loan is connected to
            loanProviderName:
              type: string
              description: Name of the institution providing the loan
            transactions:
              type: array
              description: >-
                Transactions on the loan account.
                Provider has the option to return transactions in the Transactions endpoint
              required: false
              items:
                $ref: '#/components/schemas/LoanTransaction'

    LoanTransaction:
      title: Loan Transaction entity
      description: A transaction on a loan account
      type: object
      allOf:
        - $ref: '#/components/schemas/Transaction'
        - type: object
          properties:
            transactionType:
              $ref: '#/components/schemas/LoanTransactionType'
              description: PAYMENT, FEE, ADJUSTMENT, INTEREST
            paymentDetails:
              $ref: './fdxapi.components.yaml#/components/schemas/PaymentDetails'
              description: Breakdown of payment details

    MutualFundSecurity:
      title: Mutual Fund Security entity
      description: A mutual fund
      type: object
      allOf:
        - $ref: '#/components/schemas/Security'
        - type: object
          properties:
            mutualFundType:
              $ref: '#/components/schemas/MutualFundType'
              description: Mutual fund type. One of OPENEND, CLOSEEND, OTHER
            unitsStreet:
              type: number
              description: Units in the FI's street name, positive quantity
            unitsUser:
              type: number
              description: Units in user's name directly, positive  quantity
            reinvestDividends:
              type: boolean
              description: Reinvest dividends
            reinvestCapitalGains:
              type: boolean
              description: Reinvest capital gains
            yield:
              type: number
              description: Current yield reported as portion of the fund's assets
            yieldAsOfDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: As-of date for yield value

    OpenOrder:
      title: Open Order entity
      description: An open investment transaction order
      type: object
      properties:
        orderId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long-term persistent identity of the order. Id for this order transaction
        securityId:
          type: string
          description: Unique identifier of security
        securityIdType:
          $ref: '#/components/schemas/SecurityIdType'
          description: CINS, CMC, CME, CUSIP, ISIN, ITSA, NASDAQ, SEDOL, SICC, VALOR, WKN
        symbol:
          type: string
          description: Market symbol
        description:
          type: string
          description: Description of order
        units:
          type: number
          description: Number of units (shares or bonds etc.)
        orderType:
          $ref: '#/components/schemas/OrderType'
          description: >-
            Type of order. One of BUY, SELL, BUYTOCOVER, BUYTOOPEN, SELLTOCOVER,
            SELLTOOPEN,  SELLSHORT, SELLCLOSE
        orderDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Order date
        unitPrice:
          type: number
          description: Unit price
        unitType:
          $ref: '#/components/schemas/UnitType'
          description: Type of unit. One of SHARES, CURRENCY
        orderDuration:
          $ref: '#/components/schemas/OrderDuration'
          description: This order is good for DAY, GOODTILLCANCEL, IMMEDIATE
        subAccount:
          $ref: '#/components/schemas/SubAccountType'
          description: CASH, MARGIN, SHORT, OTHER
        limitPrice:
          type: number
          description: Limit price
        stopPrice:
          type: number
          description: Stop price
        inv401kSource:
          $ref: '#/components/schemas/Inv401kSourceType'
          description: >-
            For 401(k) accounts, source of money for this order. PRETAX,
            AFTERTAX, MATCH, PROFITSHARING, ROLLOVER, OTHERVEST, OTHERNONVEST.
            Default if not present is OTHERNONVEST

    OptionSecurity:
      title: Option Security entity
      description: An option
      type: object
      allOf:
        - $ref: '#/components/schemas/Security'
        - type: object
          properties:
            secured:
              $ref: '#/components/schemas/Secured'
              description: How the option is secured. One of NAKED, COVERED
            optionType:
              $ref: '#/components/schemas/OptionType'
              description: Option type. One of PUT, CALL
            strikePrice:
              type: number
              description: Strike price / Unit price
            expireDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Expiration date of option
            sharesPerContract:
              type: number
              description: Shares per contract

    OtherSecurity:
      title: Other Security entity
      description: Any other kind of security
      type: object
      allOf:
        - $ref: '#/components/schemas/Security'
        - type: object
          properties:
            typeDescription:
              type: string
              description: Description of other security

    PaymentNetworkOccurrenceTransferLimits:
      title: Occurrence based limits for a Payment Network
      description: This provides the occurrence-based limits applied to the account within the payment network
      type: object
      properties:
        transferMaxAmount:
          type: number
          description: Maximum limit of funds that can be transferred to/from the account using the timeframe limits
        transferRemainingAmount:
          type: number
          description: Remaining value of the maximum limit of funds that can be transferred to/from the account using the timeframe limits

    PaymentNetworkTimeframeTransferLimits:
      title: Timeframe based limits for a Payment Network
      description: This provides the time-based limits applied to the account within the payment network
      type: object
      properties:
        resetsOn:
          type: string
          format: date-time
          description: Date/time at which this timeframe will reset next
        transferMaxAmount:
          type: number
          description: Maximum limit of funds that can be transferred to/from the account in this timeframe
        transferRemainingAmount:
          type: number
          description: Remaining value of the maximum limit of funds that can be transferred to/from the account in this timeframe
        maxOccurrence:
          type: integer
          description: Maximum number of transfers that can be made in this direction for this timeframe
        remainingOccurrence:
          type: integer
          description: Remaining number of transfers that can be made in this direction for this timeframe

    PaymentNetworkTransferLimits:
      title: Time and occurrence based transfer limits
      description: The transfer amount limits for each timeframe or occurrence
      type: object
      properties:
        day:
          $ref: '#/components/schemas/PaymentNetworkTimeframeTransferLimits'
          description: The transfer limits for the current day
        week:
          $ref: '#/components/schemas/PaymentNetworkTimeframeTransferLimits'
          description: The transfer limits for the current week
        month:
          $ref: '#/components/schemas/PaymentNetworkTimeframeTransferLimits'
          description: The transfer limits for the current month
        year:
          $ref: '#/components/schemas/PaymentNetworkTimeframeTransferLimits'
          description: The transfer limits for the current year
        transaction:
          $ref: '#/components/schemas/PaymentNetworkOccurrenceTransferLimits'
          description: The transfer limits taking effect from all the timeframe limits

    PensionSource:
      title: Pension Source entity
      description: The source of pension funds
      type: object
      properties:
        displayName:
          type: string
          description: Name of the source
        amount:
          type: number
          description: Benefit Amount
        paymentOption:
          type: string
          description: Form of payment
        asOfDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date benefit was calculated
        frequency:
          $ref: '#/components/schemas/PaymentFrequency'
          description: ANNUALLY, BIWEEKLY, DAILY, MONTHLY, SEMIANNUALLY, SEMIMONTHLY, WEEKLY
        startDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Assumed retirement date. As of date amount is payable

    Portion:
      title: Portion entity
      description: An asset allocation with class and percentage
      type: object
      properties:
        assetClass:
          $ref: '#/components/schemas/AssetClass'
          description: The asset class for this allocation
        percent:
          type: number
          description: The percentage of this allocation

    RewardBalance:
      title: Reward Balance entity
      description: Reward program balance
      type: object
      properties:
        name:
          type: string
          description: Name used to denominate the balance
        type:
          $ref: '#/components/schemas/RewardType'
          description: The type of the reward balance - CASHBACK, MILES, POINTS
        balance:
          type: number
          description: Total units available for redemption at time of download
        accruedYtd:
          type: number
          description: Total units accrued in the current program year at time of download
          minimum: 0
        redeemedYtd:
          type: number
          description: Total units redeemed in the current program year at time of download
          minimum: 0
        qualifying:
          type: boolean
          description: Balance used for qualifying purposes
          default: false
        fiAttributes:
          type: array
          description: Array of FI-specific attributes
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'

    RewardCategories:
      title: Reward Categories entity
      description: An optionally paginated array of reward categories
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            rewardCategories:
              description: Array of reward categories
              type: array
              items:
                $ref: '#/components/schemas/RewardCategory'
              uniqueItems: true

    RewardCategory:
      title: Reward Category entity
      description: Reward category used to calculate rewards on a transaction
      type: object
      properties:
        rewardProgramId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long term persistent identity of the reward program
        categoryName:
          type: string
          description: Reward category name
        categoryId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long term persistent identity of the reward category
        multiplier:
          type: number
          description: Factor used to calculate rewards accrued
          minimum: 0
        description:
          type: string
          description: Description of the reward category
        fiAttributes:
          type: array
          description: Array of FI-specific attributes
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'

    RewardMembership:
      title: Reward Program Membership entity
      description: Details of a single membership in a reward programs
      type: object
      properties:
        accountIds:
          type: array
          description: accountIds associated to the reward program
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          uniqueItems: true
        customerId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long-term persistent identity of the associated Customer
        memberId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long term persistent identity of the program member
        memberNumber:
          type: string
          description: Reward program membership number
        memberTier:
          type: string
          description: If the reward program is tiered, member's current tier
        businessOrConsumer:
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessOrConsumer'
          description: BUSINESS or CONSUMER membership
        balances:
          type: array
          description: Array of balances
          items:
            $ref: '#/components/schemas/RewardBalance'
          minItems: 1

    RewardProgram:
      title: Reward Program entity
      description: Reward program detail
      type: object
      properties:
        rewardProgramId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long term persistent identity of the reward program
        programName:
          type: string
          description: Name of reward program
        programUrl:
          type: string
          description: URL of reward program
        memberships:
          description: Array of reward memberships
          type: array
          items:
            $ref: '#/components/schemas/RewardMembership'
        fiAttributes:
          type: array
          description: Array of FI-specific attributes
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'

    RewardPrograms:
      title: Reward Programs entity
      description: An optionally paginated array of reward programs
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            rewardPrograms:
              description: Array of reward programs
              type: array
              items:
                $ref: '#/components/schemas/RewardProgram'

    Security:
      title: Security entity
      description: A base Security entity which defines the type of this security
      type: object
      required:
        - securityCategory
      discriminator:
        propertyName: securityCategory
      properties:
        securityCategory:
          $ref: '#/components/schemas/SecurityCategory'
          description: The main type of this Security

    SecurityId:
      title: Security ID entity
      description: Unique identifier for a security
      type: object
      properties:
        id:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Security identifier
        idType:
          $ref: '#/components/schemas/SecurityIdType'
          description: CINS, CMC, CME, CUSIP, ISIN, ITSA, NASDAQ, SEDOL, SICC, VALOR, WKN

    Statement:
      title: Statement entity
      description: An account statement
      type: object
      properties:
        accountId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Corresponds to accountId in Account entity
        statementId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long-term persistent identity of the statement
        statementDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date of the statement
        description:
          type: string
          description: Description of statement
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'
          description: The links to retrieve this account statement, or to invoke other APIs
        status:
          $ref: '#/components/schemas/DocumentStatus'
          description: Availability status of statement

    Statements:
      title: An array of statements
      description: A paginated array of account statements
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            statements:
              type: array
              description: An array of Statement, each with its HATEOAS link to retrieve the account statement
              items:
                $ref: '#/components/schemas/Statement'

    StockSecurity:
      title: Stock Security entity
      description: A stock security
      type: object
      allOf:
        - $ref: '#/components/schemas/Security'
        - type: object
          properties:
            unitsStreet:
              type: number
              description: The units in the FI's street name as a positive quantity
            unitsUser:
              type: number
              description: The units in user's name directly as a positive quantity
            reinvestDividends:
              type: boolean
              description: Selection to reinvest dividends
            stockType:
              $ref: '#/components/schemas/StockType'
              description: COMMON, PREFERRED, CONVERTIBLE, OTHER
            yield:
              type: number
              description: The current yield
            yieldAsOfDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Yield as-of date

    SweepSecurity:
      title: Sweep Security entity
      description: A sweep security
      type: object
      allOf:
        - $ref: '#/components/schemas/Security'
        - type: object
          properties:
            currentBalance:
              type: number
              description: Balance of funds in account
            availableBalance:
              type: number
              description: Balance of funds available for use
            balanceAsOf:
              $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
              description: As-of date of balances
            checks:
              type: boolean
              description: Whether or not checks can be written on the account

    TaxLot:
      title: Tax Lot entity
      description: Block of securities receiving the same tax treatment
      type: object
      properties:
        originalPurchaseDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Lot acquired date
        quantity:
          type: number
          description: Lot quantity
        purchasedPrice:
          type: number
          description: Original purchase price
        costBasis:
          type: number
          description: >-
            Total amount of money spent acquiring this lot including any fees or
            commission expenses incurred
        currentValue:
          type: number
          description: Lot market value
        positionType:
          $ref: '#/components/schemas/PositionType'
          description: LONG, SHORT

    Transaction:
      title: Transaction
      description: Base entity for financial transactions
      type: object
      required:
        - accountCategory
      discriminator:
        propertyName: accountCategory
      properties:
        accountCategory:
          $ref: '#/components/schemas/AccountCategory'
          description: The entity type of the account of this Transaction
        accountId:
          description: Corresponds to AccountId in Account
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        transactionId:
          description: Long term persistent identity of the transaction (unique to account)
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        referenceTransactionId:
          description: >-
            For reverse postings, the identity of the transaction being
            reversed. For the correction transaction, the identity of the
            reversing post. For credit card posting transactions, the identity
            of the authorization transaction
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        postedTimestamp:
          description: >-
            The date and time that the transaction was posted to the account. If
            not provided then TransactionTimestamp can be used as
            PostedTimeStamp
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
        transactionTimestamp:
          description: >-
            The date and time that the transaction was added to the server
            backend systems
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
        cardNumberDisplay:
          type: string
          description: The payment card number (e.g. debit, credit or digital), suitably masked,
            used to originate the transaction. May differ from primary account number as a
            secondary or employee card or a one-time use number. This is an optional field
            and won't be returned for certain types of transactions such as cash or check deposits
        description:
          type: string
          description: >-
            The description of the transaction, such as information about a merchant's
            name or place of business in a manner that is user friendly and accessible to the customer.
            Detailed information on a payee, such as address, can be sent in `transactionPayee`
        transactionPayee:
          $ref: '#/components/schemas/TransactionPayee'
          description: The merchant or individual payee who was involved in the transaction
        memo:
          $ref: './fdxapi.components.yaml#/components/schemas/String255'
          description: Secondary transaction description
        debitCreditMemo:
          $ref: '#/components/schemas/DebitCreditMemo'
          description: DEBIT, CREDIT, MEMO
        category:
          type: string
          description: 'Transaction category, preferably MCC or SIC.'
        subCategory:
          type: string
          description: Transaction category detail specifying the standard of the transaction category.
            For example, "MCC"
        reference:
          type: string
          description: A tracking reference identifier
        status:
          $ref: '#/components/schemas/TransactionStatus'
          description: PENDING, MEMO, POSTED, AUTHORIZATION
        amount:
          type: number
          description: The amount of money in the account currency
        foreignAmount:
          type: number
          description: The amount of money in the foreign currency
        foreignCurrency:
          $ref: './fdxapi.components.yaml#/components/schemas/Iso4217CurrencyCode'
          description: The ISO 4217 code of the foreign currency
        imageIds:
          type: array
          items:
            type: string
          description: >-
            Array of Image Identifiers (unique to this transaction) used to retrieve Images of
            check or transaction receipt
        lineItem:
          type: array
          description: Breakdown of the transaction details
          items:
            $ref: '#/components/schemas/LineItem'
        reward:
          $ref: '#/components/schemas/TransactionReward'
          description: Rewards earned with this transaction
        fiAttributes:
          type: array
          description: Array of FI-specific attributes
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'
          description: >-
            Links (unique to this transaction) used to retrieve images of
            checks or transaction receipts

    TransactionPayee:
      title: Transaction Payee entity
      description: Primary demographic information for payee on a transaction;
        name, location, contact phone
      type: object
      properties:
        merchantName:
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
          description: Name when payee is a merchant,
            typically a business from which goods or services are rendered
        merchantId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Merchant identifier (MID) for card processing
        individualName:
          $ref: './fdxapi.components.yaml#/components/schemas/IndividualName'
          description: Name when payee is an individual
        address:
          $ref: './fdxapi.components.yaml#/components/schemas/DeliveryAddress'
          description: Address of the payee who received the payment
        phone:
          $ref: './fdxapi.components.yaml#/components/schemas/TelephoneNumber'
          description: Phone number of the payee who received the payment

    TransactionReward:
      title: Transaction Reward entity
      description: Rewards earned on a transaction
      type: object
      properties:
        categoryId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: >-
            Long term persistent identity of the reward category.
            This ID is mapped to a category definition returned by calling
            the getRewardProgramCategories operation
        accrued:
          type: number
          description: Reward units accrued on this transaction
        adjusted:
          type: number
          description: Reward units adjusted on this transaction

    Transactions:
      title: Transactions entity
      description: Optionally paginated array of transactions
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            transactions:
              description: >-
                An array of transactions with entity type dependent on the account type
                (commercial, deposit, insurance, investment, line of credit, loan or digital wallet)
              type: array
              items:
                discriminator:
                  propertyName: accountCategory
                  mapping:
                    COMMERCIAL_ACCOUNT: '#/components/schemas/CommercialTransaction'
                    DEPOSIT_ACCOUNT: '#/components/schemas/DepositTransaction'
                    DIGITAL_WALLET: '#/components/schemas/DigitalWalletTransaction'
                    INSURANCE_ACCOUNT: '#/components/schemas/InsuranceTransaction'
                    INVESTMENT_ACCOUNT: '#/components/schemas/InvestmentTransaction'
                    LOAN_ACCOUNT: '#/components/schemas/LoanTransaction'
                    LOC_ACCOUNT: '#/components/schemas/LineOfCreditTransaction'
                oneOf:
                  - $ref: '#/components/schemas/CommercialTransaction'
                  - $ref: '#/components/schemas/DepositTransaction'
                  - $ref: '#/components/schemas/DigitalWalletTransaction'
                  - $ref: '#/components/schemas/InsuranceTransaction'
                  - $ref: '#/components/schemas/InvestmentTransaction'
                  - $ref: '#/components/schemas/LineOfCreditTransaction'
                  - $ref: '#/components/schemas/LoanTransaction'

    TransferLimits:
      title: Incoming and outgoing transfer limits
      description: The amount limits for incoming and outgoing transfers
      type: object
      properties:
        out:
          description: Limits for outgoing transfers from the account
          $ref: '#/components/schemas/PaymentNetworkTransferLimits'
        in:
          description: Limits for incoming transfers to the account
          $ref: '#/components/schemas/PaymentNetworkTransferLimits'

    Vesting:
      title: Vesting entity
      description: Represents the vesting of ownership of an investment account
      type: object
      properties:
        vestingDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Vesting date
        symbol:
          type: string
          description: Security symbol
        strikePrice:
          type: number
          description: Strike price
        vestingPercentage:
          type: number
          description: Vesting percentage
        otherVestAmount:
          type: number
          description: Other vested amount
        otherVestPercentage:
          type: number
          description: Other vested percentage
        vestedBalance:
          type: number
          description: Vested balance
        unVestedBalance:
          type: number
          description: Unvested balance
        vestedQuantity:
          type: number
          description: Vested quantity
        unVestedQuantity:
          type: number
          description: Unvested quantity

    ############################################################
    #
    # Core data types
    #
    ############################################################

    AccountBillPayStatus:
      title: Account Bill Pay Status
      description: >-
        Indicates bill pay capabilities for an account.
          * `ACTIVE`: Can be used for bill payment
          * `AVAILABLE`: Account can be requested for bill payment
          * `NOT_AVAILABLE`: Account cannot participate in bill payment
          * `PENDING`: Account requested for bill payment, but not available yet
      type: string
      enum:
        - ACTIVE
        - AVAILABLE
        - NOT_AVAILABLE
        - PENDING

    AccountCategory:
      title: Account Category type
      description: The category of account
      type: string
      enum:
        - ANNUITY_ACCOUNT
        - COMMERCIAL_ACCOUNT
        - DEPOSIT_ACCOUNT
        - DIGITAL_WALLET
        - INSURANCE_ACCOUNT
        - INVESTMENT_ACCOUNT
        - LOAN_ACCOUNT
        - LOC_ACCOUNT

    AccountStatus:
      title: Account Status
      description: The status of an account
      type: string
      enum:
        - CLOSED
        - DELINQUENT
        - NEGATIVECURRENTBALANCE
        - OPEN
        - PAID
        - PENDINGCLOSE
        - PENDINGOPEN
        - RESTRICTED

    AssetClass:
      title: Asset Class
      description: The class of an investment asset
      type: string
      enum:
        - DOMESTICBOND
        - INTLBOND
        - INTLSTOCK
        - LARGESTOCK
        - MONEYMARKET
        - OTHER
        - SMALLSTOCK

    AssetTransferType:
      title: Asset Transfer Type
      description: The possible values for type of asset transfer
      type: string
      enum:
        - CA_ATON
        - US_ACATS
        - US_DTC

    BalanceType:
      title: Balance Type
      description: >-
        Type of balance for the account.
          * `ASSET`: Positive transaction amount increases balance
          * `LIABILITY`: Positive transaction amount decreases balance
      type: string
      enum:
        - ASSET
        - LIABILITY

    CallType:
      title: Call Type
      description: The call type for a stock option
      type: string
      enum:
        - CALL
        - MATURITY
        - PREFUND
        - PUT

    CompoundingPeriod:
      title: Compounding Period
      description: Interest compounding Period
      type: string
      enum:
        - ANNUALLY
        - BIWEEKLY
        - DAILY
        - MONTHLY
        - SEMIANNUALLY
        - SEMIMONTHLY
        - WEEKLY

    CouponMatureFrequency:
      title: Coupon Mature Frequency
      description: The frequency of a bond's coupon maturity
      type: string
      enum:
        - ANNUAL
        - MONTHLY
        - OTHER
        - QUARTERLY
        - SEMIANNUAL

    DebitCreditMemo:
      title: DebitCreditMemo
      description: The posting type of a transaction
      type: string
      enum:
        - CREDIT
        - DEBIT
        - MEMO

    DebtClass:
      title: Debt Class
      description: The classification of a debt instrument
      type: string
      enum:
        - CORPORATE
        - MUNICIPAL
        - OTHER
        - TREASURY

    DebtType:
      title: Debt Type
      description: The type of a debt instrument
      type: string
      enum:
        - COUPON
        - ZERO

    DepositTransactionType:
      title: Deposit Transaction Type
      description: The type of a deposit transaction
      type: string
      enum:
        - ADJUSTMENT
        - ATMDEPOSIT
        - ATMWITHDRAWAL
        - BILLPAYMENT
        - CHECK
        - DEPOSIT
        - DIRECTDEPOSIT
        - DIVIDEND
        - FEE
        - INTEREST
        - POSCREDIT
        - POSDEBIT
        - PREAUTHORIZEDDEPOSIT
        - PREAUTHORIZEDWITHDRAWAL
        - TRANSFER
        - WITHDRAWAL

    DigitalWalletTransactionType:
      title: Digital Wallet Transaction Type
      description: The type of a digital wallet transaction
      type: string
      enum:
        - ADJUSTMENT
        - BILL_PAYMENT
        - CREDIT
        - DEBIT
        - DEPOSIT
        - DIRECT_DEPOSIT
        - DIVIDEND
        - FEE
        - INTEREST
        - MERCHANT_PAYMENT
        - MERCHANT_REFUND
        - TRANSFER_IN
        - TRANSFER_OUT
        - WITHDRAWAL

    DocumentStatus:
      title: Document Status
      description: Defines the status of a document
      type: string
      enum:
        - AVAILABLE
        - PROCESSING
        - FAILED

    HeldInAccount:
      title: Held In Account
      description: The type of holdings of an investment account
      type: string
      enum:
        - CASH
        - MARGIN
        - OTHER
        - SHORT

    HoldingSubType:
      title: Holding SubType
      description: The subtype of an investment holding
      type: string
      enum:
        - CASH
        - MONEYMARKET

    HoldingType:
      title: Holding Type
      description: >-
        The type of an investment holding

          | Value | Description |
          |-----|-----|
          | ANNUITY | Financial product that pays out a fixed stream of payments |
          | BOND | Debt security as a loan to a government, agency or company, repaid with interest |
          | CD | Certificate of Deposit, a savings account with a fixed rate and term |
          | DIGITALASSET | Digital representation of an asset or right that is stored and transferred on a digital network such as the internet or a blockchain |
          | MUTUALFUND | Pooled collection of assets invested in stocks, bonds, and other securities |
          | OPTION | The right to buy a specific number of stock shares at a pre-set price |
          | OTHER | Another type of holding not listed here |
          | STOCK | A share in the ownership of a company |
      type: string
      enum:
        - ANNUITY
        - BOND
        - CD
        - DIGITALASSET
        - MUTUALFUND
        - OPTION
        - OTHER
        - STOCK

    IncomeType:
      title: Income Type
      description: The type of income of an investment transaction
      type: string
      enum:
        - CGLONG
        - CGSHORT
        - MISC

    InsurancePremiumTerm:
      title: Policy Premium Term Type
      description: Payment terms for insurance premiums
      type: string
      enum:
        - ANNUAL
        - MONTHLY

    InsuranceTransactionType:
      title: Insurance Transaction Type
      description: The type of an insurance transaction
      type: string
      enum:
        - ADJUSTMENT
        - FEE
        - INTEREST
        - PAYMENT

    InterestRateType:
      title: Interest Rate Type
      description: The type of interest rate
      type: string
      enum:
        - FIXED
        - VARIABLE

    Inv401kSourceType:
      title: Investment 401k Source Type
      description: The source of a 401k investment
      type: string
      enum:
        - AFTERTAX
        - MATCH
        - OTHERNONVEST
        - OTHERVEST
        - PRETAX
        - PROFITSHARING
        - ROLLOVER

    InvestmentBalanceType:
      title: Investment Balance Type
      description: The type of an investment balance
      type: string
      enum:
        - AMOUNT
        - PERCENTAGE

    InvestmentTransactionType:
      title: Investment Transaction Type
      description: The type of an investment transaction
      type: string
      enum:
        - ADJUSTMENT
        - AIRDROP
        - ATM
        - CASH
        - CHECK
        - CLOSURE
        - CLOSUREOPT
        - CONTRIBUTION
        - DEP
        - DEPOSIT
        - DIRECTDEBIT
        - DIRECTDEP
        - DIV
        - DIVIDEND
        - DIVIDENDREINVEST
        - EXPENSE
        - FEE
        - FORKED
        - INCOME
        - INTEREST
        - INVEXPENSE
        - JRNLFUND
        - JRNLSEC
        - MARGININTEREST
        - MINED
        - OPTIONEXERCISE
        - OPTIONEXPIRATION
        - OTHER
        - PAYMENT
        - POS
        - PURCHASED
        - PURCHASEDTOCOVER
        - PURCHASETOCLOSE
        - PURCHASETOOPEN
        - REINVESTOFINCOME
        - REPEATPMT
        - RETURNOFCAPITAL
        - SOLD
        - SOLDTOCLOSE
        - SOLDTOOPEN
        - SPLIT
        - SRVCHG
        - STAKED
        - TRANSFER
        - WITHDRAWAL
        - XFER

    LoanPaymentFrequency:
      title: Loan Payment Frequency
      description: The frequency of payments on a loan
      type: string
      enum:
        - ANNUALLY
        - BIMONTHLY
        - BIWEEKLY
        - FOURWEEKS
        - MONTHLY
        - OTHER
        - QUARTERLY
        - SEMIANNUALLY
        - TWICEMONTHLY
        - WEEKLY

    LoanTransactionType:
      title: Loan Transaction Type
      description: >-
        Defines the type of a loan transaction:
          * `ADJUSTMENT`: Adjustment or correction
          * `DOUBLE_UP_PAYMENT`: Additional payment beyond the required payment to reduce the principal
          * `FEE`: Fee charge. For example, a late payment fee
          * `INTEREST`: Interest charge
          * `LUMP_SUM_PAYMENT`: A single payment of money, as opposed to a series of payments made over time
          * `PAYMENT`: Required payment that satisfies the minimum payment (e.g. principal + interest for mortgages)
          * `PAYOFF`: Payment that satisfies the terms of the mortgage loan and completely pays off the debt
          * `SKIP_PAYMENT`: Payment that satisfies deferral of a required payment
      type: string
      enum:
        - ADJUSTMENT
        - DOUBLE_UP_PAYMENT
        - FEE
        - INTEREST
        - LUMP_SUM_PAYMENT
        - PAYMENT
        - PAYOFF
        - SKIP_PAYMENT

    LineOfCreditTransactionType:
      title: Line of Credit Transaction Type
      description: The type of a line of credit transaction
      type: string
      enum:
        - ADJUSTMENT
        - CHECK
        - FEE
        - INTEREST
        - PAYMENT
        - PURCHASE
        - WITHDRAWAL

    MutualFundType:
      title: Mutual Fund Type
      description: The type of a mutual fund
      type: string
      enum:
        - CLOSEEND
        - OPENEND
        - OTHER

    OptionType:
      title: Option Type
      description: The type of a stock option
      type: string
      enum:
        - CALL
        - PUT

    OrderDuration:
      title: Order Duration
      description: The duration of the order
      type: string
      enum:
        - DAY
        - GOODTILLCANCEL
        - IMMEDIATE

    OrderType:
      title: Order Type
      description: The type of the order
      type: string
      enum:
        - BUY
        - BUYTOCOVER
        - BUYTOOPEN
        - SELL
        - SELLCLOSE
        - SELLSHORT
        - SELLTOCOVER
        - SELLTOOPEN

    PaymentFrequency:
      title: Payment Frequency
      description: The frequency of payments
      type: string
      enum:
        - ANNUALLY
        - BIWEEKLY
        - DAILY
        - MONTHLY
        - SEMIANNUALLY
        - SEMIMONTHLY
        - WEEKLY

    PaymentNetworkIdentifierType:
      title: Payment Network Identifier Type
      description: Suggested values for Payment Initiation Identifier Type
      type: string
      enum:
        - ACCOUNT_NUMBER
        - TOKENIZED_ACCOUNT_NUMBER

    PaymentNetworkType:
      title: Payment Network Type
      description: >-
        Suggested values for Payment Network Type.

          | Value | Description |
          |-----|-----|
          | CA_ACSS | Automated Clearing House Settlement System |
          | CA_LVTS | Large-Value Transfer System |
          | US_ACH | Automated Clearing House |
          | US_CHIPS | Clearinghouse Interbank Payments System |
          | US_FEDNOW | Federal Reserve Instant Payment System |
          | US_FEDWIRE | Fedwire Funds Service |
          | US_RTP | US Real Time Payments System |
      type: string
      enum:
        - CA_ACSS
        - CA_LVTS
        - US_ACH
        - US_CHIPS
        - US_FEDNOW
        - US_FEDWIRE
        - US_RTP

    PayoutMode:
      title: Payout Mode
      description: >-
        Frequency of annuity payments.

          | Value | Description |
          |-----|-----|
          | ANNUALLY | Paid Annually |
          | BIWEEKLY | Paid Bi-weekly |
          | DAILY | Paid Daily |
          | MONTHLY | Paid Monthly |
          | SEMIANNUALLY | Paid Semi-annually |
          | SEMIMONTHLY | Paid Semi-monthly |
      type: string
      enum:
        - ANNUALLY
        - BIWEEKLY
        - DAILY
        - MONTHLY
        - SEMIANNUALLY
        - SEMIMONTHLY
        - WEEKLY

    PayoutType:
      title: Payout Type
      description: >-
        Indicates a type of payout such as immediate or deferred.

          | Value | Description |
          |-----|-----|
          | DEFERRED | Deferred payout starts at a predetermined date in the future |
          | IMMEDIATE | Immediate payout begins paying out shortly after the annuity is purchased |
      type: string
      enum:
        - DEFERRED
        - IMMEDIATE

    PeriodCertainType:
      title: Period Certain Type
      description: >-
        The number of modal periods comprising the duration of the certain period of an annuity payout.

          | Value | Description |
          |-----|-----|
          | 5_YEAR | Five year duration |
          | 10_YEAR | Ten year duration |
          | 20_YEAR | Twenty year duration |
          | 30_YEAR | Thirty year duration |
          | NONE | Not a Period Certain |
      type: string
      enum:
        - 5_YEAR
        - 10_YEAR
        - 20_YEAR
        - 30_YEAR
        - NONE

    PolicyProductType:
      title: Policy Product Type
      description: >-
        Distinguishes options in annuity payouts; values are defined by the carrier.

          | Value | Description |
          |-----|-----|
          | FIXED | Payout is based on a guaranteed rate of return by the carrier |
          | VARIABLE | Payout is based on the variable performance of the investments the buyer chooses |
      type: string
      enum:
        - FIXED
        - VARIABLE

    PolicyStatus:
      title: Policy Status
      description: >-
        The status of an insurance policy account.

          | Value | Description |
          |-----|-----|
          | ACTIVE | At least one component of the insurance policy is in force |
          | DEATH_CLAIM_PAID | Benefits for a death claim have been settled with the insured |
          | DEATH_CLAIM_PENDING | A death claim has been submitted but not yet settled |
          | EXPIRED | Nonpayment of premium has exhausted the policy's Grace Period |
          | GRACE_PERIOD | A premium is due but before lapse in coverage begins |
          | LAPSE_PENDING | After the Grace Period has been exhausted but before final expiration; during Lapse Pending, policy reinstatement may still be possible |
          | TERMINATED | Either the insurance company or the insured cancel the coverage of a cancellable insurance policy |
          | WAIVER | A premium payment is waived under certain conditions due to a payer benefit clause |
      type: string
      enum:
        - ACTIVE
        - DEATH_CLAIM_PAID
        - DEATH_CLAIM_PENDING
        - EXPIRED
        - GRACE_PERIOD
        - LAPSE_PENDING
        - TERMINATED
        - WAIVER

    PositionType:
      title: Position Type
      description: The type of an investment position
      type: string
      enum:
        - LONG
        - SHORT

    RewardType:
      title: Reward Type
      description: >-
        The type of the reward balance.  Example: a reward program awarding
        "Stars" for purchases would use the `POINTS` reward type.
          * `CASHBACK`: Rewards balances enumerated using a monetary amount
          * `MILES`: Rewards balances enumerated using distance
          * `POINTS`: Default when a reward balance is not of type CASHBACK or MILES
      type: string
      enum:
        - CASHBACK
        - MILES
        - POINTS

    Secured:
      title: Secured
      description: How the option is secured
      type: string
      enum:
        - COVERED
        - NAKED

    SecurityCategory:
      title: Security Category
      description: The type of security
      type: string
      enum:
        - DEBT_SECURITY
        - MUTUAL_FUND_SECURITY
        - OPTION_SECURITY
        - OTHER_SECURITY
        - STOCK_SECURITY
        - SWEEP_SECURITY

    SecurityIdType:
      title: Security Id Type
      description: >-
        The source of the identifier for a security

          | Value | Description |
          |-----|-----|
          | CINS | CUSIP International Numbering System) is a global securities identification numbering system that provides |
          | CMC | Coin Market Cap |
          | CME | Chicago Mercantile Exchange |
          | CUSIP | Committee on Uniform Securities Identification Procedures |
          | ISIN | International Securities Identification Number |
          | ITSA | International Securities Identification Number Technical Committee |
          | NASDAQ | National Association of Securities Dealers Automated Quotations |
          | SEDOL | Stock Exchange Daily Official List |
          | SICC | Standard Identification Code for Institutional Investment |
          | VALOR | SIX Swiss Exchange |
          | WKN | Wertpapierkennnummer |
      type: string
      enum:
        - CINS
        - CMC
        - CME
        - CUSIP
        - ISIN
        - ITSA
        - NASDAQ
        - SEDOL
        - SICC
        - VALOR
        - WKN

    SecurityType:
      title: Security Type
      description: >-
        The type of a security

          | Value | Description |
          |-----|-----|
          | BOND | Debt security as a loan to a government, agency or company, repaid with interest |
          | DEBT | Any type of security that must be paid back in full along with interest |
          | DIGITALASSET | Digital representation of an asset or right that is stored and transferred on a digital network such as the internet or a blockchain |
          | MUTUALFUND | Pooled collection of assets invested in stocks, bonds, and other securities |
          | OPTION | The right to buy a specific number of stock shares at a pre-set price |
          | OTHER | Another type of security not listed here |
          | STOCK | A share in the ownership of a company |
          | SWEEP | Interest-earning account used to collect low- or non-interest-earning cash at close of day |
      type: string
      enum:
        - BOND
        - DEBT
        - DIGITALASSET
        - MUTUALFUND
        - OPTION
        - OTHER
        - STOCK
        - SWEEP

    StockType:
      title: Stock Type
      description: The type of a stock instrument
      type: string
      enum:
        - COMMON
        - CONVERTIBLE
        - OTHER
        - PREFERRED

    SubAccountType:
      title: Sub Account Type
      description: The subtype of an account
      type: string
      enum:
        - CASH
        - MARGIN
        - OTHER
        - SHORT

    TransactionReason:
      title: Transaction Reason
      description: The reason for an investment transaction
      type: string
      enum:
        - CALL
        - MATURITY
        - SELL

    TransactionStatus:
      title: Transaction Status
      description: The status of a transaction
      type: string
      enum:
        - AUTHORIZATION
        - MEMO
        - PENDING
        - POSTED

    TransferDirection:
      title: Investment Transfer Action Direction
      description: Transaction transfer direction
      type: string
      enum:
        - IN
        - OUT

    TreasuryManagementType:
      title: Treasury Management Type
      description: The source of Treasury Management account definition; one of BAI, BTRS, ISO, SWIFT
      type: string
      enum:
        - BAI
        - BTRS
        - ISO
        - SWIFT

    UnitType:
      title: Unit Type
      description: The units of an investment transaction
      type: string
      enum:
        - CURRENCY
        - SHARES
