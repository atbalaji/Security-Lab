import hashlib
import sys

password_hash = sys.argv[1]

def crack():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().split()

    for word in words:
        word_hash = hashlib.md5(word).hexdigest()

        if word_hash == password_hash:
            return word


def main():
    password = crack()

    if password:
        print('The password is `{0}`.'.format(password))
    else:
        print("The password can't be cracked using a dictionary attack.")


if __name__ == "__main__":
    main()


