# 하위 디렉터리 검색 쉽게 해주는 os.walk
import os 
for (path, dir, files) in os.walk("C:/") : 
    for filename in files : 
        ext = os.path.splitext(filename)[-1]
        if ext == ".py" : 
            print(os.path.join(path, filename))


''' python 

C:/Users\임상민\AppData\Roaming\Python\Python311\site-packages\pythonwin\pywin\tools/browseProjects.py
C:/Users\임상민\AppData\Roaming\Python\Python311\site-packages\pythonwin\pywin\tools/browser.py
C:/Users\임상민\AppData\Roaming\Python\Python311\site-packages\pythonwin\pywin\tools/hierlist.py
C:/Users\임상민\AppData\Roaming\Python\Python311\site-packages\pythonwin\pywin\tools/regedit.py

이하 생략'''