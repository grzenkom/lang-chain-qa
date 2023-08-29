# Building a Q&A engine with LangChain and open-source LLMs

The main object in this repository is the `qa_engine.ipynb` notebook.

It contains a presentation showing how to run a large language model (LLM)
on a laptop using LangChain and then index Web documents, to query their
content with natural language.

There are different ways to view the presentation:

1. `jupyter notebook qa_engine.ipynb` and then `Alt+R` to enter the presentation
   mode,
2. open the notebook [`qa_engine.ipynb`](./qa_engine.ipynb) in GitLab/GitHub,
3. download one of the HTML files [`qa_engine.html`](./qa_engine.html) or
   [`qa_engine.slides.html`](./qa_engine.slides.html).

## Jupyter

Jupyter Notebook v6 is used, because [RISE](https://github.com/damianavila/RISE)
does not work well with Jupyter Lab or v7. This may change when
[jupyterlab-contrib/rise](https://github.com/jupyterlab-contrib/rise) becomes
more mature.

### Execute Time extension

[execute_time](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/execute_time)

```bash
jupyter contrib nbextension install --user
jupyter nbextension enable execute_time/ExecuteTime
```

### Converting to HTML

```bash
jupyter nbconvert qa_engine.ipynb --to html

jupyter nbconvert qa_engine.ipynb --to slides
```
