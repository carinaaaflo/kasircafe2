import streamlit as st

st.title("                        Selamat Datang Di Tora Bika Cafe                     ")
st.write("""
    ==============================
    
    Tora Bika Cafe
    List Menu Minuman Kopi Dan Dessert
 
    ==============================
    A. ES Kopi Susu   : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam  : Rp 11.000
    D. Ice Americano  : Rp 14.000
    E. Rainbow Cake   : Rp 12.000
    F. Huzlenut Drink: Rp 18.000
    ==============================
    """)
    pesan= st.text_input("Pilihan Menu")
    jumlahpesan= st.number_input("masukkan jumlah pesanan :")

    if pesan == "ES Kopi Susu":
        harga = (11000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif pesan == "ES Kopi Coklat":
        harga = (12000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif pesan == "ES Kopi Hitam":
        harga = (11000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif pesan == "Ice Americano":
        harga = (14000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif pesan == "Rainbow Cake":
        harga =(12000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    elif pesan == "f":
        harga = (18000*jumlahpesan)
        ppn = (harga * 0.1)
        totalharga = (harga+ppn)
    
    st.write("--------------------------")
    st.write("TORA BIKA CAFE")
    st.write("--------------------------")
    st.write("Menu :", pesan )
    st.write("Jumlah Pesan :", jumlahpesan)
    st.write("Harga :", harga)
    st.write("PPN :", ppn)
    st.write("Bayar:", totalharga) 
