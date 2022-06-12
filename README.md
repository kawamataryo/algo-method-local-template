# Algo-Method local template
Repository template for a local development environment to efficiently learn the [Algo-method](https://algo-method.com/).

https://user-images.githubusercontent.com/11070996/173215285-f6446cfa-3ead-4e91-b69d-ae6f908e4b94.mp4

## 🚀 How to use

### 1. Create a repository
Create a repository from [this link](https://github.com/kawamataryo/algo-method-local-template/generate) and clone it locally.


### 2. Generate test cases and answer sheet
Generate test cases and answer sheet for the target question under `/questions`.  
The question number is the number at the end of the URL. (e.g. `https://algo-method.com/tasks/116/` is `No=116`)

```
make get_question No=116
```

### 3. Run test
 Run test on the target question.

```
make run_test No=116
```

### 4. Submit answer.
Go to the question page and submit your answers 🎉
