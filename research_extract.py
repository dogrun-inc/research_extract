# encoding: utf-8
import requests
import config
# argparseをimportしてコマンドライン引数を受け取れるようにする？？
# 汎用的なのはconfig.pyやconfig.pyを作る


def get_pmids(query:str) -> list:
    """
    APIを使って、PubMedをキーワード検索し、必要なPMIDをリストで出力する
    
    Parameters
    -------------
    query: str
        検索キーワード

    returns
    -------------
    pmids: list
        検索結果のPMIDのリスト
    """
    pass


def get_abstract(pmids:list) -> dict:
    """
    APIを使って、PubMedのPMIDを引数とし、PubMedからAbstractの文字列を取得。
    PMIDとAbstractのセットを辞書として返す
    
    Parameters
    -------------
    pmids: list
        検索結果のPMIDのリスト

    returns
    -------------
    abstracts: dict
        検索結果のPMIDと、そのPMIDの抄録の辞書
    """
    pass


def use_openai(abstracts:str,prompt:str) -> dict:
    """
    promptとabstractsを引数とし、OpenAIのAPIをコールし、その結果を返す

    """
    pass


def dict2googlespreadsheet(openai_result:dict) -> None:
    """
    OpenAIの結果をGoogleSpreadSheetに書き込む
    GoogleのAPIを使って書き出す
    Google DriveかなにかのModuleをインストールする必要あり
    """
    pass


def main():
    """
    処理を書いていく
    """
    query_strings = config.query
    pmids = get_pmids(query_strings)

    abstracts = []
    for pmid in pmids:
        abstract = get_abstract(pmid)
        abstracts.append(abstract)
    
    for abstract in abstracts:
        openai_result = use_openai(abstract)
        # 途中で止まった場合にもったいないので、１件ずつ書き込むのもあり
        # googleのAPIは回数制限があるので、考慮が必要
        # もしgoogleのAPIの制限で処理が止まってしまう場合は書き換える
        dict2googlespreadsheet(openai_result)
    pass

if __name__ == "__main__":
    main()
