'''
2024년05월24일
202195057 손패택
'''
# 파일을 open()
f = open("test.txt", "w")   # 쓰기 모드로 test.txt 파일을 열어라.
# test.txt 파일이 없으면 알아서 만들어 열어준다.

# 파일에 쓸 내용 작성.
for i in range(1, 11) :
    f.write(f"{i}번째 메세지입니다. \n")  # \n => 줄바꿈.
    # write() => 출력. : 파일에 출력.
 
# 파일 종료
f.close()