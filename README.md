---
id: child-dataset
name: CHILD Dataset
brief-description: Dataset for experiments within the CHILD Pilot
type: Dataset
release-date: 
release-number: 
work-package: 
- WP1
- WP4
pilot:
- CHILD
licence: 
related-component:
- led
links:
- https://github.com/polifonia-project/child-dataset
credits:
- https://github.com/enridaga
---
# child-dataset


## Data

Two CSV files:

sources.csv: entity, source-file, title, author-entity, author-name, year

experiences.csv: source-entity, excerpt, time, environment, listener, place, listening-to, written-by, performed-by

## Tasks

Task 1: retrieve documentary evidence relevant to Music + Child

Given: sources (all data), experience (source-entity)
Find: experience (excerpt)

Task 2: retrieve documentary evidence extended metadata

Given: sources (all data), experience (source-entity, excerpt)
Find: experience (time, medium, environment, listener, listening-to, written-by, performed-by, listening-where)


## Benchmark construction process

Generate list of sources from exemplary LED entities

```
fx -q queries/sources.sparql -l led-SNAPSHOT.nt -o data/sources.csv -f CSV
fx -q queries/experiences.sparql -l led-SNAPSHOT.nt -o data/sources.csv -f CSV
fx -q queries/child.sparql -l led-SNAPSHOT.nt -o data/child.csv -f CSV
```





