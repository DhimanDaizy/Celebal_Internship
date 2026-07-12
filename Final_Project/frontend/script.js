const chatBox = document.getElementById("chatBox");
const promptInput = document.getElementById("prompt");
const sendBtn = document.getElementById("sendBtn");
const typing = document.getElementById("typing");
const welcome = document.getElementById("welcome");
const clearBtn = document.getElementById("clearChat");
const newChatBtn = document.getElementById("newChat");

const API_URL = "http://127.0.0.1:5000/chat";   // Change after deployment

function scrollBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

function currentTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}

function createMessage(text, type) {

    const wrapper = document.createElement("div");
    wrapper.className = `message ${type}`;

    wrapper.innerHTML = `
        <div>${text}</div>

        <div style="
            margin-top:10px;
            display:flex;
            justify-content:space-between;
            align-items:center;
            font-size:12px;
            opacity:.7;
        ">
            <span>${currentTime()}</span>

            ${
                type === "bot"
                    ? `<button class="copyBtn"
                        style="
                        background:none;
                        border:none;
                        color:#bbb;
                        cursor:pointer;
                        ">
                        📋
                    </button>`
                    : ""
            }
        </div>
    `;

    if (type === "bot") {

        wrapper.querySelector(".copyBtn")
            .addEventListener("click", () => {

                navigator.clipboard.writeText(text);

                const btn = wrapper.querySelector(".copyBtn");
                btn.innerText = "✅";

                setTimeout(() => {
                    btn.innerText = "📋";
                }, 1500);

            });

    }

    chatBox.appendChild(wrapper);

    scrollBottom();
}

async function sendMessage() {

    const prompt = promptInput.value.trim();

    if (!prompt) return;

    welcome.style.display = "none";

    createMessage(prompt, "user");

    promptInput.value = "";

    typing.style.display = "flex";

    scrollBottom();

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: prompt
            })

        });

        const data = await response.json();

        typing.style.display = "none";

        createMessage(
            data.response || "No response received.",
            "bot"
        );

    }

    catch (err) {

        typing.style.display = "none";

        createMessage(
            "⚠️ Unable to connect to backend.",
            "bot"
        );

        console.error(err);

    }

}

sendBtn.addEventListener("click", sendMessage);

promptInput.addEventListener("keydown", function (e) {

    if (e.key === "Enter" && !e.shiftKey) {

        e.preventDefault();

        sendMessage();

    }

});

clearBtn.addEventListener("click", () => {

    chatBox.innerHTML = "";

    welcome.style.display = "block";

});

newChatBtn.addEventListener("click", () => {

    chatBox.innerHTML = "";

    welcome.style.display = "block";

    promptInput.value = "";

});

document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("click", () => {

        promptInput.value = card.innerText;

        sendMessage();

    });

});

scrollBottom();