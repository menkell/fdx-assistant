openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Payroll API
  description: Financial Data Exchange V6.3.0 Payroll API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Payroll API
tags:
  - name: Pay Stub Information
    description: Retrieve latest income payments
  - name: Payroll Information
    description: Verify employment and/or income

paths:
  ############################################################
  #
  # Payroll paths
  #
  ############################################################

  /payroll/paystubs:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getPaystubs
      tags:
        - Pay Stub Information
      description: Search for and retrieve the employee's latest paystubs
      summary: Search for and retrieve paystubs
      parameters:
        - $ref: './fdxapi.components.yaml#/components/parameters/StartDateQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/EndDateQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/PageKeyQuery'
      responses:
        '200':
          description: List of paystubs retrieved
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaystubList'
        '400':
          $ref: './fdxapi.components.yaml#/components/responses/400'
        '401':
          $ref: './fdxapi.components.yaml#/components/responses/401'
        '404':
          $ref: './fdxapi.components.yaml#/components/responses/404'
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /payroll/paystubs/{paystubId}:
    parameters:
      - $ref: '#/components/parameters/PaystubIdPath'
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getPaystub
      tags:
        - Pay Stub Information
      description: Retrieve the employee's specified paystub as a Base64 PDF file
      summary: Pay Stub detail
      responses:
        '200':
          description: The specific paystub PDF file
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                description: JSON response containing Base64-encoded content of the paystub PDF file
                $ref: '#/components/schemas/PaystubPdf'
            application/pdf:
              schema:
                description: The paystub PDF downloaded as raw pdf
                type: string
                format: binary
        '400':
          description: Required input data not sent
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Invalid Input:
                  value:
                    code: '401'
                    message: Pay Stub ID is required
                    debugMessage: Custom developer-level error details for troubleshooting
        '404':
          description: Pay Stub with provided ID was not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Resource not found:
                  value:
                    code: '1402'
                    message: Pay Stub for provided ID not found
                    debugMessage: Custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /payroll/reports:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getPayrollReports
      tags:
        - Payroll Information
      description: Search for the employee's latest payroll report
      summary: Search for a payroll report
      parameters:
        - $ref: './fdxapi.components.yaml#/components/parameters/ResultTypeQuery'
        - $ref: '#/components/parameters/ReportTypeQuery'
      responses:
        '200':
          description: List of payroll reports available or the full reports themselves
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayrollReportList'
        '400':
          $ref: './fdxapi.components.yaml#/components/responses/400'
        '401':
          $ref: './fdxapi.components.yaml#/components/responses/401'
        '404':
          $ref: './fdxapi.components.yaml#/components/responses/404'
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /payroll/reports/{reportId}:
    parameters:
      - $ref: '#/components/parameters/ReportIdPath'
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getPayrollReport
      tags:
        - Payroll Information
      description: Retrieve the employee's specified payroll report
      summary: Payroll Report detail
      responses:
        '200':
          description: Details of the specific payroll report
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayrollReport'
        '400':
          description: Required input data not sent
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Invalid Input:
                  value:
                    code: '401'
                    message: Report ID is required
                    debugMessage: Custom developer-level error details for troubleshooting
        '404':
          description: Payroll Report with provided ID was not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Resource not found:
                  value:
                    code: '1401'
                    message: Payroll Report for provided ID not found
                    debugMessage: Custom developer-level error details for troubleshooting
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
    # Payroll parameters
    #
    ############################################################

    PaystubIdPath:
      name: paystubId
      in: path
      description: >-
        The specific paystub ID to retrieve. This can be any ID which the data provider creates
        specific to the consenting person's paystub, perhaps simply the pay date as a string
        optionally followed by a sequence number: "2024-09-30-01". Need only be unique within
        the current employee's consent / token, according to data provider's preference
      required: true
      schema:
        $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

    ReportIdPath:
      name: reportId
      in: path
      description: Specific reportId to retrieve
      required: true
      schema:
        $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

    ReportTypeQuery:
      name: reportType
      in: query
      description: Whether to retrieve Verification of Employment ("VOE")
        or Verification of Income and Employment ("VOIE") reports
      required: true
      schema:
        $ref: '#/components/schemas/PayrollReportType'

  schemas:
    ############################################################
    #
    # Payroll data entities
    #
    ############################################################

    AnnualPaymentAmounts:
      title: Annual Payment Amounts
      description: Year to date amounts for current and previous years
      type: object
      properties:
        year:
          description: The year in which this income was earned
          type: integer
        grossPay:
          description: Gross pay for covered period
          $ref: '#/components/schemas/GrossPay'
        netPay:
          description: Net pay for covered period
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
      required:
        - year
        - grossPay

    BasePayroll:
      title: Base Payroll Rate
      description: Provides a person's base pay rate
      type: object
      properties:
        rate:
          description: The amount and currency of the base pay rate of employee
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        rateType:
          description: The unit for the worker's rate. In time period length order, one of
            HOURLY, DAILY, WEEKLY, BI-WEEKLY, SEMI-MONTHLY, EVERY 2.6 WEEKS, EVERY 4 WEEKS,
            MONTHLY, EVERY 5.2 WEEKS, QUARTERLY, SEMI-ANNUALLY, ANNUAL, OTHER
          $ref: '#/components/schemas/PayrollRateType'
      required:
        - rate
        - rateType

    DirectDeposit:
      title: Direct Deposit
      description: If payment by DIRECT_DEPOSIT, the details of the target account
      type: object
      properties:
        routingTransitNumber:
          description: The deposit bank's routing transit number
          type: string
        accountNumber:
          description: Account number last four for the deposit, i.e. masked xxxxx-x0000
          type: string
        accountType:
          description: Type of bank account into which deposit was made,
            typically CHECKING or SAVINGS
          $ref: './fdxapi.components.yaml#/components/schemas/AccountType'

    EarningComponent:
      title: Earning Component
      description: A single named pay component earned on this paystub
        with amount and optional currency and/or year-to-date amount.
        Common names to use for earned components that would fall under
        OTHER type (in addition to names for BASE, BONUS, COMMISSION,
        and OVERTIME types) are Tips, Stock, Workers Compensation,
        Pension, and Severance. (Inheriting properties `amount`, `currency`,
        `name` and `yearToDate` from `PayAmount`)
      type: object
      allOf:
        - $ref: '#/components/schemas/PayAmount'
        - type: object
          properties:
            rate:
              description: The rate used to calculate this earned component amount
              type: number
            rateType:
              description: The unit for this rate. In time period length order, one of HOURLY,
                DAILY, WEEKLY, BI-WEEKLY, SEMI-MONTHLY, EVERY 2.6 WEEKS, EVERY 4 WEEKS,
                MONTHLY, EVERY 5.2 WEEKS, QUARTERLY, SEMI-ANNUALLY, ANNUAL, OTHER
              $ref: '#/components/schemas/PayrollRateType'
            hours:
              description: The number of hours paid for this component amount
              type: number
            type:
              description: The GSE Mapping for a specific earning component.
                For a Government Sponsored Enterprise (GSE), such as Fannie Mae or Freddie Mac.
                One of BASE, BONUS, COMMISSION, OTHER, OVERTIME
              $ref: '#/components/schemas/EarningType'

    Employee:
      title: Employee entity
      description: Represents an employee
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/Person'
        - type: object
          properties:
            employeeId:
              description: Provider's long-term persistent id for the employee
              $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
            name:
              description: Employee's full name
              $ref: './fdxapi.components.yaml#/components/schemas/IndividualName'
      required:
        - name

    Employer:
      title: Employer entity
      description: Represents an employer
      type: object
      properties:
        employerId:
          description: Provider's long-term persistent id for the employer
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        name:
          description: The employer's name
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
        dbas:
          description: Array of Doing Business As names for this employer
          type: array
          items:
            type: string
        taxId:
          description: Country specific Tax Id associated with this employer (FEIN in USA or BN in Canada)
          type: string
        taxIdCountry:
          description: Country originating the employer's taxId element
          $ref: './fdxapi.components.yaml#/components/schemas/Iso3166CountryCode'
        contacts:
          description: Employer's various contact information
          $ref: './fdxapi.components.yaml#/components/schemas/Contacts'
      required:
        - name

    Employment:
      title: Employment
      description: Provides a person's employment details
      type: object
      properties:
        employer:
          description: The employer for the job/position
          $ref: '#/components/schemas/Employer'
        jobTitle:
          description: The title of the job/position
          type: string
        originalHireDate:
          description: The date when employee joined for the first time
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        mostRecentHireDate:
          description: The date when employee re-joined most recently
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        endDate:
          description: The employment end date
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        status:
          description: The employee's employment status, ACTIVE or INACTIVE
          $ref: '#/components/schemas/ActiveStatus'
        supplementalStatus:
          description: Supplemental detail of employee's employment status
          $ref: '#/components/schemas/SupplementalStatus'
        type:
          description: The employee's employment type,
            CONTRACTED, FULL-TIME, OTHER, PART-TIME, SEASONAL, TEMPORARY
          $ref: '#/components/schemas/EmploymentType'
      required:
        - employer
        - status

    FederalTaxWithholding:
      title: Federal Tax Withholding
      description: National / federal tax withholding.
        Common names to use for federal withholdings are Federal,
        Social Security, and Medicare. (Inheriting properties `amount`,
        `currency`, `name` and `yearToDate` from `PayAmount`)
      type: object
      allOf:
        - $ref: '#/components/schemas/PayAmount'
        - type: object
          properties:
            percent:
              description: Percentage rate for this federal tax withholding, if specified
              type: number
      required:
        - name
        - amount

    GrossPay:
      title: Payment Amounts
      description: Year to date amounts for current and previous years
      type: object
      properties:
        total:
          description: Total gross pay for covered period
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        base:
          description: Base pay part of Gross pay for covered period
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        bonus:
          description: Bonus pay for covered period
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        commission:
          description: Commission for covered period
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        overtime:
          description: Overtime pay for covered period
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        otherEarnings:
          description: Other earnings received in covered period. With name, amount,
            and currency (and can optionally contain year-to-date amount)
          type: array
          items:
            $ref: '#/components/schemas/PayAmount'
      required:
        - total

    Income:
      title: Income
      description: Provides a person's employment income details.
        Applicable only for VOIE (Verification of Income and Employment) data retrieval
      type: object
      properties:
        baseRate:
          description: The employee's base payroll rate
          $ref: '#/components/schemas/BasePayroll'
        payrollFrequency:
          description: The frequency of payments. In pay period length order, one of
            DAILY, WEEKLY, BI-WEEKLY, SEMI-MONTHLY, EVERY 2.6 WEEKS, EVERY 4 WEEKS,
            MONTHLY, EVERY 5.2 WEEKS, QUARTERLY, SEMI-ANNUALLY, ANNUALLY, OTHER
          $ref: '#/components/schemas/PayrollFrequency'
        otherFrequency:
          description: Description of the frequency, required if specified as OTHER
          type: string
        latestPayDate:
          description: The date of employee's most recent pay
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        latestPayPeriodEndDate:
          description: The end date of employee's most recent pay period
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        annualPay:
          description: Year-to-date pay for current year and total annual pay for previous years
          $ref: '#/components/schemas/AnnualPaymentAmounts'
      required:
        - payrollFrequency

    PayAmount:
      title: Pay Amount
      description: The payment amount and year-to-date amount, with optional name and/or currency,
        for this named pay element, earning or deduction. (Inherits properties `amount` and `currency`
        from `MonetaryAmount`)
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        - type: object
          properties:
            name:
              description: Name of this pay element, earning or deduction, if needed
              type: string
            yearToDate:
              description: Year-to-date currency amount for this pay element, earning or deduction,
                if relevant
              type: number

    PaymentDetail:
      title: Payment Detail
      description: Detail for split payments
      type: object
      properties:
        method:
          description: Name of the payment method, either CHECK or DIRECT_DEPOSIT (or CASH)
          $ref: '#/components/schemas/PaymentMethod'
        payment:
          description: Amount of the check or direct deposit amount
          $ref: './fdxapi.components.yaml#/components/schemas/MonetaryAmount'
        percentSplit:
          description: Percentage split for this check or direct deposit
          type: number
        checkNumber:
          description: If payment by CHECK, the last four of the check number, i.e. xxxxx-x0000
          type: string
        directDeposit:
          description: If payment by DIRECT_DEPOSIT, the details of the deposit account
          $ref: '#/components/schemas/DirectDeposit'

    PayPeriod:
      title: Pay Period
      description: The date range and payment date for this paystub
      type: object
      properties:
        payDate:
          description: The date of the payment for this paystub
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        startDate:
          description: The start date of the pay period for this paystub
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        endDate:
          description: The end date of the pay period for this paystub
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
      required:
        - payDate
        - endDate

    PayPeriodWithholding:
      title: Pay Period Withholding
      description: National, regional and local tax withholdings
      type: object
      properties:
        taxFilingStatus:
          description: Tax filing status of the employee for this pay period
          type: string
        country:
          description: The country for the federal withholding amount
          $ref: './fdxapi.components.yaml#/components/schemas/Iso3166CountryCode'
        federalWithholdings:
          description: All the various named national / federal withholdings for this pay period
          type: array
          items:
            $ref: '#/components/schemas/FederalTaxWithholding'
        regionalWithholdings:
          description: All the various named regional and/or local withholdings for this pay period
          type: array
          items:
            $ref: '#/components/schemas/RegionalTaxWithholding'
      required:
        - taxFilingStatus
        - country

    PayrollReport:
      title: Payroll Report entity
      description: An employee's Payroll Report
      type: object
      properties:
        reportId:
          description: The report identification number
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        reportType:
          description: The type of report
          $ref: '#/components/schemas/PayrollReportType'
        generationDate:
          description: The generation date of the report
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        dataAsOf:
          description: The data in the report is as of this date
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        employee:
          description: The employee
          $ref: '#/components/schemas/Employee'
        employment:
          description: The employee's employment
          $ref: '#/components/schemas/Employment'
        incomes:
          description: The employee's year to date income amounts for current and previous years
            omitted for Verification of Employment requests (VOE),
            included for Verification of Income and Employment requests (VOI / VOIE)
          type: array
          items:
            $ref: '#/components/schemas/Income'
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'
          description: Links to retrieve this payroll report, or to invoke related APIs
      required:
        - reportId
        - reportType
        - generationDate
        - employee
        - employment

    PayrollReportList:
      title: Payroll Report List entity
      description: Response object for /payroll/reports API with list of reports available
      type: object
      properties:
        resultType:
          description: Indicates whether response array of `lightweight` payroll report summaries
            or of `detail` full payroll reports is being returned
          $ref: './fdxapi.components.yaml#/components/schemas/ResultType'
        summaries:
          description: Zero or more PayrollReportSummaries for lightweight response
          type: array
          items:
            $ref: '#/components/schemas/PayrollReportSummary'
        reports:
          description: Zero or more PayrollReports, for details response
          type: array
          items:
            $ref: '#/components/schemas/PayrollReport'

    PayrollReportSummary:
      title: Payroll Report Summary entity
      description: The list of payroll reports for an employee
      type: object
      properties:
        reportId:
          description: The report identification number
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        reportType:
          description: The type of report
          $ref: '#/components/schemas/PayrollReportType'
        generationDate:
          description: The generation date of the report
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        dataAsOf:
          description: The data in the report is as of this date
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        employeeId:
          description: Provider's long-term persistent id for the employee
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        employeeName:
          description: Employee's full name
          $ref: './fdxapi.components.yaml#/components/schemas/IndividualName'
        employerId:
          description: The employer for this report
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        employerName:
          description: The employer's name
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'
          description: Links to retrieve this payroll report, or to invoke related APIs
      required:
        - reportId
        - reportType
        - generationDate
        - employeeName
        - employerName

    Paystub:
      title: Paystub entity
      description: An employee's paystub
      type: object
      properties:
        paystubId:
          description: >-
            The paystub identification number, if any. This can be any ID which the data provider creates
            specific to the consenting person's paystub, perhaps simply the pay date as a string
            optionally followed by a sequence number: "2024-09-30-01". Need only be unique within
            the current employee's consent / token, according to data provider's preference
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        dataAsOf:
          description: The data on the paystub is as of this date
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        source:
          description: The original source of the paystub data
          $ref: '#/components/schemas/PaystubSource'
        employee:
          description: The employee
          $ref: '#/components/schemas/Employee'
        employer:
          description: The employer for the job/position
          $ref: '#/components/schemas/Employer'
        payPeriod:
          description: The date range and payment date for this paystub
          $ref: '#/components/schemas/PayPeriod'
        payrollFrequency:
          description: The frequency of payments. In pay period length order, one of
            DAILY, WEEKLY, BI-WEEKLY, SEMI-MONTHLY, EVERY 2.6 WEEKS, EVERY 4 WEEKS,
            MONTHLY, EVERY 5.2 WEEKS, QUARTERLY, SEMI-ANNUALLY, ANNUALLY, OTHER
          $ref: '#/components/schemas/PayrollFrequency'
        otherFrequency:
          description: Description of the frequency, required if specified as OTHER
          type: string
        grossPay:
          description: Gross pay and year-to-date amounts and currency for this paystub
          $ref: '#/components/schemas/PayAmount'
        netPay:
          description: Net pay and year-to-date amounts and currency for this paystub
          $ref: '#/components/schemas/PayAmount'
        withholding:
          description: National, regional and local tax withholdings
          $ref: '#/components/schemas/PayPeriodWithholding'
        earnings:
          description: All the earning components for this pay period
          type: array
          items:
            $ref: '#/components/schemas/EarningComponent'
        deductions:
          description: All the named deductions for this pay period,
            with pay period and year-to-date amounts and currency.
            Common names to use for deductions are Retirement, Medical,
            Dental, Vision, Garnishment, and Other Miscellaneous
          type: array
          items:
            $ref: '#/components/schemas/PayAmount'
        paymentDetails:
          description: The detailed splits of this payment between checks and/or deposits
          type: array
          items:
            $ref: '#/components/schemas/PaymentDetail'
        disclaimers:
          description: All the disclaimer notes for this pay period
          type: array
          items:
            type: string
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'
          description: Links to retrieve the PDF for this paystub, or to invoke related APIs
      required:
        - employee
        - employer
        - payPeriod
        - payrollFrequency
        - grossPay
        - netPay
        - withholding

    PaystubList:
      title: Paystub List entity
      description: Response object for /payroll/paystubs API with list of paystubs retrieved
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            paystubs:
              description: Zero or more Paystubs found within the startTime to endTime range
              type: array
              items:
                $ref: '#/components/schemas/Paystub'

    PaystubPdf:
      title: Paystub entity
      description: PDF file of a single paystub
      type: object
      properties:
        paystubId:
          description: >-
            The paystub identification number requested. This can be any ID which the data provider creates
            specific to the consenting person's paystub, perhaps simply the pay date as a string
            optionally followed by a sequence number: "2024-09-30-01". Need only be unique within
            the current employee's consent / token, according to data provider's preference
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        paystubPdf:
          description: The Base64-encoded content of the paystub PDF file
          type: string
          format: base64
        embeddedData:
          description: >-
            Whether the paystub PDF also contains an embedded JSON payload of the Paystub data.
            That should include three custom properties: `fdxVersion` containing the version number of the
            FDX release, `fdxSoftwareId` if software creating the embedded data is registered with FDX,
            and `fdxJson` containing the JSON payload matching the Paystub entity defined here
          type: boolean

    RegionalTaxWithholding:
      title: Regional Tax Withholding
      description: Regional and/or locality tax withholding.
        Common names to use for regional withholdings are State, Local,
        State Unemployment Insurance, Voluntary Plan Disability Insurance,
        State Disability Insurance, and Temporary Disability Insurance.
        (Inheriting properties `amount`, `currency`, `name` and
        `yearToDate` from `PayAmount`)
      type: object
      allOf:
        - $ref: '#/components/schemas/PayAmount'
        - type: object
          properties:
            region:
              description: Name or code of state, province, canton, prefecture or sub-national region
              type: string
            locality:
              description: Name of sub-regional locality such as city, if any
              type: string
            percent:
              description: Percentage rate for this regional or local tax withholding, if specified
              type: number
      required:
        - name
        - amount
        - region

    ############################################################
    #
    # Payroll data types
    #
    ############################################################

    ActiveStatus:
      title: Active/Inactive Status
      description: Specifies the employment status of ACTIVE or INACTIVE
      type: string
      enum:
        - ACTIVE
        - INACTIVE

    EarningType:
      title: Earning Type
      description: The GSE Mapping for a specific earning component.
        For a Government Sponsored Enterprise (GSE), such as Fannie Mae or Freddie Mac.
        One of BASE, BONUS, COMMISSION, OTHER, OVERTIME
      type: string
      enum:
        - BASE
        - BONUS
        - COMMISSION
        - OTHER
        - OVERTIME

    EmploymentType:
      title: Employment type
      description: Specifies the employment type, such as
        CONTRACTED, FULL-TIME, OTHER, PART-TIME, SEASONAL, TEMPORARY
      type: string
      enum:
        - CONTRACTED
        - FULL_TIME
        - OTHER
        - PART_TIME
        - SEASONAL
        - TEMPORARY

    PaymentMethod:
      title: Payment Method
      description: Specifies the method of this payment. One of CASH, CHECK or DIRECT_DEPOSIT
      type: string
      enum:
        - CASH
        - CHECK
        - DIRECT_DEPOSIT

    PayrollFrequency:
      title: Payroll Frequency type
      description: The frequency of employee payments.
        In pay period length order,
          - DAILY
          - WEEKLY
          - BI-WEEKLY
          - SEMI-MONTHLY
          - EVERY 2.6 WEEKS
          - EVERY 4 WEEKS
          - MONTHLY
          - EVERY 5.2 WEEKS
          - QUARTERLY
          - SEMI-ANNUALLY
          - ANNUALLY
          - OTHER
      type: string
      enum:
        - ANNUALLY
        - BI_WEEKLY
        - DAILY
        - EVERY_2_6_WEEKS
        - EVERY_4_WEEKS
        - EVERY_5_2_WEEKS
        - MONTHLY
        - OTHER
        - QUARTERLY
        - SEMI_ANNUALLY
        - SEMI_MONTHLY
        - WEEKLY

    PayrollRateType:
      title: Payroll Rate Type
      description: Specifies the time period of the employee's pay rate.
        In time period length order,
          - HOURLY - Hourly rate
          - DAILY
          - WEEKLY
          - BI-WEEKLY
          - SEMI-MONTHLY
          - EVERY 2.6 WEEKS
          - EVERY 4 WEEKS
          - MONTHLY
          - EVERY 5.2 WEEKS
          - QUARTERLY
          - SEMI-ANNUALLY
          - ANNUAL - Annual salary
          - OTHER
      type: string
      enum:
        - ANNUAL
        - BI_WEEKLY
        - DAILY
        - EVERY_2_6_WEEKS
        - EVERY_4_WEEKS
        - EVERY_5_2_WEEKS
        - HOURLY
        - MONTHLY
        - OTHER
        - QUARTERLY
        - SEMI_ANNUALLY
        - SEMI_MONTHLY
        - WEEKLY

    PayrollReportType:
      title: Payroll Report Type
      description: The type of payroll report,
        VOE - for Verification of Employment,
        VOIE - for Verification of Income and Employment
      type: string
      enum:
        - VOE
        - VOIE

    PaystubSource:
      title: Paystub Source
      description: The source of the paystub data,
        PAYROLL_PROCESSOR, EMPLOYER, or THIRD_PARTY
      type: string
      enum:
        - EMPLOYER
        - PAYROLL_PROCESSOR
        - THIRD_PARTY

    SupplementalStatus:
      title: Supplemental Status
      description: Additional information about ACTIVE/INACTIVE employment status
      type: string
      enum:
        - FURLOUGHED
        - LEAVE
        - MEDICAL_LEAVE
        - MILITARY_LEAVE
        - PATERNITY_LEAVE
        - QUIT
        - RETIRED
        - TERMINATED
        - VACATION
