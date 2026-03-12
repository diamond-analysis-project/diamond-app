import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("محلل شوائب الألماس 💎")

uploaded_file = st.file_uploader("ارفع صورة حجر الألماس...", type=["jpg", "png"])

if uploaded_file is not None:
    # تحويل الصورة لـ OpenCV
    image = np.array(Image.open(uploaded_file))
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # استخدام تقنية Threshold للبحث عن الشوائب (النقط الداكنة)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    
    # إيجاد العيوب
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    st.image(image, caption="الصورة الأصلية")
    st.write(f"تم اكتشاف {len(contours)} منطقة قد تكون شوائب في الحجر.")
    st.image(thresh, caption="التحليل البرمجي للشوائب (بالأبيض)")

