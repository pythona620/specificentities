from mycroft import MycroftSkill, intent_file_handler

class TomatoSkill(MycroftSkill):
    def __init__(self):
        super().__init__()

    @intent_handler('what.is.a.tomato.intent')
    def handle_what_is(self, message):
        self.speak_dialog('tomato.description')

#     @intent_handler('do.you.like.intent')
#     def handle_do_you_like(self, message):
#         tomato_type = message.data.get('type')
#         if tomato_type is not None:
#             self.speak_dialog('like.tomato.type',{'type': tomato_type})
#         else:
#             self.speak_dialog('like.tomato.generic')

    def stop(self):
        pass

def create_skill():
    return TomatoSkill()
