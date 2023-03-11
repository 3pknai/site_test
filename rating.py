import pickle

with open("result.data", "rb") as f:
    result = pickle.load(f)

content = ""
for res in range(len(result)):
    content += """<div class="rating_block">
    """
    content += f"""                    <h2 align="center">{result[res][0]}</h2>
                        <br>
                        """
    content += """<table class="rating_table">
                            <tr>"""
    for i in result[res][1]:
        content += f"""
                                <th>{i}</th>"""
    content += """
                            </tr>"""

    for i in result[res][2:]:
        x = i[-1]
        i.pop()
        i.extend(x)
        content += """
                            <tr>"""
        for j in i:
            content += f"""
                                <td>{j}</td>"""
        content += """
                            </tr>"""

    content += """
                        </table>"""
    content += """
                    </div>"""


title = "Рейтинг учеников"
with open("sidebar_menu.txt", "r", encoding="utf-8") as f:
    sidebar = "\n".join([x.replace("\n", "") for x in f.readlines()])
with open("footer.txt", "r", encoding="utf-8") as f:
    footer = "\n".join([x.replace("\n", "") for x in f.readlines()])


site = f"""<!doctype html>
<html lang="en">
	<head>
		<link rel="stylesheet" href="static\\css\\basic.css" media="screen">
		<meta charset="utf-8">
		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@300;500&display=swap" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=1">
		<title>КуМир - {title}</title>
	</head>
	<body>
        <header>
            <div class="text-pic">
                <img class="g" src="static\\images\\pic1.png">
                <p>
                    Апробация сетевого взаимодействия образовательных организаций Волгоградской области и Станично-Луганского района ЛНР с использованием системы Moodle и АСУ СГО
                </p>
                <img class="g" src="static\\images\\pic2.png">
                <img class="dev" src="static\\images\\development.png">
                <a class="dev-btn" href="">Переход на платформу</a>
            </div>
        </header>
        <div class="bar">
            Программирование на Кумире для школьников 5-7 классов
        </div>
        <div class="wrapper">
            <div class="middle">

                {sidebar}

                <content>
                
                    {content}

                </content>

            </div>
            <footer>
                {footer}
            </footer>
        </div>
	</body>
</html>"""


with open("rating.html", "w", encoding="utf-8") as f:
    f.write(site)