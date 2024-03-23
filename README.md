## wk04 seq_step

* Exercise file 실습파일 : wk04.py
* Complete function `wk04()` as follows.<br>함수 `wk04()`을 다음과 같이 완성하시오.
* Accept following arguments<br>다음과 같은 매개변수를 받아들이시오 :

argument<br>매개변수 | type<br>변수형 | description<br>설명
:-----:|:-----:|-----
`f` | `Callable[[float], float]` | the function that we want to find `x` satisfying $f(x)=0$<br>근을 찾고 싶은 함수<br>takes one float as input and returns a float<br>입력으로 실수 하나를 받아 들이고 결과값으로 실수 하나를 반환할 것임
`xp` | `float` | the argument of function `f` of the previous step<br>함수 `f`의 이전 단계의 매개변수
`delta_x` | `float` | increment of `x` (difference between `x`s of this & previous steps)<br>`x`의 증분 (이번 단계와 이전 단계의 `x`의 차이)
`epsilon` | `float` | degree of tolerance<br>오차 허용 한계

* Return a dictionay with folliwing key-value pairs<br>다음과 같은 key-value 를 담은 `dict`를 반환하시오.

key | type of value<br>value 의 자료형 | description<br>설명
:-----:|:-----:|-----
`'x'` | `float` | `x` for this step of sequential method<br>순차법에서 이번 단계의 `x`
`'found'` | `bool` | whether the `x` of this step satisfies<br>이번 단계의 `x`가 만족하는가?

* Withtin the file, leave lines belong to the functions only.<br>해당 파이썬 스크립트 파일에는 해당 함수만 제출 바랍니다.
* Do not use any other modules<br>다른 모듈은 사용하지 마시오.
* Change wk04.py file only<br>wk04.py 파일만 변경하시오.

## How to use Github web editor<br>Github 웹 편집기 사용법
* Press <kbd>.</kbd> key to start MS VS Code web editor<br><kbd>.</kbd> 키를 누르면 MS VS Code 의 Web version 이 시작됨
* Make changes to the file<br>파일을 수정
* From the left bar with the three horizontal lines at the top, (right below the magnifying glass) choose third icon, Source Control<br>왼쪽에서 줄 셋 아래 (확대경 다음) 세번째 가지치기 아이콘 선택
* Choose filename to see changes<br>변경 사항을 보려면 파일 이름 선택
* To stage changes to commit, choose + on the right side of the filename <br>수정 사항을 commit 등록 대상으로 add 추가 하려면 파일 이름의 오른쪽 + 기호 선택
* Describe the changes in the blank above<br>위 빈칸에 변경 사항 설명 입력
* Choose Commit<br>[커밋 및 푸시] 선택
* To return to the repository, use the command in the three horizontal lines<br>줄 셋 의 [리포지토리로 이동] 선택하여 저장소로 복귀
