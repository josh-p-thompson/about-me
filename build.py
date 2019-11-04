from string import Template

# import template
template = Template(open('templates/template.html').read())

# import content
index_content = open('content/index.html').read()
blog_content = open('content/blog.html').read()
projects_content = open('content/projects.html').read()

# function to generate pages
def generate_page(name, content, title): 
    full_page = template.safe_substitute(
        title=title,
        body_content=content, 
    )
    open('docs/' + name + '.html', 'w+').write(full_page)

generate_page(name='index', content=index_content, title='About Me')
generate_page(name='blog', content=blog_content, title='Blog')
generate_page(name='projects', content=projects_content, title='Projects')

"""
bonus_template_text = open('bonus_challenge_template.html').read()
template = Template(bonus_template_text)

# Use "format" feature of Python strings to insert data where needed for the
# index page
index_content = open('middle_index.html').read()
index_html = template.safe_substitute(
    title="About Me",
    index_class="active",
    content=index_content,
)
open('index.html', 'w+').write(index_html)

insert: ${index_class}
"""