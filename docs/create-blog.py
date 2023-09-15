import os
import re
import markdown

html ="""
<!DOCTYPE html>
<html lang="en">
  <head>

    <title>João Alvim</title>
    <meta charset="utf-8">
    <!-- ensures proper rendering for mobile -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

    <!-- jQuery library
    <script
      src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    -->
    <!-- Latest compiled JavaScript
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    -->
  </head>

  <body>

    <nav class="navbar navbar-default">

      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="../index.html">
            <img src="../img/rubiks2.png" alt="rubik" style="width:72%">
          </a>
        </div>
        <ul class="nav navbar-nav">
          <!-- <li><a href="../index.html"><h3>about me</h3></a></li> -->
          <li><a href="../blog.html"><h3>blog</h3></a></li>
          <li><a href="../vitae.html"><h3>curriculum vitæ</h3></a></li>
        </ul>
      </div>
    </nav>

   
    <div class="container">
"""
foot = """
    <br>
    <br>
    </div>
    <footer>
      <div class="jumbotron">
        <div class="container-fluid">
          <div class="text-center">
            <div class="mx-auto">
              <!-- <h2>Contact Information</h2> -->

              <p style="font-size: 16px;">github: <a
                  href="https://github.com/jotaalvim">github.com/jotaalvim</a></p>
              <p style="font-size: 16px;">email: <a
                  href="mailto:joaoafonsoalvim@gmail.com">joaoafonsoalvim@gmail.com</a></p>
              <p style="font-size: 16px;">location: Braga, Portugal</p>
              <p style="font-size: 16px;">phone: +351 934662832</p>

            </div>

          </div>
        </div>
      </div>
    </footer>

  </body>

</html>
"""

directory_path = 'blogs/'

try:
    items = os.listdir(directory_path)
    for file in items:
        if file[-3:] != ".md":
            items.remove(file)
except:
    items = []

table_of_contents = []

for file in items:
    path = os.path.join('blogs',file)
    with open(path, "r") as f:
        file_content = f.read()

    html_content = markdown.markdown(file_content)

    # retirar data e título
    lines = html_content.split('\n')
    date  = lines.pop(0)
    date = re.sub(r'<\s*p\s*>','<p style="font-size: 17px;">',date)

    title = lines.pop(0)
    lines.insert(0,title)
    # COLOCAR OS TITULOS COM TAMANHO 2
    title = re.sub(r'h\d','h2',title,2)

    newhtml = '\n'.join(lines)

    newhtml = re.sub(r'<\s*p\s*>','<p style="font-size: 16px;">',newhtml)

    blog_pos = html + newhtml + foot


    newpath = os.path.join(directory_path,file[:-3]+'.html')
    with open(newpath, "w") as wfile:
        #print(blog_pos)
        wfile.write(blog_pos)

    table_of_contents.append((title,date,newpath))

    #print(date)
    #print(title)
    #print(table_of_contents)





blog_toc = html           # sort by date
for t,d,n in sorted(table_of_contents, key=lambda x: x[1]):
    blog_toc += f"""
      <li>
        <ul>
          <a href="{newpath}">{title}</a>
          <p style="font-size: 17px;">2023-09-14</p>
        </ul>
      </li>
      <br>
"""

blog_toc += foot

with open('blog.html', "w") as wfile:
    blog_toc = re.sub(r'../img/rubiks2.png','img/rubiks2.png',blog_toc)
    blog_toc = re.sub(r'../vitae.html','vitae.html',blog_toc)
    blog_toc = re.sub(r'../blog.html','blog.html',blog_toc)
    blog_toc = re.sub(r'../index.html','index.html',blog_toc)
    wfile.write(blog_toc)

