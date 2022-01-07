import sys
import os

args = sys.argv[1:]

os.mkdir(args[0])
f = open(args[0] + "/index.php", "w")
f.write("<?php\nrequire_once(\"inclusions/init.php\");\n//CODE PHP\nrequire_once(\"inclusions/haut.php\");\n\n//CONTENU\n\nrequire_once(\"inclusions/bas.php\");\n?>")
inc = args[0] + "/inclusions"

os.mkdir(inc)

os.mkdir(inc + "/JS")
script = open(inc + "/JS/script.js", "w")

os.mkdir(inc + "/css")
style = open(inc + "/css/style.css", "w")

haut = open(inc + "/haut.php", "w")
haut.write("<!Doctype html>\n<html>\n\t<head>\n\t\t<title>Titre</title>\n\t\t<link rel=\"stylesheet\" href=\"<?php echo Racine; ?>inclusions/css/style.css\">\n\t\t<script type=\"text/javascript\" src=\"<?php echo Racine; ?>inclusions/JS/script.js\"></script>\n\t\t<meta charset=\"utf-8\">\n\t</head>\n\t<body>\n\t\t<header>\n\t\t\t<div class=\"conteneur\">\n\n\t\t\t</div>\n\t\t</header>\n\t\t<section>\n\t\t\t<div class=\"conteneur\">")

bas = open(inc + "/bas.php", "w")
bas.write("\t\t\t</div>\n\t\t</section>\n\t\t<footer>\n\t\t\t<div class=\"conteneur\">\n\t\t\t\t<?php echo date(\'M ý\'); ?>\n\t\t\t</div>\n\t\t</footer>\n\t</body>\n</html>")

init = open(inc + "/init.php", "w")
init.write("<?php\n\n$mysqli=new mysqli(\"localhost\", \"user\", \"mdp\", \"BDD\");\nif ($mysqli->connect_error) die(\"Problème lors de la connexion à la BDD : \" . $mysqli->connect_error);\nsession_start();\n\ndefine(\"Racine\", \"/\");\n\n?>")
 