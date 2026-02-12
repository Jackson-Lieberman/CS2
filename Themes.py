"""
Shakespeare Thematic Analysis 
Student Name: Jackson Lieberman
Date: 2/27/26
Discription: 
Makes set of key for words for certain themes
analyze shakesphere for a genre and create a map/chart of the most common theme in that genere
then in each genre show the top thematic words and their distribution
Bugs:
Log: 1.0
"""
import string
import re
import csv
import matplotlib.pyplot as plt



themes = {                                                                                         #sets the thematic words
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

                                                                                                   #gives the regex pattern
article_pattern = re.compile(r'\b(a|an|the|and|i|to|of|my|you|that|this|in|me|not|is|be|it|with|for|but|as|have|his|her|your|so|do|he|she|it|all|are|what|will|o|no|now|him|if|by|which|thou|thy|thee|by|they|we|on|here|sir|ll|or|let|our|s|at|was|how|shall|their|there|would|them|like|when|from|were|upon|most|more|come|make|tis|well|may|know|go|us|t|did|am|say|yet|such|some|one|had|hath)\b', re.IGNORECASE)            

genres = {                                                                                         #sets the specific plays that will be analyzed in each genre
    "Comedies": [
        "All's_Well_That_Ends_Well.txt", 
        "midsummer_nights_dream.txt", 
        "as_you_like_it.txt", 
        "the_tempest.txt", 
        "Comedy_of_Errors.txt"
    ],
    "Tragedies": [
        "hamlet.txt", 
        "othello.txt", 
        "macbeth.txt", 
        "romeo_and_juliet.txt", 
        "Antony_and_Cleopatra.txt", 
        "Coriolanus.txt", 
        "Cymbeline.txt"
    ],
    "Histories": [
        "richard_iii.txt", 
        "henry_v.txt", 
        "richard_ii.txt", 
        "Henry_IV_part_1.txt", 
        "Henry_IV_part_2.txt", 
        "Henry_VI_part_1.txt", 
        "Henry_VI_part_2.txt", 
        "Henry_VI_part_3.txt"
    ]
}

def analyze_genre(genre_name, file_list):   
    """
    Processes files and matches words against thematic keywords.

    Args:   
        genre_name (str): chosen genre for analysis
        file_list (list): list of all files
    """
    theme_counts = {theme: 0 for theme in themes}                                                  #creates a dictonary where every theme has a vlaue of zero
    word_freq = {}                                                                                 # track specific top words found

                                                                                                   # Regex to strip common stop words and articles
    article_pattern = re.compile(r'\b(a|an|the|and|i|to|of|my|you|that|this|in|me|not|is|be|it|with|for|but|as|have|his|her|your|so|do|he|she|it|all|are|what|will|o|no|now|him|if|by|which|thou|thy|thee|by|they|we|on|here|sir|ll|or|let|our|s|at|was|how|shall|their|there|would|them|like|when|from|were|upon|most|more|come|make|tis|well|may|know|go|us|t|did|am|say|yet|such|some|one|had|hath)\b', re.IGNORECASE)

    for fname in file_list:                                                                        #for every file
        try:
            with open(fname, 'r', encoding='utf-8') as fhand:                                      #try to open the file
                for line in fhand:
                    line = line.rstrip()                                                           #strip the text
                    line = article_pattern.sub("", line)                                           # Remove articles
                    line = line.translate(line.maketrans("", "", string.punctuation))              # Remove punctuation
                    line = line.lower()                                                            #make it lower case and put each word in a list
                    words = line.split()
                    
                    for word in words:
                        for theme, keywords in themes.items():                                     # checks if a word in the list of theme words and if it is add one to the value of that theme
                            if word in keywords:
                                theme_counts[theme] += 1
                                word_freq[word] = word_freq.get(word, 0) + 1
        except FileNotFoundError:
            print(f'File cannot be opened: {fname}')
            
    return theme_counts, word_freq


user_input = input('''
Which genre would you like to look at:
           1. Tragedies
           2. Comedies
           3. Histories 
Selection: ''')                                                                                    #asks what genre the user wants to analyze 

if user_input == "1":                                                                              #sets the genre accordingly
    genre_choice = "Tragedies"
elif user_input == "2":
    genre_choice = "Comedies"
elif user_input == "3":
    genre_choice = "Histories"
else:
    print("Invalid selection. Exiting.")
    exit()

counts, specific_words = analyze_genre(genre_choice, genres[genre_choice])                         #runs analysis

                                                                                                   # Sort and slice top 10 thematic words
sorted_top_words = sorted(specific_words.items(), key=lambda x: x[1], reverse=True)[:10]


print(f"\n{genre_choice} Thematic Results")                                                        # Print summary to console
for theme, count in counts.items():
    print(f"{theme}: {count}")


csv_filename = f"{genre_choice}_data.csv"                                                          #makes the csv
with open(csv_filename, 'w', newline='') as out:
    writer = csv.writer(out)    
    writer.writerow(["Category", "Item", "Count"])                                                 # Headers
    for theme, count in counts.items():                                                            #takes the data into the csv
        writer.writerow(["Theme Total", theme, count])
    for word, count in sorted_top_words:
        writer.writerow(["Top Keyword", word, count])

print(f"\nResults saved to '{csv_filename}'.")


labels = list(counts.keys())                                                                       #sets labels
values = list(counts.values())                                                                     #sets the values

plt.figure(figsize=(12, 6))                                                                        #creates the area for graphs

                                                                                                   # Plot 1: Bar Chart of Themes
plt.subplot(1, 2, 1)                                                                               #creastes a subplot
plt.bar(labels, values, color=['pink', 'gold', 'darkred', 'purple'])                               #makes the bars of each theme and their colors, hights based on the values
plt.title(f"Theme Distribution: {genre_choice}")                                                   #labels the chart and axis
plt.ylabel("Keyword Frequency")

                                                                                                   # Plot 2: Pie Chart of Top Words
plt.subplot(1, 2, 2)                                                                               #creates the subplot
top_w = [item[0] for item in sorted_top_words]                                                     # creates a list of labels
top_c = [item[1] for item in sorted_top_words]                                                     #list of values
plt.pie(top_c, labels=top_w, autopct='%1.1f%%', startangle=140)                                    #makes the pie chart
plt.title(f"Top 10 Thematic Words")

                                                                                                   #saves and shows graphs
plt.tight_layout()
graph_name = f"{genre_choice}_analysis.pdf"                                     
plt.savefig(graph_name)                                                             
plt.show()

print(f"'{graph_name}' created successfully.")