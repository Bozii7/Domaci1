# 30.Dimenzije pravougaonika su 543 i 130. Koliko kvadrata stranice 65 je moguće
# izrezati iz tog pravougaonika?

a_pravougaonika = 543
b_pravougaonika = 130

a_kvadrata = 65

p_pravougaonika = a_pravougaonika * b_pravougaonika
p_kvadrata = a_kvadrata * a_kvadrata

m = p_pravougaonika // p_kvadrata
print(m)