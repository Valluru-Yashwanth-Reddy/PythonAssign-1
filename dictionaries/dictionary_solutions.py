# Easy - 1

def invert_dictionary(d):
    return {v: k for k, v in d.items()}
# Example usage:
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Should return {1: "a", 2: "b", 3: "c"}

# Easy - 2 

def merge_dictionaries(d1, d2):
    result = {}
    for k in d1:
        result[k] = d1[k]
    for k in d2:
        result[k] = d2[k]
    return result
# Example usage:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}



# Medium - 1

def word_frequencies(txt):
    word_count={}
    txt = txt.lower()
    words= txt.split()
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count 
# Example usage:
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}


# Medium - 2
def add_contact(contact_book, name, phone=None, email=None,adress=None):
    contact_details={}
    if phone is not None:
        contact_details['phone']=phone
    if email is not None:
        contact_details['email']=email
    if adress is not None:
        contact_details['adress']=adress
    if name in contact_book:
        contact_book[name].update(contact_details)
    else:
        contact_book[name]=contact_details
# Example usage:
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", adress="123 Main St")  # Updates Alice's info

print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }

