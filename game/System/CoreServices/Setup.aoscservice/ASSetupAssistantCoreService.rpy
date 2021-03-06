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

        def runStep(self, title, instruction, typeInput=False, complete=False):
            return renpy.call_screen("ASSetupAssistantView", title=title, instructions=instruction, useInputMethod=typeInput, completed=complete)
        
        def startSetup(self, express=True, disclaimer=None):
            persistent.AS_COMPLETED_SETUP = False
            if not express:
                self.runStep("Welcome to AliceOS", "Welcome to the Setup Assistant for AliceOS. This assistant will help set up crucial parts of AliceOS such as your username and taking care of any legal agreements.\n\nTo continue with the assistant, press Next.")
                self.runStep("Know Your Rights", "AliceOS is free and open-source software, licensed under the BSD license. This license allows you and the game creator to modify AliceOS to however you like and need without needing to seek permission.\n\nA version of the BSD license should have been included in the AliceOS package; if unavailable, visit {b}https://opensource.org/licenses/BSD-2-Clause{/b} and contact the game's developer to include the license.")
            if disclaimer != None:
                self.runStep("Game Licensing Agreement", "Your game provider has requested that you read the following information and agree to any terms.\n\n" + disclaimer)
            persistent.playername = self.runStep("Create Your Username", "Type in a username that you want to use while using AliceOS. This name will also appear as your character name if applicable.", typeInput=True)
            if not express:
                self.runStep("Setup Complete", "The Setup Assistant has completed all of the necessary setup tasks and AliceOS is ready for use.\n\nMore information about what AliceOS is, notes for this release, and what you can do with it can be found at {b}https://aliceos.app{/b}.\n\nThank you for choosing AliceOS. To exit the Setup Assistant, press Finish.", complete=True)
            persistent.AS_COMPLETED_SETUP = True
            return persistent.playername

        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Setup.aoscservice/")
    
    ASSetup = ASSetupAssistantCoreService()
