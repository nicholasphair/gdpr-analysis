# plugin_meta
**meta.json** - A scrape of the entire WordPress plugin info API. This contains all metadata relating to plugins as of Fri Apr  8 07:06:21 UTC 2022  

**authors.json** - All extractable information on all plugin authors. Namely, author, author profile, and home page. You can consult this to figure out how to contact the plugin author  

**manual_analysis_meta.csv** - frequently used metadata concerning only the
plugins used for manual analysis. Most of the columns are self-explanatory,
with the exception of `path`. `path` is the location in the [zip file][1] that
contains all of the plugins. You can use this value to extract only the plugin
you want.   


```bash
unzip plugins.zip <path>
```


[1]: https://drive.google.com/file/d/1v7yo_XIe3-_J3fLWwVuYuW5ozs42r7Ty/view?usp=sharing
