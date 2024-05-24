'''
2024년05월24일
202195057 손패택
'''
# 파일을 open()
f = open("test.txt", "r")   # 읽기 모드로 test.txt 파일을 열어라.

# 파일의 내용을 읽어와서 변수에 저장.
text = f.read()

# 변수에 저장된 내용 출력
print(text)
 
# 파일 종료
f.close()