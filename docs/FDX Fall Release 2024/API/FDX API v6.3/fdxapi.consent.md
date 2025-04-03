openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Consent API
  description: Financial Data Exchange V6.3.0 Consent API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Consent API
tags:
  - name: User Consent
    description: Manage customer consent grants
security:
  - OAuthFapi1Baseline: []
paths:
  ############################################################
  #
  # Consent paths
  #
  ############################################################

  /consents/{consentId}:
    parameters:
      - $ref: '#/components/parameters/ConsentIdPath'
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      summary: Get Consent Grant
      description: Get a Consent Grant
      operationId: getConsentGrant
      tags:
        - User Consent
      responses:
        '200':
          description: Ok
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConsentGrant'
              examples:
                (1) Single Resource:
                  value:
                    id: 9585694d3ae58863
                    status: ACTIVE
                    parties:
                      - name: Seedling App
                        type: DATA_RECIPIENT
                        homeUri: https://www.seedling.com
                        logoUri: https://www.seedling.com/assets/seedling-logo.png
                        registry: FDX
                        registeredEntityName: Oak Tree Holdings, Inc
                        registeredEntityId: 5493001052I34KDC1O18
                      - name: Midwest Primary Bank, NA
                        type: DATA_PROVIDER
                        homeUri: https://www.midwest.com
                        logoUri: https://www.midwest.com/81d88112572c.jpg
                        registry: GLEIF
                        registeredEntityName: Midwest Primary Bank, NA
                        registeredEntityId: 549300ATG070THRDJ595
                    createdTime: "2021-07-03T21:28:10.375Z"
                    expirationTime: "2021-07-03T22:28:10.374Z"
                    durationType: ONE_TIME
                    lookbackPeriod: 60
                    resources:
                      - resourceType: ACCOUNT
                        resourceId: b14e1e714693bc00
                        dataClusters:
                          - ACCOUNT_DETAILED
                          - TRANSACTIONS
                          - STATEMENTS
                (2) Multiple Resources:
                  value:
                    id: 0e67811f9c12468f
                    status: ACTIVE
                    parties:
                      - name: Seedling App
                        type: DATA_RECIPIENT
                        homeUri: https://www.seedling.com
                        logoUri: https://www.seedling.com/assets/seedling-logo.png
                        registry: GLEIF
                        registeredEntityName: Oak Tree Holdings, Inc
                        registeredEntityId: 5493001052I34KDC1O18
                      - name: Midwest Primary Bank, NA
                        type: DATA_PROVIDER
                        homeUri: https://www.midwest.com
                        logoUri: https://www.midwest.com/81d88112572c.jpg
                        registry: GLEIF
                        registeredEntityName: Midwest Primary Bank, NA
                        registeredEntityId: 549300ATG070THRDJ595
                    createdTime: "2021-07-03T22:08:10.375Z"
                    expirationTime: "2022-07-03T22:08:10.374Z"
                    durationType: TIME_BOUND
                    durationPeriod: 365
                    lookbackPeriod: 60
                    resources:
                      - resourceType: ACCOUNT
                        resourceId: b14e1e714693bc00
                        dataClusters:
                          - ACCOUNT_DETAILED
                          - TRANSACTIONS
                          - STATEMENTS
                      - resourceType: ACCOUNT
                        resourceId: ad6794161f45bc96
                        dataClusters:
                          - ACCOUNT_DETAILED
                          - TRANSACTIONS
                          - STATEMENTS
                      - resourceType: CUSTOMER
                        resourceId: aed694b22bc3d2b3
                        dataClusters:
                          - CUSTOMER_CONTACT
        '401':
          $ref: './fdxapi.components.yaml#/components/responses/401'
        '404':
          $ref: './fdxapi.components.yaml#/components/responses/404'

  /consents/{consentId}/revocation:
    parameters:
      - $ref: '#/components/parameters/ConsentIdPath'
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    put:
      summary: Revoke a Consent Grant
      description: Revoke a Consent Grant
      operationId: revokeConsentGrant
      tags:
        - User Consent
      requestBody:
        description: Reason and initiator of revocation
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ConsentRevocationRequest'
            examples:
              Standard Request:
                value:
                  reason: BUSINESS_RULE
                  initiator: DATA_ACCESS_PLATFORM
      responses:
        '204':
          description: No Content
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
        '400':
          $ref: './fdxapi.components.yaml#/components/responses/400'
        '401':
          $ref: './fdxapi.components.yaml#/components/responses/401'
        '403':
          $ref: './fdxapi.components.yaml#/components/responses/403'
        '404':
          $ref: './fdxapi.components.yaml#/components/responses/404'
        '409':
          $ref: './fdxapi.components.yaml#/components/responses/409'

    get:
      summary: Retrieve Consent Revocation record
      description: Retrieve Consent Revocation record
      operationId: getConsentRevocation
      tags:
        - User Consent
      responses:
        '200':
          description: Ok
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConsentRevocationList'

components:

  securitySchemes:
    ############################################################
    #
    # Security Schemes
    #
    ############################################################

    OAuthFapi1Baseline:
      $ref: './fdxapi.components.yaml#/components/securitySchemes/OAuthFapi1Baseline'

  parameters:
    ############################################################
    #
    # Consent parameters
    #
    ############################################################

    ConsentIdPath:
      name: consentId
      in: path
      description: Consent Identifier
      required: true
      schema:
        $ref: '#/components/schemas/ConsentId'
      example: '9585694d3ae58863'

  schemas:
    ############################################################
    #
    # Consent entities
    #
    ############################################################

    ConsentGrant:
      title: Consent Grant entity
      description: Record of user consent
      type: object
      properties:
        id:
          description: The persistent identifier of the consent
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        status:
          description: The current status of the consent
          $ref: '#/components/schemas/ConsentGrantStatus'
        parties:
          description: The non-end user parties participating in the Consent Grant
          type: array
          items:
            $ref: '#/components/schemas/ConsentGrantParty'
        createdTime:
          description: When the consent was initially granted
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
        expirationTime:
          description: When the consent grant will become expired
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
        updatedTime:
          description: When the consent grant was updated
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
        durationType:
          description: The type of duration of the consent
          $ref: './fdxapi.components.yaml#/components/schemas/ConsentDurationType'
        durationPeriod:
          description: The consent duration in days from day of original grant
          $ref: '#/components/schemas/ConsentDurationPeriod'
        lookbackPeriod:
          description: >-
            Period, in days, for which historical data may be requested;
            measured from request time, not grant time
          $ref: '#/components/schemas/LookbackPeriod'
        resources:
          description: The permissioned resource entities
          type: array
          items:
            $ref: '#/components/schemas/ConsentGrantResource'
        links:
          description: Links for related Consent Grant records
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'

    ConsentGrantParty:
      title: Consent Grant Party entity
      description: >-
        Details on the non-end user parties in the Consent Grant. Includes the
        legal entity operating branded products or services in the data sharing chain.
        Descriptive information is collected during Data Recipient registration at
        Data Provider, and populated during issuance by Data Provider from its registry
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/Party'
      required:
        - homeUri
        - registry
        - registeredEntityName
        - registeredEntityId

    ConsentGrantResource:
      title: Consent Grant Resource entity
      description: Entity of permissioned resources
      type: object
      properties:
        resourceType:
          description: Type of resource to be permissioned
          $ref: '#/components/schemas/ConsentResourceType'
        resourceId:
          description: Identifier of resource to be permissioned
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        dataClusters:
          description: Names of clusters of data elements permissioned
          type: array
          items:
            $ref: '#/components/schemas/DataCluster'
          minItems: 1
      required:
        - resourceType
        - resourceId
        - dataClusters

    ConsentRequest:
      title: Consent Request entity
      description: >-
        Details of request to create new consent grant.
        This schema is to be used in POST request to Data Provider's
        `POST /par` endpoint using the Pushed Authorization Request (PAR) method
      type: object
      properties:
        durationType:
          description: The type of duration of the consent
          $ref: './fdxapi.components.yaml#/components/schemas/ConsentDurationType'
        durationPeriod:
          description: The consent duration in days from day of original grant
          $ref: '#/components/schemas/ConsentDurationPeriod'
        lookbackPeriod:
          description: >-
            Period, in days, for which historical data may be requested;
            measured from request time, not grant time
          $ref: '#/components/schemas/LookbackPeriod'
        resources:
          description: The requested resource entities
          type: array
          items:
            $ref: '#/components/schemas/ConsentRequestedResource'

    ConsentRequestedResource:
      title: Consent Requested Resource entity
      description: Details of requested resource and data clusters
      type: object
      properties:
        resourceType:
          description: Type of resource permission requested
          $ref: '#/components/schemas/ConsentResourceType'
        dataClusters:
          description: Names of clusters of data elements requested
          type: array
          items:
            $ref: '#/components/schemas/DataCluster'
          minItems: 1
      required:
        - resourceType
        - dataClusters

    ConsentRevocation:
      title: Consent Revocation entity
      description: Details of request to revoke consent grant
      type: object
      properties:
        status:
          description: The status of the consent = REVOKED
          $ref: '#/components/schemas/ConsentGrantStatus'
        reason:
          description: The reason for consent revocation
          $ref: '#/components/schemas/ConsentUpdateReason'
        initiator:
          description: The party initiating consent revocation
          $ref: './fdxapi.components.yaml#/components/schemas/PartyType'
        updatedTime:
          description: When the consent grant was revoked
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'

    ConsentRevocationList:
      title: Consent Revocation List entity
      description: List of consent grant revocation requests
      type: object
      properties:
        revocations:
          description: The list of revocation requests
          type: array
          items:
            $ref: '#/components/schemas/ConsentRevocation'

    ConsentRevocationRequest:
      title: Consent revocation request entity
      description: Details of request to revoke consent grant
      type: object
      properties:
        reason:
          description: The reason for consent revocation
          $ref: '#/components/schemas/ConsentUpdateReason'
        initiator:
          description: The party initiating revocation
          $ref: './fdxapi.components.yaml#/components/schemas/PartyType'

    FdxTokenIntrospectionResponse:
      title: FDX OAuth Token Introspection Response
      summary: OAuth token-introspection response for use with opaque 'access_tokens'
      description: FDX response enabling transport of ConsentGrant details extended from
        [JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
      type: object
      properties:
        active:
          type: boolean
          description: Flag indicating whether 'ConsentGrant' is active
        iss:
          type: string
          description: >-
            Issuer claim 'iss' identifies the principal that issued the JWT.
            Contains a [StringOrURI](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        sub:
          type: string
          description: >-
            Subject claim 'sub' identifies the principal that is the subject of the JWT.
            Contains a [StringOrURI](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        aud:
          type: string
          description: >-
            Audience claim 'aud' identifies the recipients for whom the JWT is intended.
            May be a single StringOrURI value or an array of
            [StringOrURI](https://datatracker.ietf.org/doc/html/rfc7519#section-2) values
        exp:
          type: number
          description: >-
            Expiration Time claim 'exp' identifies the time on or after which the JWT MUST NOT be accepted
            Contains a number which is a [NumericDate](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        iat:
          type: number
          description: >-
            Issued At claim 'iat' identifies the time at which the JWT was issued.
            Contains a number which is a [NumericDate](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        jti:
          type: string
          description: >-
            JWT ID claim 'jti' provides a unique identifier for the JWT.
            Contains a case-sensitive string value
        client_id:
          type: string
          description: The unique client identifier for the Data Recipient granted the consent
        scope:
          type: string
          description: Space-delimited array of any number of scopes from those in FdxOauthScope,
            plus 'openid' and 'offline_access'
        fdxConsentId:
          $ref: '#/components/schemas/ConsentId'
          description: The unique identifier of the current user's active FDX 'ConsentGrant'

    JwtProfile:
      title: FDX JWT Profile
      description: FDX JWT Profile enabling transport of ConsentGrant details in OAuth 'access_token', extended from
                   [JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
      type: object
      properties:
        iss:
          type: string
          description: >-
            Issuer claim 'iss' identifies the principal that issued the JWT.
            Contains a [StringOrURI](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        sub:
          type: string
          description: >-
            Subject claim 'sub' identifies the principal that is the subject of the JWT.
            Contains a [StringOrURI](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        aud:
          type: string
          description: >-
            Audience claim 'aud' identifies the recipients for whom the JWT is intended.
            May be a single StringOrURI value or an array of
            [StringOrURI](https://datatracker.ietf.org/doc/html/rfc7519#section-2) values
        exp:
          type: number
          description: >-
            Expiration Time claim 'exp' identifies the time on or after which the JWT MUST NOT be accepted
            Contains a number which is a [NumericDate](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        iat:
          type: number
          description: >-
            Issued At claim 'iat' identifies the time at which the JWT was issued.
            Contains a number which is a [NumericDate](https://datatracker.ietf.org/doc/html/rfc7519#section-2) value
        jti:
          type: string
          description: >-
            JWT ID claim 'jti' provides a unique identifier for the JWT.
            Contains a case-sensitive string value
        client_id:
          type: string
          description: The unique client identifier for the Data Recipient granted the consent
        scope:
          type: string
          description: Space-delimited array of any number of scopes from those in FdxOauthScope,
            plus 'openid' and 'offline_access'
        fdxConsentId:
          $ref: '#/components/schemas/ConsentId'
          description: The unique identifier of the current user's active FDX 'ConsentGrant'

    ############################################################
    #
    # Consent data types
    #
    ############################################################

    ConsentDurationPeriod:
      title: Consent Duration Period
      description: Consent duration, in days, from day of original grant
      type: integer

    ConsentGrantStatus:
      title: Consent Grant Status
      description: Current status of Consent Grant
      type: string
      enum:
        - ACTIVE
        - EXPIRED
        - REVOKED

    ConsentId:
      title: Consent Identifier
      description: Unique ID for a consent grant
      $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

    ConsentResourceType:
      title: Consent Resource Type
      description: >-
        Resource for which data may be permissioned;
        can be extended to support additional types of resources
      type: string
      enum:
        - ACCOUNT
        - CUSTOMER
        - DOCUMENT

    ConsentUpdateReason:
      title: Consent Update Reason
      description: Reason for Updating a Consent Grant
      type: string
      enum:
        - BUSINESS_RULE
        - USER_ACTION

    DataCluster:
      title: Data Cluster
      description: >-
        Name of permissioned Data Cluster. For Data Cluster definitions refer
        to the Consent Components > Data Clusters section of the
        User Experience Guidelines document included in the FDX API.
        `ACCOUNT_PAYMENTS` is deprecated and replaced with `PAYMENT_SUPPORT`
        in FDX release V6.1.0, `ACCOUNT_PAYMENTS` will be removed with V7 release
      type: string
      enum:
        - ACCOUNT_BASIC
        - ACCOUNT_DETAILED
        - ACCOUNT_PAYMENTS  # Deprecated
        - BILLS
        - CUSTOMER_CONTACT
        - CUSTOMER_PERSONAL
        - IMAGES
        - INVESTMENTS
        - NOTIFICATIONS
        - PAYMENT_SUPPORT
        - REWARDS
        - STATEMENTS
        - TAX
        - TRANSACTIONS

    LookbackPeriod:
      title: Lookback Period
      description: >-
        Period, in days, for which historical data may be requested;
        period is measured from request time, not grant time
      type: integer
