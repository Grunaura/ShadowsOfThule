#quests.py

from game import Quest, SideQuest
from story import story

# Define quests and side quests
main_quest = Quest("Unravel the Mystery", "Embark on a journey to unravel the mystery behind the lost civilization.", ["Unravel the Mystery"])
decipher_quest = Quest("Decipher the Ancient Text", "Decipher the encrypted portion of the tome to gain deeper knowledge.", ["Decipher the Ancient Text"])
allies_quest = Quest("Seek Allies", "Seek out potential allies who can aid you in your quest to protect Lumina.", ["Seek Allies"])
confrontation_quest = Quest("Confront Lord Vexis", "Prepare for the final confrontation and defeat Lord Vexis to save Lumina.", ["Confront Lord Vexis"])

first_barrier_side_quest = SideQuest("Unearth the Lost Art of Deciphering", "Find and learn the lost art of deciphering the arcane script.", ["Unearth the Lost Art of Deciphering"])
evidence_side_quest = SideQuest("Gather Evidence of the Threat", "Search for evidence that connects Lord Vexis's ambitions with the prophetic warning.", ["Gather Evidence of the Threat"])
unexpected_ally_side_quest = SideQuest("Earn the Trust of an Unexpected Ally", "Prove your worth and earn the trust of Eris, the enigmatic warrior-mage.", ["Earn the Trust of an Unexpected Ally"])
hidden_secrets_side_quest = SideQuest("Search for Hidden Secrets", "Explore the Royal Library and uncover the hidden chambers filled with scrolls of lost knowledge.", ["Search for Hidden Secrets"])
journey_to_shrine_side_quest = SideQuest("Embark on the Journey to the Hidden Shrine", "Embark on a perilous journey to find the hidden shrine linked to the lost civilization.", ["Embark on the Journey to the Hidden Shrine"])

blank_quest = Quest("No Active Quests", "You currently have no active quests.", [])

# Assign the blank quest for sections without quests
for section in story.values():
    if "quest" not in section:
        section["quest"] = blank_quest
    if "side_quest" not in section:
        section["side_quest"] = blank_quest

# Assign quests and side quests to the corresponding story sections
story["start"]["quest"] = main_quest
story["decision_to_learn"]["quest"] = decipher_quest
story["first_barrier"]["side_quest"] = first_barrier_side_quest
story["learning_the_language"]["side_quest"] = decipher_quest
story["first_insight"]["side_quest"] = hidden_secrets_side_quest
story["evidence_of_threat"]["side_quest"] = evidence_side_quest
story["burden_of_knowledge"]["quest"] = allies_quest
story["seeking_allies"]["quest"] = allies_quest
story["doubt_and_rejection"]["side_quest"] = unexpected_ally_side_quest
story["unexpected_ally"]["side_quest"] = unexpected_ally_side_quest
story["solidifying_the_partnership"]["side_quest"] = unexpected_ally_side_quest
story["curiosity_piqued"]["quest"] = hidden_secrets_side_quest
story["unexpected_allies"]["side_quest"] = hidden_secrets_side_quest
story["realizing_common_goals"]["side_quest"] = hidden_secrets_side_quest
story["first_shared_adventure"]["quest"] = journey_to_shrine_side_quest
story["revelation_of_eris_past"]["side_quest"] = journey_to_shrine_side_quest


