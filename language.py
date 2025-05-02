import mysql.connector

# All language–code pairs as a tuple
languages = (
    'afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 'arabic', 'ar',
    'armenian', 'hy', 'azerbaijani', 'az', 'basque', 'eu', 'belarusian', 'be',
    'bengali', 'bn', 'bosnian', 'bs', 'bulgarian', 'bg', 'catalan', 'ca',
    'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)', 'zh-cn',
    'chinese (traditional)', 'zh-tw', 'corsican', 'co', 'croatian', 'hr',
    'czech', 'cs', 'danish', 'da', 'dutch', 'nl', 'english', 'en',
    'esperanto', 'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi',
    'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka',
    'german', 'de', 'greek', 'el', 'gujarati', 'gu', 'haitian creole', 'ht',
    'hausa', 'ha', 'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi',
    'hmong', 'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo', 'ig',
    'indonesian', 'id', 'irish', 'ga', 'italian', 'it', 'japanese', 'ja',
    'javanese', 'jw', 'kannada', 'kn', 'kazakh', 'kk', 'khmer', 'km',
    'korean', 'ko', 'kurdish (kurmanji)', 'ku', 'kyrgyz', 'ky', 'lao', 'lo',
    'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish', 'lb',
    'macedonian', 'mk', 'malagasy', 'mg', 'malay', 'ms', 'malayalam', 'ml',
    'maltese', 'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian', 'mn',
    'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
    'pashto', 'ps', 'persian', 'fa', 'polish', 'pl', 'portuguese', 'pt',
    'punjabi', 'pa', 'romanian', 'ro', 'russian', 'ru', 'samoan', 'sm',
    'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho', 'st', 'shona', 'sn',
    'sindhi', 'sd', 'sinhala', 'si', 'slovak', 'sk', 'slovenian', 'sl',
    'somali', 'so', 'spanish', 'es', 'sundanese', 'su', 'swahili', 'sw',
    'swedish', 'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 'te', 'thai', 'th',
    'turkish', 'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug',
    'uzbek', 'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
    'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu'
)

# DB connection
conn = mysql.connector.connect(
    host="localhost",      
    user="root",  
    password="11491149@Ni",  
    database="linguabridge"
)

cursor = conn.cursor()

# Step 1: Ensure table exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS languages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    language_name VARCHAR(100) NOT NULL UNIQUE,
    language_code VARCHAR(10)
)
""")

# Step 2: Insert using ON DUPLICATE KEY UPDATE
for i in range(0, len(languages), 2):
    name = languages[i].lower()
    code = languages[i+1]
    cursor.execute("""
        INSERT INTO languages (language_name, language_code)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE language_code = VALUES(language_code)
    """, (name, code))

conn.commit()

# Step 3: Read data into dictionary
cursor.execute("SELECT language_name, language_code FROM languages")
lang_dict = {name.lower(): code for name, code in cursor.fetchall()}

# Debug print
print("Total languages loaded:", len(lang_dict))

# Cleanup
cursor.close()
conn.close()