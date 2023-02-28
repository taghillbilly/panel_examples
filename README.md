# ✨ Awesome Panel Examples

A repository of awesome [Panel](https://panel.holoviz.org/) data app examples.

The source files are available in the [src](/src) folder.

The apps are converted to webassembly and released to
[awesome-panel.github.io/examples/](https://awesome-panel.github.io/examples/) as simple as

1. `$ panel convert app.py` (1 second)
2. `$ git push` (1 second)

This is **THE FASTEST WAY TO DEPLOY DATA APPS** in Python.

The apps are **very performant** when loaded because there is no latency for communication between
server and client.

![awesome-panel-examples-tour.gif](assets/gifs/awesome-panel-examples-tour.gif)

BUT the apps **take time to load** as they need to download a Python runtime and additional packages
(50MB per app).

This is **THE FUTURE OF DATAVIZ** in Python.

If you like [Panel](https://panel.holoviz.org/) and [Awesome Panel](https://awesome-panel.org) please support the projects by giving them a ⭐ on Github

[⭐ holoviz/panel](https://github.com/holoviz/panel) [⭐ awesome-panel/awesome-panel](https://github.com/awesome-panel/awesome-panel) [⭐ awesome-panel/examples](https://github.com/awesome-panel/examples)

Thanks 👍

## 📙 How to

### ⚙️ Install the repository

```bash
git clone https://github.com/awesome-panel/examples.git
```

Create and activate a virtual environment, c.f.
[Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

Install the `requirements.txt` file

```bash
pip install -r requirements.txt -U
```

### 💻 Serve a server app locally

You can serve for example the [hello-world](src/hello-world/app.py) application on your Panel server via

```python
panel serve src/hello-world/app.py --autoreload
```

It will be available at [http://localhost:5006/app](http://localhost:5006/app).

![Panel Hello World App](assets/images/hello-world.png)

### 🏗️ Convert an app to webassembly

You can [panel convert](https://panel.holoviz.org/user_guide/Running_in_Webassembly.html) for
example the [hello-world](src/hello-world/app.py) application to webassembly via

```python
panel convert src/hello-world/app.py --to pyodide-worker --out docs/hello-world
```

If you want to avoid repeating the big download over and over again, you can even convert to a
[progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app) that can be installed on
your laptop! It is as simple as adding the `--pwa` and `--title` flags.

Check out the [Panel WebAssembly Guide](https://panel.holoviz.org/user_guide/Running_in_Webassembly.html)
for more details.

### 💻 Serve a webassembly app locally

```bash
python3 -m http.server
```

The app is now available at [http://localhost:8000/docs/hello-world/app.html](http://localhost:8000/docs/hello-world/app.html)

### ⚙️ Configure the repository for Github Pages

You can learn how to configure Github Pages in general via the [Quickstart for Github Pages](https://docs.github.com/en/pages/quickstart).

The Github Pages of `awesome-panel/examples` is configured as described below

1. Add a `.nojekyll` file push all changes.
2. Navigate to the *Settings* page
3. Navigate to the *Pages* page
4. Configure your Pages Settings as shown below

![Github Pages Settings](assets/images/gh-pages-settings.png)

### 🔥 Release to Github Pages

Git `add`, `commit`, `push` and *merge* your PR as you would normally do.

The applications are now available at [awesome-panel.github.io/examples/](awesome-panel.github.io/examples/) or similar.

## Development

The below instructions are preliminary and for the project contributors

### Build the project

```bash
panel convert src/hello-world/app.py --to pyodide-worker --out docs/hello-world
panel convert src/test_panel_speed/app.py --to pyodide-worker --out docs/test_panel_speed
python src/index/index.py
```

```bash
python3 -m http.server
```

[http://localhost:8000/docs/index.html](http://localhost:8000/docs/index.html)
