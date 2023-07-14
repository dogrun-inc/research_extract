# ミーティングのメモ

## 230714

- 設計をコードにどう落としていくか
- __丸角を処理として関数にしてしまう__ のが一番良い
- どの処理を最初にするかなどは後で考える
- 関数命名法：GET､PARSE 一般的な動詞+ 名詞
- doc strung を書いてしまおう
- 正式な書き方があるらしい
- argumentも書ける
- もしかしたら関数を分割する必要があるかもしれない

&nbsp;

### 大石さんからのアドバイス

- 自分の設計だと､スプレッドシート2つに書き込むことになっていたが､ブックに書き込む方法のほうがAPIの回数の節約になる??

```python

def get pmids(query:str) -> list:
    """
    APIを使って､Pubmedをキーワードを検索し､必要なPMIDをリストで出力する

    Parameters
    ----------

    query : str
        検索キーワード
    
    Returns
    -------
    pmids : list
        検索結果のPMIDのリスト
    """
    pass

def get _abstract(pmid:str) -> str:
    """
    APIを使って､PubmedのPMIDを引数とし､指定して､PubmedからAbstractの文字列を取得する
    リストとAbstractの辞書を返す

    Parameters
    ----------

    pmid : list
        検索結果のPMIDのリスト
    
    Returns
    -------
    abstract : dict
        検索結果のPMIDと､そのPMIDのAbstractの辞書
    """
    pass

def use_openai(abstract:str, prompt:str) -> dict: # JSON file as a dict
    """

    promptとabstractを引数とし､OpenAIのAPIをコールし､その結果を返す

    Parameters
    ----------
    
    Returns
    -------
 
    """
    pass

def dict2googlespreadsheet(openai_result:dict) -> None:
    """

    OpenAIの結果をGoogleSpreadSheetに書き込む
    GoogleのAPIを使って書き出す
    Google DriveかなにかのModuleをインストールする必要あり

    Parameters
    ----------
    
    Returns
    -------
 
    """
    pass

def main():
    """
    処理をここに書いていく
    Config yamlとかに書いた設定ファイルを読み込むか､コマンドライン引数(argparseをインポート)で受け取る
    Config.pyを作って､変数(文字列)を作っておくと良い
    このように設定ファイルに別の設定を書いておく

    """
    query_strings = config.query
    pmids = get_pmids("your query")
    abstracts = []
    for pmid in pmids:
        abstract = get_abstract(pmid)
        abstracts.append(abstract)

    #ここでabstractsを使ってOpenAIに投げる処理を書く 

    for abstarct in abstracts:
        openai_result = use_openai(abstract, prompt)
    
    # ここでopenai_resultを使ってGoogleSpreadSheetに1件ずつ書き込む処理を書く
    # googleのAPIは回数制限があるので､考慮が必要
    # もしgoogleのAPIの制限で処理が止まってしまう場合は書き換える
        dict2googlespreadsheet(openai_result)

    pass


```

&nbsp;

&nbsp;

## 230713

- Perplexityでちょっとわからないところがあったので聞いてみた
- [How do I get the PMC ID and the paper's title associated with it using the NCBI API?](https://www.perplexity.ai/search/7ee30316-65c5-4ad1-b6da-2520a63dee50?s=u)

```python

from Bio import Entrez

# メールアドレスを設定
Entrez.email = "your.email@example.com"

# 検索クエリを作成
search_term = "your search term here"

# 検索を実行
handle = Entrez.esearch(db="pmc", term=search_term)

# 検索結果を解析
record = Entrez.read(handle)

# PMC IDを取得
pmc_id = record["IdList"][0]

# PMC IDを使用して論文のメタデータを取得
handle = Entrez.esummary(db="pmc", id=pmc_id)
record = Entrez.read(handle)

# 論文のタイトルを取得
title = record[0]["Title"]

```

## 230707

- 一つの処理を一つの関数にブチ込めるようにアクティビティ図を完成させる
- 差分をとってくる処理をわかりやすく書く
- API 周りの設計図は鈴木さんを参考に
- メモ：繰り返し処理を後で追加

&nbsp;

### 1. どのような情報を取得するのかを決める(優先)

- メタデータに詳細な記述がない情報を取得したい
- 処理温度､処理時間､処理(incubator, water bath, fieldなど)
- この前ちらっと考えていたこと:処理温度と処理時間の散布図を作りたい
- [Marginal Plot with Seaborn](https://python-graph-gallery.com/82-marginal-plot-with-seaborn/)
- ![Alt text](./image/scatterplot.png)

&nbsp;

### 2. どのような処理を行うのか

Eーdirectに変更
研究で使うならGPT使わないほうが良い?
どういうattributionが欲しいのか