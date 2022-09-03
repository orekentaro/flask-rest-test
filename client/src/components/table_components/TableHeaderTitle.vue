<template>
  <div>
    <h1 class="pb-5">{{ title }}</h1>
  </div>
</template>
<script lang="ts" setup>
interface Props {
  title: string | undefined;
}
withDefaults(defineProps<Props>(), {
  title: "",
});
</script>
<style scoped>
h1 {
  color: #7b7c7f;
  font-weight: 600;
  font-size: 1.5rem;
}
</style>
