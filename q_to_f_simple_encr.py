q="qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f="fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"
translate_table=str.maketrans(q,f)
text=input("Input:\n")
enc_text=text.translate(translate_table)
print("Enc: "+enc_text)
