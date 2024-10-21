# C:/ 디렉터리와 그 하위 디렉터리 모든 파일 검색
# 
import os

def search(dirname) :
    try : 
        # os listdir : 해당 디렉터리에 있는 파일들의 리스트
        # dirname : 경로를 포함한 파일 이름
        filenames = os.listdir(dirname)
        for filename in filenames : 
            
            # os.path.join : 디렉터리를 포함한 전체 경로를 구할 수 있다.
            full_filename = os.path.join(dirname, filename)

            if os.path.isdir(full_filename) :
                search(full_filename)
            else :
                # 파일이름에서 확장자만 추출하기 위해 splitext 사용
                # os.path.splitext : 파일 이름과 확장자로 분리
                # ex) example.txt -> (example,txt)
                # -1 : 시퀸스의 마지막 요소를 가르킨다 -> 확장자
                ext = os.path.splitext(full_filename)[-1]
                if ext  =='.py' : 
                    print(full_filename)
    
    # os.listdir를 수행할 때 권한이 없는 디렉터리에 접근시
    # 프로그램이 종료되지 않게 하기위해 예외처리
    except PermissionError :
        pass

search("C:/")
        
    

