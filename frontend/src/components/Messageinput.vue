<template>
    <div>
        <h6 class="dm1">All direct messages</h6>
        <div class="card-body">
            <div class="form-group">
                <input
                    type="email"
                    class="form-control"
                    placeholder="To:  @somebody or somebody@example.com"
                />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MessageInput',
};
</script>

<style scoped>
.form-control {
    height: 50px;
    background-color: white;
}
.dm1 {
    margin-top: 30px;
    text-align: left;
    margin-left: 20px;
}
</style>
