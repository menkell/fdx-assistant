openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Fraud API
  description: Financial Data Exchange V6.3.0 Fraud API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Fraud API
tags:
  - name: Fraud Notification
    description: Notify of suspected fraud
security:
  - OAuthFapi1Baseline: []
paths:
  ############################################################
  #
  # Fraud paths
  #
  ############################################################

  /fraud/suspected-incident:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    post:
      summary: Notify Data Provider of fraud
      description: Notify Data Provider of suspected fraud
      operationId: reportSuspectedFraudIncident
      tags:
        - Fraud Notification
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SuspectedFraudIncident'
            examples:
              RISK:
                value:
                  type: "RISK"
                  suspectedIncidentId: "0a318518-ca16-4e66-be76-865a632ea771"
                  reporter:
                    name: 'ABC Inc'
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'http://example.com'
                    logoUri: 'http://example.com'
                    registry: FDX
                    registeredEntityName: ABC
                    registeredEntityId: ABC123
      responses:
        '200':
          description: OK
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

  schemas:
    ############################################################
    #
    # Fraud entities
    #
    ############################################################

    SuspectedFraudIncident:
      title: Suspected Fraud Incident entity
      description: Notification of suspected fraud
      type: object
      properties:
        type:
          description: >-
            Extensible string enum identifying the type of suspected fraud.
            Initially this will always be set to "ACCOUNT_TAKEOVER".
            Additional values may be defined in the future
          type: string
          minLength: 1
          maxLength: 256
          example: "ACCOUNT_TAKEOVER"
        suspectedIncidentId:
          description: Unique identifier for the suspected fraud incident
          type: string
          minLength: 1
          maxLength: 256
          example: "0a318518-ca16-4e66-be76-865a632ea771"
        reason:
          description: Free text justification for suspecting fraud
          type: string
          minLength: 1
          maxLength: 256
          example: User-submitted identity data did not match account
        fiAttributes:
          type: array
          description: >-
            Array of financial institution-specific attributes. Can be used to
            provide additional structured context on the suspected fraud for the
            FI to use in determining a resolution
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'
        reporter:
          description: >-
            Identity of the party responsible for identifying and reporting the
            suspected fraud. This might be the DP, DAP, a vendor, a payment
            network, or other entity
          $ref: './fdxapi.components.yaml#/components/schemas/Party'
