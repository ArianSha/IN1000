from datasenter import Datasenter

def hovedprogram():

    google = Datasenter()
    google.lesRegneklynge('abel.txt')
    google.lesRegneklynge('saga.txt')

    google.utskriftAlt()


if __name__ == '__main__':
    hovedprogram()