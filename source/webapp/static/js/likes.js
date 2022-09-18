
async function SendLike(event){
    event.preventDefault();
    let target = event.target;
    let url = target.href;
    let response = await fetch(url);
    let response_json = await response.json();

    let count = response_json.count;
    let articleId = target.dataset.articleId;
    console.log(articleId) //"💔" "❤"
    let span = document.getElementById(articleId);
    span.innerText = `💕 ${count}`;
    if (target.innerText === "💔"){
        target.innerText = "❤";
    }
    else{
        target.innerText = "💔";
    }
}

function onloadFunc(){
    let likes = document.getElementsByClassName("likes");
    for(let i=0; i<likes.length; i++){
        likes[i].addEventListener("click", SendLike);
    }
}

window.addEventListener("load", onloadFunc);
