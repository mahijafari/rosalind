# https://rosalind.info/problems/gc/

gc_counter = {
    "current": {
        "fasta_id": "",
        "gc_count": 0,
        "char_count": 0,
        "gc_percentage": 0,
    },
    "selected": {
        "fasta_id": "",
        "gc_percentage": 0
    }
}

while True:
    input_str = input()
    if not input_str:
        if gc_counter["current"]["gc_percentage"] > gc_counter["selected"]["gc_percentage"]:
            gc_counter["selected"]["gc_percentage"] = gc_counter["current"]["gc_percentage"]
            gc_counter["selected"]["fasta_id"] = gc_counter["current"]["fasta_id"]
        break

    if input_str[0] == ">":
        if gc_counter["current"]["gc_percentage"] > gc_counter["selected"]["gc_percentage"]:
            gc_counter["selected"]["gc_percentage"] = gc_counter["current"]["gc_percentage"]
            gc_counter["selected"]["fasta_id"] = gc_counter["current"]["fasta_id"]
        gc_counter["current"]["fasta_id"] = input_str[1:]
        gc_counter["current"]["char_count"] = 0
        gc_counter["current"]["gc_count"] = 0
        gc_counter["current"]["gc_percentage"] = 0
    else:
        gc_counter["current"]["char_count"] += len(input_str)
        gc_counter["current"]["gc_count"] += len([char for char in input_str if char in ["C","G"]])
        gc_counter["current"]["gc_percentage"] = gc_counter["current"]["gc_count"]/gc_counter["current"]["char_count"]

print(gc_counter["selected"]["fasta_id"])
print(f'{gc_counter["selected"]["gc_percentage"]*100:0.6f}')

