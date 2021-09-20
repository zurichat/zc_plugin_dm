<template>
  <div class="pinned-info d-inline-flex align-items-center mb-3 px-3 py-1">
        <div class="me-1"><img src="../assets/pin.png" alt="Pin photo"></div>
        <div>
            <!-- {{ totalMesssagesPinned }} Pinned -->
            {{counter}} Pinned
        </div>
    </div>
</template>

<script>
export default {
    name: 'PinMessageThread',
    data() {
        return {
            counter: 1
        }
    }
}
</script>

<style>
.pinned-info {
    cursor: pointer;
    background-color: #e1fdf4;
}
</style>