## For Loop

## Looping through a collection

for name in ["Christopher", "Susan"]:
    print(name)
    
    
for tool in ["Python", "Linux", "Terraform", "Docker", "AWS"]:
    print(tool)
    
    
backend_languages = ["JS", "Ruby", "Python", "Go"]

for lang in backend_languages:
    print(lang)
    
    
## Looping a number of times

for index in range(0, 2):
    print(index)
    
## While Loop
## Looping with a condition

names = ["Brian", "Mathenge"]
index = 0
while index < len(names):
    print(names[index])
    # Change the condition
    index = index + 1