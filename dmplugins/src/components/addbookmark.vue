<template>
    <div id="app">
        <b-container>
            <div id="card">
                <div id="frame">
                    <h1 id="add">Add a bookmark</h1>
                    <i class="fal fa-times"></i>
                </div>
                <h3>Link</h3>
                <b-form-textarea
                    id="textarea-default"
                    size="sm"
                    placeholder="https://docs.acme.com "
                    style="overflow-y: hidden; resize: none;"
                >
                </b-form-textarea>
            </div>
        </b-container>
    </div>
</template>

<script>
export default {
    name: 'addbookmark',
};
</script>

<style scoped>
#card {
    position: absolute;
    width: 464px;
    height: 195px;
    top: 300px;
    left: 488px;
    border: 1px solid #e7e7e7;
    border-radius: 4px;
    box-sizing: border-box;
    box-shadow: 1px 1px 44px rgba(64, 64, 64, 0.5);
}

#frame {
    display: flex;
    justify-content: space-between;
    width: 416px;
    height: 61px;
}

#add {
    width: 205px;
    height: 34px;
    font-size: 28px;
    font-family: 'Lato';
    font-style: normal;
    font-weight: bold;
    line-height: 34px;
    position: absolute;
    left: 24px;
    top: 24px;
}

i {
    width: 14px;
    height: 14px;
    position: absolute;
    right: 24px;
    top: 32px;
}

h3 {
    width: 24px;
    height: 16px;
    font-family: 'Lato';
    font-style: normal;
    font-size: 13px;
    font-weight: normal;
    line-height: 16px;
    color: #454545;
    position: absolute;
    left: 24px;
    top: 82px;
}

#textarea-default {
    width: 416px;
    height: 61px;
    font-family: 'Lato';
    font-style: normal;
    font-size: 11px;
    line-height: 13px;
    color: #747374;
    position: absolute;
    left: 24px;
    bottom: 24px;
    padding-top: 21px;
    border: 1px solid #1a1a1a;
    box-sizing: border-box;
    border-radius: 6px;
}
</style>
