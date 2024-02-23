import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data CSV
day_data = pd.read_csv("bike_day.csv")
hour_data = pd.read_csv("bike_hour.csv")


# sidebar
st.sidebar.write("# Dashboard")
st.sidebar.write("# Kelompok Independent")
menu = st.sidebar.selectbox(
    "", ["Dashboard(Data Mining)", "Pertanyaan Bisnis", "About Us"])

# Pilihan Dashboard
if menu == "Dashboard(Data Mining)":
    # Header dan Tabs
    st.title("Dashboard Analisis dan Visualisasi Clustering Penyewaan Sepeda")
    st.write("--------------------------------------------------------------")
    # sidebar checkbpx data per hari
    if st.sidebar.checkbox('Tampilkan Data Per Hari', False):
        st.header("Data Bike Per Hari")
        st.write("Data Bike Per Hari:")
        st.write(day_data.head())

        # Pembersihan Data
        st.subheader("Pembersihan Data Per Hari")
        st.write("Nilai yang Hilang/Null")
        missing_values = hour_data.isnull().sum()
        st.write(missing_values)

        # Tampilkan data yang akan dihapus karena duplikasi
        st.subheader("Pembersihan Data dari Duplikasi Data")
        st.write("Menghapus dan Menampilkan Data Duplikasi Per Hari  :")
        duplicates_products = day_data[day_data.duplicated()]
        st.write(duplicates_products)

        st.write("Data Bike Per Hari Setelah Hapus Data Duplikasi:")
        day_data.drop_duplicates(inplace=True)
        st.write(day_data.head())
        st.write(
            "========================================================================================")

    # sidebar checkbpx data per jam
    if st.sidebar.checkbox('Tampilkan Data Per Jam', False):
        st.header("Data Bike Per Jam")
        st.write("Data Bike Per Jam:")
        st.write(hour_data.head())

        # Pembersihan Data
        st.subheader("Pembersihan Data Per Day")
        st.write("Nilai yang Hilang/Null")
        missing_values = day_data.isnull().sum()
        st.write(missing_values)

        # Tampilkan data yang akan dihapus karena duplikasi
        st.subheader("Pembersihan Data dari Duplikasi Data")
        st.write("Menghapus dan Menampilkan Data Duplikasi Per Jam  :")
        duplicates_products = hour_data[hour_data.duplicated()]
        st.write(duplicates_products)

        st.write("Data Bike Per Jam Setelah Hapus Data Duplikasi:")
        hour_data.drop_duplicates(inplace=True)
        st.write(hour_data.head())
        st.write(
            "========================================================================================")
    # Eksplorasi Data
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    day_data = pd.read_csv("bike_day.csv")
    hour_data = pd.read_csv("bike_hour.csv")

    # Explorasi Data
    st.subheader("Eksplorasi Data")
    eda = plt.figure(figsize=(10, 6))
    sns.countplot(data=day_data, x='weathersit', hue='season')
    plt.title('Distribusi Weathersit berdasarkan Season')
    plt.xlabel('Weathersit')
    plt.ylabel('Count')
    plt.legend(title='Season')
    st.pyplot(eda)

    # Menghitung korelasi antar variabel
    day_data['dteday'] = pd.to_datetime(day_data['dteday'])
    correlation_matrix = day_data.corr()

    # Membuat heatmap korelasi
    kor = plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Heatmap Korelasi antar Variabel')
    st.pyplot(kor)


# Pilihan About Us
elif menu == "Pertanyaan Bisnis":
    day_data = pd.read_csv("bike_day.csv")
    hour_data = pd.read_csv("bike_hour.csv")

# Pertanyaan 1
    st.write(
        "## Pertanyaan 1 : Berapa Rata-rata jumlah sepeda yang dipinjam pada setiap hari dan setiap jam nya?")

    # Tabel Per Hari
    st.write("### Tabel jumlah sepeda yg dipinjam pada per hari")
    no1_tableh = day_data[['dteday', 'cnt']]
    no1_tableh = no1_tableh.rename(columns={
        'dteday': 'Tanggal', 'cnt': 'Jumlah'})
    st.write(no1_tableh)
    # Tabel Per Jam
    st.write("### Tabel jumlah sepeda yg dipinjam pada per hari")
    no1_table = hour_data[['hr', 'cnt']]
    no1_table = no1_table.rename(columns={
        'hr': 'Jam', 'cnt': 'Jumlah'})
    st.write(no1_table)

    # Visualisasi Data
    st.write("### Visualisasi Data")
    satu = plt.figure(figsize=(10, 6))
    sns.lineplot(x="dteday", y="cnt", data=day_data)
    plt.title("Rata-rata jumlah sepeda dipinjam setiap hari")
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Sepeda")
    st.pyplot(satu)

    hour_data.describe()

    satuj = plt.figure(figsize=(10, 6))
    sns.lineplot(x="hr", y="cnt", data=hour_data)
    plt.title("Rata-rata jumlah sepeda dipinjam setiap jam")
    plt.xlabel("jam")
    plt.ylabel("Jumlah Sepeda")
    st.pyplot(satuj)

    # Informasi Rata-rata, nilai max, dan nilai min jumlah penyewaan sepeda
    avg_pinjamhari = day_data['cnt'].mean()
    avg_pinjamjam = hour_data['cnt'].mean()
    max_cntHari = day_data['cnt'].max()
    max_cntJam = hour_data['cnt'].max()
    min_cntHari = day_data['cnt'].min()
    min_cntJam = hour_data['cnt'].min()

    # Menampilkan informasi untuk jumlah penyewaan sepeda
    with st.expander("Informasi Jumlah Peminjaman/Penyewaan"):
        st.write(f"Rata-rata Peminjaman Per Hari: {avg_pinjamhari:.2f} kali")
        st.write(f"Rata-rata Peminjaman Per Jam: {avg_pinjamjam:.2f} kali")
        st.write(
            f"Jumlah Peminjaman Terbanyak dari Per Hari: {max_cntHari} kali")
        st.write(
            f"Jumlah Peminjaman Terendah dari Per Hari: {min_cntHari} kali")
        st.write(
            f"Jumlah Peminjaman Terbanyak dari Per Jam: {max_cntJam} kali")
        st.write(f"Jumlah Peminjaman Terendah dari Per Jam: {min_cntJam} kali")

# pertanyaan 2
    st.write(
        "### Pertanyaan 2: Apakah terdapat perbedaan penggunaan sepeda pada hari kerja dan hari libur?")

    # Tabel
    st.write("### Tabel penggunaan sepeda pada hari kerja")
    no2_tablekerja = day_data[['dteday', 'workingday', 'cnt']]
    no2_tablekerja = no2_tablekerja.rename(columns={
        'dteday': 'Tanggal', 'workingday': 'Hari Kerja', 'cnt': 'Jumlah'})
    st.write(no2_tablekerja)
    st.write("### Tabel penggunaan sepeda pada hari libur")
    no2_tablelibur = day_data[['dteday', 'holiday', 'cnt']]
    no2_tablelibur = no2_tablelibur.rename(columns={
        'dteday': 'Tanggal', 'holiday': 'Hari Libur', 'cnt': 'Jumlah'})
    st.write(no2_tablelibur)

    # Visualisasi Data
    st.write("### Visualisasi Data")
    perbedaan_penggunaan_harilibur_dan_kerja = day_data.groupby('workingday')[
        'cnt'].mean()

    dua = plt.figure(figsize=(8, 5))
    sns.barplot(x=perbedaan_penggunaan_harilibur_dan_kerja.index,
                y=perbedaan_penggunaan_harilibur_dan_kerja.values)
    plt.title("Perbedaan Penggunaan Sepeda pada hari kerja dan hari libur")
    plt.ylabel("Hari")
    plt.ylabel("Rata-Rata Jumlah Sepeda")
    plt.xticks(ticks=[0, 1], labels=["Hari Libur", "Hari Kerja"])
    st.pyplot(dua)

    # Informasi Rata-rata perbedaan penggunaan sepeda pada hari libur dan kerja
    avg_penggunaan_hari_kerja = day_data[day_data['workingday'] == 1]['cnt'].mean(
    )
    avg_penggunaan_hari_libur = day_data[day_data['workingday'] == 0]['cnt'].mean(
    )

    # Menampilkan informasi untuk perbedaan penggunaan sepeda pada hari libur dan kerja
    with st.expander("Informasi Jumlah perbedaan penggunaan sepeda pada hari libur dan kerja"):
        st.write(
            f"Rata-rata Peminjaman Per Hari Kerja: {avg_penggunaan_hari_kerja:.0f} kali")
        st.write(
            f"Rata-rata Peminjaman Per Hari Kerja: {avg_penggunaan_hari_libur:.0f} kali")

# pertanyaan 3
    st.write(
        "### Pertanyaan 3: Bagaimana distribusi peminjaman sepeda per jam berdasarkan hari dalam seminggu?")

    # Tabel
    st.write("### Distribusi peminjaman sepeda per jam dalam seminggu")
    no3_tabel = day_data[['dteday', 'weekday', 'cnt']]
    no3_tabel = no3_tabel.rename(columns={
        'dteday': 'Tanggal', 'weekday': 'weekday', 'cnt': 'Jumlah'})
    st.write(no3_tabel)

    # Visualisasi Data
    tiga = plt.figure(figsize=(12, 6))
    sns.pointplot(x='hr', y='cnt', hue='weekday',
                  data=hour_data, palette='husl')
    plt.title('Hourly Bike Rentals by Day of the Week')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Hourly Bike Rentals')
    plt.legend(title='Day of the Week')
    plt.show()
    st.pyplot(tiga)

    # Informasi Menemukan jam dengan jumlah sewa terbanyak setiap harinya
    jam_sewa_terbanyak = hour_data.groupby(
        'weekday')['cnt'].idxmax().apply(lambda x: hour_data.loc[x]['hr'])
    # Informasi Menghitung total jumlah sepeda yang disewa setiap harinya
    total_sepeda_sewa = hour_data.groupby('weekday')['cnt'].sum()

    # Menampilkan informasi
    with st.expander("Informasi Jumlah distribusi peminjaman sepeda per jam berdasarkan hari dalam seminggu"):
        st.write(
            "Menemukan jam dengan jumlah sewa terbanyak setiap harinya: ", jam_sewa_terbanyak)
        st.write(
            "Menghitung total jumlah sepeda yang disewa setiap harinya: ", total_sepeda_sewa)

# pertanyaan 4
    st.write("### Pertanyaan 4: Bagaimana perbandingan jumlah penurunan jumlah peminjaman sepeda antara hari kerja dan hari libur?")

    # Tabel
    st.write("### Jumlah Peminjaman Sepeda per Hari Kerja dan Hari Libur")
    no4_tabel = hour_data[['dteday', 'workingday', 'cnt']]
    no4_tabel = no4_tabel.rename(columns={
                                 'dteday': 'Tanggal', 'workingday': 'Hari Kerja', 'cnt': 'Jumlah Peminjaman'})
    st.dataframe(no4_tabel)

    # Visualisasi Data
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='workingday', y='cnt', data=hour_data, ax=ax)
    ax.set_title('Total Bike Rentals on Weekends vs. Workdays')
    plt.xticks(ticks=[0, 1], labels=["Hari Libur", "Hari Kerja"])
    ax.set_xlabel('Working Day')
    ax.set_ylabel('Total Bike Rentals')
    st.pyplot(fig)

    # Informasi
    with st.expander("Informasi Perbandingan Jumlah Penurunan Peminjaman Sepeda Antara Hari Kerja dan Hari Libur"):
        st.write(
            "Jumlah peminjaman sepeda cenderung lebih tinggi pada hari kerja dibandingkan dengan akhir pekan.")

# Pertanyaan 5
    st.write("### Pertanyaan 5: Bagaimana Tampilan visualisasi Perbandingan Jumlah Registrasi antara Tahun Pertama dan Tahun Kedua?")

    day_data['dteday'] = pd.to_datetime(day_data['dteday'])
    data_tahun_pertama = day_data[day_data['dteday'].dt.year ==
                                  day_data['dteday'].dt.year.min()]
    data_tahun_kedua = day_data[day_data['dteday'].dt.year ==
                                day_data['dteday'].dt.year.max()]
    jumlah_registrasi_tahun_pertama = data_tahun_pertama['registered'].sum()
    jumlah_registrasi_tahun_kedua = data_tahun_kedua['registered'].sum()

    # Tabel
    df_registrasi = pd.DataFrame({
        'Tahun': ['Tahun Pertama', 'Tahun Kedua'],
        'Jumlah Registrasi': [jumlah_registrasi_tahun_pertama, jumlah_registrasi_tahun_kedua]
    })
    st.write(
        "### Tabel Perbandingan Jumlah Registrasi antara Tahun Pertama dan Tahun Kedua")
    st.write(df_registrasi)
    tahun = ['Tahun Pertama', 'Tahun Kedua']
    jumlah_registrasi = [jumlah_registrasi_tahun_pertama,
                         jumlah_registrasi_tahun_kedua]

    # Visualisasi Data
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(tahun, jumlah_registrasi, color=['lightgreen', 'lightblue'])
    ax.set_title(
        'Perbandingan Jumlah Registrasi antara Tahun Pertama dan Tahun Kedua')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Jumlah Registrasi')
    st.pyplot(fig)

    # Informasi
    with st.expander("Informasi Perbandingan Jumlah Registrasi antara Tahun Pertama dan Tahun Kedua"):
        st.write(
            "Dalam analisis ini, kami membandingkan jumlah registrasi antara tahun pertama dan tahun kedua.")
        st.write(
            f"Jumlah registrasi pada tahun pertama: {jumlah_registrasi_tahun_pertama}")
        st.write(
            f"Jumlah registrasi pada tahun kedua: {jumlah_registrasi_tahun_kedua}")
        st.write("Dari visualisasi grafik di atas, terlihat bahwa terdapat peningkatan jumlah registrasi dari tahun pertama ke tahun kedua.")

# Pertanyaan 6
    st.write("### Pertanyaan 6: Bagaimana hubungan antara cuaca(weathersit) dengan jumlah sepeda yang dipinjam pada jam tertentu?")

    avg_bike_count_by_weather = hour_data.groupby("weathersit")["cnt"].mean()

    # Tabel
    st.write("#### Tabel Data Jumlah Sepeda Dipinjam Berdasarkan Cuaca (weathersit)")
    st.write(avg_bike_count_by_weather.reset_index().rename(
        columns={"weathersit": "Tipe Cuaca", "cnt": "Rata-Rata Jumlah Sepeda"}))

    # Visualisasi data
    plt.figure(figsize=(10, 5))
    sns.barplot(x="weathersit", y="cnt", data=hour_data)
    plt.title("Pengaruh Cuaca Terhadap Jumlah Sepeda Dipinjam")
    plt.xlabel("Tipe Cuaca\n1: Clear, Few clouds, Partly cloudy, Partly cloudy\n2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")
    plt.ylabel("Rata-Rata Jumlah Sepeda")
    fig = plt.gcf()
    st.pyplot(fig)

    # Informasi
    with st.expander("Informasi Hubungan antara Cuaca dan Jumlah Sepeda Dipinjam"):
        st.write("Dalam analisis ini, kami mengamati hubungan antara cuaca (weathersit) dengan jumlah sepeda yang dipinjam pada jam tertentu.")
        st.write("Dari visualisasi grafik di atas, terlihat bahwa jenis cuaca tertentu memiliki pengaruh terhadap jumlah sepeda yang dipinjam.")
        st.write("Misalnya, cuaca dengan kode 1 (Clear, Few clouds, Partly cloudy, Partly cloudy) memiliki rata-rata jumlah sepeda yang dipinjam lebih tinggi daripada cuaca dengan kode 3 (Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds).")


# Anggota kelompok
elif menu == "About Us":
    st.title("Kelompok Independent")
    st.markdown(" **Anggota**:")
    st.markdown("  - 10122351 - Rifqi Khoerul Assidiq")
    st.markdown("  - 10122354 - Jafar Shidiq")
    st.markdown("  - 10122362 - Louis Jonathan")
    st.markdown("  - 10122368 - Hamdan Fauzi")
    st.markdown("  - 10122374 - Wildan Dwi Wijaksana")
    st.markdown("  - 10122384 - Aziyusman Maulana")
