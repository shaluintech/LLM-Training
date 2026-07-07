"""
Sets - unordered collection of UNIQUE items
"""
tags = {"python","ai","python","ml"}
print(tags)
print("ai" in tags)
tags.add("rag")
tags.add("ai")
print(tags)
tags.discard("ml")
print(tags)

# emtpy = {} - declares an empty dict not Set
empty = set()
#Use sets to dedup any list
sigups = ["a@x.com","b@x.com","a@x.com","c@x.com"]
unique_signups = set(sigups)
print(unique_signups)

#set algebra
arjit_skills = {"python","ai","devops","containers"}
rohit_skills = {"python","git","devops","aws"}
print("Both Know", arjit_skills & rohit_skills)
print("Either Knows |", arjit_skills | rohit_skills)
print("Only arjit -", arjit_skills - rohit_skills)
print("Exactly one ",arjit_skills ^ rohit_skills)