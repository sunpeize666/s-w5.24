'''
2024년05월24일
202195057 손패택
'''
# with open() 을 이용하여 읽기 모드로 파일 객체 생성.
with open("test2.txt", "r") as f :
    # 파일의 내용을 읽어서 리스트로 만들어 변수에 저장.
    textlist = f.readlines()
    
    print(textlist)
    print("textlist의 자료형 : ", type(textlist))
    
# with open 을 사용하면 f.close() 쓸 필요 없다.
