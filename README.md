# PyCssMinifier

A <a style="text-decoration:underline;">quick and dirty</a> script to minify your CSS files.

## Running The Script

1) In the desired directory run the command<br>
    ``` git clone <https://github.com/Hibob555556/PyCssMinifier.git> ```

2) After the cloning process has finished run the command<br>
    ``` cd .\PyCssMinifier ```

3) Once you are ready to minify your file run the command<br>
    ``` python .\minify_css.py ../the/path/to/your/file.css ```

4) Once the program is finished running a file titled "file_min.css" will appear in the same directory that the original file was in.

### Notes

- This is <a style="text-decoration:underline;">NOT</a> full featured.
- This program <b><a style="text-decoration:underline;">DOES NOT</a>:
  1) Remove comments.
  2) Remove <b><a style="text-decoration:underline;">ANY</a> code.
  3) Shorten variable names.
- This program <b><a style="text-decoration:underline;">DOES</a>
  1) Remove line breaks.
  2) Remove superfluous white spaces.
