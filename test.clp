(defrule bentuksegitiga
    (jumlahsudut 3)
    =>
    (assert (bentuk segitiga))
)

(defrule bentuksegiempat
    (jumlahsudut 4)
    =>
    (assert (bentuk segiempat))
)

(defrule bentuklima
    (jumlahsudut 5)
    =>
    (assert (bentuk segilima))
)

(defrule bentuksegienam
    (jumlahsudut 6)
    =>
    (assert (bentuk segienam))
)

;;****************
;;* segitiga     *
;;****************

(defrule samakaki
    (bentuk segitiga)
    (jumlahsudutsama 2)
    =>
    (assert (samakaki))
)

(defrule segitigasamasisi
    (bentuk segitiga)
    (jumlahsudutsama 3)
    =>
    (assert (segita_samasisi))
    (halt)
)


(defrule segitigatumpulsamakaki
    (bentuk segitiga)
    (samakaki)
    (jumlahsuduttumpul 1)
    =>
    (assert (segitiga_tumpul_samakaki))
    (halt) 
)

(defrule segitigasikusamakaki
    (bentuk segitiga)
    (samakaki)
    (jumlahsudutsiku 1)
    =>
    (assert (segitiga_siku_samakaki))
    (halt)
)

(defrule segitigalancipsamakaki
    (bentuk segitiga)
    (samakaki)
    =>
    (assert (segitiga_lancip_samakaki))
    (halt)
)

(defrule segitigasiku
    (bentuk segitiga)
    (jumlahsudutsiku 1)
    =>
    (assert (segitiga_siku))
    (halt)
)

(defrule segitigalancip
    (bentuk segitiga)
    (jumlahsudutlancip 3)
    =>
    (assert (segitiga_lancip))
    (halt)
)

(defrule segitigatumpul
    (bentuk segitiga)
    (jumlahsuduttumpul 1)
    =>
    (assert (segitiga_tumpul))
    (halt)
)

(defrule segitigatidakberaturan
    (bentuk segitiga)
    =>
    (assert (segitiga_tidak_beraturan))
    (halt)
)


;;****************
;;* Segiempat    *
;;****************


(defrule persegi
    (bentuk segiempat)
    (jumlahsudutsiku 4)
    (jumlahsisisama 4)
    =>
    (assert (persegi))
    (halt)
)

(defrule persegipanjang
    (bentuk segiempat)
    (jumlahsudutsiku 4)
    (jumlahsisisama 2)
    =>
    (assert (persegi_panjang))
    (halt)
)

(defrule jajargenjangberaturan
    (bentuk segiempat)
    (jumlahsudutsama 2)
    (jumlahsisisama 4)
    =>
    (assert (jajar_genjang_beraturan))
    (halt)
)

(defrule jajargenjanglayanglayang
    (bentuk segiempat)
    (jumlahsudutsama 1)
    (jumlahsisisama 2)
    =>
    (assert (jajar_genjang_layang_layang))
    (halt)
)

(defrule trapesiumsamakaki
    (bentuk segiempat)
    (jumlahsudutsama 2)
    (jumlahsisisama 1)
    =>
    (assert (trapesium_sama_kaki))
    (halt)
)

(defrule trapesiumratasisi
    (bentuk segiempat)
    (jumlahsudutsiku 2)
    =>
    (assert (trapesium_rata_sisi))
    (halt)
)

(defrule segiempattidakberaturan
    (bentuk segiempat)
    =>
    (assert (segiempat_tidak_beraturan))
    (halt)
)

;;****************
;;* Segilima    *
;;****************

(defrule segilimaberaturan
    (bentuk segilima)
    (jumlahsisisama 5)
    =>
    (assert (segilima_beraturan))
    (halt)
)

(defrule segilimatidakberaturan
    (bentuk segilima)
    =>
    (assert (segilima_tidak_beraturan))
    (halt)
)

;;****************
;;* Segienam   *
;;****************

(defrule segienamberaturan
    (bentuk segienam)
    (jumlahsisisama 6)
    =>
    (assert (segienam_beraturan))
    (halt)
)

(defrule segienamtidakberaturan
    (bentuk segienam)
    =>
    (assert (segienam_tidak_beraturan))
    (halt)
)