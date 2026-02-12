"""
Shakespeare Thematic Analysis 
Student Name: Jackson Lieberman
Date: 2/27/26
Discription: 
Reads a set of Shakespeare play .txt files,cleans text. Then, counts occurrences of theme keywords per theme and word. Finally it gives a csv and chart of this data

Bonuses:
Bugs:
Log: 1.0
"""
import string
import re
import csv
import matplotlib.pyplot as plt

themes = {                                                                                         #theme words list
    "Love": [
        "affection", "affect", "affectionate", "affectionately", "affecting", "affections",
        "amorous", "amour", "amatory", "amorousness", "amorously", "amours",
        "adoration", "adore", "adored", "adoring", "adoringly", "adorable", "adores", "adoreth",
        "ardour", "ardent", "ardently", "ardor", "burning", "fervor", "fervent", "fervently",
        "bequeath", "bequest", "bequeathing", "bequeathed", "bequeathment", "legacy", "bequeaths",
        "betrothed", "betrothal", "betroth", "troth", "plight", "plighted", "affiance", "affianced",
        "blandishment", "blandish", "blandished", "cajole", "flattery", "blandishments",
        "cherish", "cherishing", "cherished", "cherishes", "cherisheth", "endear", "endearment",
        "concord", "concordance", "concordant", "harmony", "harmonious", "amity", "unison",
        "courtship", "court", "courting", "courted", "courtly", "woo", "wooing", "wooed", "suitor",
        "cupid", "erotic", "aphrodite", "venus", "desire", "desirous", "desiring", "desired", "lust",
        "devotion", "devote", "devoted", "devotedly", "devotional", "piety", "pious",
        "dotage", "dote", "doting", "doted", "doteth", "besotted", "infatuation",
        "enamoured", "enamour", "enamored", "enamoring", "captivated", "charmed",
        "fancy", "fancied", "fanciful", "fanciest", "liking", "fondness",
        "favour", "favor", "favoured", "favored", "favourite", "favorite", "grace",
        "fidelity", "fealty", "faithful", "faithfully", "faithfulness", "allegiance",
        "hymen", "hymeneal", "marriage", "wedlock", "matrimony", "union",
        "idolatry", "idolize", "idol", "idolatrous", "worship", "worshipping", "worshipped",
        "infatuation", "infatuate", "infatuated", "daze", "bewitch", "bewitched",
        "mercy", "merciful", "mercifully", "clemency", "leniency", "compassion",
        "nuptial", "nuptials", "connubial", "bridal", "matrimonial", "wedding",
        "passion", "passionate", "passionately", "impassioned", "ardency",
        "plight", "plighted", "pledge", "pledged", "troth-plight",
        "rapture", "rapturous", "rapturously", "rapt", "enraptured", "ecstasy", "ecstatic",
        "sigh", "sighing", "sighed", "sigheth", "breath", "yearning",
        "sweetheart", "lover", "beloved", "darling", "paramour", "mistress",
        "thraldom", "enthrall", "enthralled", "enthralling", "thrall", "bondage", "captive",
        "vow", "vowed", "vowing", "oath", "sworn", "voweth",
        "wooing", "woo", "woos", "wooed", "wooer", "suit", "solicit"
    ],
    "Power": [
        "absolute", "absolutism", "absolutist", "unconditional", "arbitrary", "totalitarian",
        "authority", "authoritarian", "authoritative", "authorize", "authorization", "magistracy",
        "canon", "canonical", "law", "decree", "dogma", "precedent",
        "command", "commander", "commandment", "commanding", "bidding", "mandate", "behest",
        "coronation", "coronate", "crown", "crowning", "crowned", "coronet", "diadem",
        "decree", "decreed", "decreeing", "ordain", "ordinance", "fiat", "dictate",
        "dominion", "dominate", "dominance", "dominant", "domineer", "domineering", "domain",
        "edict", "proclamation", "pronouncement", "manifesto", "sanction",
        "empire", "emperor", "empress", "imperial", "imperium", "imperialism",
        "enthrone", "enthroned", "enthronement", "investiture", "exalt", "exalted",
        "hegemony", "hegemon", "hegemonic", "leadership", "predominate", "ascendancy",
        "hierarchy", "hierarchical", "ranking", "gradation", "echelon",
        "imperious", "imperiously", "overbearing", "peremptory", "dictatorial",
        "jurisdiction", "jurisdictional", "purview", "authority", "legal",
        "kingly", "king", "queen", "queenly", "princely", "regal", "royal", "royalty",
        "lineage", "dynasty", "ancestry", "descent", "bloodline", "house",
        "majesty", "majestic", "majestical", "highness", "grace", "grandeur",
        "monarch", "monarchy", "monarchic", "monarchist", "sovereign", "potentate",
        "nobility", "noble", "nobly", "aristocracy", "aristocrat", "peerage",
        "omnipotent", "omnipotence", "almighty", "all-powerful", "invincible",
        "prerogative", "privilege", "right", "entitlement", "birthright",
        "regal", "regality", "regally", "reign", "reigning", "reigned", "reigneth",
        "sceptre", "sceptred", "mace", "rod", "staff", "regalia", "insignia",
        "sovereignty", "sovereign", "suzerain", "autonomous", "paramount", "overlord",
        "state", "statism", "stately", "government", "polity", "realm",
        "supremacy", "supreme", "supremely", "paramountcy", "preeminence",
        "sway", "swaying", "swayed", "influence", "leverage", "control",
        "throne", "throned", "enthroned", "seat", "chair",
        "tyranny", "tyrant", "tyrannical", "tyrannize", "tyrannous", "despot", "despotism"
    ],
    "Revenge": [
        "appease", "appeasement", "appeased", "placate", "mollify", "propitiate",
        "avenge", "avenger", "avenging", "avenged", "revenge", "revenged", "revengeful",
        "bloodguilt", "bloodletting", "blood-feud", "gory", "sanguine", "vendetta",
        "chastisement", "chastise", "chastised", "punish", "punishment", "discipline",
        "countercheck", "thwart", "frustrate", "rebut", "countermeasure",
        "enmity", "enemy", "inimical", "hostility", "animosity", "antagonism",
        "feud", "feuding", "feuded", "quarrel", "strife", "conflict",
        "grievance", "grieve", "grievous", "wrong", "injury", "resentment",
        "honour", "honor", "honorable", "integrity", "reputation", "prestige",
        "immolation", "immolate", "sacrifice", "hecatomb", "slaughter", "holocaust",
        "inflict", "infliction", "inflicted", "wreak", "impose", "imposition",
        "justice", "just", "justify", "justification", "righteous", "equity", "retribution",
        "malice", "malicious", "maliciously", "malignity", "spite", "spiteful",
        "nemesis", "retributive", "scourge", "punisher", "downfall", "doom",
        "payback", "repayment", "reprisal", "requital", "retaliation",
        "punitive", "punish", "punishment", "penal", "penalize", "disciplinary",
        "quittance", "quit", "acquittal", "discharge", "release", "recompense",
        "reckoning", "reckon", "account", "audit", "score", "judgment", "settlement",
        "redress", "remedy", "rectify", "amend", "atonement", "reparation",
        "requital", "requite", "requited", "repay", "reciprocate", "reciprocation",
        "retaliation", "retaliate", "retaliatory", "reprisal", "counter-attack",
        "retribution", "retributive", "avengement", "vengeance", "recompense",
        "satisfaction", "satisfy", "satisfied", "amends", "expiation",
        "spite", "spiteful", "spitefully", "grudge", "malevolence",
        "tally", "tallied", "score", "reckon", "count",
        "vengeance", "vengeful", "vengefully", "vindicative", "vindicatory",
        "vindication", "vindicate", "vindicated", "exonerate", "justify",
        "wreak", "wrought", "wreaking", "inflict", "vent", "unleash"
    ],
    "Hate": [
        "abhorrence", "abhor", "abhorrent", "abhorred", "abhorring", "detest",
        "abomination", "abominate", "abominated", "anathema", "execrate",
        "animosity", "animus", "hostility", "friction", "antagonism", "enmity",
        "antipathy", "antipathetic", "averse", "aversion", "repulsion", "distaste",
        "aversion", "averse", "avoidance", "loathing", "reluctance",
        "contempt", "contemptuous", "contemptuously", "contemptible", "scorn", "derision",
        "detestation", "detest", "detested", "detestable", "abhor",
        "disdain", "disdainful", "disdainfully", "spurn", "scorn", "scorned",
        "envenom", "venom", "venomous", "poison", "poisonous", "toxic", "embitter",
        "execration", "execrate", "execrable", "curse", "malediction", "imprecation",
        "gall", "bitterness", "acrimony", "bile", "rancour",
        "hostility", "hostile", "hostilely", "antagonism", "aggression", "warfare",
        "ill-will", "malice", "malevolence", "malignity", "unfriendliness",
        "loathing", "loathe", "loathed", "loathsome", "abhor", "detest",
        "malignity", "malign", "malignant", "malicious", "malevolence", "evil",
        "misanthrope", "misanthropy", "misanthropic", "hater", "cynic",
        "odious", "odiousness", "hateful", "obnoxious", "repulsive", "revolting",
        "opprobrium", "opprobrious", "shame", "infamy", "ignominy", "vituperation",
        "poison", "poisonous", "poisoned", "toxic", "venom", "venomous",
        "rancour", "rancorous", "rancorously", "bitterness", "acrimony", "resentment",
        "repugnance", "repugnant", "repel", "repellent", "revolting", "nausea",
        "scorn", "scornful", "scornfully", "disdain", "contempt", "mockery",
        "spite", "spiteful", "spitefully", "malice", "grudge", "malevolence",
        "vile", "vilify", "vilification", "revile", "debased", "depraved", "foul",
        "virulence", "virulent", "deadly", "poisonous", "acrid", "stinging", "caustic",
        "vituperation", "vituperative", "abuse", "invective", "railing", "scolding"
    ]
}
plays = {                                                                                          #plays list
    "All's_Well_That_Ends_Well.txt", "midsummer_nights_dream.txt", "as_you_like_it.txt", "the_tempest.txt",
    "hamlet.txt", "othello.txt", "macbeth.txt", "romeo_and_juliet.txt",
    "richard_iii.txt", "henry_v.txt", "richard_ii.txt", "Comedy_of_Errors.txt", "Antony_and_Cleopatra.txt", "Coriolanus.txt", "Cymbeline.txt",
    "Henry_IV_part_2.txt", "Henry_IV_part_1.txt", "Henry_VI_part_2.txt", "Henry_VI_part_1.txt", "Henry_VI_part_3.txt"
}

stopwords_pattern = re.compile(                                                                    #regex pattern
    r"\b(a|an|the|and|i|to|of|my|you|that|this|in|me|not|is|be|it|with|for|but|as|have|his|her|your|so|do|he|she|all|are|what|will|o|no|now|him|if|by|which|thou|thy|thee|they|we|on|here|sir|ll|or|let|our|s|at|was|how|shall|their|there|would|them|like|when|from|were|upon|most|more|come|make|tis|well|may|know|go|us|t|did|am|say|yet|such|some|one|had|hath)\b",
    re.IGNORECASE
)

                                                                                                   # Flatten theme keyword lists into a set
theme_words = set()                                                                                #creates set of theme words
for words in themes.values():                                                                      #adds everything in the list of theme words to the set
    theme_words.update(w.lower() for w in words)        
word_to_theme = {}
for theme_name, words in themes.items():                                                           #tells which theme each word belongs to
    for w in words:
        lw = w.lower()
        if lw not in word_to_theme:                                                                # keep first theme if duplicates exist
            word_to_theme[lw] = theme_name

word_counts = {}                          
theme_counts = {t: 0 for t in themes}                                                              # counts per theme

for fname in plays:                                                                                #for every play
    try:
        with open(fname, "r", encoding="utf-8") as f:                                              #open the play
            for line in f:                                                                         #clean the text
                line = stopwords_pattern.sub(" ", line)
                line = line.translate(str.maketrans("", "", string.punctuation))
                line = line.lower()

                for w in line.split():                                                             #split the text by word
                    if w in theme_words:
                        word_counts[w] = word_counts.get(w, 0) + 1
                        theme_counts[word_to_theme[w]] += 1
    except FileNotFoundError:
        print(f"File cannot be opened: {fname}")





top_20 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20]                        #gets the top 20 words

for word, count in top_20:                                                                         #prints the top 20 words
    print(f"{word:>15} : {count}")


csv_filename = "top_20_theme_words.csv"                                                            #sets the file name
with open(csv_filename, "w", newline="", encoding="utf-8") as out:                                 #makes a new csv
    writer = csv.writer(out)
    writer.writerow(["Word", "Count"])                                                             #headings
    writer.writerows(top_20)                                                                       #puts the top 20 words in the csv

print(f"\nResults saved to '{csv_filename}'.")



labels = list(word_counts.keys())                                                                  #sets the labels and values
values = list(word_counts.values())
theme_labels = list(theme_counts.keys())                                                           
theme_values = list(theme_counts.values())


pie_words = [w for w, _ in top_20]                                                                 #sets the values for the pie chart
pie_counts = [c for _, c in top_20]

plt.figure(figsize=(12, 6))                                                                        #creates the figure

                                                                                                   # Bar chart: theme totals
plt.subplot(1, 2, 1)                                                                               #creates a subplot
plt.bar(theme_labels, theme_values)                                                                # makes the charts data
plt.title("Theme Distribution (Ouvre)")                                                            #title and labels Y
plt.ylabel("Keyword Frequency") 

                                                                                                   # Pie chart: top 20 words
plt.subplot(1, 2, 2)                                                                               #makes a subplot
plt.pie(pie_counts, labels=pie_words, autopct="%1.1f%%", startangle=140)                           #gives the pie chart the data
plt.title("Top 20 Thematic Words")                                                                 #titles

plt.tight_layout()                                                                                 #saves and shows the graph
graph_name = "shakespeare_theme_analysis.pdf"
plt.savefig(graph_name)
plt.show()

print(f"'{graph_name}' created successfully.")









