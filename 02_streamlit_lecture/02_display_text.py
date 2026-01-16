"""
2단계: 텍스트 출력 함수들
학습 목표: 다양한 방식으로 텍스트 출력하기
"""

import streamlit as st

# ============================================
# 1. 제목과 헤더
# ============================================
st.title("📝 텍스트 출력 함수 배우기")
st.header("1. 제목과 헤더")
st.subheader("이것은 소제목입니다")

st.write("""
Streamlit은 다양한 방식으로 텍스트를 출력할 수 있습니다.  
각 함수의 용도를 이해하고 적절히 사용하는 것이 중요합니다.
""")

# ============================================
# 2. 일반 텍스트
# ============================================
st.divider()
st.header("2. 일반 텍스트")

st.text("이것은 st.text() 함수입니다.")
st.write("이것은 st.write() 함수입니다. - 가장 많이 사용됩니다!")

# st.write는 마크다운도 지원합니다
st.write("**굵은 글씨**, *기울임*, ~~취소선~~")

# ============================================
# 3. 마크다운
# ============================================
st.divider()
st.header("3. 마크다운")

st.markdown("""
### 마크다운으로 작성한 소제목

마크다운을 사용하면 더 풍부한 서식을 사용할 수 있습니다:
- **굵은 글씨**
- *기울임*
- `코드 강조`
- [링크](https://streamlit.io)

#### 리스트
1. 첫 번째
2. 두 번째
3. 세 번째
""")

# ============================================
# 4. 코드 블록
# ============================================
st.divider()
st.header("4. 코드 블록")

st.code("""
def hello():
    print("Hello, Streamlit!")
    return "안녕하세요"
""", language="python")

# 다른 언어도 가능합니다
st.code("""
SELECT * FROM users
WHERE age > 20
ORDER BY name;
""", language="sql")

# ============================================
# 5. 수식 (LaTeX)
# ============================================
st.divider()
st.header("5. 수식")

st.latex(r"""
E = mc^2
""")

st.latex(r"""
\sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n
""")

# ============================================
# 6. 상태 메시지
# ============================================
st.divider()
st.header("6. 상태 메시지")

st.success("✅ 성공 메시지 - 작업이 성공적으로 완료되었습니다!")
st.info("ℹ️ 정보 메시지 - 유용한 정보를 제공합니다.")
st.warning("⚠️ 경고 메시지 - 주의가 필요합니다.")
st.error("❌ 에러 메시지 - 문제가 발생했습니다.")

# ============================================
# 7. 기타 유용한 함수
# ============================================
st.divider()
st.header("7. 기타 유용한 함수")

st.caption("이것은 작은 설명 텍스트입니다 (캡션)")

# 인용문
st.markdown("> 누구나 코딩을 할 수 있다. - 김정륭")

# 인터넷상 이미지
st.caption("인터넷상 이미지 표시")
st.image("data:image/jpeg;base64,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")

# 이미지 사이즈를 화면에 맞추고싶다면? 강제로 늘릴 수 있음
st.image("https://placehold.co/300x300")
# st.image("https://placehold.co/300x300", use_container_width=True)

# 로컬 이미지
st.caption("내 컴퓨터의 이미지 표시")
st.image('image/sample1.jpg')

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제: 뉴스 기사 만들기

다음 요소들을 포함한 가상의 뉴스 기사를 만들어보세요:
1. `st.title()`로 기사 제목
2. `st.caption()`으로 작성자와 날짜
3. `st.image()`로 이미지 (URL 사용 가능)
4. `st.markdown()`으로 본문 내용
5. `st.info()`로 관련 정보 박스
6. `st.code()`로 코드나 데이터 예시
""")

# 예시 답안 (접어두기)
with st.expander("💡 예시 답안 보기"):
    st.title("🚀 AI 기술의 새로운 돌파구")
    st.caption("작성자: 홍길동 | 2026-01-15")
    
    st.image("https://placehold.co/600x400", caption="AI 연구소")
    
    st.markdown("""
    최근 연구진이 새로운 AI 알고리즘을 개발했다고 발표했습니다.
    
    이 기술은 기존 방식보다 **50% 더 빠른** 처리 속도를 보여줍니다.
    """)
    
    st.info("이 기술은 2027년 상용화될 예정입니다.")
