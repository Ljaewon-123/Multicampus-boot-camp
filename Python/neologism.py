class Word:
    def __init__(self,neo,a1,a2,anwer):
        self.neo = neo
        self.a1 = a1
        self.a2 = a2
        self.anwer = anwer
    def show_question(self):
        print(f'"{self.neo}"의 뜻은??\n'
              f'1.{self.a1}\n'
              f'2.{self.a2}')
    def check_answer(self,user_amwer):
        if self.anwer == user_amwer:
            print('correct')
        else:
            print('incorrect')


# word = Word('얼죽아','얼어 죽어도 아메리카노','얼굴만은 죽어도 아기피부',1)
word = Word('혼코노','혼자서는 코딩 노노','혼자 코인 노래방',2)
word.show_question()
word.check_answer(int(input('=> ')))