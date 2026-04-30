function revealAnswer(e) {
    this.classList.add("hidden");
    this.nextElementSibling.classList.remove("hidden");
}

const qnaLabels = document.querySelectorAll(".qna.answer_label");
for (const label of qnaLabels) {
    label.addEventListener("click", revealAnswer);
}

function shuffleQuestions(section) {
    const container = document.querySelector(`.sect2:has(#${section})`)
    const questions = document.querySelectorAll(`.sect2:has(#${section}) .paragraph`)
    const shuffled = [...questions]
        .map(question => ({ question, sort: Math.random() })) // Assign random keys
        .sort((a, b) => a.sort - b.sort)                // Sort by keys
        .map(({question}, index) => {
            const questionLabel = question.querySelector('.qna.question')
            const originalText = questionLabel.textContent;
            const newText = originalText.replace(/^[0-9]+\./, `${index+1}.`);
            questionLabel.textContent = newText;
            return question;
        })

    questions.forEach(el => el.remove());
    container.append(...shuffled);
}

window.addEventListener("load", (event) => {
    shuffleQuestions('_técnica_e_ética_operacional_3');
    shuffleQuestions('_legislação_de_telecomunicações_3');
    shuffleQuestions('_conhecimentos_de_eletrônica_e_eletricidade_2');
})
