from pypinyin import lazy_pinyin


def text_to_pinyin(text: str) -> str:
    return ''.join(lazy_pinyin(text))

def load_custom_phrase(file_path: str) -> dict[str, str]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.split('\t')[0]: line.split('\t')[1].strip() for line in f.readlines() if line.strip() and not line.startswith('#')}


def add_custom_phrase(file_path: str, text: str, weight: int = 1):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'{text}\t{text_to_pinyin(text)}\t{weight}\n')

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('text', nargs='+', type=str)
    parser.add_argument('-w', '--weight', type=int, default=1)
    parser.add_argument('-f', '--file', type=str, default='custom_phrase.txt')
    args = parser.parse_args()
    custom_phrase = load_custom_phrase(args.file)
    for text in args.text:
        if text in custom_phrase:
            print(f'{text} 已存在')
            continue
        add_custom_phrase(args.file, text, args.weight)



if __name__ == '__main__':
    main()
