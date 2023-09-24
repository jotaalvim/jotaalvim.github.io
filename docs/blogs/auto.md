2023-9-3
# Automação de blogs

Criei um site pessoal onde existe este blog. 
Para escrever texto uso o prático markdown. Como não queria ser eu a converter de markdown para html à mão, decidi fazer
um script que me faz isso automaticamente. 
Quando correr esse [script](https://github.com/jotaalvim/jotaalvim.github.io/blob/main/docs/create-blog.py) há uma atualização
da table of contents dos blogs, e também de cada blog individualmente.

# Uma vez que tenho a geração do website automatizada porque é que tenho que ser eu a correr esse script?
Felizmente existe uma ferramenta que lida com esse tipo de situações: [github action](https://github.com/features/actions). O
github action permite automatizar um pipeline de instruções.

No meu caso quando faço commit de um blog em notação markdown para o github, este automaticamente recalcula as novas páginas do
website e coloca no "ar" em 2 minutos. Diminuindo o meu trabalho ao simples upload do blog. 
