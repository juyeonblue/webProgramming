# webProgramming
⚡️[Django] 웹 개발 레포 ⚡️

|프로젝트|내용|진행 상황|
|------|---|:---:|
|WebProject_1|html화면 만들기|완료|
|webproject_2_blog|블로그 만들기(classlion 실습)|**진행중**|
|webproject_3_exchange|환전 화면 - 세미나 2주차|완료|
|webproject_3_versionUp|환전 - form태그(POST활용)|high version 완료|
|webproject_4_wordcount|classlion 실습|완료|
|webproject_5|블로그(1:N Model 실습) - 세미나 2,3주차|**진행중**|
<br/>
<hr/>

### <가상 환경>   
#### 📍가상 환경 설정의 중요성   
**폴더를 생성할 때: 한 폴더 안에 한개의 가상 환경만 존재해야 한다.**   
❌:상위폴더 -> 가상환경, 프로젝트 폴더1, 프로젝트 폴더2, ...(이렇게 하면 안된다!!)   
⭕️:상위폴더 -> 가상환경, 프로젝트 폴더

<br/>

### <에러 메세지> 
#### 1. [python] urllib.error.URLError   
###### python 3.7 버전이어서 그런가 갑자기 아래와 같은 아래가 생겼다,,,!   
```python
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1076)>
```   
```python
해결책: 응용프로그램 -> python3.7 파일 클릭! -> Install Certificates.command 더블 클릭하여 실행!  
```
