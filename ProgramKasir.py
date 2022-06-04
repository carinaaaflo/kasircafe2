import streamlit as st

st.title("Kasir Chilless Cafe")
st.write("-------------------------- Selamat Datang Di Chilless Cafe --------------------------")

menu = {
    "Chicken Ball":                23000,
    "French Fries" :               15000,
    "Vanila Latte" :               18000,
    "Rose Tea" :                   15000,
    "Dumpling" :                   12000,
    "Ice Cream" :                  10000,
    "Pecel Buaya Darat" :         200000,
    "Nasi Goreng Cacing Kremi" :  150000,  
}
st.write("                      Chilless Cafe                      ")
st.write("====================== Daftar Menu ======================")
for i in menu:
    st.write("Daftar Menu : ", i, "\t Harga : ", menu[i])
st.write("seluruh menu mempunyai PPN sebesar 10%")
st.write("=========================================================")

nama = st.text_input("Nama pelanggan")
beli = st.text_input("Pilih Menu : ")
jumlah = st.number_input("Jumlah Pesanan :")
harga = (beli * jumlah )
ppn = (harga * 0.1 )
Bayar = (harga+ppn)




st.write("====================== Detail Pembayaran ======================")
st.write("Nama pelanggan           : ",nama)
st.write("Menu yang dipesan        : ",beli)
st.write("Jumlah yang dipesan      : ",jumlah)
st.write("PPN                      : ",ppn)
st.write("Total Biaya              : ",Bayar)
st.write("                TERIMA KASIH TELAH MEMESAN DI CAFE KAMI ")