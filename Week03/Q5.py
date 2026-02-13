#Question 5

contact = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print(f"Alice's number: {contact["Alice"]}")
contact["Diana"] = "555-4321"
print(f"Contact after adding Diana: {contact}")
contact["Bob"] = "555-0000"
print(f"Contact after updating Bob: {contact}")
del contact["Charlie"]
print(f"Contact after deleting Charlie: {contact}")
print(f"All names: {contact.keys()}")
print(f"All numbers: {contact.values()}")

print(f"Total Contacts: {len(contact)}")