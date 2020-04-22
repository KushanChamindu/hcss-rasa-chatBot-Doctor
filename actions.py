# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import requests
import pandas as pd
import pickle
import keras


# from rasa_sdk.events import EventType


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_your_num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(text="Hello World!")
        print(tracker.get_slot('num'))
        # dispatcher.utter_template('utter_your_num', tracker, number=details[str(tracker.get_slot('NAME')).lower()])
        return []


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["AGE", "BloodPressure", "Albumin", "PusCellClumps", "BloodGlucoseRandom", "BloodUrea", "Sodium",
                "Potassium", "Hemoglobin", "RedBloodCellCount", "DiabetesMellitus", "Appetite", ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        age = float(tracker.get_slot('AGE'))
        print(age)
        bp = float(tracker.get_slot('BloodPressure'))
        print(bp)
        al = float(tracker.get_slot('Albumin'))
        print(al)
        pcc = float(tracker.get_slot('PusCellClumps'))
        print(pcc)
        bgr = float(tracker.get_slot('BloodGlucoseRandom'))
        print(bgr)
        bu = float(tracker.get_slot('BloodUrea'))
        print(bu)
        sod = float(tracker.get_slot('Sodium'))
        print(sod)
        pot = float(tracker.get_slot('Potassium'))
        print(pot)
        hemo = float(tracker.get_slot('Hemoglobin'))
        print(hemo)
        rbcc = float(tracker.get_slot('RedBloodCellCount'))
        print(rbcc)
        dm = float(tracker.get_slot('DiabetesMellitus'))
        print(dm)
        appet = float(tracker.get_slot('Appetite'))
        print(appet)

        # final_features = pd.DataFrame(
        #     {'age': [age / 80], 'bp': [bp / 10], 'al': [al / 5], 'pcc': [pcc],
        #      'bgr': [bgr / 146], 'bu': [bu / 418], 'sod': [sod / 164], 'pot': [pot / 130.1],
        #      'hemo': [hemo / 21.7], 'rbcc': [rbcc / 12.8], 'dm': [dm], 'appet': [appet]})
        # print('After '+final_features)
        # model = pickle.load(open('model.pkl', 'rb'))
        # print('after model')
        # prediction = model.predict(final_features)
        # print('after prediction')

        request = {'age': age, 'bp': bp, 'al': al, 'pcc': pcc, 'bgr': bgr, 'bu': bu, 'sod': sod, 'pot': pot,
                   'hemo': hemo, 'rbcc': rbcc, 'dm': dm, 'appet': appet}

        register_url = 'http://127.0.0.1:5000/' + "predict"

        r = requests.get(register_url, params=request)
        print(r.content)
        pred = r.content.decode("utf-8")
        print("after string :" + pred)
        pred = float(pred)
        print('after float:' + str(pred))
        print(pred)
        print(type(pred))
        # print('after pred :'+r.content)
        # pred=int(r.content)

        if pred > 0.75:
            print('in if loop if part')
            result_prediction = 'Don\'t worry you have ' + str((1 - pred) * 100) + '% precentage to have chronicle kidney disease. We have 99.06% confident for say that !! '
            print('in if loop if part')
        elif (pred > 0.5):
            print('in if loop else part')
            result_prediction = 'You are in some denger zone. You have ' + str((1 - pred) * 100) + '% percentae to have chronicle kidney disease. We have 99.06% confident for say that !! Care full'
            print('in if loop else part')
        else:
            result_prediction = 'You are in very danger zone.You have ' + str((1 - pred) * 100) + '% percentae to have chronicle kidney disease. We have 99.06% confident for say that !! Meet your doctor as soon as possible'

        # utter submit template
        print(result_prediction)
        dispatcher.utter_message(responses="utter_submit", text=result_prediction.format())
        return [SlotSet("result", result_prediction)]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "AGE": [self.from_entity(entity="AGE", intent='my_age_is'),
                    self.from_text()],
            "BloodPressure": [self.from_entity(entity="BloodPressure", intent="my_bp_is"),
                              self.from_text()],
            "Albumin": [self.from_entity(entity="Albumin", intent='my_al_is'),
                        self.from_text()],
            "PusCellClumps": [self.from_entity(entity="PusCellClumps", intent="my_pcc_is"),
                              self.from_text()],
            "BloodGlucoseRandom": [self.from_entity(entity="BloodGlucoseRandom", intent='my_bgr_is'),
                                   self.from_text()],
            "BloodUrea": [self.from_entity(entity="BloodUrea", intent="my_bu_is"),
                          self.from_text()],
            "Sodium": [self.from_entity(entity="Sodium", intent='my_sod_is'),
                       self.from_text()],
            "Potassium": [self.from_entity(entity="Potassium", intent="my_pot_is"),
                          self.from_text()],
            "Hemoglobin": [self.from_entity(entity="Hemoglobin", intent='my_hemo_is'),
                           self.from_text()],
            "RedBloodCellCount": [self.from_entity(entity="RedBloodCellCount", intent="my_rbcc_is"),
                                  self.from_text()],
            "DiabetesMellitus": [self.from_entity(entity="DiabetesMellitus", intent="my_dm_is"),
                                 self.from_text()],
            "Appetite": [self.from_entity(entity="Appetite", intent="my_appet_is"),
                         self.from_text()],
        }

    @staticmethod
    def brand_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "samsung",
            "One plus",
            "I-phone",
        ]

    def validate_brand(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""
        print(value)
        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"BRAND": value}
        else:
            print(value)
            dispatcher.utter_message(template="utter_wrong_value")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"BRAND": None}
