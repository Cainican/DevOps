######################################
#   tekisuto p. 51 suuchinyuuryoku   #
#   inch-to-cm-input-ng.py	     #
######################################

# nyuuryoku wo ete intsi wo sentsimeetoruni henkan(mikansei-ban)
# henkan no gen ni naru atai
per_inch=2.54

# yu-za- kara nyuuryoku wo eru
inch=input("inch?")		#inch de uketoru

# keisan
cm=float(inch)*per_inch		#you can write "float" and or "int" for same results
				#"float" for comma nr, "int" kan ikke finde ud af comma tal

# kekka wo hyouji
desc="{0}inch={1}cm".format(inch,cm)
print(desc)