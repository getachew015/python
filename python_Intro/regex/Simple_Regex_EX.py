import re;

'''
Cheat Sheet
.       - Any character except new line
\d      - Digits (0-9)
\D      - Not a digit (0-9)
\w      - Word character (a-z, A-Z, 0-9, _)
\W      - Not a word character
\s      - white space (space, new line, tab)
\S      - Not a white space (space, new line, tab)
\b      - word boundary
\B      - Not a word boundary
^       - Begining of a string
$       - End of a string
[]      - Matches characters in the brackets
[^]     - Matches characters not in the brackets
'''

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
emails_to_search = '''
dagim.getachew@gmail.com
john_roberts@supreme_court.com
justice-kenedy@court.com
thomasJefrson@us-Potus.org
dagim_2020getac@umn.edu
'''
urls_to_search = '''
https://www.google.com
http://county66court.org
https://youtube.com
https://www.nasa.gov
http://my.webaddress.net
'''
sentence = 'Start a sentence and then bring it to an end'

# Search for phone numbers
    # case-1 re.compile(r'\d\d\d.\d\d\d.\d\d\d\d');
    # case-2 re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d');
    # case-3 re.compile(r'\d{3}.\d{3}.\d{4}');
    # case-4 re.compile(r'[89]00.\d{3}.\d{4}'); only 800/900 numbers
# Search for patterns using grouping
    # Case-1 re.compile(r'(Mr\.?|Ms\.?|Mrs\.?)\s[A-Z]\w*'); Mr or Ms or Mrs and a white space and begining with a caps letter
# Search for email patterns
    # case-1 re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.\w*')
    # case-2 re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.(com|edu|net|org)')
# Search for URL patterns
    # Case-1 re.compile(r'https?://(\w+\.)?\w+\.\w+')
    # Case-2 if we group the patterns we can print(match.group(0) or group(1) or group(2)



pattern = re.compile(r'https?://(\w+\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls_to_search);
print(subbed_urls);

matches = pattern.finditer(urls_to_search);

for match in matches:
    print(match.group(0));


'''
#search a file for patterns
pattern = re.compile(r'[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.\w+');

with open('data.txt', 'r', encoding= 'utf-8') as f:
    content = f.read();

matches = pattern.finditer(content);

for match in matches:
    print(match);
'''



    
    
