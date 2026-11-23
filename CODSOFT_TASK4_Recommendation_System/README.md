# Movie Recommendation System

A Python-based content-based movie recommendation system.

## Features

- Recommends movies based on user preferences.
- Uses genres and keywords.
- Uses cosine similarity.
- Ranks recommendations by relevance.
- Supports excluding watched movies through the recommendation function.
- Includes automated unit tests.
- No external Python packages required.

## Technologies

- Python
- Content-Based Filtering
- Cosine Similarity
- Set Operations
- Unit Testing

## Requirements

Python 3.8 or later.

## Run the application

```bash
py main.py
```

Enter your preferred genres or keywords separated by commas.

Example:

```text
sci-fi, adventure, space
```

## Run tests

```bash
py -m unittest -v
```

## How the algorithm works

1. The system stores movies with genres and descriptive keywords.
2. User preferences are converted into normalized features.
3. Each movie is represented by its feature set.
4. Cosine similarity measures the overlap between user preferences and movie features.
5. Movies are sorted by their similarity scores.
6. The highest-ranked movies are recommended.

## Project Structure

```text
CODSOFT_TASK4_Recommendation_System/
    main.py
    test_main.py
    README.md
    .gitignore
```

## Author

Sangam Bopche
