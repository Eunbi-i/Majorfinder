import base64
import glob
import os
import re
import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(page_title="전공탐색 MBTI", page_icon="🎓", layout="centered")

# 🎨 디자인 커스텀 CSS
st.markdown(
    """
<style>
    /* 전체 앱 배경을 흰색으로 고정 */
    .stApp {
        background-color: #FFFFFF !important;
        color: #1E293B !important;
    }

    /* 상단 헤더 스타일 */
    .header-sub1 {
        font-size: 14px !important;
        color: #64748B !important;
        margin-bottom: 4px !important;
    }
    .custom-title {
        font-size: 28px !important;
        font-weight: 800 !important;
        color: #0F172A !important;
        margin-top: 4px !important;
        margin-bottom: 4px !important;
        line-height: 1.2 !important;
    }
    .header-sub2 {
        font-size: 14px !important;
        color: #64748B !important;
        margin-bottom: 4px !important;
    }
    
    /* 질문 텍스트 스타일 */
    .question-title {
        font-size: 19px !important;
        font-weight: 700 !important;
        line-height: 1.4 !important;
        color: #0F172A !important;
        margin-top: 12px !important;
        margin-bottom: 12px !important;
        min-height: 80px !important;
        display: flex !important;
        align-items: center !important;
    }

    div[data-testid="stMarkdownContainer"] p, 
    div[data-testid="stMarkdownContainer"] span,
    label {
        color: #1E293B !important;
    }

    /* 🔘 일반 버튼 & 링크 버튼 통합 스타일 (테스트 다시하기와 동일하게 통일) */
    div.stButton > button[kind="secondary"],
    div.stButton > button:not([kind="primary"]),
    div[data-testid="stLinkButton"] > a,
    a[data-testid="stLinkButton"] {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        min-height: 52px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        white-space: normal !important;
        word-break: keep-all !important;
        line-height: 1.4 !important;
        padding: 10px 16px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        transition: all 0.2s ease !important;
        box-sizing: border-box !important;
    }

    /* 🔘 호버 및 액티브 반응 동일화 */
    div.stButton > button[kind="secondary"]:hover,
    div.stButton > button[kind="secondary"]:focus,
    div.stButton > button[kind="secondary"]:active,
    div.stButton > button:not([kind="primary"]):hover,
    div.stButton > button:not([kind="primary"]):focus,
    div.stButton > button:not([kind="primary"]):active,
    div[data-testid="stLinkButton"] > a:hover,
    div[data-testid="stLinkButton"] > a:focus,
    div[data-testid="stLinkButton"] > a:active,
    a[data-testid="stLinkButton"]:hover,
    a[data-testid="stLinkButton"]:focus,
    a[data-testid="stLinkButton"]:active {
        background-color: #E2E8F0 !important;
        color: #0F172A !important;
        border-color: #94A3B8 !important;
        box-shadow: none !important;
    }

    /* 🔴 Primary (주요 강조 버튼 및 선택된 답변) */
    div.stButton > button[kind="primary"] {
        background-color: #FF4B4B !important;
        color: #FFFFFF !important;
        border: 1px solid #FF4B4B !important;
        border-radius: 8px !important;
