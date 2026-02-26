import re
path=r'c:\Users\Sanju\OneDrive - CromptonConcepts\Sharepoint - Documents\Clients\Application development\Apps\TIA+QUEUE\Crompton_TIA_QUEUE\Crompton_TIA_Queue.html'
with open(path,'r',encoding='utf-8') as f:
    data=f.read()
scripts=re.findall(r'<script>([\s\S]*?)</script>', data)
code=scripts[0] if scripts else ''
braces=0
parens=0
brackets=0
for i,line in enumerate(code.splitlines(),1):
    stripped=re.sub(r'".*?"', '', line)
    stripped=re.sub(r"'.*?'", '', stripped)
    for ch in stripped:
        if ch=='{': braces+=1
        elif ch==' }': braces-=1
        elif ch=='(': parens+=1
        elif ch==')': parens-=1
        elif ch=='[': brackets+=1
        elif ch==']': brackets-=1
    if braces<0 or parens<0 or brackets<0:
        print('negative at',i,braces,parens,brackets)
        break
print('final counts',braces,parens,brackets)
