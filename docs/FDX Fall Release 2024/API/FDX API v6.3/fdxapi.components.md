openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Shared Components API
  description: Financial Data Exchange V6.3.0 Shared Components API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Shared Components API

# paths: {}

components:

  securitySchemes:
    ############################################################
    #
    # Security schemes
    #
    ############################################################

    OAuthFapi1Baseline:
      type: oauth2
      description: >-
        This authorization protocol uses FAPI Security Profile 1.0 Part One — Baseline.
        To be used with the following FDX API domains: Event - Notification Subscription, Meta,
        Data Recipient Registration, Tax (the two update endpoints), and FDX Participant Registry.
        Client must comply with
        [6.2.2 Client provisions](https://openid.net/specs/openid-financial-api-part-1-1_0.html#client-provisions).
        Authorization server must comply with the
        [5.2.2 Authorization server](https://openid.net/specs/openid-financial-api-part-1-1_0.html#authorization-server).
        Client, authorization server and resource server requirements described in full by:
          * [FAPI Security Profile 1.0 Part One — Baseline](https://openid.net/specs/openid-financial-api-part-1-1_0.html)
          * FDX API Security Model specification published with the FDX API
      flows:
        clientCredentials:
          tokenUrl: 'https://auth.fi.com/fdx/v6/token'
          scopes:
            fdx:notifications:publish: Scope authorizing publishing of a new notification
            fdx:notifications:subscribe: Scope authorizing creation of a new notification subscription
            offline_access: Scope authorizing the client to refresh `access_tokens` without user present

    OAuthFapi1Advanced:
      type: oauth2
      description: >-
        This authorization protocol uses FAPI Security Profile 1.0 Part Two — Advanced.
        To be used with the FDX API customer data domains. In addition, these operations employ the FDX
        User Consent framework for permissioned data sharing.

        Client must comply with
        [5.2.3 Confidential client](https://openid.net/specs/openid-financial-api-part-2-1_0.html#confidential-client).
        Authorization server must comply with the
        [5.2.2 Authorization server](https://openid.net/specs/openid-financial-api-part-2-1_0.html#authorization-server).

        Client, authorization server and resource server requirements described in full by:
          * [FAPI Security Profile 1.0 Part Two — Advanced](https://openid.net/specs/openid-financial-api-part-2-1_0.html)
          * FDX API Security Model specification published with the FDX API

        Consent User Experience and Issuance described by:
          * FDX User Experience Guidelines published with the FDX API
          * Consent API operations and data structures published within the FDX API
      flows:
        authorizationCode:
          authorizationUrl: 'https://auth.fi.com/fdx/v6/par'
          tokenUrl: 'https://auth.fi.com/fdx/v6/token'
          scopes:
            fdx:accountbasic:read: Scope authorizing retrieval of account display name, masked account number, type, description
            fdx:accountdetailed:read: Scope authorizing retrieval of account information. Includes data from "Basic" + account balances, credit limits, due dates, interest rates, rewards balances, recurrences
            fdx:accountpayments:read: Deprecated and replaced with `fdx:paymentsupport:read` in FDX release V6.1.0, `fdx:accountpayments:read` will be removed with V7 release
            fdx:bills:read: Scope authorizing retrieval of bill payments data
            fdx:customercontact:read: Scope authorizing retrieval of name, email, address, phone on file with this institution. Applies to both user and other account holders
            fdx:customerpersonal:read: Scope authorizing retrieval of name, email, address, phone, DoB, tax ID, SSN on file with this institution
            fdx:images:read: Scope authorizing retrieval of check and receipt images, which may include PII such as name, full account and routing number
            fdx:investments:read: Scope authorizing retrieval of details about individual underlying investment positions
            fdx:paymentsupport:read: Scope authorizing retrieval of full account number and payment network routing number
            fdx:rewards:read: Scope authorizing retrieval of loyalty rewards programs, transactions and balances
            fdx:statements:read: Scope authorizing retrieval of periodic PDF statement showing personal information, account and transaction details. May contain PII such as name, address
            fdx:tax:read: Scope authorizing retrieval of information reporting tax forms and data, including any PII such as name, address, tax ID and account number
            fdx:transactions:read: Scope authorizing retrieval of historical and current transactions, transaction types, amounts, dates and descriptions
            offline_access: Scope authorizing the client to refresh `access_tokens` without user present
            openid: Scope authorizing access to the user's identity details

  parameters:
    ############################################################
    #
    # Shared request parameters (usable by core and all extensions)
    #
    ############################################################

    EndDateQuery:
      name: endDate
      in: query
      description: >-
        End date for use in retrieval of elements (ISO 8601 format).
        Provider to define the date ranges and behaviors they will support.
        Example of defined behavior:
          - Recipients need to either specify both start date and end date or neither.
            If both start date and end date are not specified; default provided.
            Default range: 7 Days of past data. (Today's date - 6 days both dates are inclusive)
          - Recipient can specify the same start date and end date. The returned data will reflect transactions from that date
          - If start date and end date both are specified and if start date is later than end date,
            return 'invalid date range' error code: 703, HTTPS 400 per the FDX spec
          - If start Date and end date both are specified and if start date is older than what the Data Provider supports,
            then the Data Provider should return 'invalid date range' error code: 703, HTTPS 400 per the FDX spec.
            Example: If today is 5/14/2024 and the DP supports 24 months, the start date should be 5/14/2022 and newer;
            it should not be 5/13/2022 or older
          - If start date is specified but end date is not specified or vice versa;
            Data Provider should return 'invalid date range' error code: 703, HTTPS 400 per the FDX spec
          - If end date is today's date, the most recent transactions from the time the request is received will be returned
      schema:
        $ref: '#/components/schemas/DateString'

    EndTimeQuery:
      name: endTime
      in: query
      description: End time for use in retrieval of elements (ISO 8601).
        Will support filtering by time in a future major release.
        To support filtering by date only, see EndDateQuery
      schema:
        $ref: '#/components/schemas/DateString'

    FapiAuthDateHeader:
      name: x-fapi-auth-date
      in: header
      description: >-
        Latest customer login interaction with client as defined by
        [FAPI Profile 1.0 Part 1: Baseline, 6.2.2 Client provisions](https://openid.net/specs/openid-financial-api-part-1-1_0.html#client-provisions),
        in `HTTP-date` format from
        [IETF RFC 7231 section 7.1.1.1](https://datatracker.ietf.org/doc/html/rfc7231#section-7.1.1.1).
        Used with OAuthFapi1Advanced security scheme
      schema:
        type: string
      required: false
      example: 'Tue, 19 Sep 2023 19:43:31 GMT'

    FapiCustomerIpAddressHeader:
      name: x-fapi-customer-ip-address
      in: header
      description: >-
        Customer's IP address, as defined by
        [FAPI Profile 1.0 Part 1: Baseline, 6.2.2 Client provisions](https://openid.net/specs/openid-financial-api-part-1-1_0.html#client-provisions).
        Used with OAuthFapi1Advanced security scheme
      schema:
        type: string
      required: false
      example: '2001:DB8::1893:25c8:1946 or 192.158.1.38'

    FapiInteractionIdHeader:
      name: x-fapi-interaction-id
      in: header
      description: Unique identifier for this interaction
      schema:
        $ref: '#/components/schemas/FapiInteractionId'
      required: true
      example: c770aef3-6784-41f7-8e0e-ff5f97bddb3a

    FdxApiActorTypeHeader:
      name: FDX-API-Actor-Type
      in: header
      description: Identifies whether the customer is present (USER) or it is a BATCH operation
      schema:
        $ref: '#/components/schemas/ActorType'
      example: BATCH
      # Code generation using openapi-generator v3.3.4 as of 9-27-2023 fails on the $ref here,
      # switch to this inline re-definition of ActorType enumeration for #CODEGEN to work:
      # type: string
      # enum:
      #   - BATCH
      #   - USER

    LimitQuery:
      name: limit
      in: query
      description: >-
        Number of elements that the consumer wishes to receive.
        Providers should implement reasonable default/maximum/minimum values
        based on their internal architecture and update their documentation accordingly
      schema:
        type: integer

    OffsetQuery:
      name: offset
      in: query
      description: >-
        Opaque cursor used by the provider to send the next set of records.
        Deprecated in favor of PageKeyQuery, will be removed with a future major release
      schema:
        type: string
      deprecated: true

    PageKeyQuery:
      name: pageKey
      in: query
      description: >-
        Opaque cursor used by the provider to send the next set of records.
        Pagination can be implemented per provider's preference
      schema:
        type: string

    ResultTypeQuery:
      name: resultType
      in: query
      description: >-
        Flag to indicate if you want a lightweight array of metadata (AccountDescriptor
        or Tax or Operations) or full item details (Account or a Tax subclass or
        Availability details). If set to 'lightweight', should only return the
        fields associated with the metadata entity.
        This field is not required, defaults to lightweight
      required: false
      schema:
        $ref: '#/components/schemas/ResultType'
        # Code generation using openapi-generator v3.3.4 as of 9-27-2023 fails on the $ref here,
        # switch to this inline re-definition of ResultType enumeration for #CODEGEN to work:
        # type: string
        # enum:
        #   - details
        #   - lightweight

    StartDateQuery:
      name: startDate
      in: query
      description: >-
        Start date for use in retrieval of elements (ISO 8601 format).
        Provider to define the date ranges and behaviors they will support.
        Example of defined behavior:
          - Recipients need to either specify both start date and end date or neither.
            If both start date and end date are not specified; default provided.
            Default range: 7 Days of past data. (Today's date - 6 days both dates are inclusive)
          - Recipient can specify the same start date and end date.
            The returned data will reflect transactions from that date
          - If start date and end date both are specified and if start date is later than end date,
            return 'invalid date range' error code: 703, HTTPS 400 per the FDX spec
          - If start Date and end date both are specified and if start date is older than what the Data Provider supports,
            then the Data Provider should return 'invalid date range' error code: 703, HTTPS 400 per the FDX spec.
            Example: If today is 5/14/2024 and the DP supports 24 months, the start date should be 5/14/2022 and newer;
            it should not be 5/13/2022 or older
          - If start date is specified but end date is not specified or vice versa;
            Data Provider should return 'invalid date range' error code: 703, HTTPS 400 per the FDX spec
      schema:
        $ref: '#/components/schemas/DateString'

    StartTimeQuery:
      name: startTime
      in: query
      description: Start time for use in retrieval of elements (ISO 8601).
        Will support filtering by time in a future major release.
        To support filtering by date only, see StartDateQuery
      schema:
        $ref: '#/components/schemas/DateString'

  headers:
    ############################################################
    #
    # Standard response headers
    #
    ############################################################

    x-fapi-interaction-id:
      description: Unique identifier for this interaction
      schema:
        $ref: '#/components/schemas/FapiInteractionId'
      example: c770aef3-6784-41f7-8e0e-ff5f97bddb3a

  schemas:
    ############################################################
    #
    # Shared data entities (usable by core and all extensions)
    #
    ############################################################

    Address:
      title: Address
      description: U.S. domestic address or a foreign address with country other than 'US'
      type: object
      properties:
        line1:
          $ref: '#/components/schemas/String64'
          description: Address line 1
        line2:
          $ref: '#/components/schemas/String64'
          description: Address line 2
        line3:
          $ref: '#/components/schemas/String64'
          description: Address line 3
        city:
          $ref: '#/components/schemas/String64'
          description: City
        region:
          $ref: '#/components/schemas/String64'
          description: State, Province, Territory, Canton or Prefecture.
            From [Universal Postal Union](https://www.upu.int/en/Postal-Solutions/Programmes-Services/Addressing-Solutions#addressing-s42-standard)
            as of 2-26-2020, [S42 International Address Standards](https://www.upu.int/UPU/media/upu/documents/PostCode/S42_International-Addressing-Standards.pdf).
            For U.S. addresses can be 2-character code from '#/components/schemas/StateCode'
        postalCode:
          type: string
          maxLength: 16
          description: Postal code
        country:
          $ref: '#/components/schemas/Iso3166CountryCode'
          description: Country code

    BusinessCustomer:
      title: Business Customer entity
      description: Customers that are commercial in nature are affiliated with a business entity.
        Japanese participants should send 'Kana' values in name fields using the
        character set defined by Zengin (Japanese Banks' Payment Clearing Network)
      type: object
      properties:
        name:
          type: string
          description: Name of business customer
        registeredAgents:
          type: array
          items:
            $ref: '#/components/schemas/CustomerName'
          description: A list of registered agents who act on behalf of the business customer
        registeredId:
          type: string
          description: The registered tax identification number (TIN) or other identifier of business customer
        industryCode:
          $ref: '#/components/schemas/IndustryCode'
          description: Industry code and type
        domicile:
          $ref: '#/components/schemas/Domicile'
          description: The country and region of the business customer's location

    BusinessName:
      title: Business name
      description: Name 1, Name 2
      type: object
      properties:
        name1:
          description: Name line 1
          type: string
        name2:
          description: Name line 2
          type: string

    Contacts:
      title: Contacts entity
      description: Contains all contact details for individual or business
      type: object
      properties:
        emails:
          type: array
          items:
            type: string
          description: Array of the contact email addresses
        addresses:
          type: array
          items:
            $ref: '#/components/schemas/DeliveryAddress'
          description: Array of the contact physical addresses
        telephones:
          type: array
          items:
            $ref: '#/components/schemas/TelephoneNumber'
          description: Array of the contact telephone numbers

    Customer:
      title: Customer entity
      description: Represents a customer
      type: object
      allOf:
        - $ref: '#/components/schemas/Person'
        - type: object
          properties:
            customerId:
              $ref: '#/components/schemas/Identifier'
              description: >-
                Long-term persistent identity of the customer.
                This identity must be unique to the owning institution
            type:
              $ref: '#/components/schemas/BusinessOrConsumer'
              description: Type of entity. One of BUSINESS or CONSUMER
            name:
              $ref: '#/components/schemas/CustomerName'
              description: The customer's name
            businessCustomer:
              $ref: '#/components/schemas/BusinessCustomer'
              description: The business customer information, only used if 'type' is 'BUSINESS'.
            customerStartDate:
              $ref: '#/components/schemas/DateString'
              description: The customer's start date at the financial institution
            lastActivityDate:
              $ref: '#/components/schemas/DateString'
              description: The customer's date of last account activity at the financial institution
            accounts:
              type: array
              items:
                $ref: '#/components/schemas/CustomerToAccountRelationship'
              description: List of accounts related to this customer

    CustomerName:
      title: Customer Name entity
      description: The name of an individual in their role as a customer.
        Japanese participants should send 'Kana' values in name fields using the
        character set defined by Zengin (Japanese Banks' Payment Clearing Network)
      type: object
      allOf:
        - $ref: '#/components/schemas/IndividualName'
        - type: object
          properties:
            prefix:
              description: Name prefix, e.g. Mr.
              type: string
            company:
              type: string
              description: Company name

    CustomerToAccountRelationship:
      title: Customer to Account Relationship entity
      description: Describes an account related to a customer
      type: object
      properties:
        accountId:
          $ref: '#/components/schemas/Identifier'
          description: Account ID of the related account
        links:
          $ref: '#/components/schemas/HateoasLinks'
          description: Links to the account, or to invoke other APIs
        relationship:
          $ref: '#/components/schemas/AccountHolderRelationship'
          description: Type of relationship to the account

    DeliveryAddress:
      title: Delivery Address
      description: A delivery address and its location type
      type: object
      allOf:
        - $ref: '#/components/schemas/Address'
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/DeliveryAddressType'
              description: Type of address location. One of BUSINESS, DELIVERY, HOME, MAILING
            primary:
              type: boolean
              description: Whether this is the primary and first address to use for contact

    Domicile:
      title: Domicile entity
      description: Country and region of country for the legal jurisdiction of an entity
      type: object
      properties:
        region:
          $ref: '#/components/schemas/String64'
          description: Country sub-division; state or province or territory
        country:
          $ref: '#/components/schemas/Iso3166CountryCode'
          description: ISO 3166 Country Code

    Error:
      title: Error
      description: >-
        An error entity which can be used at the API level for error responses
        or at the account level to indicate a problem specific to a particular
        account. See the error codes and descriptions defined in the latest
        FDX API Specification document, section 6.2 Errors
      type: object
      properties:
        code:
          type: string
          description: >-
            Error code defined by FDX API Specification or Data Provider
            indicating the error situation which has occurred
        message:
          type: string
          description: >-
            End user displayable information which might help the customer
            diagnose an error
        debugMessage:
          type: string
          description: >-
            Message used to debug the root cause of the error.
            Contents should not be used in consumer's business logic.
            Can change at any time and should only be used for consumer
            to communicate with the data provider about an issue.
            Provider can include an error GUID in message for their use.

    FapiInteractionId:
      title: FAPI Interaction ID
      description: >-
        Universally unique identifier for this interaction,
        used across all FDX API requests and responses
      type: string
      format: uuid
      minLength: 36
      maxLength: 36
      example: c770aef3-6784-41f7-8e0e-ff5f97bddb3a

    FiAttribute:
      title: FI Attribute entity
      description: Financial Institution provider-specific attribute
      type: object
      properties:
        name:
          type: string
          description: Name of attribute
        value:
          type: string
          description: Value of attribute

    HateoasLink:
      title: HATEOAS Link
      description: REST application constraint (Hypermedia As The Engine Of Application State)
      required: [href]
      type: object
      properties:
        href:
          type: string
          format: uri-reference
          description: URL to invoke the action on the resource
          example: "https://api.fi.com/fdx/v4/accounts/12345"
        action:
          description: HTTP Method to use for the request
          $ref: '#/components/schemas/HttpAction'
        rel:
          description: >-
            Relation of this link to its containing entity, as defined by and with many
            example relation values at [IETF RFC5988](https://datatracker.ietf.org/doc/html/rfc5988)
          type: string
        types:
          type: array
          items:
            $ref: '#/components/schemas/ContentTypes'
          description: Content-types that can be used in the Accept header

    HateoasLinks:
      title: HATEOAS Links array
      description: Links relative to this containing entity
      type: array
      items:
        $ref: '#/components/schemas/HateoasLink'

    IndividualName:
      title: Individual name
      description: First name, middle initial, last name, suffix fields.
        Japanese participants should send 'Kana' values in name fields using the
        character set defined by Zengin (Japanese Banks' Payment Clearing Network)
      type: object
      properties:
        first:
          description: First name
          type: string
        middle:
          description: Middle initial
          type: string
        last:
          description: Last name
          type: string
        suffix:
          description: Generational or academic suffix
          type: string

    IndustryCode:
      title: Industry code
      description: Industry code and type
      type: object
      properties:
        type:
          $ref: '#/components/schemas/IndustryClassificationSystem'
          description: Code type
        code:
          type: string
          description: Code value

    Intermediary:
      title: Intermediary
      description: Data Access Platform, Service Provider, or any other entity in the data
        sharing chain between a Data Provider to a Data Recipient.
        Properties in this structure use 'snake_case' names to match
        the properties in [IETF RFC 7591](https://datatracker.ietf.org/doc/rfc7591/)
      type: object
      properties:
        name:
          type: string
          description: Name of intermediary party
        description:
          type: string
          description: A short description of the intermediary
        uri:
          type: string
          format: uri
          description: A URL string of a web page providing information about the intermediary
        logo_uri:
          type: string
          format: uri
          description: A URL string that references a logo for this intermediary
        contacts:
          type: array
          items:
            type: string
          description: Array of strings representing ways to contact people responsible for this intermediary
        registry_references:
          type: array
          items:
            $ref: '#/components/schemas/RegistryReference'
          description: Registry references for this intermediary

    MonetaryAmount:
      title: Monetary Amount
      description: Monetary amount and its currency code
      type: object
      properties:
        amount:
          description: The monetary amount
          type: number
        currency:
          description: Currency code of the monetary amount
          $ref: '#/components/schemas/Iso4217CurrencyCode'
      required:
        - amount

    PageMetadata:
      title: Page Metadata
      description: Offset IDs for paginated result sets
      type: object
      properties:
        nextOffset:
          type: string
          example: "2"
          description: Opaque identifier. Does not need to be numeric or have any specific pattern.
            Deprecated in favor of nextPageKey, will be removed with a future major release
          deprecated: true
        nextPageKey:
          type: string
          example: "2"
          description: Opaque identifier. Does not need to be numeric or have any specific pattern.
            Implementation specific
        prevOffset:
          type: string
          example: "1"
          description: Opaque identifier. Does not need to be numeric or have any specific pattern.
            Deprecated in favor of previousPageKey, will be removed with a future major release
          deprecated: true
        previousPageKey:
          type: string
          example: "1"
          description: Opaque identifier. Does not need to be numeric or have any specific pattern.
            Implementation specific
        totalElements:
          type: integer
          example: 3
          description: Total number of elements

    PageMetadataLinks:
      title: Page Metadata Links
      description: Resource URLs for retrieving next or previous datasets
      type: object
      properties:
        next:
          $ref: '#/components/schemas/HateoasLink'
          description: Resource URL for retrieving next dataset
        prev:
          $ref: '#/components/schemas/HateoasLink'
          description: Resource URL for retrieving previous dataset

    PaginatedArray:
      title: Paginated Array
      description: Base class for results that may be paginated
      type: object
      properties:
        page:
          $ref: '#/components/schemas/PageMetadata'
          description: Offset IDs for navigating result sets
        links:
          $ref: '#/components/schemas/PageMetadataLinks'
          description: Resource URLs for navigating result sets

    Party:
      title: Party entity
      description: FDX Participant - an entity or person that is a part of a FDX API transaction
      type: object
      required:
        - name
        - type
      properties:
        name:
          description: Human recognizable common name
          type: string
        type:
          description: Extensible string enum identifying the type of the party
          $ref: '#/components/schemas/PartyType'
        homeUri:
          description: >-
            URI for party, where an end user could learn more about the company
            or application involved in the data sharing chain
          type: string
          format: uri
        logoUri:
          description: URI for a logo asset to be displayed to the end user
          type: string
          format: uri
        registry:
          description: >-
            The registry containing the party's registration with name and id:
            FDX, GLEIF, ICANN, PRIVATE
          $ref: '#/components/schemas/Registry'
        registeredEntityName:
          description: Registered name of party
          type: string
        registeredEntityId:
          description: Registered id of party
          type: string

    PaymentDetails:
      title: Payment Details entity
      description: Details of this payment
      type: object
      properties:
        principalAmount:
          type: number
          description: The amount of payment applied to principal
        interestAmount:
          type: number
          description: The amount of payment applied to interest
        insuranceAmount:
          type: number
          description: The amount of payment applied to life/health/accident insurance on the loan
        escrowAmount:
          type: number
          description: The amount of payment applied to escrow
        pmiAmount:
          type: number
          description: The amount of payment applied to PMI
        feesAmount:
          type: number
          description: The amount of payment applied to fees

    Person:
      title: Person entity
      description: Represents a person
      type: object
      allOf:
        - $ref: '#/components/schemas/Contacts'
        - type: object
          properties:
            dateOfBirth:
              $ref: '#/components/schemas/DateString'
              description: The person's date of birth
            taxId:
              type: string
              description: Country specific Tax Id associated with this customer.
                Masked as last four, e.g. xxx-xx-0123, or passed in encrypted payload.
                (SIN or NAS in Canada, SSN or TIN in US, etc.)
            taxIdCountry:
              $ref: '#/components/schemas/Iso3166CountryCode'
              description: Country originating the Customer's taxId element
            governmentId:
              type: string
              description: >-
                A federal (such as passport) or state (such as driver's license)
                issued identifier

    RecipientRequest:
      title: Recipient Request
      type: object
      description: Used to request a recipient registration.
        Properties in this structure use 'snake_case' names to match
        the properties in [IETF RFC 7591](https://datatracker.ietf.org/doc/rfc7591/)
      properties:
        client_name:
          $ref: '#/components/schemas/Identifier'
          description: The Data Recipient or Data Recipient Application name displayed by Data Provider during
                       the consent Flow as well as in the Consent Dashboard
        description:
          type: string
          description: A short description of the Data Recipient application
        redirect_uris:
          type: array
          items:
            type: string
          description: An array of eligible Redirect URI targets
        logo_uri:
          type: string
          description: Data Recipient Logo URL location
          format: uri
        client_uri:
          type: string
          description: The URI which provides additional information about the Data Recipient
          format: uri
        contacts:
          type: array
          items:
            type: string
          description: Array of strings representing ways to contact individuals responsible for the Data Recipient application
        scope:
          type: string
          description: String containing a space-separated list of scope values.
            Applicable FDX scopes are defined in OauthScope and FdxOauthScope enumerations.
            Prior use of DataCluster enumeration for scopes is deprecated with release V6.3
        duration_type:
          type: array
          items:
            $ref: '#/components/schemas/ConsentDurationType'
          description: The duration of consent for the Data Recipient consumers
        duration_period:
          type: integer
          description: The maximum consent duration in days for duration_type TIME_BOUND for the Data Recipient,
            effective from the date of consent
        lookback_period:
          type: integer
          description: The maximum number of days allowed for Data Recipient to obtain in transaction history,
            effective from the current date
        registry_references:
          type: array
          items:
            $ref: '#/components/schemas/RegistryReference'
          description: An array of external registries containing registered entity name, registered entity id and
            registry fields for the registries where the data recipient is registered
        intermediaries:
          type: array
          items:
            $ref: '#/components/schemas/Intermediary'
          description: An array of the intermediaries for this data recipient
      required:
        - client_name
        - redirect_uris

    RegistryReference:
      title: Registry Reference
      type: object
      description: Used for registry references.
        Properties in this structure use 'snake_case' names to match
        the properties in [IETF RFC 7591](https://datatracker.ietf.org/doc/rfc7591/)
      properties:
        registered_entity_name:
          type: string
          description: The legal company name for the intermediary
        registered_entity_id:
          type: string
          description: An ID representing the intermediary that can be looked up from a legal identity registry source
        registry:
          $ref: '#/components/schemas/Registry'
          description: The Registry source

    TelephoneNumber:
      title: Telephone Number
      description: Standard for international phone numbers
      type: object
      properties:
        type:
          $ref: '#/components/schemas/TelephoneNumberPurpose'
          description: >-
            Purpose of the phone number: HOME, BUSINESS, PERSONAL, FAX, or BOTH.
            BOTH indicates number is used for both HOME and BUSINESS purposes.
            `CELL` value is deprecated in v6.3, replaced as a `network` value
        country:
          type: string
          minLength: 1
          maxLength: 4
          pattern: ^\+?[1-9][0-9]{0,2}$
          description: Country calling codes defined by ITU-T recommendations E.123 and E.164,
            such as '+1' for United States and Canada, see
            [List_of_country_calling_codes](https://en.wikipedia.org/wiki/List_of_country_calling_codes)
        number:
          type: string
          maxLength: 15
          pattern: '\d+'
          description: Telephone subscriber number defined by ITU-T recommendation E.164
        network:
          $ref: '#/components/schemas/TelephoneNetwork'
          description: The network technology used for this telephone.
            One of CELLULAR, LANDLINE, PAGER, SATELLITE, or VOIP
        primary:
          type: boolean
          description: Whether this is the primary and first telephone number to call

    TelephoneNumberPlusExtension:
      title: Telephone Number Plus Extension
      description: A telephone number that can contain optional text for an arbitrary length
        telephone extension number
      type: object
      allOf:
        - $ref: '#/components/schemas/TelephoneNumber'
        - type: object
          properties:
            extension:
              description: An arbitrary length telephone number extension
              type: string

    ############################################################
    #
    # Shared data types (usable by core and all extensions)
    #
    ############################################################

    AccountHolderRelationship:
      title: Account Holder Relationship
      description: >-
        Types of relationships between accounts and holders. Some definitions:
          - AUTHORIZED_SIGNER - An Authorized Signer is an individual who has been given permission
            by the account owner/holder to sign checks, make withdrawals, and conduct transactions
            on behalf of an account holder for deposit account types, such as checking or savings,
            but does not own the account. They may also have an ability to make changes to the account
            (e.g. can close the account)
          - AUTHORIZED_USER - An Authorized User is an individual added to a credit card account by
            the primary account holder, who has been authorized to make purchases using the card,
            but has no legal responsibility to repay the debt. The primary account holder remains
            legally responsible for repaying the debt for all charges incurred, including those of
            the Authorized User. Authorized User may not have access to the full account control
            (e.g. cannot close the account)
      type: string
      enum:
        - AUTHORIZED_SIGNER
        - AUTHORIZED_USER
        - BUSINESS
        - FOR_BENEFIT_OF
        - FOR_BENEFIT_OF_PRIMARY
        - FOR_BENEFIT_OF_PRIMARY_JOINT_RESTRICTED
        - FOR_BENEFIT_OF_SECONDARY
        - FOR_BENEFIT_OF_SECONDARY_JOINT_RESTRICTED
        - FOR_BENEFIT_OF_SOLE_OWNER_RESTRICTED
        - POWER_OF_ATTORNEY
        - PRIMARY
        - PRIMARY_BORROWER
        - PRIMARY_JOINT
        - PRIMARY_JOINT_TENANTS
        - SECONDARY
        - SECONDARY_BORROWER
        - SECONDARY_JOINT
        - SECONDARY_JOINT_TENANTS
        - SOLE_OWNER
        - TRUSTEE
        - UNIFORM_TRANSFER_TO_MINOR

    AccountType:
      title: Account Type
      description: >-
        The type of an account.

          | Value | Description |
          |-----|-----|
          | 401A | An employer-sponsored money-purchase retirement plan that allows dollar or percentage-based contributions from the employer, the employee, or both |
          | 401K | An employer-sponsored defined-contribution pension account defined in subsection 401(k) of the Internal Revenue Code |
          | 403B | A U.S. tax-advantaged retirement savings plan available for public education organizations, some non-profit employers (only Internal Revenue Code 501(c)(3) organizations), cooperative hospital service organizations, and self-employed ministers in the United States |
          | 529 | A tax-advantaged savings plan designed to help pay for education |
          | ANNUITY | A form of insurance or investment entitling the investor to a series of annual sums |
          | AUTOLOAN | A type of loan used to finance a car purchase |
          | BROKERAGEPRODUCT | Investment management offered by a licensed brokerage firm that places trades on behalf of the customer, utilizing any number of investment options |
          | CD | A certificate of deposit (CD) is a product offered by banks and credit unions that provides an interest rate premium in exchange for the customer agreeing to leave a lump-sum deposit untouched for a predetermined period of time |
          | CHARGE | An account to which goods and services may be charged on credit |
          | CHECKING | A deposit account held at a financial institution that allows withdrawals and deposits |
          | COMMERCIALDEPOSIT | Deposit Account for Commercial Customers e.g. Business Trust Account |
          | COMMERCIALINVESTMENT | Investment Account for Commercial Customers. e.g. Commercial Brokerage Account |
          | COMMERCIALLINEOFCREDIT | A preset borrowing limit that can be used at any time |
          | COMMERCIALLOAN | A preset borrowing limit that can be used at any time |
          | COVERDELL | A trust or custodial account set up in the United States solely for paying qualified education expenses for the designated beneficiary of the account |
          | CREDITCARD | Allows cardholders to borrow funds with which to pay for goods and services with merchants that accept cards for payment |
          | DEFERREDPROFITSHARINGPLAN | A deferred profit sharing plan (DPSP) is an employer-sponsored profit sharing plan that is registered with a government agency (such as the Canada Revenue Agency) |
          | DEFINEDBENEFIT | An employer-sponsored retirement plan where employee benefits are computed using a formula that considers several factors, such as length of employment and salary history |
          | DIGITALASSET | Encompasses cryptocurrencies as well as other digital assets such as NFTs |
          | DIGITALWALLET | A digital wallet account enables digital financial transactions through a deposit value and one or more linked funding instruments |
          | ESCROW | A contractual arrangement in which a third party (the stakeholder or escrow agent) receives and disburses money or property for the primary transacting parties, with the disbursement dependent on conditions agreed to by the transacting parties |
          | ESOP | An employee stock ownership plan (ESOP) is an employee benefit plan that gives workers ownership interest in the company |
          | FIRSTHOMESAVINGSACCOUNT | A First Home Savings Account (FHSA), registered with the Canadian federal government, which allows first-time home buyers to save to buy or build their first home tax free |
          | FIXEDANNUITY | A type of insurance contract that promises to pay the buyer a specific, guaranteed interest rate on their contributions to the account |
          | GUARDIAN | An account of a child in the parent's name, with legal title to the assets in the account, as well as all capital gains and tax liabilities produced from the account belonging to the parent |
          | HIGHINTERESTSAVINGSACCOUNT | A High Interest Savings Account (HISA), is an account type recognized in Canada, which allows individuals to save at a higher interest rate than a standard savings account |
          | HOMEEQUITYLOAN | A type of loan in which the borrower uses the equity of his or her home as collateral |
          | HOMELINEOFCREDIT | A loan in which the lender agrees to lend a maximum amount within an agreed period, where the collateral is the borrower's equity in their house |
          | INDIVIDUALPENSIONPLAN | An Individual Pension Plan (IPP) is an employer-sponsored, defined benefit pension plan that can be set up by and for a single person |
          | INSTALLMENT | A type of agreement or contract involving a loan that is repaid over time with a set number of scheduled payments |
          | INSTITUTIONALTRUST | |
          | INVESTMENTACCOUNT | A standard investment account that is not registered |
          | IRA | An individual retirement account (IRA) is a tax-advantaged account that individuals use to save and invest for retirement |
          | KEOGH | A tax-deferred pension plan available to self-employed individuals or unincorporated businesses for retirement purposes |
          | LIFEINCOMEFUND | A Life Income Fund (LIF) is a type of registered retirement income fund (RRIF) that can be used to hold locked-in pension funds as well as other assets for an eventual payout as retirement income |
          | LINEOFCREDIT | A credit facility extended by a bank or other financial institution to a government, business or individual customer that enables the customer to draw on the facility when the customer needs funds |
          | LOAN | The lending of money by one or more individuals, organizations, or other entities to other individuals, organizations etc |
          | LOCKEDINRETIREMENTACCOUNT | A Locked-in Retirement Account (LIRA) is a pension savings account that holds funds that cannot be withdrawn until retirement |
          | LOCKEDINRETIREMENTINCOMEFUND | A Locked-in Retirement Income Fund (LRIF) is a locked-in account which has been created with funds that originated with a registered pension plan (RPP) |
          | LOCKEDINRETIREMENTSAVINGSPLAN | A Locked-in Retirement Savings plan (LRSP) is a pension savings account that holds funds that cannot be withdrawn until retirement (similar to LIRA)  |
          | LONGTERMDISABILITY | Insurance that replaces a portion of the policyholder's income due to a disability for an extended period of time, usually more than a year |
          | MILITARYLOAN | |
          | MONEYMARKET | A deposit account that pays interest based on current interest rates in the money markets |
          | MORTGAGE | A type of loan you can use to buy or refinance a home |
          | NONQUALIFEDPLAN | A type of tax-deferred employer-sponsored retirement plan that falls outside of ERISA guidelines |
          | OTHERDEPOSIT | Use when none of the listed enums apply |
          | OTHERINVESTMENT | Use when none of the listed enums apply |
          | PERSONALLOAN | A type of debt that is not protected by a guarantor, or collateralized by a lien on specific assets of the borrower |
          | POOLEDREGISTEREDPENSIONPLAN | A Pooled Registered Pension Plan (PRPP) is a type of pension plan that is similar to a defined contribution plan; however, employer contributions are not mandatory |
          | PREPAID | An account that is preloaded with funds before first use, such as a gift card |
          | PRESCRIBEDREGISTEREDRETIREMENTINCOMEFUND | A Prescribed Registered Retirement Income Fund (PRRIF) is a personal retirement income fund that is governed by the federal Income Tax Act (Canada) |
          | REGISTEREDDISABILITYSAVINGSPLAN | A Registered Disability Savings Plan (RDSP) is a savings plan intended to help parents and others save for the long term financial security of a person who is eligible for the disability tax credit (DTC) |
          | REGISTEREDEDUCATIONSAVINGSPLAN | A Registered Education Savings Plan (RESP) is a special savings account for parents/custodians/others who want to save for their child's education after high school and is registered with the Canadian federal government |
          | REGISTEREDPENSIONPLAN | A Registered Pension Plan (RPP) is a pension plan that has been set up by an employer, and registered by the Canadian federal government |
          | REGISTEREDRETIREMENTINCOMEFUND | A Registered Retirement Income Fund (RRIF) is an arrangement between an individual and a carrier (an insurance company, a trust company or a bank) that is registered with the Canadian federal government |
          | REGISTEREDRETIREMENTSAVINGSPLAN | A Registered Retirement Savings Plan (RRSP) is a savings plan, registered with the Canadian federal government that you can contribute to for retirement purposes |
          | RESTRICTEDLIFEINCOMEFUND | Restricted Life Income Fund (RLIF) is a retirement option that operates like a LIF. The RLIF provides a one-time 50% unlocking option |
          | RESTRICTEDLOCKEDINSAVINGSPLAN | A Restricted Locked-In Savings Plan (RLSP) is an investment account that can only be established as a result of a transfer of funds from an RLIF |
          | ROLLOVER | |
          | ROTH | An individual retirement account that offers tax-free growth and tax-free withdrawals in retirement |
          | SARSEP | A simplified employee pension (SEP) plan set up before 1997 that includes a salary reduction arrangement |
          | SAVINGS | An interest-bearing deposit account held at a bank or other financial institution |
          | SMBLOAN | |
          | SHORTTERMDISABILITY | Insurance that replaces a portion of the policyholder's income due to a disability for a short period of time, usually less than a year |
          | SPECIFIEDPENSIONPLAN | A Specified Pension Plan (SPP) is a pension plan or similar arrangement that has been prescribed under the Income Tax Regulations as a "specified pension plan" for purposes of the Income Tax Act |
          | STUDENTLOAN | A type of loan designed to help students pay for post-secondary education and the associated fees, such as tuition, books and supplies, and living expenses |
          | TAXABLE | |
          | TAXFREESAVINGSACCOUNT | A Tax-Free Savings Account (TFSA) is a way for over the age of 18 to set money aside, tax free, throughout their lifetime |
          | TDA | |
          | TERM | Life insurance that provides coverage at a fixed rate of payments for a limited period of time |
          | TRUST | A type of financial account that is opened by an individual and managed by a designated trustee for the benefit of a third party in accordance with agreed-upon terms |
          | UGMA | |
          | UNIVERSALLIFE | A type of a cash value life insurance where the excess of premium payments above the current cost of insurance is credited to the cash value of the policy, which in turn is credited each month with interest |
          | UTMA | |
          | VARIABLEANNUITY | A type of insurance contract that promises to pay back the buyer based on the performance of an underlying portfolio of mutual funds selected by the buyer |
          | WHOLELIFE | Life insurance which is guaranteed to remain in force for the insured's entire lifetime, provided required premiums are paid, or to the maturity date |
      type: string
      enum:
        - 401A
        - 401K
        - 403B
        - '529'
        - ANNUITY
        - AUTOLOAN
        - BROKERAGEPRODUCT
        - CD
        - CHARGE
        - CHECKING
        - COMMERCIALDEPOSIT
        - COMMERCIALINVESTMENT
        - COMMERCIALLINEOFCREDIT
        - COMMERCIALLOAN
        - COVERDELL
        - CREDITCARD
        - DEFERREDPROFITSHARINGPLAN
        - DEFINEDBENEFIT
        - DIGITALASSET
        - DIGITALWALLET
        - ESCROW
        - ESOP
        - FIRSTHOMESAVINGSACCOUNT
        - FIXEDANNUITY
        - GUARDIAN
        - HIGHINTERESTSAVINGSACCOUNT
        - HOMEEQUITYLOAN
        - HOMELINEOFCREDIT
        - INDIVIDUALPENSIONPLAN
        - INSTALLMENT
        - INSTITUTIONALTRUST
        - INVESTMENTACCOUNT
        - IRA
        - KEOGH
        - LIFEINCOMEFUND
        - LINEOFCREDIT
        - LOAN
        - LOCKEDINRETIREMENTACCOUNT
        - LOCKEDINRETIREMENTINCOMEFUND
        - LOCKEDINRETIREMENTSAVINGSPLAN
        - LONGTERMDISABILITY
        - MILITARYLOAN
        - MONEYMARKET
        - MORTGAGE
        - NONQUALIFIEDPLAN
        - OTHERDEPOSIT
        - OTHERINVESTMENT
        - PERSONALLOAN
        - POOLEDREGISTEREDPENSIONPLAN
        - PREPAID
        - PRESCRIBEDREGISTEREDRETIREMENTINCOMEFUND
        - REGISTEREDDISABILITYSAVINGSPLAN
        - REGISTEREDEDUCATIONSAVINGSPLAN
        - REGISTEREDPENSIONPLAN
        - REGISTEREDRETIREMENTINCOMEFUND
        - REGISTEREDRETIREMENTSAVINGSPLAN
        - RESTRICTEDLIFEINCOMEFUND
        - RESTRICTEDLOCKEDINSAVINGSPLAN
        - ROLLOVER
        - ROTH
        - SARSEP
        - SAVINGS
        - SHORTTERMDISABILITY
        - SMBLOAN
        - SPECIFIEDPENSIONPLAN
        - STUDENTLOAN
        - TAXABLE
        - TAXFREESAVINGSACCOUNT
        - TDA
        - TERM
        - TRUST
        - UGMA
        - UNIVERSALLIFE
        - UTMA
        - VARIABLEANNUITY
        - WHOLELIFE

    ActorType:
      title: FDX API Actor Type
      description: >-
        Indicates whether a customer is present and has requested the operation (USER),
        or if a batch job has requested the operation (BATCH)
      type: string
      enum:
        - BATCH
        - USER

    BusinessOrConsumer:
      title: Business or Consumer Type
      description: Indicator if parent entity is a consumer or business
      type: string
      enum:
        - BUSINESS
        - CONSUMER

    ConsentDurationType:
      title: Consent Duration Type
      description: Duration of the Consent Grant, per FDX UX Guidelines v1.0 (pp 18 - 20)
      type: string
      enum:
        - ONE_TIME
        - PERSISTENT
        - TIME_BOUND

    ContentTypes:
      title: Content Types
      description: Types of document formats. (Suggested values)
      type: string
      enum:
        - application/json
        - application/pdf
        - application/zip
        - image/gif
        - image/jpeg
        - image/png
        - image/tiff

    DateString:
      title: Date String
      description: >-
        ISO 8601 full-date in format 'YYYY-MM-DD' according
        to [IETF RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339.html#section-5.6)
      type: string
      format: date
      maxLength: 10
      example: '2021-07-15'

    DeliveryAddressType:
      title: Delivery Address Type
      description: The location type of an address
      type: string
      enum:
        - BUSINESS
        - DELIVERY
        - HOME
        - MAILING

    FdxVersion:
      title: FDX Version
      description: The list of prior and current FDX major and minor versions.
      type: string
      enum:
        - V1.0
        - V2.0
        - V2.1
        - V3.0
        - V4.0
        - V4.1
        - V4.2
        - V4.5
        - V4.6
        - V4.6.1
        - V4.6.2
        - V5.0
        - V5.0.0
        - V5.0.1
        - V5.0.2
        - V5.0.3
        - V5.1
        - V5.1.0
        - V5.1.1
        - V5.1.2
        - V5.2
        - V5.2.0
        - V5.2.1
        - V5.2.2
        - V5.2.3
        - V5.2.4
        - V5.3
        - V5.3.0
        - V5.3.1
        - V5.3.2
        - V5.3.3
        - V6.0.0
        - V6.1.0
        - V6.2.0
        - V6.3.0

    FdxOauthScope:
      title: FDX OAuth scopes
      description: >-
        Represents an authorization claim aligned with FDX Data Cluster.
        `fdx:accountpayments:read` is deprecated and replaced with `fdx:paymentsupport:read`
        in FDX release V6.1.0, `fdx:accountpayments:read` will be removed with V7 release
      type: string
      enum:
        - fdx:accountbasic:read
        - fdx:accountdetailed:read
        - fdx:accountpayments:read  # Deprecated
        - fdx:bills:read
        - fdx:customercontact:read
        - fdx:customerpersonal:read
        - fdx:images:read
        - fdx:investments:read
        - fdx:notifications:publish
        - fdx:notifications:subscribe
        - fdx:paymentsupport:read
        - fdx:rewards:read
        - fdx:statements:read
        - fdx:tax:read
        - fdx:transactions:read

    HttpAction:
      title: HTTP Action Type
      description: HTTP Methods to use for requests
      type: string
      enum:
        - DELETE
        - GET
        - PATCH
        - POST
        - PUT

    Identifier:
      title: Identifier
      description: Value for a unique identifier
      type: string
      maxLength: 256

    IndustryClassificationSystem:
      title: Industry Classification System
      description: >-
        The Industry Classification System containing the industry code for customer.

          | Value | Description |
          |-----|-----|
          | BCLASS | [Bloomberg Classification System](https://www.bloomberg.com/professional/product/reference-data/) |
          | BICS | [Bloomberg Industry Classification System](https://www.bloomberg.com/professional/product/reference-data/) |
          | GICS | [Global Industry Classification System](https://www.msci.com/our-solutions/indexes/gics) |
          | MOODYS | Moody's Industry Classification |
          | NAICS | [North American Industry Classification System](https://www.naics.com) |
          | OTHER | Any other set of industry classification codes |
          | SIC | [Standard Industry Classification system](https://www.osha.gov/pls/imis/sicsearch.html) |
      type: string
      enum:
        - BCLASS
        - BICS
        - GICS
        - MOODYS
        - NAICS
        - OTHER
        - SIC

    Iso3166CountryCode:
      title: ISO 3166 Country Code
      description: >-
        ISO 3166-1 alpha-2 codes as of April 5, 2023, from officially assigned Country Codes on
        [ISO Online Browsing Platform](https://www.iso.org/obp/ui/). Change log is at
        [ISO 3166 Maintenance Agency](https://www.iso.org/fr/committee/48750.html?t=3V3rukDb61p05Wd6ojyTRvE0S3Yg_fZgUjrLjHWcd9-mDmTKHOGjbX3nEJ3SqHar&view=documents#section-isodocuments-top)
      type: string
      enum:
        - AD
        - AE
        - AF
        - AG
        - AI
        - AL
        - AM
        - AO
        - AQ
        - AR
        - AS
        - AT
        - AU
        - AW
        - AX
        - AZ
        - BA
        - BB
        - BD
        - BE
        - BF
        - BG
        - BH
        - BI
        - BJ
        - BL
        - BM
        - BN
        - BO
        - BQ
        - BR
        - BS
        - BT
        - BV
        - BW
        - BY
        - BZ
        - CA
        - CC
        - CD
        - CF
        - CG
        - CH
        - CI
        - CK
        - CL
        - CM
        - CN
        - CO
        - CR
        - CU
        - CV
        - CW
        - CX
        - CY
        - CZ
        - DE
        - DJ
        - DK
        - DM
        - DO
        - DZ
        - EC
        - EE
        - EG
        - EH
        - ER
        - ES
        - ET
        - FI
        - FJ
        - FK
        - FM
        - FO
        - FR
        - GA
        - GB
        - GD
        - GE
        - GF
        - GG
        - GH
        - GI
        - GL
        - GM
        - GN
        - GP
        - GQ
        - GR
        - GS
        - GT
        - GU
        - GW
        - GY
        - HK
        - HM
        - HN
        - HR
        - HT
        - HU
        - ID
        - IE
        - IL
        - IM
        - IN
        - IO
        - IQ
        - IR
        - IS
        - IT
        - JE
        - JM
        - JO
        - JP
        - KE
        - KG
        - KH
        - KI
        - KM
        - KN
        - KP
        - KR
        - KW
        - KY
        - KZ
        - LA
        - LB
        - LC
        - LI
        - LK
        - LR
        - LS
        - LT
        - LU
        - LV
        - LY
        - MA
        - MC
        - MD
        - ME
        - MF
        - MG
        - MH
        - MK
        - ML
        - MM
        - MN
        - MO
        - MP
        - MQ
        - MR
        - MS
        - MT
        - MU
        - MV
        - MW
        - MX
        - MY
        - MZ
        - NA
        - NC
        - NE
        - NF
        - NG
        - NI
        - NL
        - 'NO'
        - NP
        - NR
        - NU
        - NZ
        - OM
        - PA
        - PE
        - PF
        - PG
        - PH
        - PK
        - PL
        - PM
        - PN
        - PR
        - PS
        - PT
        - PW
        - PY
        - QA
        - RE
        - RO
        - RS
        - RU
        - RW
        - SA
        - SB
        - SC
        - SD
        - SE
        - SG
        - SH
        - SI
        - SJ
        - SK
        - SL
        - SM
        - SN
        - SO
        - SR
        - SS
        - ST
        - SV
        - SX
        - SY
        - SZ
        - TC
        - TD
        - TF
        - TG
        - TH
        - TJ
        - TK
        - TL
        - TM
        - TN
        - TO
        - TR
        - TT
        - TV
        - TW
        - TZ
        - UA
        - UG
        - UM
        - US
        - UY
        - UZ
        - VA
        - VC
        - VE
        - VG
        - VI
        - VN
        - VU
        - WF
        - WS
        - YE
        - YT
        - ZA
        - ZM
        - ZW

    Iso4217CurrencyCode:
      title: ISO 4217 Currency Code
      description: >-
        Currency, fund and precious metal codes effective from June 25, 2024 per
        [ISO 4217 Currency Code Maintenance](https://www.six-group.com/en/products-services/financial-information/data-standards.html).
        ZWL (the Zimbabwean dollar) expires August 31, 2024 and is deprecated
        and replaced with ZWG (Zimbabwe Gold), effective on June 25, 2024
      type: string
      enum:
        - AED
        - AFN
        - ALL
        - AMD
        - ANG
        - AOA
        - ARS
        - AUD
        - AWG
        - AZN
        - BAM
        - BBD
        - BDT
        - BGN
        - BHD
        - BIF
        - BMD
        - BND
        - BOB
        - BOV
        - BRL
        - BSD
        - BTN
        - BWP
        - BYN
        - BZD
        - CAD
        - CDF
        - CHE
        - CHF
        - CHW
        - CLF
        - CLP
        - CNY
        - COP
        - COU
        - CRC
        - CUC
        - CUP
        - CVE
        - CZK
        - DJF
        - DKK
        - DOP
        - DZD
        - EGP
        - ERN
        - ETB
        - EUR
        - FJD
        - FKP
        - GBP
        - GEL
        - GHS
        - GIP
        - GMD
        - GNF
        - GTQ
        - GYD
        - HKD
        - HNL
        - HTG
        - HUF
        - IDR
        - ILS
        - INR
        - IQD
        - IRR
        - ISK
        - JMD
        - JOD
        - JPY
        - KES
        - KGS
        - KHR
        - KMF
        - KPW
        - KRW
        - KWD
        - KYD
        - KZT
        - LAK
        - LBP
        - LKR
        - LRD
        - LSL
        - LYD
        - MAD
        - MDL
        - MGA
        - MKD
        - MMK
        - MNT
        - MOP
        - MRU
        - MUR
        - MVR
        - MWK
        - MXN
        - MXV
        - MYR
        - MZN
        - NAD
        - NGN
        - NIO
        - NOK
        - NPR
        - NZD
        - OMR
        - PAB
        - PEN
        - PGK
        - PHP
        - PKR
        - PLN
        - PYG
        - QAR
        - RON
        - RSD
        - RUB
        - RWF
        - SAR
        - SBD
        - SCR
        - SDG
        - SEK
        - SGD
        - SHP
        - SLE
        - SLL
        - SOS
        - SRD
        - SSP
        - STN
        - SVC
        - SYP
        - SZL
        - THB
        - TJS
        - TMT
        - TND
        - TOP
        - TRY
        - TTD
        - TWD
        - TZS
        - UAH
        - UGX
        - USD
        - USN
        - UYI
        - UYU
        - UYW
        - UZS
        - VED
        - VES
        - VND
        - VUV
        - WST
        - XAF
        - XAG
        - XAU
        - XBA
        - XBB
        - XBC
        - XBD
        - XCD
        - XDR
        - XOF
        - XPD
        - XPF
        - XPT
        - XSU
        - XTS
        - XUA
        - XXX
        - YER
        - ZAR
        - ZMW
        - ZWG
        - ZWL  # Deprecated

    OauthScope:
      title: OpenID OAuth Scopes
      description: FDX API-used OAuth 2.0 Scope values to request Claims as defined by
        [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims)
      type: string
      enum:
        - offline_access
        - openid

    PartyType:
      title: Party Type
      description: Identifies the type of a party
      type: string
      enum:
        - DATA_ACCESS_PLATFORM
        - DATA_PROVIDER
        - DATA_RECIPIENT
        - INDIVIDUAL
        - MERCHANT
        - VENDOR

    Registry:
      title: Registry
      description: Identifies the type of a Registry
      type: string
      enum:
        - FDX
        - GLEIF
        - ICANN
        - PRIVATE

    ResultType:
      title: Result Type
      description: >-
        Flag to indicate if you want a lightweight array of metadata (AccountDescriptor
        or Tax or Operations) or full item details (Account or a Tax subclass or
        Availability details). If set to 'lightweight', should only return the
        fields associated with the metadata entity.
      type: string
      enum:
        - details
        - lightweight
      default: lightweight

    StateCode:
      title: State Code
      description: >-
        The codes for U.S. states, possessions and military overseas addresses.
        From [USPS Publication 28 - Postal Addressing Standards](https://pe.usps.com/text/pub28/28apb.htm) and
        [IRS Zip Code and State Abbreviations](https://www.irs.gov/pub/irs-utl/zip_code_and_state_abbreviations.pdf).
        Includes codes for 50 states and District of Columbia plus:
          * AA - Armed Forces Americas (except Canada)
          * AE - Armed Forces Europe, Africa, the Middle East, and Canada
          * AP - Armed Forces Pacific
          * AS - American Samoa
          * FM - Federated States of Micronesia
          * GU - Guam
          * MH - Marshall Islands
          * MP - Northern Mariana Islands
          * PR - Puerto Rico
          * PW - Palau
          * VI - U.S. Virgin Islands
      type: string
      enum:
        - AA
        - AE
        - AK
        - AL
        - AP
        - AR
        - AS
        - AZ
        - CA
        - CO
        - CT
        - DC
        - DE
        - FL
        - FM
        - GA
        - GU
        - HI
        - IA
        - ID
        - IL
        - IN
        - KS
        - KY
        - LA
        - MA
        - MD
        - ME
        - MH
        - MI
        - MN
        - MO
        - MP
        - MS
        - MT
        - NC
        - ND
        - NE
        - NH
        - NJ
        - NM
        - NV
        - NY
        - OH
        - OK
        - OR
        - PA
        - PR
        - PW
        - RI
        - SC
        - SD
        - TN
        - TX
        - UT
        - VA
        - VI
        - VT
        - WA
        - WI
        - WV
        - WY

    String255:
      title: String 255
      description: String of maximum length 255
      type: string
      maxLength: 255

    String64:
      title: String 64
      description: String of maximum length 64
      type: string
      maxLength: 64

    TelephoneNetwork:
      title: Telephone Network
      description: The network technology used for this telephone.
        One of CELLULAR, LANDLINE, PAGER, SATELLITE, or VOIP
      type: string
      enum:
        - CELLULAR
        - LANDLINE
        - PAGER
        - SATELLITE
        - VOIP

    TelephoneNumberPurpose:
      title: Telephone Number Purpose
      description: Purpose of the telephone number, one of HOME, BUSINESS, PERSONAL,
        FAX, or BOTH. BOTH indicates number is used for both HOME and BUSINESS purposes.
        `CELL` value is deprecated in v6.3, replaced by TelephoneNetwork
      type: string
      enum:
        - BOTH
        - BUSINESS
        - CELL  # deprecated, replaced by a TelephoneNetwork value
        - FAX
        - HOME
        - PERSONAL

    Timestamp:
      title: Timestamp
      description: >-
        ISO 8601 date-time in format 'YYYY-MM-DDThh:mm:ss.nnn[Z|[+|-]hh:mm]' according to
        [IETF RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339.html#section-5.6)
      type: string
      format: date-time
      example: '2021-07-15T14:46:41.375Z'

  responses:
    ############################################################
    #
    # Standard error responses, among those defined in the latest
    # FDX API Specification document, section 6.2 Errors
    #
    ############################################################

    '400':
      description: Input sent by client does not satisfy API specification
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Invalid Input:
              value:
                code: '401'
                message: Invalid Input
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '401':
      description: Request lacks valid authentication credentials for the target resource
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Unauthorized:
              value:
                code: '603'
                message: Authentication failed
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '403':
      description: Forbidden, server understands the request but refuses to authorize it
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Forbidden:
              value:
                code: '403'
                message: Forbidden
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '404':
      description: Data not found for request parameters
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Data not found for request parameters:
              value:
                code: '1107'
                message: Data not found for request parameters
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '406':
      description: Content Type not Supported
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Content Type not Supported:
              value:
                code: '1203'
                message: Content Type not Supported
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '409':
      description: Conflict with current state of target resource
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Conflict:
              value:
                code: '409'
                message: Conflict with current state of target resource
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '500':
      description: Catch-all exception where request was not processed due to an internal outage/issue.
        Consider other more specific errors before using this error
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Internal server error:
              value:
                code: '500'
                message: Internal server error
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '501':
      description: Error when FdxVersion in Header is not one of those implemented at backend
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            FdxVersion not supported or not implemented:
              value:
                code: '1106'
                message: FdxVersion not supported or not implemented
                debugMessage: Data Provider's custom developer-level error details for troubleshooting

    '503':
      description: System is down for maintenance
      headers:
        x-fapi-interaction-id:
          $ref: '#/components/headers/x-fapi-interaction-id'
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          examples:
            Scheduled Maintenance:
              value:
                code: '503'
                message: Scheduled Maintenance
                debugMessage: Data Provider's custom developer-level error details for troubleshooting
