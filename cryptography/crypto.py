import nltk
nltk.download('words',quiet=True)
from nltk.corpus import words
word_list = words.words('en')

alpha_low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
,'p','q','r','s','t','u','v','w','x','y','z']
alpha_up = []
for item in alpha_low:
  alpha_up.append(item.upper())
# def encrypt(plain,key):
#   encrypted_text = ''

#   for char in plain:
#     temp = int(char) 
#     temp2 = (temp + key) % 10
#     encrypted_text += str(temp2)
#   return encrypted_text

# def decrypt(cypher,key):
#   #8901, 3-> 5678
#   return encrypt(cypher, -key)

def encrypt_alph(plain,key):
  encrypted_str = ''

  for char in plain:
    if char in alpha_up:
      encrypted_str += alpha_up[(alpha_up.index(char) + (key))%26]
    elif char in alpha_low:
      encrypted_str += alpha_low[(alpha_low.index(char) + (key))%26]
    else:
      encrypted_str += char
  return encrypted_str

def decrypt_alph(cypher,key):
  encrypted_str = ''

  for char in cypher:
    if char in alpha_up:
      encrypted_str += alpha_up[(alpha_up.index(char) -(key))%26]
    elif char in alpha_low:
      encrypted_str += alpha_low[(alpha_low.index(char) - (key))%26]
    else:
      encrypted_str += char
  return encrypted_str
  
def crack(cypher):
  count = 0
  shifted_cyphers = []
    
  for key in range(len(alpha_low)):
    shifted = ''
    for char in cypher:
      if char in alpha_low:
        shifted += alpha_low[alpha_low.index(char) - (key%26)]
      elif char in alpha_up:
        shifted += alpha_up[alpha_up.index(char) - (key%26)]
      else:
        shifted += char
    shifted_cyphers.append({ 'sentence' : f'{shifted}', 'count': 0})  
  

  for thing in shifted_cyphers:
    for word in thing['sentence'].split():
      if word in word_list:
        thing['count'] += 1
    

  ret_val = shifted_cyphers[0]
  for thing in shifted_cyphers:
    if thing['count'] > ret_val['count']:
      ret_val = thing
  
  return ret_val['sentence']
    
  

  
      
      
  
  


if __name__=="__main__":
  test = encrypt_alph('A, bc',35)

  print(test)

  print(decrypt_alph(test,35))

  print(crack('pa dhz aol dvyza'))

