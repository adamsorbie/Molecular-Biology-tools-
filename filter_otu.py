import pandas as pd


# read in otu table and mapping file
def read_files(metadata, otu, filter_file=None):
        metadata = pd.read_csv(metadata, index_col=0, header=0, sep="\t")
        otu = pd.read_csv(otu, index_col=0, header=0, sep="\t")
        if filter_file:
            filter_file = pd.read_csv(filter_file, index_col=0, header=0, sep="\t", names=["filter"])
            return metadata, otu, filter_file
        return metadata, otu

def filter_by_criteria(metadata, otu, col1, filter_by, col2=None, filter_by2=None):
    """Filter an OTU table and mapping file by user-defined variables
    """
    metadata, otu_table = read_files(metadata, otu)
    otu_table = otu_table.T
    filtered_meta = metadata[metadata[col1] == filter_by]
    list_samples = filtered_meta.index.tolist()
    filtered_otu = otu_table[otu_table.index.isin(list_samples)].T

    if col2:
        try:
            filtered_meta = metadata[(metadata[col1] == filter_by) & (metadata[col2] == filter_by2)]
            list_samples = filtered_meta.index.tolist()
            filtered_otu = otu_table[otu_table.index.isin(list_samples)].T
            return filtered_meta, filtered_otu
        except:
            print("Error, no filtering criteria selected")
    return filtered_meta, filtered_otu

# filter mapping file and otu table by user defined criteria
# write resulting dfs as tab-separated files

def filter_by_list(sample_or_otu, filter_file, metadata, otu, prefilter=False, col1=None, filter_by=None, col2=None, filter_by2=None,):
    """Filter an OTU table and mapping file by a list of samples/OTUs
    """
    metadata, otu, filter_file = read_files(metadata, otu, filter_file=filter_file)
    filter_list = filter_file.index.tolist()
    if prefilter == True:
        metadata, otu = filter_by_criteria(metadata, otu, col1=col1, filter_by=filter_by)
        if col2:
            metadata, otu = filter_by_criteria(metadata, otu, col1=col1, filter_by=filter_by, col2=col2, filter_by2=filter_by2)
    else:
        if sample_or_otu == "sample_list":
            filtered_meta = metadata[metadata.index.isin(filter_list)]
            filtered_otu = otu[filter_list]
            return filtered_meta, filtered_otu
        elif sample_or_otu == "OTU_list":
            filter_meta = metadata
            filtered_otu = filtered_otu[filter_list]
            return filtered_meta, filtered_otu

def write_tab(file1, filename1, file2, filename2):
    file1.to_csv(filename1, sep="\t", encoding="utf-8")
    file2.to_csv(filename2, sep="\t", encoding="utf-8")
