const chatBox = document.getElementById("chat-box");

async function sendMessage() {

    const input = document.getElementById("message");

    const message = input.value.trim();

    if(message==="") return;

    chatBox.innerHTML +=
    `
    <div class="user">
        <span>${message}</span>
    </div>
    `;

    input.value="";

    try{

        const response = await fetch(
            "http://127.0.0.1:5000/chat",
            {

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    message:message
                })

            }
        );

        const data = await response.json();

        chatBox.innerHTML +=
        `
        <div class="bot">
            <span>${data.response}</span>
        </div>
        `;

        chatBox.scrollTop=chatBox.scrollHeight;

    }

    catch(error){

        chatBox.innerHTML +=
        `
        <div class="bot">
            <span>❌ Backend Connection Failed</span>
        </div>
        `;
    }

}

document.getElementById("message")
.addEventListener("keypress",function(e){

    if(e.key==="Enter"){

        sendMessage();

    }

});