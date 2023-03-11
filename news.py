import os

listdirectory = os.listdir(path='news')
content = ""
for i in listdirectory:
    content += """
                    <div class="content_block">
                        """
    
    lstimg = sorted(os.listdir(path=f'news/{i}/img'))
    lstsign = sorted(os.listdir(path=f'news/{i}/signature'))
    lsttext = sorted(os.listdir(path=f'news/{i}/tabletext'))
    with open(f"news/{i}/text.txt", "r") as f:
        text = [x.replace("\n", "") for x in f.readlines()]

    if len(lstimg) > 0:

        

        # Добавление подписей к картинкам
        content += """<table>
                            <tr>"""
        for x in lstsign:
            with open(f"news/{i}/signature/{x}") as f:
                content += f"""
                                <td>
                                    {f.readline()}
                                </td>"""
        content += """
                            </tr>"""
        
        # Добавление картинок
        content += """
                            <tr>"""
        for x in lstimg:
            content += f"""
                                <td>
                                    <img src="news/{i}/img/{x}" alt="">
                                </td>"""
        content += """
                            </tr>"""

        # Добавление текста к картинкам
        if len(lsttext) != 0:
            content += """
                            <tr>"""
            for x in lsttext:
                with open(f"news/{i}/tabletext/{x}") as f:
                    content += f"""
                                <td>
                                    <p>
                                        {f.readline()}
                                    </p>
                                </td>"""
            content += """
                            </tr>"""
        
        
        content += """
                        </table>"""

    with open(f"news/{i}/text.txt") as f:
        q = f.readlines()
        if len(q) != 0:
            content += """

                        <div class="content_text">"""
            for x in [y.replace("\n", "") for y in q]:
                content += f"""
                            <p>
                                {x}
                            </p>"""
            content += """
                        </div>"""
    
    content += """
                    </div>"""
            
    #print(lstimg)
    #print(lstsign)
    #print(lsttext)
    #print(text)
    #print(content)

title = "Новостная лента"
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


with open("index.html", "w", encoding="utf-8") as f:
    f.write(site)