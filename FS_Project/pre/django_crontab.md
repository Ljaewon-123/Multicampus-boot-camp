# 장고 크론탭

`pip install django-crontab`

setting.py 에 APP 에 django-crontab 라는 설정해줌

setting.py와 같은경로에 py파일 생성 



`fcntl ` 가 윈도우 지원을 안해서 우분투에서 git을 이용해서 해봄



```python
python3 manage.py crontab add # 프로세스 생성
python3 manage.py crontab show #프로세스 보기
python3 manage.py crontab remove #프로세스 제거sudo corntab -l #프로세스 보기
python3 manage.py crontab run <hash_id> #id 값은 show했을때 나오는 id값이다, 디버깅하자
```

값이 계속 나오지는 않음 해당값을 어떻게 html 에 보여주지 ???

SetTime() 함수 사용으로 해결 

