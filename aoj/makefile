CXXFLAGS=-std=c++14 -Wall

py: genanswer testcase
cpp: cpptestcase
genanswer:
	cat  testcase.txt | python workspace.py > generate.txt
testcase: generate.txt
	diff answer.txt generate.txt

workspace_cpp: workspace_cpp.cpp
cpptestcase: workspace_cpp
	./workspace_cpp < testcase.txt > generate.txt
	diff answer.txt generate.txt
