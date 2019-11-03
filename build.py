# import templates
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# import content
index_content = open('content/index.html').read()
blog_content = open('content/blog.html').read()
projects_content = open('content/projects.html').read()

# combine to generate pages
for key, value in {'index.html': index_content, 'blog.html': blog_content, 'projects.html': projects_content}.items(): 
    full_page = top_template + value + bottom_template
    open('docs/' + key, 'w+').write(full_page)

