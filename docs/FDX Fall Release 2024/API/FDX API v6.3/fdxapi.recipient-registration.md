openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Recipient API
  description: Financial Data Exchange V6.3.0 Recipient API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Recipient API
tags:
  - name: Recipients
    description: Manage recipients
security:
  - OAuthFapi1Baseline: []
paths:
  ############################################################
  #
  # Recipient Registration paths
  #
  ############################################################

  /register:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    post:
      summary: Recipient Registration Request
      description: Request to Register Recipient by Creating a Recipient Record
      operationId: createRecipient
      tags:
        - Recipients
      requestBody:
        content:
          application/json:
            schema:
              $ref: './fdxapi.components.yaml#/components/schemas/RecipientRequest'
            examples:
              Create Recipient Record at Provider:
                value:
                  client_name: My Example Client
                  description: Recipient Application servicing financial use case requiring permissioned data sharing
                  redirect_uris:
                    - 'https://partner.example/callback'
                  logo_uri: 'https://client.example.org/logo.png'
                  client_uri: 'https://example.net/'
                  contacts:
                    - support@example.net
                  scope: fdx:accountbasic:read fdx:transactions:read fdx:investments:read
                  duration_type:
                    - TIME_BOUND
                  duration_period: 365
                  lookback_period: 365
                  registry_references:
                    - registered_entity_name: Official recipient name
                      registered_entity_id: 4HCHXIURY78NNH6JH
                      registry: GLEIF
                  intermediaries:
                    - name: Data Access Platform Name
                      description: Data Access Platform specializing in servicing permissioned data sharing for Data Recipients
                      uri: 'https://partner.example/'
                      logo_uri: 'https://partner.example/logo.png'
                      contacts:
                        - support@partner.com
                      registry_references:
                        - registered_entity_name: Data Access Platform listed company Name
                          registered_entity_id: JJH7776512TGMEJSG
                          registry: FDX
                    - name: Digital Service Provider Name
                      description: Digital Service Provider to the Recipient
                      uri: 'https://sub-partner-one.example/'
                      logo_uri: 'https://sub-partner-one.example/logo.png'
                      contacts:
                        - support@sub-partner-one.com
                      registry_references:
                        - registered_entity_name: Service Provider listed company Name
                          registered_entity_id: 9LUQNDG778LI9D1
                          registry: GLEIF
      responses:
        '201':
          description: Created
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Recipient'
              examples:
                Provider Response With Full Record Of Recipient:
                  value:
                    client_id: V8tvEkZWhDAdxSaKGUJZ
                    client_secret: SpsuwZIxnp8bBEhp5sk1EKiIKTZ4X4DKU
                    grant_types:
                      - authorization_code
                      - refresh_token
                    token_endpoint_auth_method: private_key_jwt
                    registration_client_uri: 'https://server.example.com/register/V8tvEkZWhDAdxSaKGUJZ'
                    status: Approved
                    registration_access_token: V8tvEkZWhDAdxSaKGUJZ
                    client_name: My Example Client
                    description: Recipient Application servicing financial use case requiring permissioned data sharing
                    redirect_uris:
                      - 'https://partner.example/callback'
                    logo_uri: 'https://client.example.org/logo.png'
                    client_uri: 'https://example.net/'
                    contacts:
                      - support@example.net
                    scope: fdx:accountbasic:read fdx:transactions:read fdx:investments:read
                    duration_type:
                      - TIME_BOUND
                    duration_period: 365
                    lookback_period: 365
                    registry_references:
                      - registered_entity_name: Official recipient name
                        registered_entity_id: 4HCHXIURY78NNH6JH
                        registry: GLEIF
                    intermediaries:
                      - name: Data Access Platform Name
                        description: Data Access Platform specializing in servicing permissioned data sharing for Data Recipients
                        uri: 'https://partner.example/'
                        logo_uri: 'https://partner.example/logo.png'
                        contacts:
                          - support@partner.com
                        registry_references:
                          - registered_entity_name: Data Access Platform listed company Name
                            registered_entity_id: JJH7776512TGMEJSG
                            registry: FDX
                      - name: Digital Service Provider Name
                        description: Digital Service Provider to the Recipient
                        uri: 'https://sub-partner-one.example/'
                        logo_uri: 'https://sub-partner-one.example/logo.png'
                        contacts:
                          - support@sub-partner-one.com
                        registry_references:
                          - registered_entity_name: Service Provider listed company Name
                            registered_entity_id: 9LUQNDG778LI9D1
                            registry: GLEIF

  /register/{clientId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
      - $ref: '#/components/parameters/ClientIdPath'
    get:
      summary: Get Recipient
      operationId: getRecipient
      tags:
        - Recipients
      description: Get a specific recipient data identified with clientId
      responses:
        '200':
          description: OK
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Recipient'
    put:
      summary: Update a Recipient
      operationId: updateRecipient
      tags:
        - Recipients
      description: Update data for a specific recipient identified with clientId
      requestBody:
        content:
          application/json:
            schema:
              $ref: './fdxapi.components.yaml#/components/schemas/RecipientRequest'
            examples:
              Update to same Recipient Record:
                value:
                  client_name: My Example Client
                  description: Recipient Application servicing financial use case requiring permissioned data sharing
                  redirect_uris:
                    - 'https://partner.example/callback'
                  logo_uri: 'https://client.example.org/logo.png'
                  client_uri: 'https://example.net/'
                  contacts:
                    - support@example.net
                  scope: fdx:accountbasic:read fdx:transactions:read fdx:investments:read
                  duration_type:
                    - TIME_BOUND
                  duration_period: 365
                  lookback_period: 365
                  registry_references:
                    - registered_entity_name: Official recipient name
                      registered_entity_id: 4HCHXIURY78NNH6JH
                      registry: GLEIF
                  intermediaries:
                    - name: Data Access Platform Name
                      description: Data Access Platform specializing in servicing permissioned data sharing for Data Recipients
                      uri: 'https://partner.example/'
                      logo_uri: 'https://partner.example/logo.png'
                      contacts:
                        - support@partner.com
                      registry_references:
                        - registered_entity_name: Data Access Platform listed company Name
                          registered_entity_id: JJH7776512TGMEJSG
                          registry: FDX
                    - name: Digital Service Provider Name
                      description: Digital Service Provider to the Recipient
                      uri: 'https://sub-partner-one.example/'
                      logo_uri: 'https://sub-partner-one.example/logo.png'
                      contacts:
                        - support@sub-partner-one.com
                      registry_references:
                        - registered_entity_name: Service Provider listed company Name
                          registered_entity_id: 9LUQNDG778LI9D1
                          registry: GLEIF
      responses:
        '200':
          description: OK
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Recipient'
    delete:
      summary: Delete Recipient
      operationId: deleteRecipient
      tags:
        - Recipients
      description: Delete data for a specific recipient identified with clientId
      responses:
        '204':
          description: No Content
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'

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
    # Recipient Registration request parameters
    #
    ############################################################

    ClientIdPath:
      name: clientId
      in: path
      description: Client Identifier. Uniquely identifies a Client
      required: true
      schema:
        $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

  schemas:
    ############################################################
    #
    # Recipient Registration data entities
    #
    ############################################################

    Recipient:
      title: Recipient Provider
      type: object
      description: >-
        Record of Recipient at the Provider.
        Properties in this structure use 'snake_case' names to match
        the properties in [IETF RFC 7591](https://datatracker.ietf.org/doc/rfc7591/)
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/RecipientRequest'
        - type: object
          properties:
            client_id:
              type: string
              description: OAuth 2.0 client identifier.  Unique ID representing Data Recipient and Identity Chain combination
            client_secret:
              type: string
              description: OAuth 2.0 client secret string
            grant_types:
              type: array
              items:
                type: string
              description: Array of OAuth 2.0 grants made available to the Data Recipient
            token_endpoint_auth_method:
              type: string
              description: Requested Authentication method for Authorization Server
            registration_client_uri:
              type: string
              format: uri
              description: Fully qualified URI for subsequent DCR calls (GET, PUT, DELETE) for managing the Data Recipient registration
            status:
              type: string
              description: Status of FDX OAuth 2.0 extension
            registration_access_token:
              type: string
              description: String containing a unique DCR access token to be used in subsequent operations to manage the Data Recipient
      required:
        - client_id
        - status
        - grant_types
        - token_endpoint_auth_method
