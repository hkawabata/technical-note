set -e

DIR=$(dirname $0)

${DIR}/path_tree_generator.py > ${DIR}/../docs/_includes/pagetree.xml

git add --all && \
  git commit -m"$(date +%Y/%m/%d\ %H:%M) update" && \
  git push

