openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 US Tax API
  description: Financial Data Exchange V6.3.0 US Tax API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 US Tax API
tags:
  - name: Submit Tax Forms
    description: Submit vendor-produced customer tax reporting documents and data to providers
  - name: Tax Forms
    description: Search and retrieve customer tax reporting documents and data
paths:
  ############################################################
  #
  # US Tax paths
  #
  ############################################################

  /tax-forms:
    parameters:
      - $ref: '#/components/parameters/AuthorizationHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: searchForTaxForms
      summary: Search tax forms
      description: Get the full lists of tax document data and tax form images
        available for a specific year for the current authorized customer
      tags:
        - Tax Forms
      security:
        - TaxBasicAuth: []
        - OAuthFapi1Advanced:
            - fdx:tax:read
      parameters:
        - $ref: '#/components/parameters/AccountIdQuery'
        - $ref: '#/components/parameters/TaxYearQuery'
        - $ref: '#/components/parameters/TaxFormsQuery'
        - $ref: '#/components/parameters/AcceptHeader'
        - $ref: '#/components/parameters/TaxDataTypeQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/ResultTypeQuery'
      responses:
        '200':
          description: Array of all the tax document data and tax form
            images available for the customer matching search criteria
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/zip:
              schema:
                description: All the document image(s) downloaded as a zip file, containing one or more forms
                type: string
                format: binary
            application/json:
              schema:
                $ref: '#/components/schemas/TaxStatementList'
              examples:
                ResultType lightweight Search Response with Forms 1099-DIV and 1099-INT:
                  value:
                    statements:
                      - taxYear: 2020
                        taxStatementId: "9876987698769876"
                        attributes:
                          - name: "federalTaxWithheld"
                            value: "4014.00"
                        taxDataType: JSON
                        forms:
                          - tax1099Div:
                              taxYear: 2020
                              taxFormId: "9876987698769876"
                              taxFormDate: 2021-03-30
                              additionalInformation: FDX v6.0
                              taxFormType: Tax1099Div
                      - taxYear: 2020
                        taxStatementId: "6543654365436543"
                        attributes:
                          - name: "federalTaxWithheld"
                            value: "4011.00"
                        taxDataType: JSON
                        forms:
                          - tax1099Int:
                              taxYear: 2020
                              taxFormId: "6543654365436543"
                              taxFormDate: 2021-03-30
                              additionalInformation: FDX v6.0
                              taxFormType: Tax1099Int
                ResultType details Search Response with Form 1098:
                  value:
                    statements:
                      - taxYear: 2023
                        taxStatementId: ID-09990111
                        issuer:
                          tin: 12-3456789
                          partyType: BUSINESS
                          businessName:
                            name1: Financial Intelligence Associates
                          address:
                            line1: 12022 Sundown Valley Dr
                            line2: Suite 230
                            city: Reston
                            region: VA
                            postalCode: "20191"
                            country: US
                          phone:
                            number: "8885551212"
                        recipient:
                          tin: xxx-xx-1234
                          partyType: INDIVIDUAL
                          individualName:
                            first: Kris
                            middle: Q
                            last: Public
                          address:
                            line1: 1 Main St
                            city: Melrose
                            region: NY
                            postalCode: "12121"
                            country: US
                        forms:
                          - tax1098:
                              taxYear: 2023
                              taxFormId: ID-09990111-1098
                              taxFormDate: 2024-02-15
                              taxFormType: Tax1098
                              mortgagedProperties: 9
                              otherInformation: "10. Property tax: $10,017.00"
                              accountNumber: 111-23456
                              mortgageInterest: 1008
                              outstandingPrincipal: 200900
                              originationDate: 2022-03-10
                              overpaidRefund: 4011
                              mortgageInsurance: 5012
                              pointsPaid: 6013
                              isPropertyAddressSameAsBorrowerAddress: true
                              acquisitionDate: 2022-11-15
                              propertyTax: 10017
        '206':
          description: Partial Content success searching for customer Tax Data forms,
            some errors are being returned
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TaxStatementList'
              examples:
                Lightweight Response With Error:
                  value:
                    statements:
                      - taxYear: 2020
                        taxStatementId: "9876987698769876"
                        attributes:
                          - name: "federalTaxWithheld"
                            value: "4014.00"
                        taxDataType: JSON
                        forms:
                          - tax1099Div:
                              taxYear: 2020
                              taxFormId: "9876987698769876"
                              taxFormDate: 2021-03-30
                              additionalInformation: FDX v6.0
                              taxFormType: Tax1099Div
                      - taxYear: 2020
                        taxDataType: JSON
                        forms:
                          - tax1099Int:
                              taxYear: 2020
                              taxFormType: Tax1099Int
                              error:
                                code: '1205'
                                message: Tax Forms not yet been made available
                                debugMessage: 1099-INT forms should be available after 02-01-2021
        '400':
          description: Request is invalid or parameter values are not supported
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Tax Year not Supported:
                  value:
                    code: '1202'
                    message: Tax Year not Supported
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Tax Form Type not supported:
                  value:
                    code: '1201'
                    message: Tax Form Type not supported
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Account ID is required:
                  value:
                    code: '1204'
                    message: Account ID is required
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '404':
          description: Tax Form not Found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Tax Form not Found:
                  value:
                    code: '1200'
                    message: Tax Form not Found
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '406':
          $ref: './fdxapi.components.yaml#/components/responses/406'
        '409':
          description: Tax forms are not currently available for this account or this year
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Operation not supported by Closed account:
                  value:
                    code: '705'
                    message: Tax Forms not available for Closed account
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Tax Forms not yet been made available:
                  value:
                    code: '1205'
                    message: Tax Forms not yet been made available
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'
    post:
      operationId: createTaxForm
      summary: Create tax form
      description: Submit the data for a specific tax document
      tags:
        - Submit Tax Forms
      security:
        - OAuthFapi1Baseline: []
      requestBody:
        content:
          application/json:
            schema:
              description: The full data contents of the tax document and all its included forms including the indexing metadata values
              $ref: '#/components/schemas/TaxStatement'
      responses:
        '201':
          description: Created document for the tax data submitted
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                description: The full data contents of the tax document and all its included forms as ingested
                $ref: '#/components/schemas/TaxStatement'
        '206':
          description: Partial Content success creating customer tax document, some errors are being returned
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                description: The data contents of the tax document as ingested, with Errors on some included forms
                $ref: '#/components/schemas/TaxStatement'
        '400':
          description: Tax Form type is not supported
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Tax Form type is not supported:
                  value:
                    code: '1201'
                    message: Tax Form type is not supported
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Tax Year not supported:
                  value:
                    code: '1202'
                    message: Tax Year not supported
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Account ID is required:
                  value:
                    code: '1204'
                    message: Account ID is required
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /tax-forms/{taxFormId}:
    parameters:
      - $ref: '#/components/parameters/TaxFormIdPath'
      - $ref: '#/components/parameters/AuthorizationHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getTaxForm
      summary: Retrieve tax form
      description: >-
        Get the form image or TaxStatement as json for a single tax document for the customer. Use
        [HTTP Accept request-header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)
        to specify desired content types. See `AcceptHeader` definition for typical values
      tags:
        - Tax Forms
      security:
        - TaxBasicAuth: []
        - OAuthFapi1Advanced:
            - fdx:tax:read
      parameters:
        - $ref: '#/components/parameters/AcceptHeader'
        - $ref: '#/components/parameters/TaxDataTypeQuery'
      responses:
        '200':
          description: >-
            The document image or TaxStatement as json for a single tax document
            for the customer. A single document can include multiple IRS tax forms
            and/or other reporting statements as delivered by providers
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/pdf:
              schema:
                description: The document image downloaded as pdf
                type: string
                format: binary
            application/zip:
              schema:
                description: The document image downloaded as zip file, containing one or more form images
                type: string
                format: binary
            image/gif:
              schema:
                description: The document image downloaded as gif
                type: string
                format: binary
            image/jpeg:
              schema:
                description: The document image downloaded as jpeg
                type: string
                format: binary
            image/tiff:
              schema:
                description: The document image downloaded as tiff
                type: string
                format: binary
            image/png:
              schema:
                description: The document image downloaded as png
                type: string
                format: binary
            application/json:
              schema:
                description: >-
                  The TaxStatement json for a single tax document containing
                  one or more tax reporting forms for the customer
                $ref: '#/components/schemas/TaxStatement'
              examples:
                Tax1099Div and Tax1099Int:
                  value:
                    taxYear: 2020
                    taxStatementId: "1234123412341234"
                    attributes:
                      - name: "Total tax withheld"
                        value: "8025.00"
                    issuer:
                      tin: 12-3456789
                      partyType: BUSINESS
                      businessName:
                        name1: Financial Data Exchange
                      address:
                        line1: 12020 Sunrise Valley Dr
                        line2: Suite 230
                        city: Reston
                        region: VA
                        postalCode: "20191"
                        country: US
                      phone:
                        number: "8885551212"
                    recipient:
                      tin: xxx-xx-1234
                      partyType: INDIVIDUAL
                      individualName:
                        first: Kris
                        middle: Q
                        last: Public
                      address:
                        line1: 1 Main St
                        city: Melrose
                        region: NY
                        postalCode: "12121"
                        country: US
                    taxDataType: JSON
                    forms:
                      - tax1099Div:
                          taxYear: 2020
                          taxFormId: "9876987698769876"
                          taxFormDate: 2021-03-30
                          additionalInformation: FDX v6.0
                          taxFormType: Tax1099Div
                          foreignAccountTaxCompliance: false
                          accountNumber: 111-5555555
                          ordinaryDividends: 1107.0
                          qualifiedDividends: 1208.0
                          totalCapitalGain: 2109.0
                          unrecaptured1250Gain: 2210.0
                          section1202Gain: 2311.0
                          collectiblesGain: 2412.0
                          nonTaxableDistribution: 3013.0
                          federalTaxWithheld: 4014.0
                          section199ADividends: 5015.0
                          investmentExpenses: 6016.0
                          foreignTaxPaid: 7017.0
                          foreignCountry: Mexico
                          cashLiquidation: 9019.0
                          nonCashLiquidation: 10020.0
                          taxExemptInterestDividend: 11021.0
                          specifiedPabInterestDividend: 12022.0
                          stateAndLocal:
                            - stateCode: NY
                              state:
                                taxWithheld: 15023.0
                                taxId: 14-000023
                      - tax1099Int:
                          taxYear: 2020
                          taxFormId: "6543654365436543"
                          taxFormDate: 2021-03-30
                          additionalInformation: FDX v6.0
                          taxFormType: Tax1099Int
                          foreignAccountTaxCompliance: false
                          accountNumber: 111-5555555
                          payerRtn: "007007007"
                          interestIncome: 1008.0
                          earlyWithdrawalPenalty: 2009.0
                          usBondInterest: 3010.0
                          federalTaxWithheld: 4011.0
                          investmentExpenses: 5012.0
                          foreignTaxPaid: 6013.0
                          foreignCountry: Canada
                          taxExemptInterest: 8015.0
                          specifiedPabInterest: 9016.0
                          marketDiscount: 10017.0
                          bondPremium: 11018.0
                          usBondPremium: 12019.0
                          taxExemptBondPremium: 13020.0
                          cusipNumber: CUSIP
                          stateAndLocal:
                            - stateCode: NY
                              state:
                                taxWithheld: 17022.0
                                taxId: 15-000022
        '206':
          description: Partial Content success retrieving a customer tax document, some errors are being returned
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                description: >-
                  The TaxStatement json for a single tax document containing one or more
                  tax reporting forms for the customer, one or more of which contain an Error
                $ref: '#/components/schemas/TaxStatement'
        '400':
          description: Account ID is required for searching or validating authorization
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Tax Form not Found:
                  value:
                    code: '1204'
                    message: Account ID is Required
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '404':
          description: Tax Form for provided Tax Form ID was not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Tax Form not Found:
                  value:
                    code: '1200'
                    message: Tax Form not Found
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '406':
          $ref: './fdxapi.components.yaml#/components/responses/406'
        '409':
          description: Tax forms are not currently available for this account or this year
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Account is Closed:
                  value:
                    code: '705'
                    message: Account is Closed
                    debugMessage: Provider custom developer-level error details for troubleshooting
                Tax Forms not yet been made available:
                  value:
                    code: '1205'
                    message: Tax Forms not yet been made available
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'
    put:
      operationId: updateTaxForm
      summary: Update tax form
      description: Update tax document. Allows you to upload and replace binaries or json document
      tags:
        - Submit Tax Forms
      security:
        - OAuthFapi1Baseline: []
      requestBody:
        content:
          application/json:
            schema:
              description: The full data contents of the document and all its contained forms including the indexing metadata values
              $ref: '#/components/schemas/TaxStatement'
          application/pdf:
            schema:
              description: The document image to upload as pdf
              type: string
              format: binary
          image/gif:
            schema:
              description: The document image to upload as gif
              type: string
              format: binary
          image/jpeg:
            schema:
              description: The document image to upload as jpeg
              type: string
              format: binary
          image/tiff:
            schema:
              description: The document image to upload as tiff
              type: string
              format: binary
          image/png:
            schema:
              description: The document image to upload as png
              type: string
              format: binary
      responses:
        '200':
          description: Ok
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
        '206':
          description: Partial Content success updating customer tax document, some errors are being returned
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                description: The data contents of the tax document as updated, with Errors on some included forms
                $ref: '#/components/schemas/TaxStatement'
        '415':
          description: Server does not support the content type uploaded
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'

components:

  securitySchemes:
    ############################################################
    #
    # Security Schemes
    #
    ############################################################

    OAuthFapi1Baseline:
      $ref: './fdxapi.components.yaml#/components/securitySchemes/OAuthFapi1Baseline'

    OAuthFapi1Advanced:
      $ref: './fdxapi.components.yaml#/components/securitySchemes/OAuthFapi1Advanced'

    TaxBasicAuth:
      type: http
      scheme: basic

  parameters:
    ############################################################
    #
    # US Tax request parameters
    #
    ############################################################

    AcceptHeader:
      name: Accept
      in: header
      description: >-
        Use the [Accept HTTP request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept)
        to indicate one or more content types to request for the search result response. Use `application/json`
        to request data, `application/pdf`, `application/zip` or `image/*` MIME-types to
        request images. In comma-separated array format using values typically from
        './fdxapi.components.yaml#/components/schemas/ContentTypes' enumeration.
        Use in combination with TaxDataTypeQuery parameter to request `application/json`
        responses in 'JSON' or 'BASE64_PDF' format for tax form data
      schema:
        type: string
      required: true
      examples:
        Only JSON data:
          value:
            'Accept: application/json'
        Multiple types accepted:
          value:
            'Accept: application/json, application/zip'

    AccountIdQuery:
      name: accountId
      in: query
      description: Account Identifier for use in searching or authorization. Optional
      schema:
        type: string

    AuthorizationHeader:
      name: Authorization
      in: header
      description: >-
        The [Authorization HTTP request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
        provides credentials to allow access to a protected resources
      schema:
        type: string
      required: true
      examples:
        OAuthFapi2Advanced OAuth 2.0 securityScheme example:
          summary: Follows published FDX API standard OAuth 2.0 security requirements
          description: See [IETF RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750)
            regarding OAuth 2.0 bearer tokens to access protected resources
          value:
            # yamllint disable-line rule:line-length
            'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkZEWCBUYXggVEYgUnVsZXMiLCJpYXQiOjE1MTYyMzkwMjJ9.SZGaxSt9EXqK1GbYTckZbygBDiqS1KaZybzzqf2VxOw'
        OAuthFapi1Baseline securityScheme example:
          summary: Follows published FDX API Data Receiving Entity credentials-based security
          description: See [IETF RFC 7617](https://datatracker.ietf.org/doc/html/rfc7617)
            regarding base64-encoded Basic tokens to access protected resources
          value:
            'Authorization: Basic (Base64 of client_id:client_secret)'
        TaxBasicAuth securityScheme example:
          summary: Follows published FDX Tax Document Alternate Authentication v2023
          description: Also following IETF RFC 7617 Basic Authorization
          value:
            'Authorization: Basic (Base64 of documentId:documentPasscode)'

    TaxDataTypeQuery:
      name: taxDataType
      in: query
      description: Use taxDataType to request `application/json` tax form data response
        in 'JSON' or 'BASE64_PDF' format. Omit if either format is acceptable.
        Used in combination with AcceptHeader requesting `application/json` response
      schema:
        $ref: '#/components/schemas/TaxDataType'

    TaxFormIdPath:
      name: taxFormId
      in: path
      description: The unique ID for this tax form or tax statement
      required: true
      schema:
        $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

    TaxFormsQuery:
      name: taxForms
      in: query
      description: One or more tax form type enums for the specific documents being requested. Comma separated
      style: form
      explode: false
      schema:
        type: array
        items:
          $ref: '#/components/schemas/TaxFormType'

    TaxYearQuery:
      name: taxYear
      in: query
      description: Tax year in which to search for tax forms. Optional
      schema:
        $ref: '#/components/schemas/TaxYear'

  schemas:
    ############################################################
    #
    # US Tax data entities
    #
    ############################################################

    BasicAuthCredentials:
      title: Basic Auth Credentials
      description: Tax form credentials container for QR Code purposes
      type: object
      properties:
        taxYear:
          description: Year for which taxes are being paid
          $ref: '#/components/schemas/TaxYear'
        taxFormType:
          description: Enumerated name of the tax form entity e.g. "TaxW2"
          $ref: '#/components/schemas/TaxFormType'
        id:
          description: Confidential and unique identifier of the tax form
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        passcode:
          description: Unique, randomized and restricted password for this document
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

    BasicAuthForQR:
      title: Basic Auth for QR
      description: Tax form credentials container for QR Code purposes
      type: object
      properties:
        basicAuth:
          description: The Basic Authentication credentials to retrieve a tax form
          $ref: '#/components/schemas/BasicAuthCredentials'
        version:
          description: >-
            [Financial Data Exchange (FDX)](https://financialdataexchange.org/) schema version number (e.g. "V5.0").
          $ref: './fdxapi.components.yaml#/components/schemas/FdxVersion'
        softwareId:
          description: The FDX registration ID of company or software generating this tax data
          type: string
      # Basic Auth for a large 1099-B:
      example:
        basicAuth:
          taxYear: 2023
          taxFormType: Tax1099B
          id: 00677560089990B1
          passcode: PK2Z-0QP-L6EF
        version: V5.0
        softwareId: OakTreeSecurities

    BusinessIncomeStatement:
      title: Business Income Statement
      description: Business Income Statement for IRS Form 1040 Schedule C
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            businessName:
              type: string
              description: Box C, Business name
            sales:
              type: number
              description: Box 1, Gross receipts or sales
            returns:
              type: number
              description: Box 2, Returns and allowances
            otherIncome:
              type: array
              description: Box 6, Other income, including federal and state gasoline
                or fuel tax credit or refund
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            advertising:
              type: number
              description: Box 8, Advertising
            carAndTruck:
              type: number
              description: Box 9, Car and truck expenses
            commissions:
              type: number
              description: Box 10, Commissions and fees
            contractLabor:
              type: number
              description: Box 11, Contract labor
            depletion:
              type: number
              description: Box 12, Depletion
            depreciation:
              type: number
              description: Box 13, Depreciation
            employeeBenefits:
              type: number
              description: Box 14, Employee benefit programs
            insurance:
              type: number
              description: Box 15, Insurance
            mortgageInterest:
              type: number
              description: Box 16a, Mortgage interest
            otherInterest:
              type: number
              description: Box 16b, Other interest
            legal:
              type: number
              description: Box 17, Legal and professional services
            office:
              type: number
              description: Box 18, Office expense
            pension:
              type: number
              description: Box 19, Pension and profit-sharing plans
            equipmentRent:
              type: number
              description: Box 20a, Equipment rent
            otherRent:
              type: number
              description: Box 20b, Other rent
            repairs:
              type: number
              description: Box 21, Repairs and maintenance
            supplies:
              type: number
              description: Box 22, Supplies
            taxes:
              type: number
              description: Box 23, Taxes and licenses
            travel:
              type: number
              description: Box 24a, Travel
            meals:
              type: number
              description: Box 24b, Deductible meals
            utilities:
              type: number
              description: Box 25, Utilities
            wages:
              type: number
              description: Box 26, Wages
            otherExpenses:
              type: array
              description: Box 27, Other expenses
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            beginningInventory:
              type: number
              description: Box 35, Inventory at beginning of year
            purchases:
              type: number
              description: Box 36, Purchases
            costOfLabor:
              type: number
              description: Box 37, Cost of labor
            materials:
              type: number
              description: Box 38, Materials and supplies
            otherCosts:
              type: array
              description: Box 39, Other costs
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            endingInventory:
              type: number
              description: Box 41, Inventory at end of year
            capitalExpenditures:
              type: array
              description: Capital expenditures, for use in calculating Depreciation
              items:
                $ref: '#/components/schemas/DateAmount'

    CodeAmount:
      title: Code and Amount
      description: Code and amount pair used on IRS W-2, K-1, etc.
      type: object
      properties:
        code:
          description: Code
          type: string
        amount:
          description: Amount
          type: number

    CryptocurrencyGainOrLoss:
      title: Gain or loss from cryptocurrency transaction
      description: Tax information for a single cryptocurrency transaction.
        If reported on Form 1099-B, use Tax1099B and SecurityDetail instead of this entity.
      type: object
      properties:
        cryptocurrencyName:
          description: Cryptocurrency name (e.g. Bitcoin)
          type: string
        symbol:
          description: Cryptocurrency abbreviation or symbol (e.g. BTC)
          type: string
        quantity:
          description: Quantity (e.g. 0.0125662)
          type: number
        saleDescription:
          description: Description of property (1099-B box 1a)
          type: string
        dateAcquired:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date acquired (1099-B box 1b)
        variousDatesAcquired:
          type: boolean
          description: Acquired on various dates (1099-B box 1b)
        dateOfSale:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date sold or disposed (1099-B box 1c)
        salesPrice:
          description: Proceeds (not price per share, 1099-B box 1d)
          type: number
        costBasis:
          description: Cost or other basis (1099-B box 1e)
          type: number
        longOrShort:
          $ref: '#/components/schemas/SaleTermType'
          description: LONG or SHORT (1099-B box 2)

    CryptocurrencyTaxStatement:
      title: Cryptocurrency Tax Statement list
      description: Array of cryptocurrency gains and losses
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            gainsAndLosses:
              type: array
              description: The list of cryptocurrency gains and losses
              items:
                $ref: '#/components/schemas/CryptocurrencyGainOrLoss'

    DateAmount:
      title: Date and Amount
      description: Date, description, and amount. When used in 1098-Q, description is optional
      type: object
      properties:
        date:
          description: Date of amount. When used in 1098-Q, date of last payment in month
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
        description:
          description: Description of amount. When used in 1098-Q, may use MonthAbbreviation
          type: string
        amount:
          type: number
          description: Amount of payment or receipt. When used in 1098-Q, monthly total

    DescriptionAmount:
      title: Description and Amount
      description: Description and amount pair used on IRS W-2, etc.
      type: object
      properties:
        description:
          description: Description
          type: string
        amount:
          description: Amount
          type: number

    FarmIncomeStatement:
      title: Farm Income Statement
      description: Farm Income Statement for IRS Form 1040 Schedule F
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            cropOrActivity:
              type: string
              description: Box A, Principal crop or activity
            sales:
              type: number
              description: Box 1a, Sales of livestock and other resale items
            costOfItemsSold:
              type: number
              description: Box 1b, Cost or other basis of livestock or other items
            salesOfRaised:
              type: number
              description: Box 2, Sales of livestock, produce, grains, and other products
                you raised
            coopDistributions:
              type: number
              description: Box 3a, Cooperative distributions
            agProgramPayments:
              type: number
              description: Box 4a, Agricultural program payments
            cccLoans:
              type: number
              description: Box 5a, Commodity Credit Corporation (CCC) loans reported
                under election
            cropInsuranceProceeds:
              type: number
              description: Box 6a, Crop insurance proceeds and federal crop disaster
                payments
            customHireIncome:
              type: number
              description: Box 7, Custom hire (machine work) income
            otherIncome:
              type: array
              description: Box 8, Other income
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            carAndTruck:
              type: number
              description: Box 10, Car and truck expenses
            chemicals:
              type: number
              description: Box 11, Chemicals
            conservation:
              type: number
              description: Box 12, Conservation expenses
            customHireExpenses:
              type: number
              description: 'Box 13, Custom hire (machine work) '
            depreciation:
              type: number
              description: Box 14, Depreciation
            employeeBenefitPrograms:
              type: number
              description: Box 15, Employee benefit programs
            feed:
              type: number
              description: Box 16, Feed
            fertilizers:
              type: number
              description: Box 17, Fertilizers and lime
            freight:
              type: number
              description: Box 18, Freight and trucking
            fuel:
              type: number
              description: Box 19, Gasoline, fuel, and oil
            insurance:
              type: number
              description: Box 20, Insurance (other than health)
            mortgageInterest:
              type: number
              description: Box 21a, Mortgage Interest
            otherInterest:
              type: number
              description: Box 21b, Other interest
            laborHired:
              type: number
              description: Box 22, Labor hired
            pension:
              type: number
              description: Box 23, Pension and profit-sharing plans
            equipmentRent:
              type: number
              description: 'Box 24a, Rent or lease: Vehicles, machinery, equipment'
            otherRent:
              type: number
              description: 'Box 24b, Rent or lease: Other'
            repairs:
              type: number
              description: Box 25, Repairs and maintenance
            seeds:
              type: number
              description: Box 26, Seeds and plants
            storage:
              type: number
              description: Box 27, Storage and warehousing
            supplies:
              type: number
              description: Box 28, Supplies
            taxes:
              type: number
              description: Box 29, Taxes
            utilities:
              type: number
              description: Box 30, Utilities
            veterinary:
              type: number
              description: Box 31, Veterinary, breeding, and medicine
            otherExpenses:
              type: array
              description: Box 32, Other expenses
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            capitalExpenditures:
              type: array
              description: Capital expenditures, for use in calculating Depreciation
              items:
                $ref: '#/components/schemas/DateAmount'

    FarmRentalIncomeStatement:
      title: Farm Rental Income Statement
      description: Farm Rental Income Statement for IRS Form 4835
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            incomeFromProduction:
              type: number
              description: Box 1, Income from production of livestock, produce, grains,
                and other crops
            coopDistributions:
              type: number
              description: Box 2a, Cooperative distributions
            agProgramPayments:
              type: number
              description: Box 3a, Agricultural program payments
            cccLoans:
              type: number
              description: Box 4a, Commodity Credit Corporation (CCC) loans reported
                under election
            cropInsuranceProceeds:
              type: number
              description: Box 5a, Crop insurance proceeds and federal crop disaster
                payments
            otherIncome:
              type: array
              description: Box 6, Other income
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            carAndTruck:
              type: number
              description: Box 8, Car and truck expenses
            chemicals:
              type: number
              description: Box 9, Chemicals
            conservation:
              type: number
              description: Box 10, Conservation expenses
            customHireExpenses:
              type: number
              description: 'Box 11, Custom hire (machine work) '
            depreciation:
              type: number
              description: Box 12, Depreciation
            employeeBenefitPrograms:
              type: number
              description: Box 13, Employee benefit programs
            feed:
              type: number
              description: Box 14, Feed
            fertilizers:
              type: number
              description: Box 15, Fertilizers and lime
            freight:
              type: number
              description: Box 16, Freight and trucking
            fuel:
              type: number
              description: Box 17, Gasoline, fuel, and oil
            insurance:
              type: number
              description: Box 18, Insurance (other than health)
            mortgageInterest:
              type: number
              description: Box 19a, Mortgage Interest
            otherInterest:
              type: number
              description: Box 19b, Other interest
            laborHired:
              type: number
              description: Box 20, Labor hired
            pension:
              type: number
              description: Box 21, Pension and profit-sharing plans
            equipmentRent:
              type: number
              description: 'Box 22a, Rent or lease: Vehicles, machinery, equipment'
            otherRent:
              type: number
              description: 'Box 22b, Rent or lease: Other'
            repairs:
              type: number
              description: Box 23, Repairs and maintenance
            seeds:
              type: number
              description: Box 24, Seeds and plants
            storage:
              type: number
              description: Box 25, Storage and warehousing
            supplies:
              type: number
              description: Box 26, Supplies
            taxes:
              type: number
              description: Box 27, Taxes
            utilities:
              type: number
              description: Box 28, Utilities
            veterinary:
              type: number
              description: Box 29, Veterinary, breeding, and medicine
            otherExpenses:
              type: array
              description: Box 30, Other expenses
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            capitalExpenditures:
              type: array
              description: Capital expenditures, for use in calculating Depreciation
              items:
                $ref: '#/components/schemas/DateAmount'

    Form1042Agent:
      title: Form 1042-S Agent
      description: >-
        One of various persons or businesses involved in Form 1042-S reporting. Use
          * `tin` for
            * Box 12a, Withholding Agent EIN,
            * Box 13e, Recipient U.S. TIN,
            * Box 14b, Primary Withholding Agent EIN,
            * Box 15a, Intermediary or flow-through entity EIN,
            * Box 16b, Payer TIN
          * `individualName` or `businessName` for
            * Box 12d, Withholding Agent name,
            * Box 13a, Recipient name,
            * Box 14a, Primary Withholding Agent name,
            * Box 15d, Intermediary or flow-through entity name,
            * Box 16a, Payer name
          * `address.country` for
            * Box 12f, Withholding Agent Country code,
            * Box 13b, Recipient Country code,
            * Box 15f, Intermediary or flow-through entity Country code
          * `address` for
            * Boxes 12h-i, Withholding Agent Address,
            * Boxes 13c-d, Recipient Address,
            * Boxes 15h-i, Intermediary or flow-through entity Address
      type: object
      allOf:
        - $ref: '#/components/schemas/TaxParty'
        - type: object
          properties:
            ch3StatusCode:
              type: string
              description: >-
                Ch. 3 status code,
                  * Box 12b, Withholding Agent,
                  * Box 13f, Recipient,
                  * Box 15b, Intermediary or flow-through entity,
                  * Box 16d, Payer
            ch4StatusCode:
              type: string
              description: >-
                Ch. 4 status code,
                  * Box 12c, Withholding Agent,
                  * Box 13g, Recipient,
                  * Box 15c, Intermediary or flow-through entity,
                  * Box 16e, Payer
            giin:
              type: string
              description: >-
                Agent's Global Intermediary Identification Number (GIIN),
                  * Box 12e, Withholding Agent,
                  * Box 13h, Recipient,
                  * Box 15e, Intermediary or flow-through entity,
                  * Box 16c, Payer
            foreignTin:
              type: string
              description: >-
                Foreign tax identification number, if any,
                  * Box 12g, Withholding Agent,
                  * Box 13i, Recipient,
                  * Box 15g, Intermediary or flow-through entity

    Form1042Recipient:
      title: Form 1042-S Recipient
      description: Recipient for Form 1042-S, Boxes 13a-j, 13l
      type: object
      allOf:
        - $ref: '#/components/schemas/Form1042Agent'
        - type: object
          properties:
            lobCode:
              type: string
              description: Box 13j, Recipient's LOB code, if any
            dateOfBirth:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 13l, Recipient's date of birth

    HealthInsuranceCoverage:
      title: Health Insurance Coverage
      description: Used on Form 1095-A Part III
      type: object
      properties:
        enrollmentPremium:
          description: Monthly enrollment premiums
          type: number
        slcspPremium:
          description: Monthly second lowest cost silver plan (SLCSP) premium
          type: number
        advancePremiumTaxCreditPayment:
          description: Monthly advance payment of premium tax credit
          type: number
        month:
          $ref: '#/components/schemas/CoverageMonth'
          description: Month of coverage

    HealthInsuranceCoveredIndividual:
      title: Health Insurance Covered Individual
      description: Used on Form 1095-B Part IV and Form 1095-C Part III
      type: object
      properties:
        name:
          $ref: './fdxapi.components.yaml#/components/schemas/IndividualName'
          description: Name of responsible individual
        tin:
          description: Social security number or other TIN
          type: string
        dateOfBirth:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date of birth
        coveredAll12Months:
          type: boolean
          description: Covered all 12 months
        coveredMonths:
          description: Months covered
          type: array
          items:
            $ref: '#/components/schemas/MonthAbbreviation'

    HealthInsuranceMarketplaceCoveredIndividual:
      title: Health Insurance Marketplace Covered Individual
      description: Used on Form 1095-A Part II
      type: object
      properties:
        name:
          description: Covered individual name
          type: string
        tin:
          description: Covered individual SSN
          type: string
        dateOfBirth:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Covered individual date of birth
        policyStartDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Coverage start date
        policyTerminationDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Coverage termination date

    LocalTaxWithholding:
      title: Local Tax Withholding
      description: Income in a locality and its tax withholding
      type: object
      properties:
        taxWithheld:
          description: Amount of local income tax withheld
          type: number
        localityName:
          description: Locality name
          type: string
        income:
          description: Income amount for local tax purposes
          type: number

    MonthAmount:
      title: Month and Amount
      description: Month and amount pair used on IRS Form 1099-K, etc.
      type: object
      properties:
        month:
          $ref: '#/components/schemas/MonthAbbreviation'
          description: Month
        amount:
          description: Amount
          type: number

    NameAddress:
      title: Name and Address
      description: Individual or business name with address
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/Address'
        - $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'

    NameAddressPhone:
      title: Name, Address and Phone
      description: Contact phone number with name and address
      type: object
      allOf:
        - $ref: '#/components/schemas/NameAddress'
        - type: object
          properties:
            phone:
              $ref: './fdxapi.components.yaml#/components/schemas/TelephoneNumberPlusExtension'
              description: Phone number

    OfferOfHealthInsuranceCoverage:
      title: Offer of Health Insurance Coverage
      description: Health insurance coverage offer for part II of IRS Form 1095-C
      type: object
      properties:
        coverageCode:
          description: Offer of Coverage (enter required code)
          type: string
        requiredContribution:
          description: Employee required contribution
          type: number
        section4980HCode:
          description: Section 4980H Safe Harbor and Other Relief (enter code)
          type: string
        postalCode:
          type: string
          maxLength: 10
          description: Box 17, ZIP Code
        month:
          $ref: '#/components/schemas/CoverageMonth'
          description: Month

    RentalIncomeStatement:
      title: Rental Income Statement
      description: Rental Income Statement for IRS Form 1040 Schedule E
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            propertyAddress:
              description: Box 1a, Physical address of property (street, city, state, ZIP code)
              $ref: './fdxapi.components.yaml#/components/schemas/Address'
            rents:
              type: number
              description: Box 3, Rents received
            advertising:
              type: number
              description: Box 5, Advertising
            auto:
              type: number
              description: Box 6, Auto and travel
            cleaning:
              type: number
              description: Box 7, Cleaning and maintenance
            commissions:
              type: number
              description: Box 8, Commissions
            insurance:
              type: number
              description: Box 9, Insurance
            legal:
              type: number
              description: Box 10, Legal and other professional fees
            managementFees:
              type: number
              description: Box 11, Management fees
            mortgageInterest:
              type: number
              description: Box 12, Mortgage interest paid to banks, etc.
            otherInterest:
              type: number
              description: Box 13, Other interest
            repairs:
              type: number
              description: Box 14, Repairs
            supplies:
              type: number
              description: Box 15, Supplies
            taxes:
              type: number
              description: Box 16, Taxes
            utilities:
              type: number
              description: Box 17, Utilities
            depreciationExpense:
              type: number
              description: Box 18, Depreciation
            otherExpenses:
              type: array
              description: Box 19, Other expenses
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            capitalExpenditures:
              type: array
              description: Capital expenditures, for use in calculating Depreciation
              items:
                $ref: '#/components/schemas/DateAmount'

    RoyaltyIncomeStatement:
      title: Royalty Income Statement
      description: Royalty Income Statement for IRS Form 1040 Schedule E
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            propertyAddress:
              description: Box 1a, Physical address of property (street, city, state, ZIP code)
              $ref: './fdxapi.components.yaml#/components/schemas/Address'
            royalties:
              type: number
              description: Box 3, Royalties received
            advertising:
              type: number
              description: Box 5, Advertising
            auto:
              type: number
              description: Box 6, Auto and travel
            cleaning:
              type: number
              description: Box 7, Cleaning and maintenance
            commissions:
              type: number
              description: Box 8, Commissions
            insurance:
              type: number
              description: Box 9, Insurance
            legal:
              type: number
              description: Box 10, Legal and other professional fees
            managementFees:
              type: number
              description: Box 11, Management fees
            mortgageInterest:
              type: number
              description: Box 12, Mortgage interest paid to banks, etc.
            otherInterest:
              type: number
              description: Box 13, Other interest
            repairs:
              type: number
              description: Box 14, Repairs
            supplies:
              type: number
              description: Box 15, Supplies
            taxes:
              type: number
              description: Box 16, Taxes
            utilities:
              type: number
              description: Box 17, Utilities
            depletionExpense:
              type: number
              description: Box 18, Depletion
            otherExpenses:
              type: array
              description: Box 19, Other expenses
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            capitalExpenditures:
              type: array
              description: Capital expenditures, for use in calculating Depreciation
              items:
                $ref: '#/components/schemas/DateAmount'

    SecurityDetail:
      title: Security Detail, IRS Form 1099-B
      description: Tax information for a single security transaction
      type: object
      properties:
        checkboxOnForm8949:
          description: Applicable checkbox on Form 8949
          type: string
        securityName:
          description: Security name
          type: string
        numberOfShares:
          description: Number of shares
          type: number
        saleDescription:
          description: Box 1a, Description of property
          type: string
        dateAcquired:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Box 1b, Date acquired
        variousDatesAcquired:
          type: boolean
          description: Box 1b, Date acquired Various
        dateOfSale:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Box 1c, Date sold or disposed
        salesPrice:
          description: Box 1d, Proceeds (not price per share)
          type: number
        accruedMarketDiscount:
          description: Box 1f, Accrued market discount
          type: number
        adjustmentCodes:
          description: Other adjustments (code and amount)
          type: array
          items:
            $ref: '#/components/schemas/CodeAmount'
        costBasis:
          description: Box 1e, Cost or other basis
          type: number
        correctedCostBasis:
          description: >-
            Corrected cost basis. May be supplied in lieu of adjustmentCode code B.
            If both adjustmentCodes and correctedCostBasis are supplied,
            costBasis plus adjustmentCode B should equal correctedCostBasis
          type: number
        washSaleLossDisallowed:
          description: Box 1g, Wash sale loss disallowed
          type: number
        longOrShort:
          $ref: '#/components/schemas/SaleTermType'
          description: Box 2, LONG or SHORT
        ordinary:
          type: boolean
          description: Box 2, Ordinary
        collectible:
          type: boolean
          description: Box 3, Collectibles
        qof:
          type: boolean
          description: Box 3, Qualified Opportunity Fund (QOF)
        federalTaxWithheld:
          description: Box 4, Federal income tax withheld
          type: number
        noncoveredSecurity:
          type: boolean
          description: Box 5, Noncovered security
        grossOrNet:
          $ref: '#/components/schemas/SaleProceedsType'
          description: 'Box 6, Reported to IRS: GROSS or NET'
        lossNotAllowed:
          type: boolean
          description: Box 7, Loss not allowed based on proceeds
        basisReported:
          type: boolean
          description: Box 12, Basis reported to IRS
        stateAndLocal:
          description: Boxes 14-16, State and Local tax withholding
          type: array
          items:
            $ref: '#/components/schemas/StateAndLocalTaxWithholding'
        cusip:
          description: CUSIP number
          type: string
        foreignAccountTaxCompliance:
          type: boolean
          description: Foreign account tax compliance
        expiredOption:
          $ref: '#/components/schemas/ExpiredOptionType'
          description: >-
            To indicate gain or loss resulted from option expiration.
            If salesPrice (1d, proceeds) is zero, use PURCHASED.
            If costBasis (1e) is zero, use GRANTED
        investmentSaleType:
          $ref: '#/components/schemas/InvestmentSaleType'
          description: Type of investment sale

    StateAndLocalTaxWithholding:
      title: State and Local Tax Withholding
      description: Income in a state and/or locality and its or their tax withholding
      type: object
      properties:
        stateCode:
          description: State two-digit code
          $ref: './fdxapi.components.yaml#/components/schemas/StateCode'
        state:
          description: Amount of state income tax withheld
          $ref: '#/components/schemas/StateTaxWithholding'
        local:
          description: Amount of local income tax withheld, if any
          $ref: '#/components/schemas/LocalTaxWithholding'

    StateTaxWithholding:
      title: State Tax Withholding
      description: Income in a state and its tax withholding
      type: object
      properties:
        taxWithheld:
          description: Amount of state income tax withheld
          type: number
        taxId:
          description: Filer's state tax id
          type: string
        income:
          description: Income amount for state tax purposes
          type: number

    Tax:
      title: Tax
      description: Base entity for all IRS Tax forms
      type: object
      properties:
        taxYear:
          description: Year for which taxes are being paid
          $ref: '#/components/schemas/TaxYear'
        corrected:
          type: boolean
          description: True to indicate this is a corrected tax form
        accountId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long-term persistent identity of the source account. Not the account number
        taxFormId:
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
          description: Long-term persistent id for this tax form.
            Depending upon the data provider, this may be the same id as the enclosing tax statement id,
            or this may be a different id, or this id may be omitted.
        taxFormDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Date of production or delivery of the tax form
        additionalInformation:
          description: Additional explanation text or content about this tax form
          type: string
        taxFormType:
          $ref: '#/components/schemas/TaxFormType'
          description: Enumerated name of the tax form entity e.g. "TaxW2"
        issuer:
          $ref: '#/components/schemas/TaxParty'
          description: Issuer's name, address, phone, and TIN.
            Issuer data need only be transmitted on enclosing TaxStatement,
            if it is the same on all its included tax forms.
        recipient:
          $ref: '#/components/schemas/TaxParty'
          description: Recipient's name, address, phone, and TIN.
            Recipient data need only be transmitted on enclosing TaxStatement,
            if it is the same on all its included tax forms.
        attributes:
          description: >-
            Additional attributes for this tax form when defined fields are not available.
            Some specific additional attributes already defined by providers:
            Fields required by [IRS FIRE](https://www.irs.gov/e-file-providers/filing-information-returns-electronically-fire):
            Name Control, Type of Identification Number (EIN, SSN, ITIN, ATIN).
            (ATIN is tax ID number for pending adoptions.)
            Tax form provider field for taxpayer notification: Recipient Email Address.
          type: array
          items:
            $ref: '#/components/schemas/TaxFormAttribute'
          example:
            # IRS FIRE Name Control
            - name: nameControl
              value: WILC
            # IRS FIRE EIN Type of Identification Number
            - name: recipientIdType
              value: EIN
              code: '1'
            # IRS FIRE SSN Type of Identification Number
            - name: recipientIdType
              value: SSN
              code: '2'
            # IRS FIRE ITIN Type of Identification Number
            - name: recipientIdType
              value: ITIN
              code: '2'
            # IRS FIRE ATIN Type of Identification Number
            - name: recipientIdType
              value: ATIN
              code: '2'
        error:
          description: Present if an error was encountered while retrieving this form
          $ref: './fdxapi.components.yaml#/components/schemas/Error'
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'
          description: Links to retrieve this form as data or image, or to invoke other APIs

    Tax1041K1:
      title: Form 1041 Schedule K-1
      description: Beneficiary's Share of Income, Deductions, Credits, etc., from Estate or Trust
        (boxes A-B as issuer) and Fiduciary (box C) to Beneficiary (boxes F-G as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            finalK1:
              type: boolean
              description: Final K-1
            amendedK1:
              type: boolean
              description: Amended K-1
            fiscalYearBegin:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year begin date
            fiscalYearEnd:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year end date
            form1041T:
              type: boolean
              description: Box D, Check if Form 1041-T was filed
            date1041T:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box D, and enter the date it was filed
            final1041:
              type: boolean
              description: Box E, Check if this is the final Form 1041 for the estate or trust
            domestic:
              type: boolean
              description: Box H, Domestic beneficiary
            foreign:
              type: boolean
              description: Box H, Foreign beneficiary
            interestIncome:
              description: Box 1, Interest income
              type: number
            ordinaryDividends:
              description: Box 2a, Ordinary dividends
              type: number
            qualifiedDividends:
              description: Box 2b, Qualified dividends
              type: number
            netShortTermGain:
              description: Box 3, Net short-term capital gain
              type: number
            netLongTermGain:
              description: Box 4a, Net long-term capital gain
              type: number
            gain28Rate:
              description: Box 4b, 28% rate gain
              type: number
            unrecaptured1250Gain:
              description: Box 4c, Unrecaptured section 1250 gain
              type: number
            otherPortfolioIncome:
              description: Box 5, Other portfolio and nonbusiness income
              type: number
            ordinaryBusinessIncome:
              description: Box 6, Ordinary business income
              type: number
            netRentalRealEstateIncome:
              description: Box 7, Net rental real estate income
              type: number
            otherRentalIncome:
              description: Box 8, Other rental income
              type: number
            directlyApportionedDeductions:
              description: Box 9, Directly apportioned deductions
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            estateTaxDeduction:
              description: Box 10, Estate tax deduction
              type: number
            finalYearDeductions:
              description: Box 11, Final year deductions
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            fiduciary:
              $ref: '#/components/schemas/TaxParty'
              description: Box C, Fiduciary's name and address
            amtAdjustments:
              description: Box 12, Alternative minimum tax adjustment
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            credits:
              description: Box 13, Credits and credit recapture
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            otherInfo:
              description: Box 14, Other information
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'

    Tax1042S:
      title: Form 1042-S
      description: Foreign Person's U.S. Source Income Subject to Withholding,
        from WithholdingAgent (boxes 12a-i) to Recipient (boxes 13a-j, 13l as form1042Recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            formId:
              type: string
              description: Unique form identifier
            amended:
              type: boolean
              description: Amended
            amendmentNumber:
              type: integer
              description: Amendment number
              format: int32
            incomeTypeCode:
              type: string
              description: Box 1, Income code
            grossIncome:
              type: number
              description: Box 2, Gross income
            chapterIndicator:
              type: string
              description: Box 3, Chapter indicator
            ch3ExemptionCode:
              type: string
              description: Box 3a, Exemption code
            ch3TaxRate:
              type: number
              description: Box 3b, Tax rate
              format: double
            ch4ExemptionCode:
              type: string
              description: Box 4a, Exemption code
            ch4TaxRate:
              type: number
              description: Box 4b, Tax rate
              format: double
            withholdingAllowance:
              type: number
              description: Box 5, Withholding allowance
            netIncome:
              type: number
              description: Box 6, Net income
            federalTaxWithheld:
              type: number
              description: Box 7a, Federal tax withheld
            escrowProceduresApplied:
              type: boolean
              description: Box 7b, Check if federal tax withheld was not deposited with
                the IRS because escrow procedures were applied
            subsequentYear:
              type: boolean
              description: Box 7c, Check if withholding occurred in subsequent year
                with respect to a partnership interest
            otherAgentsTaxWithheld:
              type: number
              description: Box 8, Tax withheld by other agents
            recipientRepaidAmount:
              type: number
              description: Box 9, Overwithheld tax repaid to recipient pursuant to adjustment
                procedures
            totalTaxWithholdingCredit:
              type: number
              description: Box 10, Total withholding credit
            withholdingAgentTaxPaid:
              type: number
              description: Box 11, Tax paid by withholding agent (amounts not withheld)
            withholdingAgent:
              description: Boxes 12a-i, Withholding agent
              $ref: '#/components/schemas/Form1042Agent'
            form1042Recipient:
              description: Boxes 13a-j, 13l, Recipient for Form 1042-S
              $ref: '#/components/schemas/Form1042Recipient'
            accountNumber:
              description: Box 13k, Recipient account number
              type: string
            primary:
              description: Boxes 14a-b, Primary Withholding Agent
              $ref: '#/components/schemas/Form1042Agent'
            prorataBasisReporting:
              description: Box 15, Check if pro-rata basis reporting
              type: boolean
            intermediary:
              description: Boxes 15a-i, Intermediary or flow thru entity
              $ref: '#/components/schemas/Form1042Agent'
            payer:
              description: Boxes 16a-e, Payer
              $ref: '#/components/schemas/Form1042Agent'
            stateAndLocal:
              description: Box 17, State and Local tax withholding
              $ref: '#/components/schemas/StateAndLocalTaxWithholding'

    Tax1065K1:
      title: Form 1065 Schedule K-1
      description: Partner's Share of Income, Deductions, Credits, etc.,
        from Partnership (boxes A, D as issuer) to Partner (boxes E-F as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            fiscalYearBegin:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year begin date
            fiscalYearEnd:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year end data
            finalK1:
              type: boolean
              description: Final K-1
            amendedK1:
              type: boolean
              description: Amended K-1
            irsCenter:
              description: Box C, IRS Center where partnership filed return
              type: string
            publiclyTraded:
              type: boolean
              description: Box D, Check if this is a publicly traded partnership (PTP)
            generalPartner:
              type: boolean
              description: Box G, General partner or LLC member-manager
            limitedPartner:
              type: boolean
              description: Box G, Limited partner or other LLC member
            domestic:
              type: boolean
              description: Box H1, Domestic partner
            foreign:
              type: boolean
              description: Box H1, Foreign partner
            disregardedEntity:
              type: boolean
              description: Box H2, Check if the partner is a disregarded entity (DE), and enter the
                partner's TIN and Name
            disregardedEntityTin:
              description: Box H2, Disregarded entity partner's TIN
              type: string
            disregardedEntityName:
              description: Box H2, Disregarded entity partner's Name
              type: string
            entityType:
              description: Box I1, What type of entity is this partner?
              type: string
            retirementPlan:
              type: boolean
              description: Box I2, If this partner is a retirement plan (IRA/SEP/Keogh/etc.), check here
            profitShareBegin:
              description: Box J, Partner's share of profit - beginning
              type: number
              format: double
            profitShareEnd:
              description: Box J, Partner's share of profit - ending
              type: number
              format: double
            lossShareBegin:
              description: Box J, Partner's share of loss - beginning
              type: number
              format: double
            lossShareEnd:
              description: Box J, Partner's share of loss - ending
              type: number
              format: double
            capitalShareBegin:
              description: Box J, Partner's share of capital - beginning
              type: number
              format: double
            capitalShareEnd:
              description: Box J, Partner's share of capital - ending
              type: number
              format: double
            decreaseDueToSaleOrExchange:
              type: boolean
              deprecated: true
              description: Box J, Check if decrease is due to sale or exchange of partnership interest.
                Deprecated and no longer used beginning tax year 2023.
                Use `decreaseDueToSale` and `decreaseDueToExchange` instead
            decreaseDueToSale:
              type: boolean
              description: Box J, Check if decrease is due to sale of partnership interest
            decreaseDueToExchange:
              type: boolean
              description: Box J, Check if decrease is due to exchange of partnership interest
            nonrecourseLiabilityShareBegin:
              description: Box K1, Partner's share of liabilities - beginning - nonrecourse
              type: number
            nonrecourseLiabilityShareEnd:
              description: Box K1, Partner's share of liabilities - ending - nonrecourse
              type: number
            qualifiedLiabilityShareBegin:
              description: Box K1, Partner's share of liabilities - beginning - qualified nonrecourse financing
              type: number
            qualifiedLiabilityShareEnd:
              description: Box K1, Partner's share of liabilities - ending - qualified nonrecourse financing
              type: number
            recourseLiabilityShareBegin:
              description: Box K1, Partner's share of liabilities - beginning - recourse
              type: number
            recourseLiabilityShareEnd:
              description: Box K1, Partner's share of liabilities - ending - recourse
              type: number
            includesLowerTierLiability:
              type: boolean
              description: Box K2, Check this box if item K1 includes liability amounts from lower tier partnerships
            liabilitySubjectToGuarantees:
              type: boolean
              description: Box K3, Check if any of the above liability is subject to
                guarantees or other payment obligations by the partner
            capitalAccountBegin:
              description: Box L, Partner's capital account analysis - Beginning capital account
              type: number
            capitalAccountContributions:
              description: Box L, Partner's capital account analysis - Capital contributed during the year
              type: number
            capitalAccountIncrease:
              description: Box L, Partner's capital account analysis - Current year net income (loss)
              type: number
            capitalAccountOther:
              description: Box L, Partner's capital account analysis - Other increase (decrease)
              type: number
            capitalAccountWithdrawals:
              description: Box L, Partner's capital account analysis - Withdrawals & distributions
              type: number
            capitalAccountEnd:
              description: Box L, Partner's capital account analysis - Ending capital account
              type: number
            builtInGain:
              type: boolean
              description: Box M, Did the partner contribute property with a built-in gain or loss? - Yes
            unrecognizedSection704Begin:
              description: Box N, Partner's Share of Net Unrecognized Section 704(c) Gain or (Loss) - beginning
              type: number
            unrecognizedSection704End:
              description: Box N, Partner's Share of Net Unrecognized Section 704(c) Gain or (Loss) - ending
              type: number
            ordinaryIncome:
              description: Box 1, Ordinary business income (loss)
              type: number
            netRentalRealEstateIncome:
              description: Box 2, Net rental real estate income (loss)
              type: number
            otherRentalIncome:
              description: Box 3, Other net rental income (loss)
              type: number
            guaranteedPaymentServices:
              description: Box 4a, Guaranteed payments for services
              type: number
            guaranteedPaymentCapital:
              description: Box 4b, Guaranteed payments for capital
              type: number
            guaranteedPayment:
              description: Box 4c, Total guaranteed payments
              type: number
            interestIncome:
              description: Box 5, Interest income
              type: number
            ordinaryDividends:
              description: Box 6a, Ordinary dividends
              type: number
            qualifiedDividends:
              description: Box 6b, Qualified dividends
              type: number
            dividendEquivalents:
              description: Box 6c, Dividend equivalents
              type: number
            royalties:
              description: Box 7, Royalties
              type: number
            netShortTermGain:
              description: Box 8, Net short-term capital gain (loss)
              type: number
            netLongTermGain:
              description: Box 9a, Net long-term capital gain (loss)
              type: number
            collectiblesGain:
              description: Box 9b, Collectibles (28%) gain (loss)
              type: number
            unrecaptured1250Gain:
              description: Box 9c, Unrecaptured section 1250 gain
              type: number
            net1231Gain:
              description: Box 10, Net section 1231 gain (loss)
              type: number
            otherIncome:
              description: Box 11, Other income
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            section179Deduction:
              description: Box 12, Section 179 deduction
              type: number
            otherDeductions:
              description: Box 13, Other deductions
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            selfEmployment:
              description: Box 14, Self-employment earnings (loss)
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            credits:
              description: Box 15, Credits
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            scheduleK3:
              description: Box 16, Schedule K-3 is attached
              type: boolean
            amtItems:
              description: Box 17, Alternative minimum tax (AMT) items
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            taxExemptIncome:
              description: Box 18, Tax-exempt income and nondeductible expenses
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            distributions:
              description: Box 19, Distributions
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            otherInfo:
              description: Box 20, Other information
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            foreignTaxPaid:
              description: Box 21, Foreign taxes paid or accrued
              type: number
            multipleAtRiskActivities:
              description: Box 22, More than one activity for at-risk purposes
              type: boolean
            multiplePassiveActivities:
              description: Box 23, More than one activity for passive activity purposes
              type: boolean

    Tax1065K3:
      title: Form 1065 Schedule K-3
      description: Partner's Share of Income, Deductions, Credits, etc. - International,
        from Partnership (boxes A, B as issuer) to Partner (boxes C-D as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        # Uncomment following line to reference and include full IRS Form 1065 Schedule K-3
        # - $ref: './fdxapi.tax1065k3.yaml#/components/schemas/Tax1065ScheduleK3'

    Tax1095A:
      title: Form 1095-A
      description: Health Insurance Marketplace Statement, to Recipient (boxes 4-5, 12-15)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            marketplaceId:
              description: Box 1, Marketplace identifier
              type: string
            marketplacePolicyNumber:
              description: Box 2, Marketplace-assigned policy number
              type: string
            policyIssuerName:
              description: Box 3, Policy issuer's name
              type: string
            recipientDateOfBirth:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 6, Recipient's date of birth
            spouseName:
              description: Box 7, Recipient's spouse's name
              type: string
            spouseTin:
              description: Box 8, Recipient's spouse's SSN
              type: string
            spouseDateOfBirth:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 9, Recipient's spouse's date of birth
            policyStartDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 10, Policy start date
            policyTerminationDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 11, Policy termination date
            coveredIndividuals:
              description: Boxes 16+, Covered Individuals
              type: array
              items:
                $ref: '#/components/schemas/HealthInsuranceMarketplaceCoveredIndividual'
            coverages:
              description: Boxes 21-33, Coverage Information
              type: array
              items:
                $ref: '#/components/schemas/HealthInsuranceCoverage'

    Tax1095B:
      title: Form 1095-B
      description: Health Coverage, from Issuer (boxes 16-22)
        to Responsible Individual (boxes 1-2, 4-7 as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            responsibleDateOfBirth:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 3, Date of birth (if SSN or other TIN is not available)
            originOfHealthCoverageCode:
              description: Box 8, Enter letter identifying Origin of the Health Coverage
              type: string
            employer:
              $ref: '#/components/schemas/TaxParty'
              description: Boxes 10-15, Employer EIN, name and address
            coveredIndividuals:
              description: Boxes 23+, Covered Individuals
              type: array
              items:
                $ref: '#/components/schemas/HealthInsuranceCoveredIndividual'

    Tax1095C:
      title: Form 1095-C
      description: Employer-Provided Health Insurance Offer and Coverage,
        from Employer (boxes 7-13 as issuer) to Employee (boxes 1-6 as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            selfInsuredCoverage:
              type: boolean
              description: Self Insured Coverage
            offersOfCoverage:
              description: Boxes 14-16, Employee Offer of Coverage
              type: array
              items:
                $ref: '#/components/schemas/OfferOfHealthInsuranceCoverage'
            employeeAge:
              description: Employee's Age on January 1
              type: integer
              format: int32
            planStartMonth:
              description: Plan Start Month
              format: int32
              type: integer
            coveredIndividuals:
              description: Boxes 17+, Covered Individuals
              type: array
              items:
                $ref: '#/components/schemas/HealthInsuranceCoveredIndividual'

    Tax1097Btc:
      title: Form 1097-BTC
      description: Bond Tax Credit, from FORM 1097-BTC ISSUER (1st-2nd boxes)
        to RECIPIENT (3rd-6th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            filingForCredit:
              type: boolean
              description: >-
                Form 1097-BTC issuer is: Issuer of bond or its agent filing current year
                Form 1097-BTC for credit being reported
            asNominee:
              type: boolean
              description: >-
                Form 1097-BTC issuer is: An entity or a person that received or should have received
                a current year Form 1097-BTC and is distributing part or all of that credit to others
            total:
              description: Box 1, Total
              type: number
            bondCode:
              description: Box 2a, Code
              type: string
            uniqueId:
              description: Box 2b, Unique Identifier
              type: string
            bondType:
              description: Box 3, Bond type
              type: string
            amounts:
              description: Box 5, Amounts by month
              type: array
              items:
                $ref: '#/components/schemas/MonthAmount'
            comments:
              description: Box 6, Comments
              type: string

    Tax1098:
      title: Form 1098
      description: Mortgage Interest Statement, from RECIPIENT/LENDER
        (1st-2nd boxes as issuer) to PAYER/BORROWER (3rd-6th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            mortgagedProperties:
              description: Box 9, Number of properties securing the mortgage
              format: int32
              type: integer
            otherInformation:
              description: Box 10, Other (property tax)
              type: string
            accountNumber:
              description: Account number
              type: string
            mortgageInterest:
              description: Box 1, Mortgage interest received from borrower
              type: number
            outstandingPrincipal:
              description: Box 2, Outstanding mortgage principal
              type: number
            originationDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 3, Mortgage origination date
            overpaidRefund:
              description: Box 4, Refund of overpaid interest
              type: number
            mortgageInsurance:
              description: Box 5, Mortgage insurance premiums
              type: number
            pointsPaid:
              description: Box 6, Points paid on purchase of principal residence
              type: number
            isPropertyAddressSameAsBorrowerAddress:
              type: boolean
              description: Box 7, Is address of property securing mortgage same as PAYER'S/BORROWER'S address
            acquisitionDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 11, Mortgage acquisition date
            propertyAddress:
              $ref: './fdxapi.components.yaml#/components/schemas/Address'
              description: Box 8, Address of property securing mortgage
            propertyTax:
              description: Box 10, Property tax
              type: number
            propertyDescription:
              description: Box 8, Description of property securing mortgage, if property securing
                mortgage has no address
              type: string

    Tax1098C:
      title: Form 1098-C
      description: Contributions of Motor Vehicles, Boats, and Airplanes,
        from DONEE (1st-2nd boxes as issuer) to DONOR (3rd-6th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            dateOfContribution:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 1, Date of contribution
            odometerMileage:
              description: Box 2a, Odometer mileage
              format: int32
              type: integer
            carYear:
              description: Box 2b, Year
              format: int32
              type: integer
            make:
              description: Box 2c, Make
              type: string
            model:
              description: Box 2d, Model
              type: string
            vin:
              description: Box 3, Vehicle or other identification number
              type: string
            armsLengthTransaction:
              type: boolean
              description: Box 4a, Donee certifies that vehicle was sold in arm's length transaction to
                unrelated party
            dateOfSale:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 4b, Date of sale
            grossProceeds:
              description: Box 4c, Gross proceeds from sale (see instructions)
              type: number
            notTransferredBefore:
              type: boolean
              description: Box 5a, Donee certifies that vehicle will not be transferred for money, other
                property, or services before completion of material improvements or significant intervening use
            needyIndividual:
              type: boolean
              description: Box 5b, Donee certifies that vehicle is to be transferred to a needy individual for
                significantly below fair market value in furtherance of donee's charitable purpose
            descriptionOfImprovements:
              description: Box 5c, Donee certifies the following detailed description of material improvements
                or significant intervening use and duration of use
              type: string
            goodsInExchange:
              type: boolean
              description: Box 6a, Did you provide goods or services in exchange for the vehicle? Yes
            valueOfExchange:
              description: Box 6b, Value of goods and services provided in exchange for the vehicle
              type: number
            intangibleReligious:
              type: boolean
              description: Box 6c, If this box is checked, donee certifies that the goods and services consisted
                solely of intangible religious benefits
            descriptionOfGoods:
              description: Box 6c, Describe the goods and services, if any, that were provided
              type: string
            maxDeductionApplies:
              type: boolean
              description: Box 7, Under the law, the donor may not claim a deduction of more than $500 for this
                vehicle if this box is checked

    Tax1098E:
      title: Form 1098-E
      description: Student Loan Interest Statement, from RECIPIENT/LENDER
        (1st-2nd boxes as issuer) to PAYER/BORROWER (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            studentLoanInterest:
              description: Box 1, Student loan interest received by lender
              type: number
            box1ExcludesFees:
              type: boolean
              description: Box 2, If checked, box 1 does not include loan origination fee made before
                September 1, 2004

    Tax1098Ma:
      title: Form 1098-MA
      description: Mortgage Assistance Payments, from FILER (1st-2nd boxes as issuer)
        to HOMEOWNER (3rd-6th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              type: string
              description: Account number
            totalMortgagePayments:
              type: number
              description: Box 1, Total State HFA (Housing Finance Agency) and homeowner
                mortgage payments
            mortgageAssistancePayments:
              type: number
              description: Box 2, State HFA (Housing Finance Agency) mortgage assistance
                payments
            homeownerMortgagePayments:
              type: number
              description: Box 3, Homeowner mortgage payments

    Tax1098Q:
      title: Form 1098-Q
      description: Qualifying Longevity Annuity Contract Information,
        from ISSUER (1st box) to PARTICIPANT (3rd-5th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              type: string
              description: Account number
            planNumber:
              type: string
              description: Plan number
            planName:
              type: string
              description: Plan name
            planSponsorId:
              type: string
              description: Plan sponsor's EIN
            annuityAmount:
              type: number
              description: Box 1a, Annuity amount on start date
            startDate:
              description: Box 1b, Annuity start date
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            canBeAccelerated:
              type: boolean
              description: Box 2, Start date may be accelerated
            totalPremiums:
              type: number
              description: Box 3, Total premiums
            fairMarketValue:
              type: number
              description: Box 4, Fair market value of qualifying longevity annuity
                contract (FMV of QLAC)
            premiums:
              type: array
              description: Box 5, Total monthly premiums paid for the contract and date
                of the last payment in the month
              items:
                $ref: '#/components/schemas/DateAmount'

    Tax1098T:
      title: Form 1098-T
      description: Tuition Statement, from FILER (1st-2nd boxes as issuer)
        to STUDENT (3rd-6th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            studentTinCertification:
              type: boolean
              description: By checking the box in STUDENT'S TIN, filer is
                making a true and accurate certification under penalty of
                perjury that they have complied with standards promulgated
                by the Secretary for obtaining such individual's TIN
            accountNumber:
              description: Account number
              type: string
            halfTime:
              type: boolean
              description: Box 8, Check if at least half-time student
            qualifiedTuitionFees:
              description: Box 1, Payments received for qualified tuition and related expenses
              type: number
            adjustmentPriorYear:
              description: Box 4, Adjustments made for a prior year
              type: number
            scholarship:
              description: Box 5, Scholarships or grants
              type: number
            adjustScholarship:
              description: Box 6, Adjustments to scholarships or grants for a prior year
              type: number
            includeJanMar:
              type: boolean
              description: Box 7, Check if the amount in box 1 or box 2 includes amounts for an academic
                period beginning January - March of next year
            graduate:
              type: boolean
              description: Box 9, Check if graduate student
            insuranceRefund:
              description: Box 10, Insurance contract reimbursement / refund
              type: number

    Tax1099A:
      title: Form 1099-A
      description: Acquisition or Abandonment of Secured Property,
        from LENDER (1st-2nd boxes as issuer) to BORROWER (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            dateOfAcquisition:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 1, Date of lender's acquisition or knowledge of abandonment
            principalBalance:
              description: Box 2, Balance of principal outstanding
              type: number
            fairMarketValue:
              description: Box 4, Fair market value property
              type: number
            personallyLiable:
              type: boolean
              description: Box 5, If checked, the borrower was personally liable for repayment of the debt
            propertyDescription:
              description: Box 6, Description of property
              type: string

    Tax1099B:
      title: Form 1099-B
      description: Proceeds From Broker and Barter Exchange Transactions,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-6th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            stateAndLocal:
              description: Boxes 14-16, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            profitOnClosedContracts:
              description: Box 8, Profit or (loss) realized in current year on closed contracts
              type: number
            unrealizedProfitOpenContractsBegin:
              description: Box 9, Unrealized profit or loss on open contracts at end of last year
              type: number
            unrealizedProfitOpenContractsEnd:
              description: Box 10, Unrealized profit or loss on open contracts at end of current year
              type: number
            aggregateProfitOnContracts:
              description: Box 11, Aggregate profit or (loss) on contracts
              type: number
            bartering:
              description: Box 13, Bartering
              type: number
            securityDetails:
              description: Boxes 1-3, 5-7, 12, Security details
              type: array
              items:
                $ref: '#/components/schemas/SecurityDetail'
            secondTinNotice:
              type: boolean
              description: Second TIN Notice

    Tax1099C:
      title: Form 1099-C
      description: Cancellation of Debt,
        from CREDITOR (1st-2nd boxes as issuer) to DEBTOR (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            dateOfEvent:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 1, Date of identifiable event
            amountDischarged:
              description: Box 2, Amount of debt discharged
              type: number
            interestIncluded:
              description: Box 3, Interest if included in box 2
              type: number
            debtDescription:
              description: Box 4, Debt description
              type: string
            personallyLiable:
              type: boolean
              description: Box 5, If checked, the debtor was personally liable for repayment of the debt
            debtCode:
              description: Box 6, Identifiable debt code
              type: string
            fairMarketValue:
              description: Box 7, Fair market value of property
              type: number

    Tax1099Cap:
      title: Form 1099-CAP
      description: Changes in Corporate Control and Capital Structure,
        from CORPORATION (1st-2nd boxes as issuer) to SHAREHOLDER (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            dateOfSale:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 1, Date of sale or exchange
            aggregateAmount:
              description: Box 2, Aggregate amount received
              type: number
            numberOfShares:
              description: Box 3, Number of shares exchanged
              type: number
            stockClasses:
              description: Box 4, Classes of stock exchanged
              type: string

    Tax1099ConsolidatedStatement:
      title: Form 1099 Consolidated Statement
      description: >-
        Various tax-related items reported on consolidated brokerage or
        mutual fund statements not on the base 1099 forms. The component
        1099 forms are delivered as their own Tax1099Xxx entities as usual
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            marginInterestPaid:
              description: Interest paid on margin account
              type: number
            paymentInLieuPaid:
              description: Payment in lieu of dividends paid
              type: number
            advisorFeesPaid:
              description: Advisor fees paid
              type: number
            otherFeesPaid:
              description: Other fees paid
              type: number
            corporateBondInterestPaid:
              description: >-
                Accrued Interest Paid offset to form 1099-INT box 1,
                Corporate bond interest income
              type: number
            usBondInterestPaid:
              description: >-
                Accrued Interest Paid offset to form 1099-INT box 3,
                accrued U.S. Treasury Notes and Bonds interest income
              type: number
            taxExemptInterestPaid:
              description: >-
                Accrued Interest Paid offset to form 1099-INT box 8,
                tax exempt interest income from municipal bonds
              type: number
            specifiedPabInterestPaid:
              description: >-
                Accrued Interest Paid offset to form 1099-INT box 9,
                tax exempt interest income from Private Activity Bonds
              type: number

    Tax1099Div:
      title: Form 1099-DIV
      description: Dividends and Distributions,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-6th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            ordinaryDividends:
              description: Box 1a, Total ordinary dividends
              type: number
            qualifiedDividends:
              description: Box 1b, Qualified dividends
              type: number
            totalCapitalGain:
              description: Box 2a, Total capital gain distributions
              type: number
            unrecaptured1250Gain:
              description: Box 2b, Unrecaptured Section 1250 gain
              type: number
            section1202Gain:
              description: Box 2c, Section 1202 gain
              type: number
            collectiblesGain:
              description: Box 2d, Collectibles (28%) gain
              type: number
            section897Dividends:
              description: Box 2e, Section 897 ordinary dividends
              type: number
            section897CapitalGain:
              description: Box 2f, Section 897 capital gain
              type: number
            nonTaxableDistribution:
              description: Box 3, Nondividend distributions
              type: number
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            section199ADividends:
              description: Box 5, Section 199A dividends
              type: number
            investmentExpenses:
              description: Box 6, Investment expenses
              type: number
            foreignTaxPaid:
              description: Box 7, Foreign tax paid
              type: number
            foreignCountry:
              description: Box 8, Foreign country or U.S. possession
              type: string
            cashLiquidation:
              description: Box 9, Cash liquidation distributions
              type: number
            nonCashLiquidation:
              description: Box 10, Noncash liquidation distributions
              type: number
            foreignAccountTaxCompliance:
              description: Box 11, FATCA filing requirement
              type: boolean
            taxExemptInterestDividend:
              description: Box 12, Exempt-interest dividends
              type: number
            specifiedPabInterestDividend:
              description: Box 13, Specified private activity bond interest dividends
              type: number
            stateAndLocal:
              description: Boxes 14-16, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'
            foreignIncomes:
              description: Foreign income information
              type: array
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            stateTaxExemptIncomes:
              description: Tax exempt income state information
              type: array
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            secondTinNotice:
              type: boolean
              description: Second TIN Notice

    Tax1099G:
      title: Form 1099-G
      description: Certain Government Payments,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            unemploymentCompensation:
              description: Box 1, Unemployment compensation
              type: number
            taxRefund:
              description: Box 2, State or local income tax refunds, credits, or offsets
              type: number
            refundYear:
              description: Box 3, Box 2 amount is for tax year
              format: int32
              type: integer
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            rtaaPayments:
              description: Box 5, RTAA payments
              type: number
            grants:
              description: Box 6, Taxable grants
              type: number
            agriculturePayments:
              description: Box 7, Agriculture payments
              type: number
            businessIncome:
              type: boolean
              description: Box 8, If checked, box 2 is trade or business income
            marketGain:
              description: Box 9, Market gain
              type: number
            stateAndLocal:
              description: Boxes 10-11, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'
            secondTinNotice:
              type: boolean
              description: Second TIN Notice

    Tax1099H:
      title: Form 1099-H
      description: Health Coverage Tax Credit (HCTC) Advance Payments,
        from ISSUER/PROVIDER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            advancePayments:
              description: Box 1, Amount of HCTC advance payments
              type: number
            numberOfMonths:
              description: Box 2, Number of months HCTC advance payments and reimbursement credits paid to you
              format: int32
              type: integer
            payments:
              description: Boxes 3-14, Payments by month
              type: array
              items:
                $ref: '#/components/schemas/MonthAmount'

    Tax1099Int:
      title: Form 1099-INT
      description: Interest Income,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            foreignAccountTaxCompliance:
              type: boolean
              description: FATCA filing requirement
            accountNumber:
              description: Account number
              type: string
            payerRtn:
              description: Payer's RTN
              type: string
            interestIncome:
              description: Box 1, Interest income
              type: number
            earlyWithdrawalPenalty:
              description: Box 2, Early withdrawal penalty
              type: number
            usBondInterest:
              description: Box 3, Interest on U.S. Savings Bonds and Treasury obligations
              type: number
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            investmentExpenses:
              description: Box 5, Investment expenses
              type: number
            foreignTaxPaid:
              description: Box 6, Foreign tax paid
              type: number
            foreignCountry:
              description: Box 7, Foreign country or U.S. possession
              type: string
            taxExemptInterest:
              description: Box 8, Tax-exempt interest
              type: number
            specifiedPabInterest:
              description: Box 9, Specified private activity bond interest
              type: number
            marketDiscount:
              description: Box 10, Market discount
              type: number
            bondPremium:
              description: Box 11, Bond premium
              type: number
            usBondPremium:
              description: Box 12, Bond premium on Treasury obligations
              type: number
            taxExemptBondPremium:
              description: Box 13, Bond premium on tax-exempt bond
              type: number
            cusipNumber:
              description: Box 14, Tax-exempt bond CUSIP no.
              type: string
            stateAndLocal:
              description: Boxes 15-17, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'
            foreignIncomes:
              description: Supplemental foreign income amount information (description is country)
              type: array
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            stateTaxExemptIncome:
              description: Supplemental tax-exempt income by state (description is state)
              type: array
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            secondTinNotice:
              type: boolean
              description: Second TIN Notice

    Tax1099K:
      title: Form 1099-K
      description: Merchant Card and Third-Party Network Payments,
        from FILER (1st, 7th boxes as issuer) to PAYEE (4th, 8th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            paymentSettlementEntity:
              type: boolean
              description: Check to indicate if FILER is a Payment Settlement Entity (PSE)
            electronicPaymentFacilitator:
              type: boolean
              description: Check to indicate if FILER is an Electronic Payment Facilitator (EPF) /
                Other third party
            paymentCard:
              type: boolean
              description: 'Check to indicate transactions reported are: Payment card'
            thirdPartyNetwork:
              type: boolean
              description: 'Check to indicate transactions reported are: Third party network'
            pseName:
              description: PSE's name
              type: string
            psePhone:
              $ref: './fdxapi.components.yaml#/components/schemas/TelephoneNumberPlusExtension'
              description: PSE's phone number
            accountNumber:
              description: Account number
              type: string
            grossAmount:
              description: Box 1a, Gross amount of payment card/third party network transactions
              type: number
            cardNotPresent:
              description: Box 1b, Card Not Present Transactions
              type: number
            merchantCategoryCode:
              description: Box 2, Merchant category code
              type: string
            numberOfTransactions:
              description: Box 3, Number of purchase transactions
              type: number
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            monthAmounts:
              description: Box 5, Monthly amounts
              type: array
              items:
                $ref: '#/components/schemas/MonthAmount'
            stateAndLocal:
              description: Boxes 6-8, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'
            secondTinNotice:
              type: boolean
              description: Second TIN Notice

    Tax1099Ls:
      title: Form 1099-LS
      description: Reportable Life Insurance Sale,
        from ACQUIRER (1st-2nd boxes as issuer) to PAYMENT RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            policyNumber:
              type: string
              description: Policy number
            payment:
              type: number
              description: Box 1, Amount paid to payment recipient
            saleDate:
              description: Box 2, Date of sale
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            issuerName:
              type: string
              description: Issuer's name
            contactNameAddress:
              description: Acquirer's information contact name, street address, city or town,
                state or province, country, ZIP or foreign postal code, and telephone
                no. (If different from ACQUIRER)
              $ref: '#/components/schemas/NameAddressPhone'

    Tax1099Ltc:
      title: Form 1099-LTC
      description: Long-Term Care and Accelerated Death Benefits,
        from PAYER (1st-2nd boxes as issuer) to POLICY HOLDER (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            ltcBenefits:
              description: Box 1, Gross long-term care benefits paid
              type: number
            deathBenefits:
              description: Box 2, Accelerated death benefits paid
              type: number
            perDiem:
              type: boolean
              description: Box 3, Per diem
            reimbursedAmount:
              type: boolean
              description: Box 3, Reimbursed amount
            insuredId:
              description: INSURED'S taxpayer identification no.
              type: string
            insuredNameAddress:
              $ref: '#/components/schemas/NameAddress'
              description: Insured name and address
            qualifiedContract:
              type: boolean
              description: Box 4, Qualified contract
            chronicallyIll:
              type: boolean
              description: Box 5, Chronically ill
            terminallyIll:
              type: boolean
              description: Box 5, Terminally ill
            dateCertified:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Date certified

    Tax1099Misc:
      title: Form 1099-MISC
      description: Miscellaneous Income,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            rents:
              description: Box 1, Rents
              type: number
            royalties:
              description: Box 2, Royalties
              type: number
            otherIncome:
              description: Box 3, Other income
              type: number
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            fishingBoatProceeds:
              description: Box 5, Fishing boat proceeds
              type: number
            medicalHealthPayment:
              description: Box 6, Medical and health care payments
              type: number
            payerDirectSales:
              type: boolean
              description: >-
                Box 7, Payer made direct sales of $5,000 or more of consumer products to a
                buyer (recipient) for resale
            substitutePayments:
              description: Box 8, Substitute payments in lieu of dividends or interest
              type: number
            cropInsurance:
              description: Box 9, Crop insurance proceeds
              type: number
            secondTinNotice:
              type: boolean
              description: Second TIN Notice
            grossAttorney:
              description: Box 10, Gross proceeds paid to an attorney
              type: number
            fishPurchased:
              description: Box 11, Fish purchased for resale
              type: number
            section409ADeferrals:
              description: Box 12, Section 409A deferrals
              type: number
            foreignAccountTaxCompliance:
              description: Box 13, FATCA filing requirement
              type: boolean
            excessGolden:
              description: Box 14, Excess golden parachute payments
              type: number
            nonQualifiedDeferredCompensation:
              description: Box 15, Nonqualified Deferred Compensation
              type: number
            stateAndLocal:
              description: Boxes 16-18, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'

    Tax1099Nec:
      title: Form 1099-NEC
      description: Non-Employee Compensation,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            secondTinNotice:
              type: boolean
              description: Second TIN Notice
            nonEmployeeCompensation:
              description: Box 1, Nonemployee compensation
              type: number
            payerDirectSales:
              type: boolean
              description: >-
                Box 2, Payer made direct sales of $5,000 or more of consumer products to a
                buyer (recipient) for resale
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            stateAndLocal:
              description: Boxes 5-7, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'

    Tax1099Oid:
      title: Form 1099-OID
      description: Original Issue Discount,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            foreignAccountTaxCompliance:
              type: boolean
              description: FATCA filing requirement
            accountNumber:
              description: Account number
              type: string
            originalIssueDiscount:
              description: Box 1, Original issue discount
              type: number
            otherPeriodicInterest:
              description: Box 2, Other periodic interest
              type: number
            earlyWithdrawalPenalty:
              description: Box 3, Early withdrawal penalty
              type: number
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            marketDiscount:
              description: Box 5, Market discount
              type: number
            acquisitionPremium:
              description: Box 6, Acquisition premium
              type: number
            oidDescription:
              description: Box 7, Description
              type: string
            discountOnTreasuryObligations:
              description: Box 8, Original issue discount on U.S. Treasury obligations
              type: number
            investmentExpenses:
              description: Box 9, Investment expenses
              type: number
            bondPremium:
              description: Box 10, Bond premium
              type: number
            taxExemptOid:
              description: Box 11, Tax-exempt OID
              type: number
            stateAndLocal:
              description: Boxes 12-14, State and Local tax withheld
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'
            stateExemptOid:
              description: 'Supplemental: State name and tax-exempt OID by state'
              type: array
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            secondTinNotice:
              type: boolean
              description: Second TIN Notice

    Tax1099Patr:
      title: Form 1099-PATR
      description: Taxable Distributions Received From Cooperatives,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            patronageDividends:
              description: Box 1, Patronage dividends
              type: number
            nonpatronageDistributions:
              description: Box 2, Nonpatronage distributions
              type: number
            perUnitRetainAllocations:
              description: Box 3, Per-unit retain allocations
              type: number
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            redemption:
              description: Box 5, Redemption of nonqualified notices and retain allocations
              type: number
            section199Deduction:
              description: Box 6, Section 199A(g) deduction
              type: number
            qualifiedPayments:
              description: Box 7, Qualified payments
              type: number
            section199QualifiedItems:
              description: Box 8, Section 199A(a) qualified items
              type: number
            section199SstbItems:
              description: Box 9, Section 199A(a) SSTB (Specified Service Trade or Business) items
              type: number
            investmentCredit:
              description: Box 10, Investment credit
              type: number
            workOpportunityCredit:
              description: Box 11, Work opportunity credit
              type: number
            otherCreditsAndDeductions:
              description: Box 12, Other credits and deductions
              type: number
            specifiedCoop:
              description: Box 13, Specified Cooperative
              type: boolean
            stateAndLocal:
              description: State and Local tax withholding, from IRS's IRIS schema
              $ref: '#/components/schemas/StateAndLocalTaxWithholding'
            secondTinNotice:
              type: boolean
              description: Second TIN Notice

    Tax1099Q:
      title: Form 1099-Q
      description: Payments From Qualified Education Programs,
        from PAYER/TRUSTEE (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            grossDistribution:
              description: Box 1, Gross distribution
              type: number
            earnings:
              description: Box 2, Earnings
              type: number
            basis:
              description: Box 3, Basis
              type: number
            trusteeToTrustee:
              type: boolean
              description: Box 4, Trustee-to-trustee transfer
            tuitionPlanPrivate:
              type: boolean
              description: Box 5a, Qualified tuition plan - Private
            tuitionPlanPublic:
              type: boolean
              description: Box 5b, Qualified tuition plan - Public
            coverdellEsa:
              type: boolean
              description: Box 5c, Coverdell ESA
            recipientIsNotBeneficiary:
              type: boolean
              description: Box 6, If this box is checked, the recipient is not the designated beneficiary
            fairMarketValue:
              description: If fair market value (FMV) is included, see Pub. 970,
                Tax Benefits for Education, for how to figure earnings
              type: number

    Tax1099Qa:
      title: Form 1099-QA
      description: Distributions From ABLE Accounts,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              type: string
              description: Account number
            grossDistribution:
              type: number
              description: Box 1, Gross distribution
            earnings:
              type: number
              description: Box 2, Earnings
            basis:
              type: number
              description: Box 3, Basis
            programTransfer:
              type: boolean
              description: Box 4, Program-to-program transfer
            terminated:
              type: boolean
              description: Box 5, Check if ABLE account terminated in current year
            notBeneficiary:
              type: boolean
              description: Box 6, Check if the recipient is not the designated beneficiary

    Tax1099R:
      title: Form 1099-R
      description: Distributions from Pensions, Annuities, Retirement or Profit-Sharing Plans, IRAs,
        Insurance Contracts, etc., from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            allocableToIRR:
              description: Box 10, Amount allocable to IRR within 5 years
              type: number
            firstYearOfRoth:
              description: Box 11, First year of designated Roth contributions. A four-digit year.
                (Like `TaxYear` definition, but lower minimum since first year of Roth IRAs was 1997)
              type: integer
              format: int32
              minimum: 1997
              maximum: 2050
              example: 2020
            recipientAccountNumber:
              description: Account number
              type: string
            grossDistribution:
              description: Box 1, Gross distribution
              type: number
            taxableAmount:
              description: Box 2a, Taxable amount
              type: number
            taxableAmountNotDetermined:
              type: boolean
              description: Box 2b, Taxable amount not determined
            totalDistribution:
              type: boolean
              description: Box 2c, Total distribution
            capitalGain:
              description: Box 3, Capital gain
              type: number
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            employeeContributions:
              description: Box 5, Employee contributions
              type: number
            netUnrealizedAppreciation:
              description: Box 6, Net unrealized appreciation
              type: number
            distributionCodes:
              description: Box 7, Distribution codes
              type: array
              items:
                type: string
            iraSepSimple:
              type: boolean
              description: Box 7b, IRA/SEP/SIMPLE
            otherAmount:
              description: Box 8, Other
              type: number
            otherPercent:
              description: Box 8, Other percent
              type: number
              format: double
            yourPercentOfTotal:
              description: Box 9a, Your percent of total distribution
              type: number
              format: double
            totalEmployeeContributions:
              description: Box 9b, Total employee contributions
              type: number
            foreignAccountTaxCompliance:
              description: Box 12, FATCA filing requirement
              type: boolean
            dateOfPayment:
              description: Box 13, Date of payment
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            stateAndLocal:
              description: Boxes 14-19, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'

    Tax1099S:
      title: Form 1099-S
      description: Proceeds From Real Estate Transactions,
        from FILER (1st-2nd boxes as issuer) to TRANSFEROR (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account or escrow number
              type: string
            dateOfClosing:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 1, Date of closing
            grossProceeds:
              description: Box 2, Gross proceeds
              type: number
            addressOrLegalDescription:
              description: Box 3, Address or legal description
              type: string
            receivedOtherConsideration:
              type: boolean
              description: Box 4, Transferor received or will receive property or services as part of
                the consideration (if checked)
            foreignPerson:
              type: boolean
              description: Box 5, If checked, transferor is a foreign person (nonresident alien,
                foreign partnership, foreign estate, or foreign trust)
            realEstateTax:
              description: Box 6, Buyer's part of real estate tax
              type: number

    Tax1099Sa:
      title: Form 1099-SA
      description: Distributions From an HSA, Archer MSA, or Medicare Advantage MSA,
        from PAYER (1st-2nd boxes as issuer) to RECIPIENT (3rd-4th boxes)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            grossDistribution:
              description: Box 1, Gross distribution
              type: number
            earnings:
              description: Box 2, Earnings on excess contributions
              type: number
            distributionCode:
              description: Box 3, Distribution code
              type: string
            fairMarketValue:
              description: Box 4, FMV on date of death
              type: number
            hsa:
              type: boolean
              description: Box 5a, HSA
            archerAccount:
              type: boolean
              description: Box 5b, Archer MSA
            medicalSavingsAccount:
              type: boolean
              description: Box 5c, Medicare Advantage (MA) MSA

    Tax1099Sb:
      title: Form 1099-SB
      description: Seller's Investment in Life Insurance Contract,
        from ISSUER (1st-2nd boxes) to SELLER (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            policyNumber:
              type: string
              description: Policy number
            contractInvestment:
              type: number
              description: Box 1, Investment in contract
            surrenderAmount:
              type: number
              description: Box 2, Surrender amount
            contactNameAddress:
              description: Issuer's information contact name, street address, city or town, state
                or province, country, ZIP or foreign postal code, and telephone no. (if
                different from ISSUER)
              $ref: '#/components/schemas/NameAddressPhone'

    Tax1120SK1:
      title: Form 1120-S Schedule K-1
      description: Shareholder's Share of Income, Deductions, Credits, etc.,
        from Corporation (boxes A-B as issuer) to Shareholder (boxes E-F as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            finalK1:
              type: boolean
              description: Final K-1
            amendedK1:
              type: boolean
              description: Amended K-1
            fiscalYearBegin:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year begin date
            fiscalYearEnd:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year end date
            irsCenter:
              description: Box C, IRS Center where corporation filed return
              type: string
            corporationBeginningShares:
              description: Box D, Corporation's total number of shares, Beginning of tax year
              type: number
            corporationEndingShares:
              description: Box D, Corporation's total number of shares, End of tax year
              type: number
            percentOwnership:
              description: Box G, Current year allocation percentage
              type: number
              format: double
            beginningShares:
              description: Box H, Shareholder's number of shares, Beginning of tax year
              type: number
            endingShares:
              description: Box H, Shareholder's number of shares, End of tax year
              type: number
            beginningLoans:
              description: Box I, Loans from shareholder, Beginning of tax year
              type: number
            endingLoans:
              description: Box I, Loans from shareholder, Ending of tax year
              type: number
            ordinaryIncome:
              description: Box 1, Ordinary business income (loss)
              type: number
            netRentalRealEstateIncome:
              description: Box 2, Net rental real estate income (loss)
              type: number
            otherRentalIncome:
              description: Box 3, Other net rental income (loss)
              type: number
            interestIncome:
              description: Box 4, Interest income
              type: number
            ordinaryDividends:
              description: Box 5a, Ordinary dividends
              type: number
            qualifiedDividends:
              description: Box 5b, Qualified dividends
              type: number
            royalties:
              description: Box 6, Royalties
              type: number
            netShortTermGain:
              description: Box 7, Net short-term capital gain (loss)
              type: number
            netLongTermGain:
              description: Box 8a, Net long-term capital gain (loss)
              type: number
            collectiblesGain:
              description: Box 8b, Collectibles (28%) gain (loss)
              type: number
            unrecaptured1250Gain:
              description: Box 8c, Unrecaptured section 1250 gain
              type: number
            net1231Gain:
              description: Box 9, Net section 1231 gain (loss)
              type: number
            otherIncome:
              description: Box 10, Other income (loss)
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            section179Deduction:
              description: Box 11, Section 179 deduction
              type: number
            otherDeductions:
              description: Box 12, Other deductions
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            credits:
              description: Box 13, Credits
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            scheduleK3:
              description: Box 14, Schedule K-3 is attached
              type: boolean
            amtItems:
              description: Box 15, Alternative minimum tax (AMT) items
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            basisItems:
              description: Box 16, Items affecting shareholder basis
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            otherInfo:
              description: Box 17, Other information
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            multipleAtRiskActivities:
              description: Box 18, More than one activity for at-risk purposes
              type: boolean
            multiplePassiveActivities:
              description: Box 19, More than one activity for passive activity purposes
              type: boolean

    Tax2439:
      title: Form 2439
      description: Notice to Shareholder of Undistributed Long-Term Capital Gains,
        from RIC or REIT (1st-2nd boxes as issuer) to Shareholder (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            fiscalYearBegin:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year begin date
            fiscalYearEnd:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Fiscal year end date
            undistributedLongTermCapitalGains:
              description: Box 1a, Total undistributed long-term capital gains
              type: number
            unrecaptured1250Gain:
              description: Box 1b, Unrecaptured section 1250 gain
              type: number
            section1202Gain:
              description: Box 1c, Section 1202 gain
              type: number
            collectiblesGain:
              description: Box 1d, Collectibles (28%) gain
              type: number
            taxPaid:
              description: Box 2, Tax paid by the RIC or REIT on the box 1a gains
              type: number

    Tax3921:
      title: Form 3921
      description: Exercise of an Incentive Stock Option Under Section 422(b),
        from TRANSFEROR (1st-2nd boxes as issuer) to EMPLOYEE (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              type: string
              description: Account number
            optionGrantDate:
              description: Box 1, Date option granted
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            optionExerciseDate:
              description: Box 2, Date option exercised
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            exercisePrice:
              type: number
              description: Box 3, Exercise price per share
            exerciseMarketValue:
              type: number
              description: Box 4, Fair market value per share on exercise date
            numberOfShares:
              type: number
              description: Box 5, Number of shares transferred
            corporation:
              description: Box 6, If other than TRANSFEROR, name, address and tin of corporation whose
                stock is being transferred
              $ref: '#/components/schemas/TaxParty'

    Tax3922:
      title: Form 3922
      description: Transfer of Stock Acquired Through an Employee Stock Purchase Plan
        under Section 423(c), from CORPORATION (1st-2nd boxes as issuer)
        to EMPLOYEE (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              type: string
              description: Account number
            optionGrantDate:
              description: Box 1, Date option granted
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            optionExerciseDate:
              description: Box 2, Date option exercised
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            grantMarketValue:
              type: number
              description: Box 3, Fair market value per share on grant date
            exerciseMarketValue:
              type: number
              description: Box 4, Fair market value per share on exercise date
            exercisePrice:
              type: number
              description: Box 5, Exercise price paid per share
            numberOfShares:
              type: number
              description: Box 6, Number of shares transferred
            titleTransferDate:
              description: Box 7, Date legal title transferred
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
            grantDateExercisePrice:
              type: number
              description: Box 8, Exercise price per share determined as if the option
                was exercised on the option granted date

    Tax5227K1:
      title: Form 5227 Schedule K1
      description: Split-Interest Trust Beneficiary's schedule K-1, uses Tax1041K1 entity
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax1041K1'

    Tax5498:
      title: Form 5498
      description: IRA Contribution Information, from TRUSTEE/ISSUER (1st-2nd boxes as issuer)
        to PARTICIPANT (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            iraContributions:
              description: Box 1, IRA contributions
              type: number
            rolloverContributions:
              description: Box 2, Rollover contributions
              type: number
            rothIraConversion:
              description: Box 3, Roth IRA conversion amount
              type: number
            recharacterizedContributions:
              description: Box 4, Recharacterized contributions
              type: number
            fairMarketValue:
              description: Box 5, Fair market value of account
              type: number
            lifeInsuranceCost:
              description: Box 6, Life insurance cost included in box 1
              type: number
            ira:
              type: boolean
              description: Box 7a, IRA
            sep:
              type: boolean
              description: Box 7b, SEP
            simple:
              type: boolean
              description: Box 7c, SIMPLE
            rothIra:
              type: boolean
              description: Box 7d, Roth IRA
            sepContributions:
              description: Box 8, SEP contributions
              type: number
            simpleContributions:
              description: Box 9, SIMPLE contributions
              type: number
            rothIraContributions:
              description: Box 10, Roth IRA contributions
              type: number
            rmdNextYear:
              type: boolean
              description: Box 11, If checked, required minimum distribution for next year
            rmdDate:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 12a, RMD date
            rmdAmount:
              description: Box 12b, RMD amount
              type: number
            postponedContribution:
              description: Box 13a, Postponed contribution
              type: number
            postponedYear:
              description: Box 13b, Year
              format: int32
              type: integer
            postponedCode:
              description: Box 13c, Code
              type: string
            repayments:
              description: Box 14a, Repayments
              type: number
            repayCode:
              description: Box 14b, Code
              type: string
            fmvSpecifiedAssets:
              description: Box 15a, FMV of certain specified assets
              type: number
            specifiedCodes:
              description: Box 15b, Code(s)
              type: string

    Tax5498Esa:
      title: Form 5498-ESA
      description: Coverdell ESA Contribution Information,
        from TRUSTEE/ISSUER (1st-2nd boxes as issuer) to BENEFICIARY (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            coverdellEsaContributions:
              description: Box 1, Coverdell ESA contributions
              type: number
            rolloverContributions:
              description: Box 2, Rollover contributions
              type: number

    Tax5498Qa:
      title: Form 5498-QA
      description: ABLE Account Contribution Information,
        from ISSUER (1st-2nd boxes) to BENEFICIARY (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              type: string
              description: Account number
            ableContributions:
              type: number
              description: Box 1, ABLE contributions
            rollovers:
              type: number
              description: Box 2, ABLE to ABLE Rollovers
            cumulativeContributions:
              type: number
              description: Box 3, Cumulative contributions
            fairMarketValue:
              type: number
              description: Box 4, Fair market value
            openedInTaxYear:
              type: boolean
              description: Box 5, Check if account opened in current tax year
            basisOfDisabilityCode:
              type: string
              description: Box 6, Basis of eligibility
            typeOfDisabilityCode:
              type: string
              description: Box 7, Code

    Tax5498Sa:
      title: Form 5498-SA
      description: HSA, Archer MSA, or Medicare Advantage (MA) MSA Information,
        from TRUSTEE (1st-2nd boxes as issuer) to PARTICIPANT (3rd-4th boxes as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            accountNumber:
              description: Account number
              type: string
            msaContributions:
              description: Box 1, Employee or self-employed person's Archer MSA contributions made in
                current and following years for current year
              type: number
            totalContributions:
              description: Box 2, Total contributions made in current year
              type: number
            totalPostYearEnd:
              description: Box 3, Total HSA or Archer MSA contributions made in following year for current year
              type: number
            rolloverContributions:
              description: Box 4, Rollover contributions
              type: number
            fairMarketValue:
              description: Box 5, Fair market value of HSA, Archer MSA, or Medicare Advantage (MA) MSA
              type: number
            hsa:
              type: boolean
              description: Box 6a, HSA
            archer:
              type: boolean
              description: Box 6b, Archer MSA
            maMsa:
              type: boolean
              description: Box 6c, Medicare Advantage (MA) MSA

    TaxData:
      title: Tax Data
      description: Tax data container for API requests and responses
      type: object
      properties:
        businessIncomeStatement:
          $ref: '#/components/schemas/BusinessIncomeStatement'
          description: Business Income Statement for IRS Form 1040 Schedule C
        cryptocurrencyTaxStatement:
          $ref: '#/components/schemas/CryptocurrencyTaxStatement'
          description: Cryptocurrency Tax Statement list
        farmIncomeStatement:
          $ref: '#/components/schemas/FarmIncomeStatement'
          description: Farm Income Statement for IRS Form 1040 Schedule F
        farmRentalIncomeStatement:
          $ref: '#/components/schemas/FarmRentalIncomeStatement'
          description: Farm Rental Income Statement for IRS Form 4835
        rentalIncomeStatement:
          $ref: '#/components/schemas/RentalIncomeStatement'
          description: Rental Income Statement for IRS Form 1040 Schedule E
        royaltyIncomeStatement:
          $ref: '#/components/schemas/RoyaltyIncomeStatement'
          description: Royalty Income Statement for IRS Form 1040 Schedule E
        tax1041K1:
          $ref: '#/components/schemas/Tax1041K1'
          description: Beneficiary's Share of Income, Deductions, Credits, etc.
        tax1042S:
          $ref: '#/components/schemas/Tax1042S'
          description: Foreign Person's U.S. Source Income Subject to Withholding
        tax1065K1:
          $ref: '#/components/schemas/Tax1065K1'
          description: Partner's Share of Income, Deductions, Credits, etc.
        tax1065K3:
          $ref: '#/components/schemas/Tax1065K3'
          description: Partner's Share of Income, Deductions, Credits, etc. - International
        tax1095A:
          $ref: '#/components/schemas/Tax1095A'
          description: Health Insurance Marketplace Statement
        tax1095B:
          $ref: '#/components/schemas/Tax1095B'
          description: Health Coverage
        tax1095C:
          $ref: '#/components/schemas/Tax1095C'
          description: Employer-Provided Health Insurance Offer and Coverage
        tax1097Btc:
          $ref: '#/components/schemas/Tax1097Btc'
          description: Bond Tax Credit
        tax1098:
          $ref: '#/components/schemas/Tax1098'
          description: Mortgage Interest Statement
        tax1098C:
          $ref: '#/components/schemas/Tax1098C'
          description: Contributions of Motor Vehicles, Boats, and Airplanes
        tax1098E:
          $ref: '#/components/schemas/Tax1098E'
          description: Student Loan Interest Statement
        tax1098Ma:
          $ref: '#/components/schemas/Tax1098Ma'
          description: Mortgage Assistance Payments
        tax1098Q:
          $ref: '#/components/schemas/Tax1098Q'
          description: Qualifying Longevity Annuity Contract Information
        tax1098T:
          $ref: '#/components/schemas/Tax1098T'
          description: Tuition Statement
        tax1099A:
          $ref: '#/components/schemas/Tax1099A'
          description: Acquisition or Abandonment of Secured Property
        tax1099B:
          $ref: '#/components/schemas/Tax1099B'
          description: Proceeds From Broker and Barter Exchange Transactions
        tax1099C:
          $ref: '#/components/schemas/Tax1099C'
          description: Cancellation of Debt
        tax1099Cap:
          $ref: '#/components/schemas/Tax1099Cap'
          description: Changes in Corporate Control and Capital Structure
        tax1099ConsolidatedStatement:
          $ref: '#/components/schemas/Tax1099ConsolidatedStatement'
          description: Consolidated Statement for combined IRS Form 1099s
        tax1099Div:
          $ref: '#/components/schemas/Tax1099Div'
          description: Dividends and Distributions
        tax1099G:
          $ref: '#/components/schemas/Tax1099G'
          description: Certain Government Payments
        tax1099H:
          $ref: '#/components/schemas/Tax1099H'
          description: Health Coverage Tax Credit (HCTC) Advance Payments
        tax1099Int:
          $ref: '#/components/schemas/Tax1099Int'
          description: Interest Income
        tax1099K:
          $ref: '#/components/schemas/Tax1099K'
          description: Merchant Card and Third-Party Network Payments
        tax1099Ls:
          $ref: '#/components/schemas/Tax1099Ls'
          description: Reportable Life Insurance Sale
        tax1099Ltc:
          $ref: '#/components/schemas/Tax1099Ltc'
          description: Long-Term Care and Accelerated Death Benefits
        tax1099Misc:
          $ref: '#/components/schemas/Tax1099Misc'
          description: Miscellaneous Income
        tax1099Nec:
          $ref: '#/components/schemas/Tax1099Nec'
          description: Nonemployee Compensation
        tax1099Oid:
          $ref: '#/components/schemas/Tax1099Oid'
          description: Original Issue Discount
        tax1099Patr:
          $ref: '#/components/schemas/Tax1099Patr'
          description: Taxable Distributions Received From Cooperatives
        tax1099Q:
          $ref: '#/components/schemas/Tax1099Q'
          description: Payments From Qualified Education Programs
        tax1099Qa:
          $ref: '#/components/schemas/Tax1099Qa'
          description: Distributions From ABLE Accounts
        tax1099R:
          $ref: '#/components/schemas/Tax1099R'
          description: Distributions from Pensions, Annuities, Retirement or Profit-Sharing Plans,
            IRAs, Insurance Contracts, etc.
        tax1099S:
          $ref: '#/components/schemas/Tax1099S'
          description: Proceeds From Real Estate Transactions
        tax1099Sa:
          $ref: '#/components/schemas/Tax1099Sa'
          description: Distributions From an HSA, Archer MSA, or Medicare Advantage MSA
        tax1099Sb:
          $ref: '#/components/schemas/Tax1099Sb'
          description: Seller's Investment in Life Insurance Contract
        tax1120SK1:
          $ref: '#/components/schemas/Tax1120SK1'
          description: Shareholder's Share of Income, Deductions, Credits, etc.
        tax2439:
          $ref: '#/components/schemas/Tax2439'
          description: Notice to Shareholder of Undistributed Long-Term Capital Gains
        tax3921:
          $ref: '#/components/schemas/Tax3921'
          description: Exercise of an Incentive Stock Option Under Section 422(b)
        tax3922:
          $ref: '#/components/schemas/Tax3922'
          description: Transfer of Stock Acquired Through an Employee Stock Purchase Plan under Section 423(c)
        tax5227K1:
          $ref: '#/components/schemas/Tax5227K1'
          description: Split-Interest Trust Beneficiary's schedule K-1
        tax5498:
          $ref: '#/components/schemas/Tax5498'
          description: IRA Contribution Information
        tax5498Esa:
          $ref: '#/components/schemas/Tax5498Esa'
          description: Coverdell ESA Contribution Information
        tax5498Qa:
          $ref: '#/components/schemas/Tax5498Qa'
          description: ABLE Account Contribution Information
        tax5498Sa:
          $ref: '#/components/schemas/Tax5498Sa'
          description: HSA, Archer MSA, or Medicare Advantage MSA Information
        taxW2:
          $ref: '#/components/schemas/TaxW2'
          description: Wage and Tax Statement
        taxW2C:
          $ref: '#/components/schemas/TaxW2C'
          description: IRS form W-2c, Corrected Wage and Tax Statement
        taxW2G:
          $ref: '#/components/schemas/TaxW2G'
          description: Certain Gambling Winnings
        taxRefundDirectDeposit:
          $ref: '#/components/schemas/TaxRefundDirectDeposit'
          description: Tax refund direct deposit information

    TaxDataForQR:
      title: Tax Data for QR
      description: Tax data container for QR Code purposes
      type: object
      allOf:
        - $ref: '#/components/schemas/TaxData'
        - type: object
          properties:
            version:
              description: >-
                [Financial Data Exchange (FDX)](https://financialdataexchange.org/) schema version number (e.g. "V5.0").
              $ref: './fdxapi.components.yaml#/components/schemas/FdxVersion'
            softwareId:
              description: The FDX registration ID of company or software generating this tax data
              type: string
      # QR Code data for form 1098:
      example:
        version: V6.0.0
        softwareId: FdxBankSoftware-2024
        tax1098:
          taxYear: 2023
          taxFormId: ID-09990111-1098
          taxFormDate: 2024-02-15
          taxFormType: Tax1098
          issuer:
            tin: 12-3456789
            partyType: BUSINESS
            businessName:
              name1: Financial Intelligence Associates
            address:
              line1: 12022 Sundown Valley Dr
              line2: Suite 230
              city: Reston
              region: VA
              postalCode: "20191"
              country: US
            phone:
              number: "8885551212"
          recipient:
            tin: xxx-xx-1234
            partyType: INDIVIDUAL
            individualName:
              first: Kris
              middle: Q
              last: Public
            address:
              line1: 1 Main St
              city: Melrose
              region: NY
              postalCode: "12121"
              country: US
          mortgagedProperties: 9
          otherInformation: "10. Property tax: $10,017.00"
          accountNumber: 111-23456
          mortgageInterest: 1008
          outstandingPrincipal: 200900
          originationDate: 2022-03-10
          overpaidRefund: 4011
          mortgageInsurance: 5012
          pointsPaid: 6013
          isPropertyAddressSameAsBorrowerAddress: true
          acquisitionDate: 2022-11-15
          propertyTax: 10017

    TaxFormAttribute:
      title: Tax Form Attribute
      description: An additional tax form attribute for use when a defined field is not available
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'
        - type: object
          properties:
            boxNumber:
              type: string
              description: Box number on a tax form, if any
            code:
              type: string
              description: Tax form code for the given box number, if any

    TaxParty:
      title: Tax Party
      description: Legal entity for issuer or recipient, used across all tax forms
      type: object
      properties:
        tin:
          description: Issuer or recipient Tax Identification Number.
            Usually EIN for issuer and SSN for recipient
          type: string
        partyType:
          $ref: '#/components/schemas/TaxPartyType'
          description: Type of issuer or recipient legal entity, as "BUSINESS" or "INDIVIDUAL".
            Commonly BUSINESS for issuer and INDIVIDUAL for recipient
        individualName:
          $ref: './fdxapi.components.yaml#/components/schemas/IndividualName'
          description: Individual issuer or recipient name
        businessName:
          $ref: './fdxapi.components.yaml#/components/schemas/BusinessName'
          description: Business issuer or recipient name
        address:
          $ref: './fdxapi.components.yaml#/components/schemas/Address'
          description: Issuer or recipient address
        phone:
          $ref: './fdxapi.components.yaml#/components/schemas/TelephoneNumberPlusExtension'
          description: Issuer or recipient telephone number
        email:
          description: Issuer or recipient email address.
            (Additional information, not part of IRS forms)
          type: string

    TaxRefundDirectDeposit:
      title: Tax Refund Direct Deposit
      description: IRS Form 8888 Direct Deposit Information
      type: object
      properties:
        institutionName:
          description: Name of institution
          type: string
        rtn:
          description: Routing transit number
          type: string
        accountNumber:
          description: Account number
          type: string
        accountNickName:
          description: Account nickname
          type: string

    TaxStatement:
      title: Tax Statement
      description: Tax statement containing one or more tax forms
      type: object
      properties:
        taxYear:
          description: Year for which taxes are being paid
          $ref: '#/components/schemas/TaxYear'
        taxStatementId:
          description: Long-term persistent id for the tax statement.
            Depending upon the data provider, this may be the same id as the id on the enclosed tax form(s),
            or this may be a different id
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        issuer:
          description: Issuer's name, address, phone, and TIN.
            Issuer data need only be transmittted on TaxStatement, 'JSON' data type
            responses if it is the same on all included tax forms
          $ref: '#/components/schemas/TaxParty'
        recipient:
          description: Recipient's name, address, phone, and TIN.
            Recipient data need only be transmittted on TaxStatement, 'JSON' data type
            responses if it is the same on all included tax forms
          $ref: '#/components/schemas/TaxParty'
        taxDataType:
          description: Whether this `application/json` tax form response contains data
            in `forms` property (as 'JSON' format) or `pdf` property (as 'BASE64_PDF' format)
          $ref: '#/components/schemas/TaxDataType'
        forms:
          description: The list of data contents for all included tax forms,
            response should include one of `forms` or `pdf`
          type: array
          items:
            $ref: '#/components/schemas/TaxData'
        pdf:
          description: PDF version of the tax statement containing all form pages,
            binary encoded as Base64, response should include one of `pdf` or `forms`
          type: string
          format: base64
        attributes:
          description: Additional tax statement attributes that the provider wishes to include
          type: array
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'

    TaxStatementList:
      title: Tax Statement List
      description: Tax statement list containing one or more tax statements
      type: object
      properties:
        statements:
          type: array
          description: The list of tax statements
          items:
            $ref: '#/components/schemas/TaxStatement'

    TaxW2:
      title: Form W-2
      description: Wage and Tax Statement,
        from Employer (boxes b-c as issuer) to Employee (boxes a, e-f as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            controlNumber:
              description: Control number
              type: string
            wages:
              description: Box 1, Wages, tips, other compensation
              type: number
            federalTaxWithheld:
              description: Box 2, Federal income tax withheld
              type: number
            socialSecurityWages:
              description: Box 3, Social security wages
              type: number
            socialSecurityTaxWithheld:
              description: Box 4, Social security tax withheld
              type: number
            medicareWages:
              description: Box 5, Medicare wages and tips
              type: number
            medicareTaxWithheld:
              description: Box 6, Medicare tax withheld
              type: number
            socialSecurityTips:
              description: Box 7, Social security tips
              type: number
            allocatedTips:
              description: Box 8, Allocated tips
              type: number
            dependentCareBenefit:
              description: Box 10, Dependent care benefits
              type: number
            nonQualifiedPlan:
              description: Box 11, Nonqualified plans
              type: number
            codes:
              description: Box 12, Codes and amounts
              type: array
              items:
                $ref: '#/components/schemas/CodeAmount'
            statutory:
              type: boolean
              description: Box 13, Statutory employee
            retirementPlan:
              type: boolean
              description: Box 13, Retirement plan
            thirdPartySickPay:
              type: boolean
              description: Box 13, Third-party sick pay
            esppQualified:
              description: Employee Stock Purchase Plan Qualified Disposition amount
              type: number
            esppNonQualified:
              description: Employee Stock Purchase Plan Nonqualified Disposition amount
              type: number
            other:
              description: Box 14, Other descriptions and amounts
              type: array
              items:
                $ref: '#/components/schemas/DescriptionAmount'
            stateAndLocal:
              description: Boxes 15-20, State and Local tax withholding
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'

    TaxW2C:
      title: Form W-2c
      description: IRS form W-2c, Corrected Wage and Tax Statement,
        from Employer (boxes a-b as issuer) to Employee (boxes d, h-i as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            correctedTinOrName:
              description: Box e, Corrected SSN and/or name
              type: boolean
            previousEmployeeTin:
              description: Box f, Employee's previously reported SSN
              type: string
            previousEmployeeName:
              description: Box g, Employee's previously reported name
              $ref: './fdxapi.components.yaml#/components/schemas/IndividualName'
            originalW2:
              description: Boxes 1-20 of Previously reported Wage and Tax Statement
              $ref: '#/components/schemas/TaxW2'
            correctedW2:
              description: Boxes 1-20 of Correct information Wage and Tax Statement
              $ref: '#/components/schemas/TaxW2'

    TaxW2G:
      title: Form W-2G
      description: Certain Gambling Winnings,
        from PAYER (1st-3rd boxes as issuer) to WINNER (boxes 4th-6th and 9 as recipient)
      type: object
      allOf:
        - $ref: '#/components/schemas/Tax'
        - type: object
          properties:
            winnings:
              description: Box 1, Reportable winnings
              type: number
            dateWon:
              $ref: './fdxapi.components.yaml#/components/schemas/DateString'
              description: Box 2, Date won
            typeOfWager:
              description: Box 3, Type of wager
              type: string
            federalTaxWithheld:
              description: Box 4, Federal income tax withheld
              type: number
            transaction:
              description: Box 5, Transaction
              type: string
            race:
              description: Box 6, Race
              type: string
            identicalWinnings:
              description: Box 7, Winnings from identical wagers
              type: number
            cashier:
              description: Box 8, Cashier
              type: string
            window:
              description: Box 10, Window
              type: string
            firstId:
              description: Box 11, First I.D.
              type: string
            secondId:
              description: Box 12, Second I.D.
              type: string
            stateAndLocal:
              description: Boxes 13-18, State and Local tax withholding,
                use income fields for state (box 14) and local (box 16) winnings amounts
              type: array
              items:
                $ref: '#/components/schemas/StateAndLocalTaxWithholding'

    ############################################################
    #
    # US Tax data types
    #
    ############################################################

    CoverageMonth:
      title: Coverage Month
      description: Month enumeration used on forms 1095-A and 1095-C
      type: string
      enum:
        - ANNUAL
        - JANUARY
        - FEBRUARY
        - MARCH
        - APRIL
        - MAY
        - JUNE
        - JULY
        - AUGUST
        - SEPTEMBER
        - OCTOBER
        - NOVEMBER
        - DECEMBER

    ExpiredOptionType:
      title: Expired Option Type
      description: Type of expired stock option. Used by IRS Form 8949
      type: string
      enum:
        - GRANTED
        - PURCHASED

    InvestmentSaleType:
      title: Investment Sale Type
      description: Type of investment sale
      type: string
      enum:
        - CRYPTOCURRENCY
        - EMPLOYEE_STOCK_PURCHASE_PLAN
        - INCENTIVE_STOCK_OPTION
        - NONQUALIFIED_STOCK_OPTIONS
        - OTHER
        - RESTRICTED_STOCK
        - RESTRICTED_STOCK_UNITS

    MonthAbbreviation:
      title: Month Abbreviation
      description: Used by MonthAmount
      type: string
      enum:
        - JAN
        - FEB
        - MAR
        - APR
        - MAY
        - JUN
        - JUL
        - AUG
        - SEP
        - OCT
        - NOV
        - DEC

    SaleProceedsType:
      title: Sale Proceeds Type
      description: Gross or net proceeds. Used by Form 1099-B
      type: string
      enum:
        - GROSS
        - NET

    SaleTermType:
      title: Sale Term Type
      description: Long or short term. Used by Form 1099-B
      type: string
      enum:
        - LONG
        - SHORT

    TaxDataType:
      title: Type Data Type
      description: Specify which data type is requested using TaxDataTypeQuery parameter,
        to receive 'JSON' formatted tax data in `forms` property or PDF-formatted tax data
        encoded as Base64 in `pdf` property ('BASE64_PDF').
        In TaxStatement response entity indicates which tax data property was returned
      type: string
      enum:
        - BASE64_PDF
        - JSON

    TaxFormType:
      title: Type Form Type
      description: Tax form entity name e.g. "TaxW2"
      type: string
      enum:
        - BusinessIncomeStatement
        - CryptocurrencyTaxStatement
        - FarmIncomeStatement
        - FarmRentalIncomeStatement
        - RentalIncomeStatement
        - RoyaltyIncomeStatement
        - Tax1041K1
        - Tax1042S
        - Tax1065K1
        - Tax1065K3
        - Tax1095A
        - Tax1095B
        - Tax1095C
        - Tax1097Btc
        - Tax1098
        - Tax1098C
        - Tax1098E
        - Tax1098Ma
        - Tax1098Q
        - Tax1098T
        - Tax1099A
        - Tax1099B
        - Tax1099C
        - Tax1099Cap
        - Tax1099ConsolidatedStatement
        - Tax1099Div
        - Tax1099G
        - Tax1099H
        - Tax1099Int
        - Tax1099K
        - Tax1099Ls
        - Tax1099Ltc
        - Tax1099Misc
        - Tax1099Nec
        - Tax1099Oid
        - Tax1099Patr
        - Tax1099Q
        - Tax1099Qa
        - Tax1099R
        - Tax1099S
        - Tax1099Sa
        - Tax1099Sb
        - Tax1120SK1
        - Tax2439
        - Tax3921
        - Tax3922
        - Tax5227K1
        - Tax5498
        - Tax5498Esa
        - Tax5498Qa
        - Tax5498Sa
        - TaxW2
        - TaxW2C
        - TaxW2G

    TaxPartyType:
      title: Tax Party Type
      description: Whether the tax legal entity is a business or an individual
      type: string
      enum:
        - BUSINESS
        - INDIVIDUAL

    TaxYear:
      title: Tax Year Type
      description: The four-digit year for which a tax form applies.
        FDX Tax data API was completed with v3.0 in fall of 2018
      type: integer
      format: int32
      minimum: 2018
      maximum: 2050
      example: 2023
