import os

from shared.models import Site
from project1.crawler import google_crawler


def display_sites(is_interested=False):
    sites = Site.get_sites(is_interested)
    for site in sites:
        site.pretty_print()
        print '-' * 50


def decide_is_interested():
    yes_answers = ['y', 'yes', 't', 'tak']
    sites = Site.get_sites(is_interested=False)
    for site in sites:
        os.system('clear')
        site.pretty_print()
        print 'Type "exit" to back.\n'
        option = raw_input('Is interested? [y/n] ')
        if option in yes_answers:
            site.is_interested = True
            site.save()
        if option == 'exit':
            break
    os.system('clear')


def main():
    os.system('clear')
    while True:
        points = 50
        print '##' * points
        print '1' + '.' * points + 'Use crawler.'
        print '2' + '.' * points + 'Dislay interested.'
        print '3' + '.' * points + 'Dislay not interested.'
        print '4' + '.' * points + 'Decide which result is interested.'
        print '5' + '.' * points + 'Dump database to file'
        print '0' + '.' * points + 'Exit.\n'

        option = raw_input('Option: ')
        if option == '1':
            phrases = raw_input('Enter phrase[s]: ').split(' ')
            for phrase in phrases:
                google_crawler(phrase)

        if option == '2':
            display_sites(is_interested=True)
            raw_input('Click to contiune... ')
        if option == '3':
            display_sites()
            raw_input('Click to contiune... ')

        if option == '4':
            decide_is_interested()

        if option == '5':
            filename = raw_input('Enter filename: ')
            Site.dump_all_to_file(filename)

        os.system('clear')
        if option == '0':
            return


if __name__ == '__main__':
    main()
