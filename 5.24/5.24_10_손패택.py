'''
2024년05월24일
202195057 손패택
   읽기 모드 => r
    파일 읽기 = readline()   => while True 사용
    
    [알고리즘]
        1. 학생 이름과 성적을 읽어 올 파일로 f 객체 만들기.
        2. 반복하면서 내용 읽어오기
            2-1. 출력하기
'''
with open("student.txt", "r") as f:
    while True :
        student = f.readline()
        
        if student == '' :
            break
        
        print(student)