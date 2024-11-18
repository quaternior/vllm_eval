
BLOCK_SIZE_LIST=(8 16 32 64 128)
for BLOCK_SIZE in "${BLOCK_SIZE_LIST[@]}"
do
    ARGS="--block-size $BLOCK_SIZE"
    trap 'kill 0' SIGINT
    python ex.py ${ARGS}
done