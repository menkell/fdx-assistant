openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Resource API
  description: Financial Data Exchange V6.3.0 Resource API
  #################################################################################################
  #
  # This OpenAPI document is provided by FDX for use in creating a new API for a to-be-defined
  # Resource following the FDX standards for an FDX proposal--or for your own API needs.
  #
  # After copying this source template, rename the generic "Resource" and "resource" paths, tags,
  # schemas, components and properties to match the Resource(s) which the API will support.
  #
  # Search below for #template to find the important areas to edit.
  #
  #################################################################################################
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Resource API
tags:
  # #template - Update tag name and description
  - name: Resource Information
    description: Search, view and update resources
security:
  - OAuthFapi1Baseline: []

paths:
  ############################################################
  #
  # Paths
  #
  ############################################################

  # #template - Update each of the /resources paths, operationIds, description and summary
  /resources:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getResources
      tags:
        - Resource Information
      description: Retrieve all the resources
      summary: Get all the resource entities
      #############################################################################################
      #
      # This path, with no search parameters or POST request payload, would be used to retrieve all
      # occurrences of the queried resources. For example, see `/certification-metrics` endpoint in
      # the FDX API file `fdxapi.meta.yaml`.
      #
      # By adding search query parameters or a POST request payload, this can become a filtering
      # service to search for specific resources matching the request criteria. For example, see
      # `/accounts` endpoint in the FDX API file `fdxapi.core.yaml` which takes `accountId` as a
      # parameter, among other things. For search, this path's descriptive items would look like:
      #
      # operationId: searchForResources
      # tags:
      #   - Resource Information
      # description: Search for resources
      # summary: Search for matching resources
      #
      #############################################################################################
      parameters:
        - $ref: './fdxapi.components.yaml#/components/parameters/ResultTypeQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/StartDateQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/EndDateQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/PageKeyQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
      responses:
        # #template - Update successful response and (where needed) error responses
        '200':
          description: List of resources found
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResourceList'
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

  # #template - Update each of the /resources paths, operationIds, description and summary
  /resources/{resourceId}:
    parameters:
      - $ref: '#/components/parameters/ResourceIdPath'
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    get:
      operationId: getResource
      tags:
        - Resource Information
      description: Retrieve the details of the identified resource
      summary: Get the specific resource detail
      responses:
        # #template - Update successful response and (where needed) error responses
        '200':
          description: Details of the specific resource
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Resource'
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
                    message: Resource ID is required
                    debugMessage: Custom developer-level error details for troubleshooting
        '404':
          description: Resource with provided ID was not found
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
                    code: 'Code TBD for Resource ID'
                    message: Resource not found
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
    # Security schemes
    #
    ############################################################

    OAuthFapi1Baseline:
      $ref: './fdxapi.components.yaml#/components/securitySchemes/OAuthFapi1Baseline'

    OAuthFapi1Advanced:
      $ref: './fdxapi.components.yaml#/components/securitySchemes/OAuthFapi1Advanced'

  parameters:
    ############################################################
    #
    # Parameters
    #
    ############################################################

    # #template - Update parameter name to match the id name of your resource
    ResourceIdPath:
      name: resourceId
      in: path
      description: Specific resourceId for which to retrieve details
      required: true
      schema:
        $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

  schemas:
    ############################################################
    #
    # Data entities
    #
    ############################################################

    # #template - Update all the defined entity and property names to match your resource
    Resource:
      title: Resource entity
      description: Details of resource entity
      type: object
      properties:
        # #template - Update the id name of your resource
        resourceId:
          description: Long-term persistent identifier for the Resource
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        status:
          description: Status of Resource
          $ref: '#/components/schemas/ResourceStatus'
        description:
          description: Description of resource
          type: string
        links:
          description: Links to retrieve this resource, or to invoke other APIs
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLinks'

    ResourceList:
      title: Resource List entity
      description: Response object for /resources API
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            responseType:
              description: Indicates whether response array of `lightweight` resource summaries
                or of `detail` full resources is being returned
              $ref: './fdxapi.components.yaml#/components/schemas/ResultType'
            summaries:
              description: Zero or more Resource Summaries
              type: array
              items:
                $ref: '#/components/schemas/ResourceSummary'
            resources:
              description: Zero or more Resources
              type: array
              items:
                $ref: '#/components/schemas/Resource'

    ResourceSummary:
      title: Resource Summary entity
      description: High level summary of resource entity
      type: object
      properties:
        # #template - Update the id name of your resource
        resourceId:
          description: Long-term persistent identifier for the Resource
          $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
        status:
          description: Status of Resource
          $ref: '#/components/schemas/ResourceStatus'

    ############################################################
    #
    # Data types
    #
    ############################################################

    ResourceStatus:
      title: Resource Status
      description: Statuses for resource
      type: string
      enum:
        - ACTIVE
        - IN_PROGRESS
        - RETIRED
