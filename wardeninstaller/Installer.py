import argparse, sys, os

def main():
    parser = argparse.ArgumentParser(description='Warden installer')
    parser.add_argument('home', nargs=1, help="Install the data in to this folder.")
    args = parser.parse_args()
    print args.home

if __name__ == '__main__':
    main()