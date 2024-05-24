'''
2024년05월24일
202195057 손패택
'''
# with open() 을 이용하여 읽기 모드로 파일 객체 생성.
with open("test2.txt", "r") as f :
    for line in f :  # for문에 파일 객체를 지정하여 한 줄씩 반복하여 읽어온다.
        print(line)   # 터미널 창에 출력.
    
# with open 을 사용하면 f.close() 쓸 필요 없다.