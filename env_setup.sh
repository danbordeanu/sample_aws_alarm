#!/usr/bin/env bash

DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]-$0}" )" && pwd )"
export CONDA_ENV_PATH=${CONDA_ENV_PATH:-${DIR}/.condaenv}

eval "$(conda shell.bash hook)"
conda env create --force -p ${CONDA_ENV_PATH}
PS1=${PS1:-} && conda activate ${CONDA_ENV_PATH}

echo "Environment prepared."
