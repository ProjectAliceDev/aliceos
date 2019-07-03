#  Sending Notifications

![Notification banner](../images/apps/apps-sn-hero.png)

Notifications are a great way to extend your visual novel project. If done correctly, they often can add an interactive experience that immerses players into the environment. Apps using AppKit have a way to send notification requests to the user that also respect's users' preferences.

## Declaring notification permissions

Your app should have the proper permissions to send notifications via NotificationKit in the app's manifest. To ensure that your app lists itself as needing this permission, be sure to add `AS_REQUIRES_NOTIFICATIONKIT` into the `requires` field:

```python

requires = {
    AS_REQUIRES_NOTIFICATIONKIT,
    ...
}
```

## Requesting for permission

Typically, apps request for notification access before sending notification requests. There are two methods for handling this behavior:

- `requestAllPermissions()` will request for all permissions available. Use this only if notifications are dependent on other permissions that must be addressed immediately.
- `requestPermission(forPermission=AS_REQUIRES_NOTIFICATIONKIT)` will request specifically for the NotificationKit permission.

## Sending a temporary notification request

Apps using AppKit have an official means of handling temporary notifications as banners via several methods. More details are provided on the [Banners page](../NotificationKit/01-banner.md).

### `applicationShouldRequestNotification()`

This function is provided to check that the app has been given permission to send notifications.

**Returns**

- Whether the app has been given permission to send notifications as a Boolean value.

!!! danger
    Do not override this function unless you need to perform an additional check.

### `applicationWillRequestNotification()`

**Parameters**

- `message`: The message or title of the notification.
- `withDetails`: The details of the notification.
- `responseCallback` (Optional) The action to perform when clicking 'Respond'.

!!! tip
    If there are preliminary actions that should be performed _before_ requesting a notification, you may redefine the function, granted that you also include `ASAppRepresentative.applicationWillRequestNotification()`.
    
    **Example**
    
        
        def applicationWillRequestNotification(self, message, withDetails, responseCallback):
            if not "Error" in message:
                ASAppRepresentative.applicationWillRequestNotification(
                    message, 
                    withDetails, 
                    responseCallback)
            else:
                print "(Err: " + message + ") " + withDetails
                
!!! danger
    Do not use any other methods for sending temporary notifications that do not listen to `applicationShouldRequestNotification()`. All notifications should adhere to users' preference.

### `applicationDidRequestNotification()`

`applicationDidRequestNotification()` runs after a notification has been sent. This can be used to watch for a particular action or to do something else.
