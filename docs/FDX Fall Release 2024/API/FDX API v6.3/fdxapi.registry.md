openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Registry API
  description: Financial Data Exchange V6.3.0 Registry API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.registryhost.com/fdx/v6'
    description: Financial Data Exchange V6 Registry API
tags:
  - name: Recipients
    description: Manage recipients
security:
  - OAuthFapi1Baseline: []

paths:
  ############################################################
  #
  # Recipient Registry paths
  #
  ############################################################

  /recipients:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      summary: Get Recipients
      operationId: getRegistryRecipients
      description: Get recipients
      tags:
        - Recipients
      parameters:
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: OK
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RegistryRecipients'
              examples:
                Example retrieval of a list of recipient records from the ecosystem registry:
                  value:
                    page:
                      nextOffset: nextoffset
                      prevOffset: prevoffset
                      total: 5000
                    links:
                      next:
                        href: /recipients?offset=nextoffset
                      prev:
                        href: /recipients?offset=prevoffset
                    recipients:
                      - recipient_id: '12345'
                        client_name: My Example Client
                        redirect_uris:
                          - 'https://partner.example/callback'
                        description: Recipient Application servicing financial use case requiring permissioned data sharing
                        logo_uri: 'https://client.example1.org/logo.png'
                        client_uri: 'https://example1.net/'
                        contacts:
                          - support@example1.net
                        scope: fdx:accountbasic:read fdx:transactions:read fdx:investments:read
                        duration_type:
                          - TIME_BOUND
                        duration_period: 365
                        lookback_period: 365
                        registry_references:
                          - registered_entity_name: Official recipient name
                            registered_entity_id: 4HCHXIURY78NNH6JH
                            registry: GLEIF
                      - recipient_id: '23456'
                        client_name: Another Example Client
                        redirect_uris:
                          - 'https://partner.example/callback'
                        description: Recipient Application servicing financial use case requiring permissioned data sharing
                        logo_uri: 'https://client.example2.org/logo.png'
                        client_uri: 'https://example2.net/'
                        contacts:
                          - support@example2.net
                        scope: fdx:accountbasic:read fdx:investments:read
                        duration_type:
                          - TIME_BOUND
                        duration_period: 365
                        lookback_period: 365
                        registry_references:
                          - registered_entity_name: Official recipient name
                            registered_entity_id: 8XKSJGEU2465KSOGI
                            registry: GLEIF

  /recipients/{recipientId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      summary: Get Recipient by Id
      operationId: getRegistryRecipient
      description: Get a specific recipient
      tags:
        - Recipients
      parameters:
        - $ref: '#/components/parameters/RecipientIdPath'
      responses:
        '200':
          description: OK
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RegistryRecipient'
              examples:
                Example retrieval of a recipient record from the ecosystem registry:
                  value:
                    recipient_id: '12345'
                    client_name: My Example Client
                    redirect_uris:
                      - 'https://partner.example/callback'
                    description: Recipient Application servicing financial use case requiring permissioned data sharing
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
    # Recipient Registry request parameters
    #
    ############################################################

    RecipientIdPath:
      name: recipientId
      in: path
      description: Recipient Identifier. Uniquely identifies a Recipient
      required: true
      schema:
        $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

  schemas:
    ############################################################
    #
    # Recipient Registry data entities
    #
    ############################################################

    RegistryRecipient:
      title: Recipient record at ecosystem registry
      type: object
      description: >-
        Record of Recipient at the Ecosystem Registry.
        Properties in this structure use 'snake_case' names to match
        the properties in [IETF RFC 7591](https://datatracker.ietf.org/doc/rfc7591/).
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/RecipientRequest'
        - type: object
          properties:
            recipient_id:
              type: string
              description: Recipient Id at ecosystem registry
      required:
        - recipient_id

    RegistryRecipients:
      title: Recipient records at ecosystem registry
      type: object
      description: >-
        Recipient records at Ecosystem Registry.
        Properties in this structure use 'snake_case' names to match
        the properties in [IETF RFC 7591](https://datatracker.ietf.org/doc/rfc7591/).
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            recipients:
              type: array
              items:
                $ref: '#/components/schemas/RegistryRecipient'
              description: Recipients retrieved by the operation
      required:
        - recipients
