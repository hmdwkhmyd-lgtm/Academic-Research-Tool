import streamlit as st
import os

st.set_page_config(page_title="أداة خالد سعيد للبحث الأكاديمي", layout="wide")

st.title("🔬 أداة خالد سعيد للبحث الأكاديمي")
st.write("مرحباً بك في تطبيقك الخاص يا دكتور خالد. هذا التطبيق مصمم لمساعدتك في أبحاث الصيدلة.")

# كود عرض الصور مع التأكد من إغلاق الأقواس
images = [img for img in os.listdir() if img.endswith((".jpg", ".png", ".jpeg"))]

if images:
    st.subheader("📸 معرض الصور")
    st.image(images, width=200)
else:
    st.info("لا توجد صور حالياً في المجلد.")

st.sidebar.header("إعدادات البحث")
search_query = st.sidebar.text_input("ابحث عن دواء أو بحث:")
if search_query:
    st.success(f"جاري البحث عن: {search_query}")

