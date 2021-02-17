{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "immediate-paste",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method NDFrame.head of    BiayaPromo  NilaiPenjualan\n",
       "0        1500           90500\n",
       "1        1800           89500\n",
       "2        1900          105000\n",
       "3        2050          103000\n",
       "4        2050           90500\n",
       "5        2100          104500\n",
       "6        2200          109500\n",
       "7        2400          150000\n",
       "8        3050          152000>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import sklearn\n",
    "\n",
    "dataset = pd.read_csv('Documents/Sales_Data.csv')\n",
    "dataset.iloc[:, :-1].values\n",
    "dataset.iloc[:, :1].values\n",
    "\n",
    "dataku = pd.DataFrame(dataset)\n",
    "dataku.head"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "short-adobe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
