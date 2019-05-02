echo "[CLEAN DIRECTORY]"

find . -name "*.pyc" -exec rm -f "{}" \;
find . -name "*.DS_Store" -exec rm -f "{}" \;

echo "[ADD FILES/DIRECTORIES]"

git add .

echo "[COMMIT CHANGE]"

COMMIT_NAME=$1
if [ $# -eq 0 ]; then
    echo "No arguments provided"
    COMMIT_NAME="update"
fi

git commit -am "${COMMIT_NAME}"

echo "[GET CURRENT BRANCH NAME]"

OUTPUT="$(git rev-parse --abbrev-ref HEAD)"

echo ${OUTPUT}

echo "[PUSH TO ORIGIN]"

git push -u origin ${OUTPUT}

echo "[WORK COMPLETE]"
