#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Dolar History - Ambito Financiero Scrapping
# https://github.com/st1tch-bl/dolar-history
#
# Copyright 2021 St1tch3
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests
import numpy as np
import pandas as pd


tipo = input('Ingrese 1 para Dolar Blue, 2 para Dolar Oficial o 3 para Dolar Turista: ')
url="0"
if tipo=="1":
    url = "https://mercados.ambito.com//dolar/oficial/historico-general/"

if tipo=="2":
    url = "https://mercados.ambito.com//dolar/informal/historico-general/"
if tipo=="3":
    url= "https://mercados.ambito.com//dolarturista/historico-general/"

desde = input('Ingrese Fecha de inicio (en formato Día-Mes-Año, Ejemplo,23-05-2021): ')
hasta = input('Ingrese Fecha de fin (en formato Día-Mes-Año, Ejemplo,23-05-2021): ')

req = requests.get(url+desde+'/'+hasta)

data = req.json()
data2= np.array(data)
if tipo=="3":
    df = pd.DataFrame(data2, columns = ['Fecha','Venta'])
    df = df.drop(labels=0, axis=0)
    df['Venta'] = df['Venta'].str.replace(",", ".").astype(float)
    df['Fecha']=pd.to_datetime(df['Fecha'])
    df = df.set_index("Fecha")
else:
    df = pd.DataFrame(data2, columns = ['Fecha','Compra','Venta'])
    df = df.drop(labels=0, axis=0)
    df['Compra'] = df['Compra'].str.replace(",", ".").astype(float)
    df['Venta'] = df['Venta'].str.replace(",", ".").astype(float)
    df['Fecha']=pd.to_datetime(df['Fecha'])
    df = df.set_index("Fecha")

print(df)
