
def hello(number):
    print("Inside hello ", number, type(number))
    sum =0
    cnt =0
    while number>0:
        digit = number%10
        sum = sum*10 +digit
        number = number//10
        cnt = cnt +1
    print("Rev", sum, type(sum))
    return str(sum)       


def string_test():
    st = 'My First '
    st1 = "Return statment is :"
    st2 = '''
      dklfajdflkjdf
      dsflkajdflksdf
      sdflkjalkfsd
      falkdfjalkdfs
      dfalkdfjaldf
      dlkfjaldkfd
      fdlkfjalkdf
      dflkajfdlkadf
      dlkfjalkf
      dklfajdflksdf
      lkdjfalkdf
      '''
    con= st+st1+st2
    return con