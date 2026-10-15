                                                                    #REGULAR EXPRESSIONS...
# Program 1
'''
import re
s= input("Enter the string:")
dig= re.findall(r'\d',s)
print("All digits:",dig)
'''

# Program 2
'''
import re
s= input("Enter the string:")
a= re.findall(r'\b[Aa]\w*',s)
print("words:",a)
'''

# Program 3
'''
import re
s= input("Enter the string:")
v= re.findall(r'[aeiouAEIOU]',s)
print("vowels:",v)
print("Count of vowel",len(v))
'''

# Program 4
'''
import re
s= input("Enter the string:")
u= re.findall(r'[A-Z]',s)
print("All uppercase letters:",u)
'''

# Program 5
'''
import re
s= input("Enter the string:")
ws= re.findall(r'[ \t\n]',s)
print("Count of All Spaces, tabs, newline are:",len(ws))
'''

# Program 6
'''
import re
s= input("Enter the string:")
res= re.sub(r' +',' ',s)
print("combined :",res)
'''

# Program 7
'''
import re
s= input("Enter the string:")
res= re.findall(r'\b[A-Za-z]{5}\b',s)
print("Exact 5 chracter words:",res)
'''

# Program 8
'''
import re
s= input("Enter the string:")
res= re.findall(r'\b[A-Za-z]*s\b',s,re.IGNORECASE)
print("Ends with s:",res)
'''

# Program 9
'''
import re
s= input("Enter the string:")
res= re.sub(r'[^A-Za-z0-9 ]','',s)
print("After removing special characters :",res)
'''

# Program 10
'''
import re
s= input("Enter the string:")
u= re.findall(r'\b\w+\b',s)
print("All words count:",len(u))
'''

# Program 11
''''
import re
num = input("Enter mobile number: ")
if re.fullmatch(r'[6-9]\d{9}', num):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
'''

# Program 12
'''
import re
email = input("Enter email address: ")
if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
    print("Valid email address")
else:
    print("Invalid email address")
'''

# Program 13
'''
import re
text = input("Enter a paragraph: ")
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Dates:", dates)
'''

# Program 14
'''
import re
text = input("Enter a paragraph: ")
urls = re.findall(r'https?://[^\s]+', text)
print("Web addresses:", urls)
'''

# Program 15
'''
import re
post = input("Enter a social media post: ")
h = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', post)
print("Hashtags:", h)
'''

# Program 16
'''
import re
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{8,}'
if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")
'''

# Program 17
'''
import re
text = input("Enter a sentence: ")
words = re.findall(r'\b([A-Za-z]+)\s+\1\b', text, re.IGNORECASE)
print("Repeated words:", words)
'''

# Program 18
'''
import re
text = input("Enter a paragraph: ")
pins = re.findall(r'\b[1-9]\d{5}\b', text)
print("PIN codes:", pins)
'''

# Program 19
'''
import re
number = input("Enter vehicle number: ").upper()
pattern = r'[A-Z]{2}\d{2}[A-Z]{1,3}\d{1,4}'
if re.fullmatch(pattern, number):
    print("Valid registration format")
else:
    print("Invalid registration format")
'''

# Program 20
'''
import re
text = input("Enter filenames: ")
extensions = re.findall(r'\b[\w-]+\.(\w+)\b', text)
print("File extensions:", extensions)
'''

# Program 21
'''
import re
text = input("Enter text: ")
text = re.sub(r'<[^>]*>', '', text)
text = re.sub(r'[^\w\s.,!?]', '', text)
text = re.sub(r'\s+', ' ', text).strip()
print("Clean text:", text)
'''

# Program 22
'''
import re
text = input("Enter invoice text: ")
invoice = re.findall(r'Invoice\s*(?:No\.?|Number|#)\s*:?\s*([A-Z0-9-]+)', text, re.IGNORECASE)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'(?:₹|Rs\.?\s*)(\d+(?:,\d{3})*(?:\.\d{2})?)', text, re.IGNORECASE)
print("Invoice numbers:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)
'''

# Program 23
'''
import re
code = input("Enter Python source code: ")
comments = re.findall(r'#.*', code)
print("Single-line comments:", comments)
'''

# Program 24
'''
import re
code = input("Enter product code: ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")
'''

# Program 25
'''
import re
text = input("Enter student details: ")
pattern = r'Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
matches = re.findall(pattern, text)
for name, roll, marks in matches:
    print("Name:", name.strip())
    print("Roll Number:", roll)
    print("Marks:", marks)
'''

# Program 26
'''
import re
text = input("Enter research references: ")
doi = re.findall(r'\b10\.\d{4,9}/[^\s,;]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
urls = re.findall(r'https?://[^\s,;]+', text)
print("DOI identifiers:", doi)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)
'''


                                                                    
