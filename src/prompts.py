# INFO: some prompts are still in model.py

# TODO: Ignore OCR problems in the text below.

TASK = {
	'v6': (
			"Répondez à la question en vous basant sur le texte ci-dessous. "
			"Inclure la citation verbatim et un commentaire indiquant où la trouver dans le texte (numéro de page). "
			#"Après la citation, écrivez une explication étape par étape dans un nouveau paragraphe. "
			"Après la citation, écrivez une explication étape par étape. "
			"Utilisez des puces. "
			#"Après cela, essayez de reformuler la question initiale afin d'obtenir de meilleurs résultats. " 
		),
	'v5': (
			"Répondez à la question en vous basant sur le texte ci-dessous. "
			"Incluez au moins une citation verbatim (marquée par des guillemets) et un commentaire indiquant où la trouver dans le texte (c'est-à-dire le nom de la section et le numéro de page). "
			"Utilisez des points de suspension dans la citation pour omettre les parties non pertinentes de la citation. "
			"Après la citation, écrivez (dans un nouveau paragraphe) une explication étape par étape pour vous assurer que vous avez la bonne réponse."
			" (utilisez des puces sur des lignes séparées) " #, adapter le langage pour un jeune lecteur). "
			"Après l'explication, vérifiez si la réponse est cohérente avec le contexte et ne nécessite pas de connaissances externes. "
			"Sur une nouvelle ligne, écrivez 'Autocontrôle OK' si le contrôle a réussi et 'Autocontrôle échoué' s'il a échoué. " 
		),
	'v4':
		"Répondez à la question en vous basant sur le texte ci-dessous. " \
		"Inclure une citation verbatim et un commentaire sur l'endroit où la trouver dans le texte (c'est-à-dire le nom de la section et le numéro de la page). " \
		"Après la citation, écrivez une explication (dans le nouveau paragraphe) pour un jeune lecteur",
	'v3' : 'Répondez à la question en vous basant sur le texte ci-dessous. Incluez la citation verbatim et un commentaire indiquant où la trouver dans le texte (c\'est-à-dire le nom de la section et le numéro de page)',
	'v2' : 'Répondez à la question en vous basant sur le contexte. Les réponses doivent être élaborées et basées uniquement sur le contexte',
	'v1' : 'Répondre à la question en fonction du contexte',
	# 'v5':
		# "Generate a comprehensive and informative answer for a given question solely based on the provided document fragments. " \
		# "You must only use information from the provided fragments. Use an unbiased and journalistic tone. Combine fragments together into coherent answer. " \
		# "Do not repeat text. Cite fragments using [${number}] notation. Only cite the most relevant fragments that answer the question accurately. " \
		# "If different fragments refer to different entities with the same name, write separate answer for each entity.",
}

HYDE = "Rédigez un exemple de réponse à la question suivante. N'écrivez pas de réponse générique, mais supposez tout ce qui n'est pas connu."

# TODO
SUMMARY = {
	'v2' : "Décrire le document dont le fragment est extrait. Omettre tout détail",
	'v1' : "Décrivez le document dont le fragment est extrait. Ne décrivez pas le fragment, concentrez-vous sur le type de document dont il s'agit.",
}
