from tkinter import Menu
import streamlit as st

st.title("                        Selamat Datang Di Tora Bika Cafe                     ")

contact_option= ["Vanilla Late 11000", "Es Kopi Coklat 12000", "Es Kopi Hitam 11000", 
"Ice Americano 14000","Rainbow Cake 12000", "Huzlenut Drink 18000" ]

st.header("Pilihan Menu")

contact_selected = st.selectbox("Pilihlah yang anda inginkan")
Option = (contact_option)
                                    
    jumlahpesan= st.number_input("masukkan jumlah pesanan :")

if Menu = "Vanilla Latte :"
        harga = (11000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif Menu = "ES Kopi Coklat:"
        harga = (12000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif Menu = "ES Kopi Hitam:"
        harga = (11000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif Menu = "Ice Americano:"
        harga = (14000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif Menu = "Rainbow Cake:"
        harga =(12000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif Menu = "Huzlenut Drink:"
        harga = (18000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    
    st.write("--------------------------")
    st.write("TORA BIKA CAFE")
    st.write("--------------------------")
    st.write("Menu :",Menu  )
    st.write("Jumlah Pesan :", jumlahpesan)
    st.write("Harga :", harga)
    st.write("PPN :", ppn)
    st.write("Bayar:", totalharga) 
