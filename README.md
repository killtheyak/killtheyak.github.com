# KillTheYak

[http://KillTheYak.com](http://killtheyak.com)

> You see, yak shaving is what you are doing when you're doing some stupid, fiddly little task that bears no obvious relationship to what you're supposed to be working on, but yet a chain of twelve causal relations links what you're doing to the original meta-task.

<cite>- Jeremy H. Brown</cite>

[Kill The Yak][KillTheYak] is a website with guides that will reduce the time you spend yak shaving.

## Contribute content

If you are interested in contributing content, see the [killtheyak-pages][] repo.

## Hacking

Kill The Yak is a small Flask app that uses [Flask-FlatPages](https://github.com/SimonSapin/Flask-FlatPages) and [Frozen-Flask](https://github.com/SimonSapin/Frozen-Flask) to build the static content. The app itself lives in the [killtheyak/ directory](https://github.com/killtheyak/killtheyak.github.io/tree/master/killtheyak). Feel free to use, modify, or just browse around.

### Requirements

- Python 2.7
- npm
- coffee-script

To install the necessary Python packages:

```
# After activating your virtualenv
$ pip install -r requirements.txt
```

To install coffee-script with npm:

```
$ npm install
```

### Building the site

To run the local development server

```
$ python manage.py runserver
```

You can browse to `http://localhost:5000/` to view the site.

To build the static version of the site:

```
$ python manage.py build
```

### Deployment

To deploy to GitHub Pages:

```
$ python manage.py build
$ git commit -am "Update pages"
$ git push
```

Or do it all in one go:

```
$ python manage.py deploy
```

## License

Copyrights to the guides are owned by their original authors and are licensed under the [Creative Commons Attribution-Share-Alike license][CC-SA].  The website is licensed under the [MIT License](https://github.com/killtheyak/killtheyak.github.io/blob/master/LICENSE).

[KillTheYak]: http://killtheyak.com
[killtheyak-pages]: https://github.com/killtheyak/killtheyak-pages
[MIT License]: https://github.com/killtheyak/killtheyak.github.io/blob/master/LICENSE
[CC-SA]: https://creativecommons.org/licenses/by-sa/3.0/legalcode
