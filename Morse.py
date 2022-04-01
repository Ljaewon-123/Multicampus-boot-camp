class Morse():
    def __init__(self,morse):
        # self.alphabet = alphabet
        # self.digit = digit
        # self.sp = sp
        self.morse = morse
    def text2Morse(self,input_data):   # 영문텍스트를 모스부호로
        morse = self.morse
        re = ''
        for data in input_data.upper():
            # print(data)
            if data.isalpha():
                for alpha in morse[0].keys():
                    if data == alpha:
                        print(morse[0][data], end=' ')
                        re += morse[0][data] + ' '
            elif data.isdigit():
                for dig in morse[1].keys():
                    if data == dig:
                        print(morse[1][data], end=' ')
                        re += morse[1][data] + ' '
            elif data.isspace():
                print(' ', end=' ')
                re += '  '
            else:
                for sp in morse[2].keys():
                    if data == sp:
                        print(morse[2][data], end=' ')
                        re += morse[2][data] + ' '
                        # print(data)
        return re
    def morse2Text(self,text):  # 모스부호를 영문 텍스트로
        morse = self.morse
        mo = text.split(' ')
        for am in range(len(mo) - 1, 0, -1):
            if mo[am] == '' and mo[am - 1] == '':
                del mo[am]
        # print(mo)

        for morse_text in mo:

            if morse_text == '':
                print(' ', end='')
                continue
            for i in range(3):
                for key, value in morse[i].items():
                    if morse_text == value:
                        print(key.lower(), end='')

# 파이썬이니까 딕셔너리 가능? c++처럼 구분안해도 될지도?? 대소문자 때문에 해야할듯
# 만약 alphabet을 리스트로 한다면 영문자 입력받을때 전부 upper(),lower() 사용해서 통일한다음 접목시켜야함
alphabet = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
            'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
            'U':'..-','V':'...-','W':'.--','X':'.--','Y':'-.--','Z':'--..'}
digit = {'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'----..',
         '9':'----.'}

sp = {'/':'-..-.','?':'..--..',',':'--..--','.':'.-.-.-',"+":'.-.-.','=':'-..-'}

morse = []
morse.append(alphabet)
morse.append(digit)
morse.append(sp)

# 한글자당 하나의 공백 한 공백당 3개의 공백
# sp는 다른단어와 붙어있음 만약에

input_data = 'lets meet 4 pm 2014.+='

m = Morse(morse)

text = m.text2Morse(input_data)
print()
m.morse2Text(text)
print()
text = '.-.. . - ...   -- . . -   ....-   .--. --   ..--- ----- .---- ....- .-.-.- .-.-. -..-'
m.morse2Text(text)






