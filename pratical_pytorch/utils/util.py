import re
from konlpy.tag import Okt

def preprocess_mixed_text(text):
    """한글과 영어가 섞인 텍스트 전처리 함수"""
    # 1. 한글 부분 추출 및 처리
    korean_pattern = r'[가-힣]+'
    korean_words = re.findall(korean_pattern, text)
    korean_text = ' '.join(korean_words)
    
    # 2. 영어 부분 추출 및 처리
    english_pattern = r'[a-zA-Z]+'
    english_words = re.findall(english_pattern, text)
    english_text = ' '.join([word.lower() for word in english_words if len(word) > 1])
    
    # 3. 한글 형태소 분석 (한글이 있을 때만)
    korean_processed = ""
    if korean_text.strip():
        okt = Okt()
        morphs = okt.pos(korean_text, stem=True)
        korean_processed = ' '.join([word for word, pos in morphs if pos in ['Noun', 'Verb', 'Adjective']])
    
    # 4. 한글과 영어 결합
    result_parts = []
    if korean_processed.strip():
        result_parts.append(korean_processed)
    if english_text.strip():
        result_parts.append(english_text)
    
    return ' '.join(result_parts)