<template>
    <div class="b-card">
        <b-form-input
            v-model="value"
            type="text"
            debounce="500"
            placeholder="Say Something"
            class="col-sm-9 input"
        ></b-form-input>
        <b-button-toolbar class="firstIcons col-sm-9">
            <b-button-group>
                <b-button title="Shortcut" class="iconC">
                    <i class="fa fa-bolt icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Shortcut" class="iconC">
                    <i aria-hidden="true"> | </i>
                </b-button>
                <b-button title="Bold" class="iconC">
                    <i class="fa fa-bold icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Italic" class="iconC">
                    <i class="fa fa-italic icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Underline" class="iconC">
                    <i class="fa fa-underline icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Underline" class="iconC">
                    <i class="fa fa-code icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Strikethrough" class="iconC">
                    <i class="fa fa-link" aria-hidden="true"></i>
                </b-button>
                <b-button title="Underline" class="iconC">
                    <i class="fa fa-list-ul icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Underline" class="iconC">
                    <i class="fa fa-file-code-o icon" aria-hidden="true"></i>
                </b-button>
            </b-button-group>
        </b-button-toolbar>

        <b-button-toolbar class="secondIcons col-sm-9">
            <b-button-group>
                <b-button title="Shortcut" class="iconC">
                    <i class="fa fa-font icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Shortcut" class="iconC">
                    <i class="fa fa-at icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Bold" class="iconC">
                    <i class="fa fa-smile-o icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Italic" class="iconC">
                    <i class="fa fa-paperclip icon" aria-hidden="true"></i>
                </b-button>
            </b-button-group>
        </b-button-toolbar>

        <b-button-toolbar class="thirdIcons">
            <b-button-group>
                <b-button title="Underline" class="iconC">
                    <i class="fa fa-paper-plane icon" aria-hidden="true"></i>
                </b-button>
                <b-button title="Underline" class="iconC">
                    <i aria-hidden="true" class="icon1">| </i>
                    <b-icon
                        icon="chevron-down"
                        aria-hidden="true"
                        class="icon2"
                    ></b-icon>
                </b-button>
            </b-button-group>
        </b-button-toolbar>
    </div>
</template>

<script>
export default {
    name: 'InputBox',
    data() {
        return {
            value: '',
        };
    },
};
</script>

<style scoped>
.b-card {
    width: 100%;
    height: 50%;
    border: 1.5px solid #999999;
    border-radius: 5px;
}
.input {
    padding: 10px;
    width: 98.22%;
    border: none;
}

.firstIcons {
    text-align: left;
    margin-left: 10px;
}
.iconC {
    border: none;
    padding: 3px;
    background-color: white;
}
.iconC:hover {
    background-color: #e9e9e9;
}
.icon {
    color: #3a3a3a;
    padding: 3px;
}
.secondIcons {
    position: absolute;
    left: 83%;
    bottom: 89.4%;
}
.thirdIcons {
    position: absolute;
    left: 93%;
    bottom: 89.4%;
}
.thirdIcons .icon,
.thirdIcons .icon1 {
    color: #c1c1c1;
}
.thirdIcons .icon2 {
    color: #c1c1c1;
    margin-bottom: -3px;
}
</style>
