#  Default Apps

AliceOS includes several default applications that are located in `System/Applications/`. These applications are designed to enhance the AliceOS experience and provide functionalities for core parts without having to write a third-party app for them.

## Messages

![Messages app icon](../images/system/defapps/messages.png)

Messages is a simple app designed to simulate text messaging between characters and the player in a fun way.

**Available methods**

`messages.receiveMessage(fromPerson, message)`

Send a notification request that displays a text message from a person.

**Parameters**

- `fromPerson`: The person the message is being sent from
- `message`: The text message being sent

**Returns**
Returns the default values as indicated from [ASNotificationBanner](../../NotificationKit/01-banner/#returns)
