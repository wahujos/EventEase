<template>
  <RouterView />
  <Home />
</template>

<script setup>
import { RouterView } from 'vue-router'
import { Home} from './components/Home.vue'
</script>
