# Question and Answer with LangChain

:construction: DRAFT :construction:

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
