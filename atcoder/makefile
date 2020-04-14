CXXFLAGS=-std=c++14 -Wall
CC = g++

# workspace: workspace.cpp
# clean:
# 	rm workspace
py: genanswerpy testcase
cpp: genanswercpp testcase

workspace: workspace.o
	$(CC) -o workspace workspace.o
workspace.o: workspace.cpp
	$(CC) $(CFLAGS) -c workspace.cpp
genanswercpp: workspace
	cat  testcase.txt | ./workspace > generate.txt
genanswerpy:
	cat  testcase.txt | python workspace.py > generate.txt
testcase:
	diff answer.txt generate.txt && echo -e "\e[32mSuccess!\e[m"
