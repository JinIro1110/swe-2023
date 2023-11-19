<template>
    <div class="thisInfo container-fluid">
        <div class="category row">
            <div class="col text-start">
                <span style="font-size: 14px; color: rgb(221, 221, 221)">{{ bigCategory }}dd><span style="color: gray">{{
                    smallCategory }}dd</span></span>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <img src="../assets/bebeluna_mild_lotion.jpg" class="img-fluid">
            </div>
        </div>
        <div class="row text-start p-2">
            <div class="brandInfo d-flex justify-content-between">
                <div class="" style="font-size: 16px; color: rgb(150, 150, 150)">브랜드 ></div>
                <div class=""><img src="../assets/icons/share.png" width="20px"></div>
            </div>
            <div class="nameInfo">
                <div style="font-weight: bold; font-size: 20px;">드시모네 베이비 스텝 1 1+1</div>
            </div>
            <div class="reviewInfo mb-3">
                <span><img src="../assets/icons/star.svg" alt="" width="16px"></span>
                <span><img src="../assets/icons/star.svg" alt="" width="16px"></span>
                <span><img src="../assets/icons/star.svg" alt="" width="16px"></span>
                <span><img src="../assets/icons/star.svg" alt="" width="16px"></span>
                <span><img src="../assets/icons/star.svg" alt="" width="16px"></span>
                <span> 4.9 </span>
                <span style="font-size: 14px; color: rgb(150, 150, 150); text-decoration: underline;" @click="goReview">count개 리뷰보기</span>
            </div>
            <div class="priceInfo">
                <span class="discount">30%</span>
                <span class="discountedPrice">29000 <span style="font-size:18px; margin-right:5px;">원</span></span>
                <span class="price">20000원</span>
            </div>
            <div class="resultPrice">

            </div>
            <div class="coupon">

            </div>
        </div>
        <div class="deliver">
            <div class="cont">
                <div class="free">

                </div>
                <div class="mileage">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'itemMain',
    props: {
    },
    data() {
        return {
            bigCategory: '',
            smallCategory: '',
            brand: '',
            rating: '',
        }
    },
    methods: {
        goReview() {
            this.$router.push({
                name: "reviews",
            });
        }
    },
    created() {
        this.bigCategory = this.$store.state.bigCategory;
        this.smallCategory = this.$store.state.smallCategory;
    }
}
</script>

<style scoped>
.thisInfo {
    margin: 40px 0;

}
.category {
    margin: 0;
}
.discount {
    font-size: 30px;
    color: rgb(125, 157, 214);
    font-weight: bold;
    margin-right: 8px;
}

.price {
    text-decoration: line-through;
    font-size: 18px;
    font-weight: bold;
    margin-right: 5px;
    color: rgb(150, 150, 150);
}
.discountedPrice {
    font-size: 30px;
}
</style>
