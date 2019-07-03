# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image ddesktop = "System/Library/Desktop Pictures/Prospect Park.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene ddesktop

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    window hide
    
    pause 1.0
    
    $ messages.requestPermission(forPermission=AS_REQUIRES_NOTIFICATIONKIT)

    "Hello, world."
    
    call screen ASNotificationBanner(message="Just Logokas", withDetails="Just Logokas.")
    
    $ messages.receiveMessage("Eileen", "This is so cool.")

    # This ends the game.

    return
