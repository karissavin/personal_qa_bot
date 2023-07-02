$("p").scrollTop(0);

let play = true;
let currentScroll = 0;
let endOfScroll = 0;
let speed = 32;
let teleprompter = null;
let scroller = setInterval(scroll, speed);

function scroll() {
    if (play === true) {
        teleprompter = $("p.teleprompter")
        currentScroll = teleprompter.scrollTop();
        endOfScroll = Math.round(teleprompter.prop('scrollHeight') - currentScroll)
        if (endOfScroll === teleprompter.prop('clientHeight')) {
            // Scroll back to top
            teleprompter.scrollTop(0);
        } else {
            // Keep scrolling to the end of content
            teleprompter.scrollTop(currentScroll + 1);
        }
    }
}

function keyDownTextField(e) {
    let keyCode = e.keyCode;
    if (keyCode === 192) {
        event.preventDefault();
        play = !play;
        return false;
    }
}

document.addEventListener("keydown", keyDownTextField, false);