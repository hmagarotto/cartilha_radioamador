function revealAnswer(e) {
    this.classList.add("hidden");
    this.nextElementSibling.classList.remove("hidden");
}

const qnaLabels = document.querySelectorAll(".qna.answer_label");
for (const label of qnaLabels) {
    label.addEventListener("click", revealAnswer);
}
