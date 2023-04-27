# Git Hub

## 기본개념 설명

git 과 git hub 에대한 간단한 설명을 먼저 하자면 

git은 프로그램이고 git hub는 서비스 이다 

내가 git에서 add와 commit을 하고나면 push 을 해서 git hub에 push를 하고 내 컴퓨터에 자료가 없어도 깃허브에서 pull로 자료를 다시 가져올수 있다.

## 계정확인

git 과 github를 이어주기 전에 확인해야하는것이 있는데 깃과 깃허브에서 사용하는 계정을 이어주는 것이다 .

```
git config --global user.name "name"
```

```
git config --global user.email "email@a.com"
```

위 두명령어로 입력을 해주고 

아래명령어로 현재 깃에 입력된 계정을 확인 가능하다

```
git config --global --list  /현재 확인
```



## push & pull

간단한 명령어 와 설명을 하겠다.

```
git remote add origin 주소	
```

ex) 내 깃허브에 lifecylce 에 주소를 연결하는 것이다

```
git remote add origin https://github.com/Ljaewon-123/lifecylce.git
```

주소는 다음과 같이 repositories에서 Code를 눌러 확인 가능하다.

![image-20211231213927863](TIL(git특강_2).assets/image-20211231213927863.png)

간단한 명령어 부터 차례로 써보자면

```
git remote -v   = 긁어온 주소 나타냄
```

```
git pull origin master     깃허브에서 내려받기
git push origin maste	   깃허브에 올리기

git push origin 브랜치 이름
git pull origin 브랜치 이름
```

##  clone

> 깃허브에서 레파즈토리를 만든 다음에 이미 커밋까지 끝난 깃의 파일과 연결시켜 주는게 `git remote add origin '주소'	`이고 클론은 이미 깃허브에서 먼저 만들어져있던 레파즈토리에서 파일 디렉토리를 끌어올수 있다 이말은` 다른 사람의 코드나 모듈도 클론으로 가져올수있다는 말이된다`

```
git clone 카피한 주소 
```

git init 과 clone는 처음 한번만 찍는다.

* 로컬에서 시작한다 -> git init -> add commit -> 온라인으로 가서 방을 받고 주소를 연결한다 ->git remote add로
* 온라인에서 시작한다 -> git clone 주소 -> 해당 클론을 받은 곳에 폴더가 생기며 그 폴더는 이미 깃의 관리를 받고 있다 

결론 둘다 git init 와 git clone 는 한번만 작성하는 명령어 이다.

## 충돌오류

컨클루션  == 충돌 오류 에 관해

로컬이 그대로 있는데 허브를 먼저 수정했을때 와 같이 서로의 파일이 같아지지 않은 순간에
push 를 하게 되면 나타나며 
push 를 해버렸다면 그 이후에 pull을 하여 내용을 정리하고
저장후 다시 add commit push를 사용해서 안정적으로 수정한다.

## branch

브렌치는 checkout 과 유사한 사용이고 몇 커밋전의 history를 확인할수 있다는 점이 유사하다

하지만 차이점이라면 branch는 branch별로 나눠서 메인은 남겨둔채 branch별로 따로따로 코딩 한후에 유익한 부분을 합칠수있다는 것이다.

> 물론 중간중간 add와 commit는 해줘야한다.

명령어를 한번에 올리자면

![image-20211231215612973](TIL(git특강_2).assets/image-20211231215612973.png)

```
git branch -> 현재 어떤 브랜치가 내 작업공간에 있는지 확인

git switch 브랜치명

git branch -D {브랜치 이름}  지우는 명령어 

git merge 다른 브랜치명   이거를 마스터에서 하면 다른 브랜치에 코드가 마스터로 들어옴
```

가있다.

git merge 같은 경우는 master에서 git merge water을 치게되면

`다른 브렌치에있던 코드가 마스터로 돌아오게된다.`

