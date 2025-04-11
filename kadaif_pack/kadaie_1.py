def kadaie_1(input1: str, input2: int) -> None:
    """課題F用の提出用関数

    指定されたpdbファイルを読み込み、指定された数以下の残基数の割合を表示します。

    Arguments:
        input1 (str): pdbファイルのパス
        input2 (int): 残基数の上限

    Returns:
        None

    """
    import gzip

    from Bio import SeqIO

    fastafile = input1
    upper_limit = input2
    allrecords = 0
    count = 0
    target_s = "length:"
    target_e = "  "

    def superopen(filename):
        """ファイルを開く関数"""
        if filename.endswith(".gz"):
            return gzip.open(filename, "rt")
        return open(filename, "r")

    with superopen(fastafile) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            allrecords += 1
            desc_part = record.description
            start = desc_part.find(target_s)
            end = desc_part.find(target_e)
            length = int(desc_part[start + 7 : end])
            if length <= upper_limit:
                count += 1

    print(count / allrecords * 100)
