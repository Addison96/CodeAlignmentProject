# -*- coding: utf-8 -*- 
# import os
# print(os.getcwd()) # getcwd : Get current working directory


### 파일 읽기  ###
# with open("//Users//giselle//Desktop//hello.c", "r") as file:
    ## 1. read 함수 ##
    # x = file.read() # 파일 내용 전체 읽어옴
    # print(x)

    ## 2. for문 사용 ##
    # for line in file :
    #     print(line.strip())
    #     # 파일 각 줄의 끝에 줄바꿈 문자가 포함돼서 strip() 사용
    #     # strip : 공백, 문자열 제거
    
    ## 3. readline 함수 ##
    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line.strip())

    ## 4. readlines 함수 ##
    # cSource = file.readlines()

    # print(cSource)


### sys.argv[] 사용 예제 ###

# import sys

# file_path = sys.argv[1]

# if len(sys.argv) != 2:
#     print("Insufficient arguments")
#     sys.exit()

# print("file_path : " + file_path)

### map(int, input().split())
# # 여러 수를 입력받을 때 리스트로 저장
# In = input().split()
# print(In)

# # 리스트를 바로 int형으로 바꿔줄 수 없음
# # map 함수를 써서 하나씩 입력받아 사용
# In1, In2 = map(int, input().split())
# print(In1, In2)


### try, except ###

# y = [10, 20, 30]

# try:
#     index, x = map(int, input("input : index and value : ").split())
#     print(y[index] / x)
# # zero division error 일때
# except ZeroDivisionError as e:
#     print("숫자를 0으로 나눌 수 없습니다.", e)
# # index error 일때
# except IndexError as e:
#     print("잘못된 인덱스 입니다.", e)
# # 모든 예외 에러 메시지를 출력할 때
# except Exception as e:
#     print("예외가 발생하였습니다", e)

# # 디버깅용
# print("hello world")

### os.walk() ###

# import os

# root = "//Users//giselle//Desktop//CSC"

# for path, dir, file in os.walk(root):
#     print("path      : ", path)
#     print("directory : ", dir)
#     print("file      :", len(file))
#     print("------------------------")

### os.join() ###

import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print(desktop_path)

# ### 실전 1 ###
# """
# 요구 조건 
# 1. 문장 끝 빈칸 제거 ㅇ
# 2. 하나의 파일 한정 ㅇ
# 3. 중괄호 시작, 끝에 따라 스페이스 추가
# """

# from dataclasses import dataclass

# @dataclass
# class BraceStoreType:
#     index : int
#     brace : str

# BraceInstances = []
# BILen = 0
# BraceCounter = 0
# file_path = "//Users//giselle//Desktop//hello.c"

# def findBraces(index, line):
#     if "{" in line and "}" in line:
#         return BraceStoreType(index, "{ }")
#     elif "{" in line:
#         return BraceStoreType(index, "{")
#     elif "}" in line:
#         return BraceStoreType(index, "}")
#     else:
#         return None

# # # 1. 파일 열기
# with open(file_path, "r") as read_file:

#     # line 마다 빈칸 제거
#     lines = [line.strip() for line in read_file]

# #     # line 다시 쓰기
# #     # with open("//Users//giselle//Desktop//hello.c", "w") as write_file:
# #     #     for line in lines:
# #     #         write_file.write(line + '\n')

#     # line 마다 '{' or '}' 찾기
#     for i, line in enumerate(lines, start = 1):
#         if findBraces(i, line) is not None:
#             BraceInstances.append(findBraces(i, line))

#     # 디버깅
#     # for i, brace_instance in enumerate(Brace_instances, start = 1):
#     #     print(f"{i} / {brace_instance.index} / {brace_instance.brace}")
# with open(file_path, "w") as write_file:
#     for i, line in enumerate(lines, start = 1):
#         instance = BraceInstances[BILen]
#         idx = instance.index
#         brc = instance.brace

#         if i == idx:
#             BILen += 1
#             if brc == "{":
#                 write_file.write("    " * BraceCounter + line + "\n")
#                 BraceCounter += 1
#             elif brc == "}":
#                 BraceCounter -= 1
#                 write_file.write("    " * BraceCounter + line + "\n")
#             else:
#                 write_file.write("    " * BraceCounter + line + "\n")
            
#         else:
#             write_file.write("    " * BraceCounter + line + "\n")

# 실전 2
"""
요구 조건
1. 범위 확장 : 여러 폴더 안의 하위 파일까지 전부
2.  
"""



# 실전 3
"""
요구 조건
1. GUI 구현해서 위 사항 적용
"""

