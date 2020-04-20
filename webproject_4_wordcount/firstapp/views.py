from django.shortcuts import render

# Create your views here.

# render 함수는 3개의 인자까지 받을 수 있는데 첫 번째는 고정적으로 
# request라는 객체를 받아주고, 두 번째는 템플릿의 이름, 세 번째는 사전형 객체로써 사용한다. 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() # text에 작성한 것을 공백기준으로 나눠서 리스트로 만듬.
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})