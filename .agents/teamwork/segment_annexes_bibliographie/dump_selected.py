with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\entries_638_651.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('\n\n')
entries = [e.strip() for e in entries if e.strip()]

check_list = [
    846, 847, 857, 858, 862, 868, 873, 876, 877, 878, 880, 885,
    890, 891, 892, 893, 895, 896, 899, 900, 901, 902, 903, 906, 907, 908, 909,
    916, 918, 920, 921, 923, 927, 928, 935, 936, 937, 941, 944, 950, 951, 954,
    973, 974, 978, 979, 980, 1006, 1007, 1060, 1061, 1062, 1063, 1064, 1065
]

with open(r'c:\Github\EntrepriseAgentique\.agents\teamwork\segment_annexes_bibliographie\selected_entries_check.txt', 'w', encoding='utf-8') as f_out:
    for idx_num in check_list:
        idx_in_list = idx_num - 846
        if 0 <= idx_in_list < len(entries):
            f_out.write(f"=== [{idx_num}] ===\n{entries[idx_in_list]}\n\n")

print(f"Dumped {len(check_list)} entries to selected_entries_check.txt")
