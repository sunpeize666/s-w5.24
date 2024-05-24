'''
2024년05월24일
202195057 손패택
'''
with open("student.txt", "w") as f :
    for i in range(1, 6) : 
        student = input(str(i) + "번 학생 이름과 3과목 성적 입력(예:홍길동 78 98 100) : ")
        f.write(student + "\n")