<template>
    <div class="headMenu container-fluid text-center p-3">
        <div class="row justify-content-evenly">
            <div class="col d-flex justify-content-start" @click="goBack">
                <img src="../assets/icons/backward.png" class="iconWidth">
            </div>
            <div class="col d-flex justify-content-center" style="font-size: 18px; font-weight: 400;">
                {{ menu }}
            </div>
            <div class="col d-flex justify-content-end me-3">
                <img src="../assets/icons/search.png" class="me-3 iconWidth">
                <img src="../assets/icons/cart.png" class="iconWidth">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'headMenu',
    props: {
        menu: String,
    },
    data() {
        return {
            imageWidth : "25px"
        };
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
    },
}
</script>

<style scoped>
.container-fluid {
    padding: 0px;
}

.row {
    align-items: center;
}

.headMenu {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background-color: white;
}

.iconWidth {
    width: 22px;
}
</style>
