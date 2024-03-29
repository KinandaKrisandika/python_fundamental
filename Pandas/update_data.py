import pandas as pd

data_update = pd.read_csv('./task_pandas_kinanda.csv') #untuk membaca file csv yang sudah tersimpan

data_update["Gender"] = ['L','L','L','L','L','P','P',
                         'L','L','P','L','L','P','L','L',
                         'L','L','L','L','L'] 

data_update["Alamat"] = ['Leuwigajah','Leuwiseeng','Leuwiliang',
                         'Leuwihteuing','Leuwihan','Leuwipanjang',
                         'Leuwihwih','Leuwihwah','Leuwiroyong',
                         'Leuwigar','Leuwigajah','Leuwiseeng','Leuwiliang',
                         'Leuwihteuing','Leuwihan','Leuwipanjang',
                         'Leuwihwih','Leuwihwah','Leuwiroyong',
                         'Leuwigar']

data_update["Pekerjaan"] = ['Pegawai Swasta','PNS','Wiraswasta','Influencer',
                            'Pegawai Swasta','PNS','Wiraswasta','Influencer',
                            'Pegawai Swasta','PNS','Wiraswasta','Influencer',
                            'Pegawai Swasta','PNS','Wiraswasta','Influencer',
                            'Pegawai Swasta','PNS','Wiraswasta','Influencer'] #Mengupdate data

data_update.to_csv(path_or_buf='./update_data.csv', index=False) #mengexport data
