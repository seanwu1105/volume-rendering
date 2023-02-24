# Volume Rendering

CS530 Introduction to Scientific Visualization assignment 3 @Purdue.

## Dataset

See [instruction](./instruction.md).

## Getting Started

Install Python 3.11.1 or later.

Install Poetry **1.3.2 or later**. See
[Poetry's documentation](https://python-poetry.org/docs/) for details.

> Poetry earlier than 1.3 will not work.

Install the project's dependencies:

```sh
poetry install --no-root
```

Activate the virtual environment:

```sh
poetry shell
```

Execute the application:

Use isosurface rendering to visualize the head dataset.

```sh
python iso_head.py -i[--input] <head.vti>
```

Use isosurface rendering to visualize the flame dataset.

```sh
python iso_flame.py -i[--input] <flame.vti>
```

Use volume rendering to visualize the head dataset.

```sh
python dvr_head.py -i[--input] <head.vti>
```

Use volume rendering to visualize the flame dataset.

```sh
python dvr_flame.py -i[--input] <flame.vti>
```

You can find the datasets in the `assets` directory.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
