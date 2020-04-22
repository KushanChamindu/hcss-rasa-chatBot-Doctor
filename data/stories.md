## happy CKD path
* greet_patient
  - utter_greet_patient
* CKD
  - utter_CKD
* confirm_report
  - utter_confirm_report
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}


## happy Diabetes path
* greet_patient
  - utter_greet_patient
* Diabetes
  - utter_Diabetes
  - utter_goodbye
 
## sad CKD path
* greet_patient
  - utter_greet_patient
* CKD
  - utter_CKD
* deny_report
  - utter_deny_report
* goodbye
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## New Story
* greet
* mood_unhappy
* affirm
* goodbye
