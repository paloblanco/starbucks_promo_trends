from simplepysite.site import establish_site, build_site


establish_site() # creates a pages folder, a sample markdown file, and a generic style.css which can be edited

build_site() # assuming there is a "pages" folder, all markdown files contained therein are converted to html