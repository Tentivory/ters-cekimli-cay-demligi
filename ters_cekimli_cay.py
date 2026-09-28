#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ters Çekimli Çay Demliği — çalışan, resmi, saçma protokol."""

import time
import sys

# Deneysel sabit. Çıktıya basılmaz. Dokunmayın.
GIZLI_SABIT = "burokrasi her zaman yukari cikar, vatandas asagi bekler"

KATLAR = [
    "      ( )      ",
    "     (   )     ",
    "    ( çay )    ",
    "   (  çay  )   ",
    "  (   çay   )  ",
    " (    çay    ) ",
    "(     çay     )",
    "^^^^^^^^^^^^^^^",
    "   TAVAN FİNCANI ",
]


def temizle():
    print("\033[2J\033[H", end="")


def demle():
    print("Ters Çekim Motoru ısınıyor...")
    time.sleep(0.6)
    print("Newton itiraz etti. Reddedildi.")
    time.sleep(0.6)
    print("Çay molekülleri yukarı izin belgesi aldı.")
    time.sleep(0.6)
    print()
    for i in range(len(KATLAR)):
        temizle()
        print("=== TERS ÇEKİMLİ ÇAY DEMLEME ===\n")
        gorunen = KATLAR[: i + 1]
        # Aşağıdan yukarı biriksin diye ters basıyoruz
        for satir in reversed(gorunen):
            print(satir)
        print()
        print(f"Yükseklik: {i + 1}/{len(KATLAR)} kat")
        time.sleep(0.35)
    print()
    print("Çay tavanda. Afiyet olsun (merdiven şart).")
    print("Program bilimsel olarak tamamlandı.")


if __name__ == "__main__":
    try:
        demle()
    except KeyboardInterrupt:
        print("\nYerçekimi geri geldi. Çay döküldü. Utanç.")
        sys.exit(1)
