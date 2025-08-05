import nltk

nltk.download('punkt')

text = """
Name: Gagare Nikita 
Roll No: 42
Year: B.Tech
Branch: Information Technology
Mobile No: 9876543210
Email: nikita@example.com
"""

tokens = nltk.word_tokenize(text)

print("Tokens:")
print(tokens)


#Tokens:
#['Name', ':', 'Gagare', 'Nikita', 'Roll', 'No', ':', '42', 'Year', ':', 'B.Tech', 'Branch', ':', 'Information', 'Technology', 'Mobile', 'No', ':', '9876543210', 'Email', ':', 'nikita', '@', 'example.com']
