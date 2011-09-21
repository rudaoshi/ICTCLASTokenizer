
mkdir build

cd build
cmake ../src/
make 

cd ..

mkdir egg
mkdir egg/ICTCLASTokenizer

cp build/libpyICTCLASCore.dylib egg/ICTCLASTokenizer/libpyICTCLASCore.so
cp src/*.py egg/ICTCLASTokenizer/
cp -r src/ictclas/Data egg/ICTCLASTokenizer/Data

cd egg/ICTCLASTokenizer
touch __init__.py

mv setup.py ..
cd ..


python setup.py egg_info --tag-date --tag-build=DEV bdist_egg