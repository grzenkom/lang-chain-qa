# Building a Q&A engine with LangChain and open-source LLMs

The main object in this repository is the `qa_engine.ipynb` notebook.

It contains a presentation showing how to run a large language model (LLM)
on a laptop using LangChain and then index Web documents, to query their
content with natural language.

## How to open?

There are different ways to view the presentation:

1. 🐍 create environment with `poetry install`, then load the notebook with
   `jupyter notebook qa_engine.ipynb` and press `Alt+R` to enter
   the presentation mode,
2. ▶️ open the notebook [`qa_engine.ipynb`](./qa_engine.ipynb) in GitLab/GitHub,
3. 📥 download one of the `exported_*.html` files (if you choose the "slides"
   file, you also to download the `images/` directory).

## Jupyter

Jupyter Notebook v6 is used, because the [RISE](https://github.com/damianavila/RISE)
extension does not work well with Jupyter Lab or v7. This may change when
[jupyterlab-contrib/rise](https://github.com/jupyterlab-contrib/rise) becomes
more mature.

### Other small extensions for Jupyter

- [execute_time](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/execute_time)
- [export_embedded](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/export_embedded)

```bash
jupyter contrib nbextension install --user

jupyter nbextension enable execute_time/ExecuteTime
jupyter nbextension enable export_embedded/main
```

### Converting to HTML

```bash
jupyter nbconvert qa_engine.ipynb --to html_embed --output ./exported_qa_engine.one_page.html

# export_embedded does not add the option to export slides with embedded images
jupyter nbconvert qa_engine.ipynb --to slides --output ./exported_qa_engine
```
