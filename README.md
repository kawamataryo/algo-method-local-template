# Algo-Method local template
Repository template for a local development environment to efficiently learn the [Algo-method](https://algo-method.com/).

https://user-images.githubusercontent.com/11070996/173185423-a750ab0f-1808-43a1-9308-b82383273085.mp4


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