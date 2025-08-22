import streamlit as st
import random

# 영화 데이터 (예시)
movies = {
    "액션": [
        {"title": "존 윅", "desc": "킬러의 복수극", "img": "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg"},
        {"title": "매드맥스: 분노의 도로", "desc": "광기의 질주 액션", "img": "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg"},
        {"title": "다크 나이트", "desc": "히어로 명작", "img": "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg"}
    ],
    "로맨스": [
        {"title": "어바웃 타임", "desc": "시간여행 로맨스", "img": "https://upload.wikimedia.org/wikipedia/en/3/3c/About_Time_Poster.jpg"},
        {"title": "라라랜드", "desc": "꿈과 사랑의 뮤지컬", "img": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png"},
        {"title": "노트북", "desc": "운명적인 사랑 이야기", "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg"}
    ],
    "공포": [
        {"title": "겟 아웃", "desc": "인종차별 스릴러", "img": "https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png"},
        {"title": "컨저링", "desc": "실화 바탕의 공포", "img": "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg"},
        {"title": "인시디어스", "desc": "초자연적 공포", "img": "https://upload.wikimedia.org/wikipedia/en/2/2d/Insidious_poster.jpg"}
    ],
    "코미디": [
        {"title": "나홀로 집에", "desc": "크리스마스 코미디", "img": "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg"},
        {"title": "극한직업", "desc": "한국형 코믹 수사극", "img": "https://upload.wikimedia.org/wikipedia/en/f/f9/Extreme_Job_poster.jpg"},
        {"title": "주토피아", "desc": "동물들의 도시 코미디", "img": "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg"}
    ]
}

# 페이지 설정
st.set_page_config(page_title="넷플릭스 스타일 영화 추천", layout="wide")

# 앱 제목
st.markdown("<h1 style='text-align: center; color: red;'>🎬 Netflix Style Movie Recommender 🍿</h1>", unsafe_allow_html=True)
st.markdown("---")

# 장르 선택
genre = st.selectbox("장르 선택", list(movies.keys()))

# 버튼 클릭 시 영화 추천
if st.button("🎥 추천 받기"):
    selected_movies = random.sample(movies[genre], k=min(3, len(movies[genre])))

    # 넷플릭스 스타일: 3개 영화 가로로 배치
    cols = st.columns(len(selected_movies))
    for col, movie in zip(cols, selected_movies):
        with col:
            st.image(movie["img"], use_column_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{movie['title']}</h4>", unsafe_allow_html=True)
            st.caption(movie["desc"])
