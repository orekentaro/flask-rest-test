<template>
  <div class="common-layout">
    <div class="border-b-4 bg-sky-400">
      <el-header>
        <Header />
      </el-header>
    </div>
    <el-container>
      <el-aside width="200px"> <SideBar /> </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>
<script lang="ts" setup></script>

<style></style>
