openapi: 3.1.0
info:
  version: '6.3.0'
  title: FDX V6.3.0 Event Publication and Subscription API
  description: Financial Data Exchange V6.3.0 Event Publication and Subscription API
  contact:
    name: Financial Data Exchange
    url: 'https://financialdataexchange.org/'
    email: fdxsupport@financialdataexchange.org
  license:
    name: FDX API License Agreement (11-13-2019)
    url: 'https://financialdataexchange.org/common/Uploaded%20files/Policies/FDX%20API%20License%20Agreement-(11-13-2019).pdf'
servers:
  - url: 'https://api.fi.com/fdx/v6'
    description: Financial Data Exchange V6 Event Publication and Subscription API
tags:
  - name: Event Notifications
    description: Manage Event Notifications
security:
  - OAuthFapi1Baseline: []
paths:
  ############################################################
  #
  # Event Notifications paths
  #
  ############################################################

  /notification-subscriptions:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    post:
      summary: Create a notification subscription
      operationId: createNotificationSubscription
      description: Creates notification subscription entry on the server
      tags:
        - Event Notifications
      requestBody:
        description: Notification subscription
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NotificationSubscription'
            examples:
              Create Consent Revoked Notification:
                value:
                  type: CONSENT_REVOKED
                  category: CONSENT
                  callbackUrl: 'https://abc.com/notification'
                  subscriber:
                    name: ABC Inc
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'https://abc.com/logo'
                    logoUri: 'https://abc.com/logo'
                    registry: FDX
                    registeredEntityName: ABC
                    registeredEntityId: ABC123
                  effectiveDate: '2021-11-24'
                  subscriptionId: GUID-SubscriptionId1
              Account Takeover Subscription:
                value:
                  type: RISK
                  category: FRAUD
                  callbackUrl: 'https://abc.com/notification'
                  subscriber:
                    name: ABC Inc
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'https://abc.com/logo'
                    logoUri: 'https://abc.com/logo'
                    registry: FDX
                    registeredEntityName: ABC
                    registeredEntityId: ABC123
                  effectiveDate: '2021-11-24'
                  subscriptionId: GUID-0a318518-ca16-4e66-1234
      responses:
        '201':
          description: Created
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotificationSubscription'
              examples:
                Consent Revoked Notification created:
                  value:
                    type: CONSENT_REVOKED
                    category: CONSENT
                    callbackUrl: 'https://abc.com/notification'
                    subscriber:
                      name: ABC Inc
                      type: DATA_ACCESS_PLATFORM
                      homeUri: 'https://abc.com/logo'
                      logoUri: 'https://abc.com/logo'
                      registry: FDX
                      registeredEntityName: ABC
                      registeredEntityId: ABC123
                    effectiveDate: '2021-11-24'
                    subscriptionId: GUID-SubscriptionId2
        '400':
          $ref: './fdxapi.components.yaml#/components/responses/400'
        '401':
          $ref: './fdxapi.components.yaml#/components/responses/401'
        '405':
          description: Method Not Allowed
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Method Not Allowed:
                  value:
                    code: '1206'
                    message: Method Not Allowed
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '429':
          description: Too Many Requests
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Too Many Requests:
                  value:
                    code: '1207'
                    message: Too Many Requests
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /notification-subscriptions/{subscriptionId}:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
      - $ref: '#/components/parameters/SubscriptionIdPath'
    get:
      summary: Get a notification subscription
      operationId: getNotificationSubscription
      description: Call to get notification subscription
      tags:
        - Event Notifications
      responses:
        '200':
          description: OK
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotificationSubscription'
              examples:
                Notification Subscription by ID success response:
                  value:
                    type: CONSENT_REVOKED
                    category: CONSENT
                    callbackUrl: 'https://abc.com/notification'
                    subscriber:
                      name: ABC Inc
                      type: DATA_ACCESS_PLATFORM
                      homeUri: 'https://abc.com/logo'
                      logoUri: 'https://abc.com/logo'
                      registry: FDX
                      registeredEntityName: ABC
                      registeredEntityId: ABC123
                    effectiveDate: '2021-11-24'
                    subscriptionId: GUID-SubscriptionId2
        '400':
          $ref: './fdxapi.components.yaml#/components/responses/400'
        '401':
          $ref: './fdxapi.components.yaml#/components/responses/401'
        '405':
          description: Method Not Allowed
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Method Not Allowed:
                  value:
                    code: '1206'
                    message: Method Not Allowed
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '429':
          description: Too Many Requests
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Too Many Requests:
                  value:
                    code: '1207'
                    message: Too Many Requests
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

    delete:
      summary: Delete a notification subscription
      operationId: deleteNotificationSubscription
      description: Delete a notification subscription
      tags:
        - Event Notifications
      responses:
        '204':
          description: No Content
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
        '400':
          description: Bad Request
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
        '401':
          $ref: './fdxapi.components.yaml#/components/responses/401'
        '405':
          description: Method Not Allowed
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Method Not Allowed:
                  value:
                    code: '1206'
                    message: Method Not Allowed
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '429':
          description: Too Many Requests
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Too Many Requests:
                  value:
                    code: '1207'
                    message: Too Many Requests
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'

  /notifications:
    parameters:
      - $ref: './fdxapi.components.yaml#/components/parameters/FapiInteractionIdHeader'
      - $ref: './fdxapi.components.yaml#/components/parameters/FdxApiActorTypeHeader'
    post:
      summary: Publish a notification
      operationId: publishNotification
      description: Publish Notification
      tags:
        - Event Notifications
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Notification'
            examples:
              Publish Consent Revoked Notification:
                value:
                  notificationId: 'req123456-GUID'
                  type: CONSENT_REVOKED
                  sentOn: '2021-07-15T14:46:41.375Z'
                  category: SECURITY
                  severity: EMERGENCY
                  priority: HIGH
                  publisher:
                    name: 'XYZ Inc'
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'http://example.com'
                    logoUri: 'http://example.com'
                    registry: FDX
                    registeredEntityName: XYZ
                    registeredEntityId: xyz1234
                  subscriber:
                    name: 'ABC Inc'
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'http://example.com'
                    logoUri: 'http://example.com'
                    registry: FDX
                    registeredEntityName: ABC
                    registeredEntityId: ABC123
                  notificationPayload:
                    id: 'ConsentID-1'
                    idType: CONSENT
                    customFields:
                      name: INITIATOR
                      value: INDIVIDUAL
                  url:
                    href: 'https://api.xyz.com/fdx/v6/consents/ConsentID-1/revocation'
                    action: GET
                    rel: consent
                    types:
                      - application/json
              Publish Consent Updated Notification:
                value:
                  notificationId: 'req123457-GUID'
                  type: CONSENT_UPDATED
                  sentOn: '2022-04-15T14:46:41.375Z'
                  category: CONSENT
                  severity: EMERGENCY
                  priority: HIGH
                  publisher:
                    name: 'XYZ Inc'
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'http://example.com'
                    logoUri: 'http://example.com'
                    registry: FDX
                    registeredEntityName: XYZ
                    registeredEntityId: xyz1234
                  subscriber:
                    name: 'ABC Inc'
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'http://example.com'
                    logoUri: 'http://example.com'
                    registry: FDX
                    registeredEntityName: ABC
                    registeredEntityId: ABC123
                  notificationPayload:
                    id: '9585694d3ae58863'
                    idType: CONSENT
                    customFields:
                      name: INITIATOR
                      value: INDIVIDUAL
                  url:
                    href: 'https://api.xyz.com/fdx/v5/consents/9585694d3ae58863'
                    action: GET
                    rel: consent
                    types:
                      - application/json
              Publish Account Takeover Notification:
                value:
                  notificationId: '0a318518-ca16-4e66-1234'
                  type: RISK
                  sentOn: '2021-07-15T14:46:41.375Z'
                  category: FRAUD
                  severity: EMERGENCY
                  priority: HIGH
                  publisher:
                    name: 'XYZ Inc'
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'http://example.com'
                    logoUri: 'http://example.com'
                    registry: FDX
                    registeredEntityName: XYZ
                    registeredEntityId: xyz1234
                  subscriber:
                    name: 'ABC Inc'
                    type: DATA_ACCESS_PLATFORM
                    homeUri: 'http://example.com'
                    logoUri: 'http://example.com'
                    registry: FDX
                    registeredEntityName: ABC
                    registeredEntityId: ABC123
                  notificationPayload:
                    id: '0a318518-ca16-4e66-be76-865a632ea771'
                    idType: ACCOUNT
                  url:
                    href: 'https://api.xyz.com/fdx/v4/notifications?dataRecipientId=FIREFLY'
                    action: GET
                    rel: notification
                    types:
                      - application/json
      responses:
        '204':
          description: No Content
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
        '405':
          description: Method Not Allowed
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Method Not Allowed:
                  value:
                    code: '1206'
                    message: Method Not Allowed
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '429':
          description: Too Many Requests
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Too Many Requests:
                  value:
                    code: '1207'
                    message: Too Many Requests
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '500':
          $ref: './fdxapi.components.yaml#/components/responses/500'
        '501':
          $ref: './fdxapi.components.yaml#/components/responses/501'
        '503':
          $ref: './fdxapi.components.yaml#/components/responses/503'
    get:
      summary: Retrieve notifications for a Data Access Platform (DAP) or Data Recipient (DR)
      operationId: getNotifications
      description: Get Notifications
      tags:
        - Event Notifications
      parameters:
        - $ref: './fdxapi.components.yaml#/components/parameters/LimitQuery'
        - $ref: './fdxapi.components.yaml#/components/parameters/OffsetQuery'
        - name: dataRecipientId
          in: query
          description: ID of Data Recipient (DR), omit for all DRs of a Data Access Platform
          required: false
          schema:
            $ref: './fdxapi.components.yaml#/components/schemas/Identifier'
      responses:
        '200':
          description: OK
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Notifications'
              examples:
                Risk Notification for DR:
                  value:
                    notifications:
                      - notificationId: '0a318518-ca16-4e66-1234'
                        type: RISK
                        sentOn: '2021-07-15T14:46:41.375Z'
                        category: FRAUD
                        severity: EMERGENCY
                        priority: HIGH
                        publisher:
                          name: 'XYZ Inc'
                          type: DATA_ACCESS_PLATFORM
                          homeUri: 'http://example.com'
                          logoUri: 'http://example.com'
                          registry: FDX
                          registeredEntityName: XYZ
                          registeredEntityId: xyz1234
                        subscriber:
                          name: 'ABC Inc'
                          type: DATA_ACCESS_PLATFORM
                          homeUri: 'http://example.com'
                          logoUri: 'http://example.com'
                          registry: FDX
                          registeredEntityName: ABC
                          registeredEntityId: ABC123
                        notificationPayload:
                          id: '0a318518-ca16-4e66-be76-865a632ea771'
                          idType: ACCOUNT
                        url:
                          href: 'https://api.xyz.com/fdx/v4/notifications?dataRecipientId=FIREFLY'
                          action: GET
                          rel: notification
                          types:
                            - application/json
        '405':
          description: Method Not Allowed
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Method Not Allowed:
                  value:
                    code: '1206'
                    message: Method Not Allowed
                    debugMessage: Provider custom developer-level error details for troubleshooting
        '429':
          description: Too Many Requests
          headers:
            x-fapi-interaction-id:
              $ref: './fdxapi.components.yaml#/components/headers/x-fapi-interaction-id'
          content:
            application/json:
              schema:
                $ref: './fdxapi.components.yaml#/components/schemas/Error'
              examples:
                Too Many Requests:
                  value:
                    code: '1207'
                    message: Too Many Requests
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

    OAuthFapi1Baseline:
      $ref: './fdxapi.components.yaml#/components/securitySchemes/OAuthFapi1Baseline'

  parameters:
    ############################################################
    #
    # Event Notifications request parameters
    #
    ############################################################

    SubscriptionIdPath:
      name: subscriptionId
      in: path
      description: ID of notification subscription
      required: true
      schema:
        $ref: './fdxapi.components.yaml#/components/schemas/Identifier'

  schemas:
    ############################################################
    #
    # Event Notifications entities
    #
    ############################################################

    Notification:
      title: Notification entity
      description: Provides the base fields of a notification. Clients will read the
                   `type` property to determine the expected notification payload
      type: object
      properties:
        notificationId:
          type: string
          description: Id of notification
        type:
          $ref: '#/components/schemas/NotificationType'
          description: Type of notification
        sentOn:
          $ref: './fdxapi.components.yaml#/components/schemas/Timestamp'
          description: Time notification was sent
        category:
          $ref: '#/components/schemas/NotificationCategory'
          description: Category of notification
        severity:
          $ref: '#/components/schemas/NotificationSeverity'
          description: Notification severity
        priority:
          $ref: '#/components/schemas/NotificationPriority'
          description: Notification priority
        publisher:
          $ref: './fdxapi.components.yaml#/components/schemas/Party'
          description: Publisher of notification
        subscriber:
          $ref: './fdxapi.components.yaml#/components/schemas/Party'
          description: Subscriber to this notification
        notificationPayload:
          $ref: '#/components/schemas/NotificationPayload'
          description: Notification-specific key-value paired data
        url:
          $ref: './fdxapi.components.yaml#/components/schemas/HateoasLink'
          description: URL to retrieve further details related to notification
      required:
        - notificationId
        - type
        - sentOn
        - category
        - publisher
        - notificationPayload

    NotificationPayload:
      title: Notification Payload entity
      description: Custom key-value pairs payload for a notification
      type: object
      properties:
        id:
          type: string
          description: ID for the origination entity related to the notification
        idType:
          $ref: '#/components/schemas/NotificationPayloadIdType'
          description: Type of entity causing origination of the notification with the given ID
        customFields:
          $ref: './fdxapi.components.yaml#/components/schemas/FiAttribute'
          description: Custom key-value pairs for a notification

    Notifications:
      title: Notifications entity
      description: A paginated array of Notifications
      type: object
      allOf:
        - $ref: './fdxapi.components.yaml#/components/schemas/PaginatedArray'
        - type: object
          properties:
            notifications:
              type: array
              description: An array of Notifications
              items:
                $ref: '#/components/schemas/Notification'

    NotificationSubscription:
      title: Notification Subscription entity
      description: Provides the fields of a notification subscription
      type: object
      properties:
        type:
          $ref: '#/components/schemas/NotificationType'
          description: Type of notification
        category:
          $ref: '#/components/schemas/NotificationCategory'
          description: Category of notification
        callbackUrl:
          type: string
          description: Callback URL. Previous callback URL will be updated with latest.
        subscriber:
          $ref: './fdxapi.components.yaml#/components/schemas/Party'
          description: The Party who is subscribing to the notification
        effectiveDate:
          $ref: './fdxapi.components.yaml#/components/schemas/DateString'
          description: Effective date of notification
        subscriptionId:
          type: string
          description: Subscription id of notification
      required:
        - type
        - category
        - callbackUrl
        - subscriber

    ############################################################
    #
    # Event Notifications data types
    #
    ############################################################

    NotificationCategory:
      title: Notification Category
      description: Category of Notification
      type: string
      enum:
        - CONSENT
        - FRAUD
        - MAINTENANCE
        - NEW_DATA
        - SECURITY

    NotificationPayloadIdType:
      title: Notification Payload Id Type
      description: Type of entity causing origination of a notification
      type: string
      enum:
        - ACCOUNT
        - CONSENT
        - CUSTOMER
        - MAINTENANCE
        - PARTY

    NotificationPriority:
      title: Notification Priority
      description: Priority of notification
      type: string
      enum:
        - HIGH
        - MEDIUM
        - LOW

    NotificationSeverity:
      title: Notification Severity
      description: Severity level of notification
      type: string
      enum:
        - EMERGENCY
        - ALERT
        - WARNING
        - NOTICE
        - INFO

    NotificationType:
      title: Notification Type
      description: Type of notification
      type: string
      enum:
        - BALANCE
        - CONSENT_REVOKED
        - CONSENT_UPDATED
        - CUSTOM
        - PLANNED_OUTAGE
        - RISK
        - SERVICE
