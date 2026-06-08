document.addEventListener("DOMContentLoaded", function () {
    const fetchQuoteButton = document.getElementById("fetch-quote-button");
    const loadingDiv = document.getElementById("loading");
    const errorDiv = document.getElementById("error");
    const quoteDiv = document.getElementById("quote");
    const authorDiv = document.getElementById("author");

    // JSON読み込み+ランダム選択Promise
    function fetchRandomQuote() {
        loadingDiv.classList.remove("hidden");
        errorDiv.classList.add("hidden");
        quoteDiv.classList.add("hidden");
        authorDiv.classList.add("hidden");

        return new Promise((resolve, reject) => {
            const xhr = new XMLHttpRequest();
            // TODO: APIのURLを適切に設定する http://xxxxx/api/quotes.json
            // 同一サーバ: ./api/quotes.json
            const uri = "./api/quotes.json";
            xhr.open("GET", uri, true);

            xhr.onreadystatechange = () => {
                if (xhr.readyState !== 4) return;  // 完了前は無視

                if (xhr.status >= 200 && xhr.status < 300) {
                    let quotes;
                    try {
                        quotes = JSON.parse(xhr.responseText);
                    } catch (err) {
                        return reject("JSON のパースに失敗しました。");
                    }

                    // 90% の確率で成功
                    if (Math.random() > 0.1) {
                        const index = Math.floor(Math.random() * quotes.length);
                        resolve(quotes[index]);
                    } else {
                        reject("🥺 失敗！だがそれでいい");
                    }
                } else {
                    reject(`ステータスエラー: ${xhr.status}`);
                }
            };

            xhr.onerror = () => {
                reject("ネットワークエラーが発生しました。");
            };

            xhr.send();
        });
    }


    function handlerRandomQuote() {
        fetchRandomQuote()
            .then(quote => {
                displayQuote(quote);
            })
            .catch(errMsg => {
                displayError(errMsg);
            })
            .finally(() => {
                loadingDiv.classList.add("hidden");
            });
    }

    function displayQuote({ text, author }) {
        quoteDiv.textContent = `"${text}"`;
        authorDiv.textContent = `- ${author}`;
        quoteDiv.classList.remove("hidden");
        authorDiv.classList.remove("hidden");
    }

    function displayError(message) {
        errorDiv.textContent = message;
        errorDiv.classList.remove("hidden");
    }

    fetchQuoteButton.addEventListener("click", handlerRandomQuote);
});