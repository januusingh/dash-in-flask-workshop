### Templates

In the terminal, change into the templates directory by typing `cd templates/` in your terminal. The `curl` command can let us grab the whole HTML from another website and save it to our local machine. Then we can configure our Flask server can use it as a template to render data.

Run the following command in your terminal: `curl https://codenext.withgoogle.com > codenext.html`.

The second part `> codenext.html` means that we want to save the contents of the HTTP request to our own machine with that file name. You only want to store static HTML templates in this directory.
