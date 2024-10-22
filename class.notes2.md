## 6-1 파이썬 프로그래밍
  - 1000 미만의 자연수에서 3과 5의 배수의 총합을 구하시오
    입력 받을 값 : 1~999
    출력 하는 값 : 3,5의 배수
    
    python
      result = 0
      for n in range(1,1000) :
      if n % 3 == 0 or n % 5 == 0:
          result += n 
      print(result) 

## 6-3 게시판 페이징 하기

## 6-4 간단한 메모장 만들기
  - 필요한 기능 : 메모 추가하기, 메모 조회하기
  - 입력 받는 기능 : 메모 내용, 프로그램 실행 옵션
  - 출력값 : memo.txt
  - python memo.py -a "Life is too short"
    a : 실행옵션, memo.py 만들고 코드 입력은 터미널 창에서 진행
