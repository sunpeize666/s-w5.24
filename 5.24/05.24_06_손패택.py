'''
2024년05월24일
202195057 손패택
'''
# with open() 을 이용하여 읽기 모드로 파일 객체 생성.
with open("test2.txt", "r") as f :
    while True :   # 무한 반복하면서
        line = f.readline()    # 한 줄씩 읽어와서 변수에 저장.
        
        # 읽어 올 내용이 없으면 반복을 종료한다.
        if line == '' :
            break
            
        print(line)
    
# with open 을 사용하면 f.close() 쓸 필요 없다.