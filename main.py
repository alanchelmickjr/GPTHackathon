from unstructured.partition.pdf import partition_pdf

elements = partition_pdf("/Users/alanhelmick/Downloads/NIPS-2017-attention-is-all-you-need-Paper.pdf",
                         strategy="hi_res",
                         infer_table_structured=True)

print(*[(type(element), element.text) for element in elements[14:18]]) 



