# 
# ASSetupAssistantCoreService.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 5 python:
    
    class ASSetupAssistantCoreService(ASCoreServiceRepresentative):
        bundleName = "Setup Assistant"
        bundleId = "app.aliceos.core-services.setup-assitant"
        bundleDir = AS_CORESERVICES_DIR + "Setup.aoscservice/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Quickly set up AliceOS for configuration.
        """
        
        def getFromElements(self, filename):
            return self.bundleDir + "Resources/Elements/" + filename
        
        def startSetup(self, express=True, disclaimer=None):
            persistent.AS_COMPLETED_SETUP = False
            if express:
                if disclaimer != None:
                    renpy.call_screen("ASSetupAssistantView", title="Game Licensing Agreement", instructions="Your game provider has requested that you read the following information and agree to any terms.\n\n" + disclaimer)
                persistent.playername = renpy.call_screen("ASSetupAssistantView", title="Create Your Username", instructions="Type in a username that you want to use while using AliceOS. This name will also appear as your character name if applicable.", useInputMethod=True)
            else:
                renpy.call_screen("ASSetupAssistantView", title="Welcome to AliceOS", instructions="Welcome to the Setup Assistant for AliceOS. This assistant will help set up crucial parts of AliceOS such as your username and taking care of any legal agreements.\n\nTo continue with the assistant, press Next.")
                renpy.call_screen("ASSetupAssistantView", title="Know Your Rights", instructions="AliceOS is free and open-source software, licensed under the GNU Lesser GPL. This license allows you and the game creator to modify AliceOS to however you like and need without needing to seek permission.\n\nA version of the LGPL license should have been included in the AliceOS package; if unavailable, consult the GPL website at {b}https://www.gnu.org/licenses/lgpl-3.0.en.html{/b}.")
                if disclaimer != None:
                    renpy.call_screen("ASSetupAssistantView", title="Game Licensing Agreement", instructions="Your game provider has requested that you read the following information and agree to any terms.\n\n" + disclaimer)
                persistent.playername = renpy.call_screen("ASSetupAssistantView", title="Create Your Username", instructions="Type in a username that you want to use while using AliceOS. This name will also appear as your character name if applicable.", useInputMethod=True)
                renpy.call_screen("ASSetupAssistantView", title="Setup Complete", instructions="The Setup Assistant has completed all of the necessary setup tasks and AliceOS is ready for use.\n\nMore information about what AliceOS is, notes for this release, and what you can do with it can be found at {b}https://aliceos.app{/b}.\n\nThank you for choosing AliceOS. To exit the Setup Assistant, press Finish.", completed=True)
            persistent.AS_COMPLETED_SETUP = True
            return persistent.playername
        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Setup.aoscservice/")
    
    ASSetup = ASSetupAssistantCoreService()
