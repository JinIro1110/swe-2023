<template>
    <div class="headMenu container-fluid text-center p-3">
        <div class="row justify-content-evenly">
            <div class="col d-flex justify-content-start" @click="goBack">
                <img src="../assets/icons/backward.png" class="iconWidth">
            </div>
            <div class="col d-flex justify-content-center" style="font-size: 17px; font-weight: lighter;">
                리뷰count개
            </div>
            <div class="col">
            </div>
        </div>
    </div>
    <ReviewTemplate/>
</template>

<script>
import ReviewTemplate from './reviewTemplate.vue';
export default {
    name: "reviewPage",
    data() {
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
    },
    components: { ReviewTemplate }
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

.main {
    margin-top: 40px;
}
</style>