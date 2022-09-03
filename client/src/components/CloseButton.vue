<template>
  <p class="close-button" v-on:click="clickClose">✖️</p>
</template>

<script lang="ts" setup>
interface Emits {
  (e: "close"): void;
}
const emit = defineEmits<Emits>();

const clickClose = () => {
  emit("close");
};
</script>

<style scoped>
.close-button {
  float: right;
}
.close-button:hover {
  cursor: pointer;
}
</style>
