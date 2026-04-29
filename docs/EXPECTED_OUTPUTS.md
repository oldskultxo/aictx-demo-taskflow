# Expected demo outputs

## Baseline CLI

```bash
python -m taskflow.cli examples/tasks.txt
```

```text
todo: 2
done: 1
total: 3
```

## Baseline tests

```bash
pytest -q
```

```text
.............                                                            [100%]
```

The exact dot count may change if tests are added during the demo.

## Baseline unsupported BLOCKED example

```bash
python -m taskflow.cli examples/session_1_target.txt
```

Expected before session 1:

```text
taskflow: error: line 6: unsupported task status 'BLOCKED' (expected: TODO, DONE): 'BLOCKED: waiting for API credentials'
```

Expected after session 1, once the agent adds BLOCKED support:

```text
todo: 1
done: 1
blocked: 1
total: 3
```
