import os
import re
import markdown

html ="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>João Alvim</title>
    <meta charset="utf-8">
    <!-- ensures proper rendering for mobile 
    <meta name="viewport" content="width=device-width, initial-scale=1">
    -->

    <link rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script> 
    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> 
    <link rel="stylesheet" href="../style.css">

  </head>

  <body>

  <nav class="navbar navbar-default">
      <div class="container">
          <div class="navbar-header">
              <a class="navbar-brand" href="../index.html">
                  <div class="d-flex align-items-center">
                      <img src="../img/rubiks2.png" alt="rubik" style="width:37%">
                      <span class="ml-auto">João Alvim</span>
                  </div>
              </a>
          </div>
          <ul class="nav navbar-nav navbar-right">
              <li><a href="../blog.html">Blog</a></li>
              <li><a href="../vitae.html">Curriculum Vitæ</a></li>
              <li><a href="../contact.html">Contact</a></li>
          </ul>
      </div>
  </nav>

   
    <div class="container mx-auto" style="max-width:50%;">
"""
foot = """
    <br>
    <br>
    </div>
  </body>
</html>
"""

directory_path = 'blogs/'

try:
    itemst = os.listdir(directory_path)
    print(itemst)
    items = []
    # FIXME usar glob
    for file in itemst:
        if file[-3:] == ".md":
            items.append(file)
    print(items)
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
    title = re.sub(r'h\d','h3',title,2)

    newhtml = '\n'.join(lines)
    #newhtml = re.sub(r'<\s*p\s*>','<p style="font-size: 16px;">',newhtml)

    blog_pos = html + newhtml + foot


    newpath = os.path.join(directory_path,file[:-3]+'.html')
    print(newpath)
    with open(newpath, "w") as wfile:
        #print(blog_pos)
        wfile.write(blog_pos)

    table_of_contents.append((title,date,newpath))



blog_toc = html           # sort by date
sl = sorted(table_of_contents, key=lambda x: x[1])
sl.reverse()

for b in sl:
    t,d,n  = b
    blog_toc += f"""
      <li>
        <ul>
          <a href="{n}">{t}</a>
          {d}
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
    blog_toc = re.sub(r'../style.css','style.css',blog_toc)
    wfile.write(blog_toc)

