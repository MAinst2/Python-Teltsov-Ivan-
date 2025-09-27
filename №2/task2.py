import re

def uniq(xs):
    s = set()
    r = []
    for x in xs:
        if x not in s:
            s.add(x)
            r.append(x)
    return r

def main():
    try:
        with open('log.txt', 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print('Не найден файл log.txt')
        return

    ipv4_re = re.compile(r'\b(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}\b')
    ts_re = re.compile(r'\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b')
    upper_re = re.compile(r'\b[А-ЯЁA-Z]{2,}\b')
    email_re = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

    ipv4 = uniq(ipv4_re.findall(text))
    ts = uniq(ts_re.findall(text))
    upper = uniq(upper_re.findall(text))

    print('IPv4:')
    for x in ipv4:
        print(x)

    print('\nTIMESTAMPS:')
    for x in ts:
        print(x)

    print('\nUPPERCASE:')
    for x in upper:
        print(x)

    sanitized = email_re.sub('[EMAIL PROTECTED]', text)
    with open('log_sanitized.txt', 'w', encoding='utf-8') as f:
        f.write(sanitized)
    print('\nСанитизированный лог записан: log_sanitized.txt')

if __name__ == '__main__':
    main()