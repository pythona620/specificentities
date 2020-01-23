# number adding
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

__author__ = 'pythona620/prasad'
LOGGER = getLogger(__name__)

class NameAddingSkill(MycroftSkill):

# MyNameIs = input("Ask user for something")
# MyFriendNameIs = input("Ask user for something")

# str3 = MyNameIs+MyFriendNameIs
# c = MyNameIs +" "+"and"+" "+ MyFriendNameIs

	myname = 0
	myfriendname = 0
	
	def get_names(self, dialog):
		while True:
			yip = self.get_response(dialog)
			try:
				yip = 'str'
				return yip
			except ValueError:
				self.speak_dialog("invalid.input")
			except:
				self.speak_dialog("input.error")

	@intent_handler(IntentBuilder("").require("funny").optionally("Play").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start.game")

		# get myname
		myname = self.get_names("get.myname")
		# get myfriendname
		myfriendname = self.get_names("get.myfriendname")
		answer = myname + myfriendname
		tr=answer['text']
		self.speak_dialog("friends",{"answer":tr})
	def stop(self):		
		pass
def create_skill():
	return NameAddingSkill()
