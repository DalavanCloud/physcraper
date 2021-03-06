import sys
from physcraper.concat import Concat

#
workdir_its = "runs/tiny_comb_its"
workdir_ets = "runs/tiny_comb_ets"
email = "martha.kandziora@yahoo.com"
pickle_fn = "scrape_checkpoint.p"

workdir_comb = "tests/output/impl_concat"
genelist = {"its": {"workdir": workdir_its, "pickle": pickle_fn}, "ets": {"workdir": workdir_ets, "pickle": pickle_fn}}

# get to test status

sys.stdout.write("\ntests Concat func sp_counter\n")

def test():
    concat = Concat(workdir_comb, email)
    for item in genelist.keys():
        concat.load_single_genes(genelist[item]["workdir"], genelist[item]["pickle"], item)

    concat.combine()
    concat.sp_seq_counter()

    # print("tests if nothing gets lost from loading single runs to make sp_counter")

    counter = 0
    for sp in concat.sp_counter:
        for gene in concat.sp_counter[sp]:
            counter += concat.sp_counter[sp][gene]
    # print(counter)

    single_run_items = 0
    for item in concat.single_runs:
        single_run_items += (len(concat.single_runs[item].data.aln.taxon_namespace))

    assert counter == single_run_items
