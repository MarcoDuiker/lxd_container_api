#pdoc --html --html-dir ./api ksm

pdoc --html lxd_utils 
rm -rf ./api/*
mv ./lxd_utils/* ./api
rmdir ./lxd_utils

