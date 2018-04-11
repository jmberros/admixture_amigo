# Admixture Amigo

A python tool to run Admixture easily on a PLINK dataset of `{.bed, .bim, .fam}` files for many values of K.

```bash

# Run admixture with a given plink dataset and multiple K values:

admixture_amigo
    --plink /path/to/plink/dataset
    --k-values 2,3,4,5,6,7,8,9,10
    --out-dir /path/to/results_dir
    --threads 8

# Same but with short parameter names:

admixture_amigo
    -i /path/to/plink/dataset
    -k 2,3,4,5,6,7,8,9,10
    -o /path/to/results_dir
    -t 8


admixture_amigo --help
```
