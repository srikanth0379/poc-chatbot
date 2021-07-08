from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict



class VantageLearnings(Action):
 def name(self):
  """name of the custom action"""
  return "action_vantage"  
 def run(self,dispatcher,tracker,domain):
  
  dispatcher.utter_message("https://vantage.pwc.com/")
  return []

class PrecisionFillUp(Action):
 def name(self):
  """name of the custom action"""
  return "action_precision"  
 def run(self,dispatcher,tracker,domain):
  
  dispatcher.utter_message("http://precision.in.nam.ad.pwcinternal.com/OA_HTML/AppsLocalLogin.jsp?langCode=US&_logoutRedirect=y")
  return []

class RASALearnings(Action):
 def name(self):
  """name of the custom action"""
  return "action_rasa"  
 def run(self,dispatcher,tracker,domain):
  
  dispatcher.utter_message("https://rasa.com/docs/rasa/playground/")
  return []