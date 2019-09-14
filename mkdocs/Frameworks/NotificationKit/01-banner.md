# Banners

![Sample banner](../../images/nk/banner.png)

**Banners** provide a temporary pop-up at the top of the screen that automatically dismiss after five seconds. Banners usually include an app's name, primary message, details, and a response callback upon clicking 'Respond'.

## `ASNotificationBanner()`

`ASNotificationBanner(applet=None, message, withDetails, responseCallback=Return('didClickRespond'))`

### Parameters

- `applet`: (Optional) The app object to pass in. If None, the app icon and bundle name on the top will display as "Unknown Bundle".
- `message`: (Required) The main message or sender.
- `withDetails`: (Required) The details of the message.
- `responseCallback` (Optional) The action to run upon clicking "Respond".


### Returns

- If the notification times out and dismisses, the banner will return `'notificationTimedOut'`.
- If the notification's response callback is left as the default, the banner will return `'didClickRespond'` when clicking the "Respond" button.

## Guidelines

Banners are intended for temporary actions that can be ignored, if possible. Keep these guidelines in mind when using banners:

- **Refrain from overloading banners**. This can be visually distracting and may annoy the user.
- **Keep the message and details short**. Banners are intended for a quick glance or something that doesn't require a lot of attention.
- **Don't force the user to interact with the banner**. Banners shouldn't require the user to perform an action.
