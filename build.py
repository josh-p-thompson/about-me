from string import Template
 
# function to generate pages
def generate_page(name, content, title, about_btn="", projects_btn="", blog_btn=""): 
    template = Template(open('templates/template.html').read())
    full_page = template.safe_substitute(
        title=title,
        right_block_content=content, 
        about_btn=about_btn, 
        projects_btn=projects_btn, 
        blog_btn=blog_btn
    )
    open('docs/' + name + '.html', 'w+').write(full_page)

def main(): 
    # import content
    index_content = open('content/index.html').read()
    blog_content = open('content/blog.html').read()
    projects_content = open('content/projects.html').read()

    # create pages
    generate_page(name='index', content=index_content, title='About Me', about_btn='active')
    generate_page(name='blog', content=blog_content, title='Blog', blog_btn='active')
    generate_page(name='projects', content=projects_content, title='Projects', projects_btn='active')

if __name__ == "__main__": 
    main()