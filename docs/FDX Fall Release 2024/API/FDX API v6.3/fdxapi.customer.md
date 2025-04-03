openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Customer API
  description: Financial Data Exchange V6.3.0 Customer API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Customer API
tags:
  - name: Personal Information
    description: Search and view customer or customers
paths:

  ############################################################
  #
  # Common paths
  #
  ############################################################

  /customers:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getCustomers
      tags:
        - Personal Information
      description: Retrieve account holders related to permissioned accounts
      summary: Retrieve customers
      parameters:
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        '200':
          description: Customers
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Customers'

  /customers/current:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getCustomerInfo
      tags:
        - Personal Information
      description: Get information about the customer within the authorization scope
      summary: Get current authenticated customer information
      responses:
        '200':
          description: Data describing current authenticated customer
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Customer'

  /customers/{customerId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getCustomer
      tags:
        - Personal Information
      description: Retrieve customer information by customer id
      summary: Customer by id
      parameters:
        - name: customerId
          in: path
          description: Customer Identifier
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Customer
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Customer'
        '404':
          description: Customer with id not found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Customer not found:
                  value:
                    code: '601'
                    message: Customer not found
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

  parameters: {}

  schemas:
    ############################################################
    #
    # Common data entities
    #
    ############################################################

    Customers:
      title: Customers Entity
      description: List of customers
      type: object
      properties:
        page:
          $ref: './fdxapi.components.yaml#/components/schemas/PageMetadata'
          description: Information required to paginate results
        links:
          $ref: './fdxapi.components.yaml#/components/schemas/PageMetadataLinks'
          description: Links used to paginate results
        customers:
          type: array
          items:
            $ref: './fdxapi.components.yaml#/components/schemas/Customer'
          description: Array of customers
