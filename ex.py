from vllm import LLM
import os
import logging
import sys
import argparse

parser = argparse.ArgumentParser(description="Inference Runner")
parser.add_argument(
        "--block-size",
        type=int,
        default=8,
        metavar="S",
        help="block_size",
    )
parser.add_argument(
        "--batch-size",
        type=int,
        default=1,
        metavar="S",
        help="batch_size",
    )
args = parser.parse_args()

batch = ["Q:Who are you? A:"] * args.batch_size
# (TODO) Batch made by public dataset
# batch= prompts[:args.batch_size]
output_path = "output_batch{}_bs{}.txt".format(args.block_size)
sys.stdout = open(output_path, "w")
os.environ['VLLM_ATTENTION_BACKEND'] = 'XFORMERS'

llm = LLM(model="facebook/opt-125m", max_model_len=2048, block_size=args.block_size)  # Name or path of your model
output = llm.generate(batch)
print(output)

# for block_size in [8, 16, 32, 64 ,128]:
#     llm = LLM(model="facebook/opt-125m", max_model_len=2048, block_size=block_size)  # Name or path of your model
#     output = llm.generate("Q:Who are you? A:")
#     print(output)

