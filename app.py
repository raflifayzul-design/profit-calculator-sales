import streamlit as st

st.set_page_config(page_title='Profit Calculator Reseller', page_icon='📈', layout='centered')

def rupiah(v):
    return 'Rp' + f'{v:,.0f}'.replace(',', '.')

st.title('📈 Profit Calculator')
st.caption('Simulasi keuntungan reseller • Harga dan kuantitas dalam kilogram (kg)')
st.info('Masukkan harga per kg dan jumlah kg untuk menghitung potensi keuntungan reseller.')

col1, col2 = st.columns(2)
with col1:
    harga_beli = st.number_input('Harga beli reseller (Rp/kg)', min_value=0.0, value=45000.0, step=1000.0, format='%.0f')
with col2:
    harga_jual = st.number_input('Harga jual reseller (Rp/kg)', min_value=0.0, value=65000.0, step=1000.0, format='%.0f')
kuantitas = st.number_input('Kuantitas penjualan (kg)', min_value=0.0, value=10.0, step=0.5, format='%.2f')
biaya_tambahan = st.number_input('Biaya tambahan (Rp/kg, opsional)', min_value=0.0, value=0.0, step=500.0, format='%.0f', help='Contoh: ongkir, kemasan, atau biaya transaksi per kg.')

laba_kg = harga_jual - harga_beli - biaya_tambahan
modal = harga_beli * kuantitas
omzet = harga_jual * kuantitas
biaya = biaya_tambahan * kuantitas
laba = laba_kg * kuantitas
margin = laba_kg / harga_jual * 100 if harga_jual > 0 else None
markup = laba_kg / (harga_beli + biaya_tambahan) * 100 if (harga_beli + biaya_tambahan) > 0 else None

st.divider()
st.subheader('Hasil simulasi')
a,b = st.columns(2)
a.metric('Laba per kg', rupiah(laba_kg))
b.metric('Profit margin', f'{margin:.2f}%' if margin is not None else '—')
c,d = st.columns(2)
c.metric('Potensi laba total', rupiah(laba))
d.metric('Markup', f'{markup:.2f}%' if markup is not None else '—')
st.write(f'**Total modal produk:** {rupiah(modal)}')
st.write(f'**Total biaya tambahan:** {rupiah(biaya)}')
st.write(f'**Estimasi omzet:** {rupiah(omzet)}')
st.write(f'**Total biaya modal + tambahan:** {rupiah(modal + biaya)}')

if harga_jual == 0:
    st.warning('Harga jual harus lebih dari Rp0/kg untuk menghitung margin.')
elif laba_kg < 0:
    st.error('Harga jual lebih rendah dari biaya per kg. Simulasi menunjukkan kerugian.')
elif laba_kg == 0:
    st.warning('Simulasi menunjukkan titik impas sebelum biaya lain yang belum dimasukkan.')
else:
    st.success('Simulasi menghasilkan potensi keuntungan positif.')

summary = f'''SIMULASI PROFIT RESELLER\nHarga beli: {rupiah(harga_beli)}/kg\nHarga jual: {rupiah(harga_jual)}/kg\nKuantitas: {kuantitas:g} kg\nBiaya tambahan: {rupiah(biaya_tambahan)}/kg\nLaba per kg: {rupiah(laba_kg)}\nProfit margin: {f'{margin:.2f}%' if margin is not None else 'Tidak tersedia'}\nMarkup: {f'{markup:.2f}%' if markup is not None else 'Tidak tersedia'}\nTotal modal: {rupiah(modal)}\nEstimasi omzet: {rupiah(omzet)}\nPotensi laba total: {rupiah(laba)}\n\nCatatan: ini simulasi, bukan jaminan penjualan atau keuntungan.\n'''
st.download_button('⬇️ Download Ringkasan Simulasi', data=summary, file_name='simulasi_profit_reseller.txt', mime='text/plain', use_container_width=True)
st.caption('Margin = laba per kg ÷ harga jual per kg × 100%. Semua angka merupakan estimasi dan belum termasuk biaya lain yang tidak dimasukkan.')
