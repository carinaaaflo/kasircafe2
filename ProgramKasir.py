import streamlit as st

st.title("Kasir Chilless Cafe")
st.write("-------------------------- Selamat Datang Di Chilless Cafe --------------------------")

menu = {
    "1. Chicken Ball  :           @23000",
    "2. French Fries  :           @15000",
    "3. Vanila Latte  :           @18000",
    "4. Rose Tea      :           @15000"
    "5. Dumpling      :           @12000",
    "6. Ice Cream     :           @10000",
    "7. Pecel Buaya Darat :       @200000",
    "8. Nasi Goreng Cacing Kremi :@150000",  
}
st.write("                      Chilless Cafe                      ")
st.write("====================== Daftar Menu ======================")
for i in menu:
    st.write("Daftar Menu : ", i, "\t Harga : ", menu[i])
st.write("=========================================================")

nama = st.text_input('Nama pelanggan')
beli = st.number_input("Pilih Menu : ")
jumlah =int(st.number_input("Jumlah Pesanan :"))
totalharga = jumlah*beli


st.write("====================== Detail Pembayaran ======================")
st.write("Nama pelanggan           : ",nama)
st.write("Menu yang dipesan        : ",beli)
st.write("Jumlah yang dipesan      : ",jumlah)
st.write("Total Biaya              : ",totalharga)
st.write("                TERIMA KASIH TELAH MEMESAN DI CAFE KAMI ")