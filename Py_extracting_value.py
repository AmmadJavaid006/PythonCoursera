text = "X-DSPAM-Confidence:    0.8475"

val = text.find(":")
val_final = text[val + 1 :]
print(float(val_final))
