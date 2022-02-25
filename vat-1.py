price = int(input("รับค่าราคาสินค้า:"))
vat = price*(7/100)
disc = price*(5/100)
total = price-disc-vat
print("-------------------------------")
print("ภาษีัมูลค่าเพิ่ม %.2f" % vat, " บาท")
print("ส่วนลด %.2f" % disc, "    บาท")
print("ราคารวม %.2f" % total, "  บาท")