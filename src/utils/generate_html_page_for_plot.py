def generate_html_page_for_plot(title, plot_html):
    html_page = f"""
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            {plot_html}
        </body>
    </html>
    """
    
    return html_page