all: genanswer testcase
genanswer:
	cat  testcase.txt | python workspace.py > generate.txt
testcase: generate.txt
	diff answer.txt generate.txt
