
const speak = () => {
    const conf = confirm("Do you want to hear a joke?");

    if (conf) {
        alert("Let me tell you a joke!");
        let text = document.getElementById("input").value;
        let utterance = new SpeechSynthesisUtterance(text);
        speechSynthesis.speak(utterance);
    } else {
        alert("Okay, maybe next time!");
    }
}

const test = () => {
    console.log('Hello World');
    confirm("Does this work?");
    alert("Yes it does!");
  };

test();
