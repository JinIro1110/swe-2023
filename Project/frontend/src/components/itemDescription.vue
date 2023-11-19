<template>
  <headMenu :menu="menu" />
  <itemMain />
  <purchaseItem />
</template>
  
<script scoped>
import headMenu from './headMenu.vue'
import itemMain from './itemMain.vue';
import purchaseItem from './purchaseItem.vue';
export default {
  name: 'itemDescription',
  components: {
    headMenu,
    itemMain,
    purchaseItem
  },
  data() {
    return {
      menu: '상품정보'
    };
  }
}
</script>
  
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}

</style>
  
  