#!/bin/bash
URL="https://github.com/grunwmar/helpers.git"

GITDIR=".tmpgit_make_project.d"
GITDIR_MKP="$GITDIR/make_project"
GITDIR_TEM="$GITDIR/make_project/templates"

function echo_info(){
    color="92"
    echo ""
    echo -e "\033[${color}m$1\033[0m"
}

echo_info ">> Clonning helpers git repository"
git clone "$URL" "$GITDIR"

echo_info ">> Copying files from helpers git repository"

cp "$GITDIR_TEM/run.sh" ./run.sh
chmod +x ./run.sh

cp "$GITDIR_TEM/make_venv.sh" ./make_venv.sh
chmod +x ./make_venv.sh

cp "$GITDIR_TEM/requirements.txt" ./requirements.txt
cp "$GITDIR_TEM/gitignore" ./.gitignore
cp "$GITDIR_TEM/__main__.py" ./__main__.py

cp -R "$GITDIR_TEM/config" ./config
cp -R "$GITDIR_TEM/src" ./src
cp -R "$GITDIR/helpers" ./helpers

echo_info ">> Making ./logs directory"
mkdir ./logs

echo_info ">> Making ./test directory"
mkdir ./tests

echo_info ">> Removing helpers git repository"
if [[ -d "$GITDIR" ]]; then
    rm -rf "$GITDIR"
fi

# init virtual environment
echo_info ">> Making python virtual environment"
./make_venv.sh

# init git repository
echo_info ">> Initializing git repository"
git init
git branch -m main
git add .
git commit -m "init"

echo_info ">> Done."
