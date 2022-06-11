# Algo-Method local template
It is a github repository template for a local development environment to efficiently learn the [Algo-method](https://algo-method.com/).

## How to use

1. Create a repository from [this link](https://github.com/kawamataryo/algo-method-local-template/generate) and clone it locally.

2. Generate test cases and problem files for the target problem under `/tasks`.

```
make generate_task TASK=116
```

3. Run test on the target problem.

```
make run_test TASK=116
```

4. Go to the problem page and submit your answers.