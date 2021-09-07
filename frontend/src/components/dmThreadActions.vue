<template>
    <div class="options">
        <div class="emoji">
            <img src="../assets/Gbemi/1.svg" alt="" />
            <img src="../assets/Gbemi/2.svg" alt="" />
            <img src="../assets/Gbemi/3.svg" alt="" />
            <img src="../assets/Gbemi/4.svg" alt="" />
            <img src="../assets/Gbemi/5.svg" alt="" />
            <img src="../assets/Gbemi/6.svg" alt="" />
        </div>
        <div class="select">
            <div class="option">
                <img src="../assets/Gbemi/clock/active.svg" alt="" />
                <p>Remind me</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/default.svg" alt="" />
                <p>Add to saved items</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/Threads.svg" alt="" />
                <p>Reply in thread</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/message-circle/active.svg" alt="" />
                <p>Follow message</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/share/active.svg" alt="" />
                <p>Share message</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/link/active.svg" alt="" />
                <p>Copy link to message</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/copy/active.svg" alt="" />
                <p>Copy text</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/P.svg" alt="" />
                <p>Pin to conversation</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/bar-chart/active.svg" alt="" />
                <p>Turn question into poll</p>
            </div>
            <div class="option">
                <img src="../assets/Gbemi/external-link/active.svg" alt="" />
                <p>More message shortcuts</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DmThreadActions',
};
</script>

<style scoped>
.option {
    display: flex;
    margin: 1em;
}
.options {
    text-align: left;
    border-radius: 1rem;
    background-color: whitesmoke;
}
p {
    margin-left: 3rem;
}
.emoji {
    margin: 1rem;
    padding-bottom: 0.2rem;
}
.select {
    border-top: grey solid 1px;
    padding-top: 1em;
}
</style>
