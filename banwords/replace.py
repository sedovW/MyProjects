import os
delete_elements=[',','.',':','!']
with open('banwords.txt','r') as word:
    banword=word.read()
with open('text_input.txt','r') as file:
    File=file.read()
with open('text_input.txt', 'r') as file:
    Buff_File = file.read()
print(banword)
Banned_id=[]
Text,banword=str(File),str(banword)
Text1=Text
banword1=banword
Text,banword=Text.lower(),banword.lower()
Text,banword=Text.split(),banword.split()
for i in range(len(Text)):
    for b in range(len(banword)):
        if Text[i] == banword[b]:
            Banned_id.append(i)
print(Text)
print(Banned_id)
for index in Banned_id:
    Text[index] = '***'
Output_Text=' '.join(Text)
print(Output_Text)
with open('text_output.txt','+w') as file:
    file.write(Output_Text)


