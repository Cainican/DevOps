// バニラJSで、DOM読み込み後にアラート表示
document.addEventListener("DOMContentLoaded", function () {
  alert("バニラJS")
})

// 合ってるのに実行されない場合
// Win: Ctrl + Shift + R

// TODO: jQueryで、DOM読み込み後にアラート表示
$(function () {
  alert('始まるよ～')
});

alert('次行きます');

// TODO:DOM読み込み前の処理
