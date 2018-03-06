*  First use "pip list --outdated --format json > update.json" to generate a json file.
* Then generate "update.txt" by this program.
* Final use "pip install -r update.txt" to update your env.

這產生二個檔案, 一個是現在env 中python 套件版本列表, 一個是最新的python 套件版本列表。
然後我們可以用pip install -r 來進行升級或還原開發環境。