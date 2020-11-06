from typing import List, Dict
from collections import defaultdict


FILENAME = 'data_description.txt'
def read_file(filename: str=FILENAME) -> List[str]:
    with open(filename) as f:
        content = f.readlines()
    return [x.strip() for x in content]

def parse_file(contents: List[str]) -> Dict[str, List[str]]:
    data, key = defaultdict(list), None
    for cont in contents:
        if '\t' in cont: data[key].append(cont.split('\t')[0])
        elif ':' in cont: key = cont.split(':')[0]
    return data


if __name__ == '__main__':
    contents = read_file()
    data = parse_file(contents)
    print(data)