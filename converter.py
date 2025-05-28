# converter.py
import sys
import re

def convert_cpp_for_local_testing(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Step 1: 헤더 삽입 여부 확인
    has_fstream = any('#include <fstream>' in line for line in lines)

# Step 2: <fstream>이 없다면 iostream 다음 줄에 추가
    if not has_fstream:
        for idx, line in enumerate(lines):
            if '#include <iostream>' in line:
                lines.insert(idx + 1, '#include <fstream>\n')
                break
            
    new_lines = []
    injected = False
    inside_main = False

    for line in lines:
        if not injected and re.match(r'\s*int\s+main\s*\(', line):
            inside_main = True
            if 'argc' not in line:
                line = line.replace('main()', 'main(int argc, char* argv[])')
            new_lines.append(line)
            continue

        if inside_main and not injected and '{' in line:
            new_lines.append(line)
            new_lines.append("""\
    istream* in = &cin;
    ostream* out = &cout;
    ifstream fin;
    ofstream fout;
    if (argc >= 3) {
        fin.open(argv[1]);
        fout.open(argv[2]);
        in = &fin;
        out = &fout;
    }\n""")
            injected = True
            inside_main = False
            continue

        line = re.sub(r'\bcin\b', '(*in)', line)
        line = re.sub(r'\bcout\b', '(*out)', line)
        new_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"✅ 변환 완료 → {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❌ 사용법: python3 converter.py input.cpp output.cpp")
        sys.exit(1)
    convert_cpp_for_local_testing(sys.argv[1], sys.argv[2])
