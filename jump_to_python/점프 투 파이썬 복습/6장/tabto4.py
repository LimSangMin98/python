import sys
# sys 모듈 : 파이썬 스크립트에 전달된 명령줄 인수를 포함하는 리스트

src = sys.argv[1]

dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t",""*4)

f = open(dst, 'w')
f.write(space_content)
f.close()
# print(space_content)
# print(src)
# print(dst)

''' python 
python tabto4.py a.txt b.txt
a.txt
b.txt
 
'''