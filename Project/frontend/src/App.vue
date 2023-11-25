<template>
  <div id="app">
    <transition name="anim">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
    }
  }
}
</script>

<style>
#app {
  width: 100%;
  overflow-x: hidden;
}

.anim-enter-active, .anim-leave-active {
  transition: opacity 0.5s;
}

.anim-enter, .anim-leave-to{
  opacity: 0;
}
</style>