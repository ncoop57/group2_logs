from datasets import load_dataset
from datasets import load_from_disk
from datasets import Dataset
import pandas as pd
lst_pandas= []
for i in range(9):
    print(i)
    ds = load_from_disk(f"pilev2_local_dedup/C4_DKPRO/C4_DKPRO_{i}/")
    try:
        ds = ds.remove_columns(['check_char_repetition_criteria', 'check_flagged_words_criteria', 'check_stop_word_ratio_criteria'])
    except:
        pass
    df = ds.to_pandas()
    # remove duplicates based on the text column
    df = df.drop_duplicates(subset=['text'])
    lst_pandas.append(df)

all_df = pd.concat(lst_pandas)
all_df = all_df.drop_duplicates(subset=['text'])
dataset = Dataset.from_pandas(all_df)
dataset.save_to_disk("C4_DKPRO_0-8_dedup/")
