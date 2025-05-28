.PHONY: all test clean

all:
	g++ codetest.cpp -o codetest
	@for f in test/input*.txt; do \
		num=$$(basename $$f | sed 's/input//; s/.txt//'); \
		echo "== 테스트 케이스 $$num =="; \
		./codetest test/input$$num.txt test/output$$num.txt; \
	done

test:
	bash test_runner.sh

convert:
	python3 converter.py plane.cpp codetest.cpp

clean:
	rm -f codetest test/output*.txt