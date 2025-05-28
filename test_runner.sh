#!/bin/bash

g++ codetest.cpp -o codetest || exit 1

for i in {1..4}; do
    echo "== 테스트 케이스 $i =="
    ./codetest test/input${i}.txt test/output${i}.txt

    # 결과 비교
    if diff -q test/output${i}.txt test/expected${i}.txt > /dev/null; then
        echo "✅ PASSED"
    else
        echo "❌ FAILED"
        echo "  [출력 결과]"
        cat test/output${i}.txt
        echo "  [예상 결과]"
        cat test/expected&{i}.txt
    fi
    echo
done
