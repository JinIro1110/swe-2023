<template>
    <div class="headMenu container-fluid text-center p-3">
        <div class="row justify-content-evenly">
            <div class="col d-flex justify-content-start" @click="goBack">
                <img src="../assets/icons/backward.png" class="iconWidth">
            </div>
            <div class="col d-flex justify-content-center" style="font-size: 17px; font-weight: lighter;">
                리뷰 {{ reviewCount }}개
            </div>
            <div class="col">
            </div>
        </div>
    </div>
    <div class="main">
        <div class="photo d-flex align-items-center p-3">
            <span style="font-size:25px; font-weight: bold; margin-right:5px;">{{ rating }}</span>
            <svg v-for="i in 5" :key="i" width="22" height="22" viewBox="0 0 30 30">
                <path :fill="i <= rating ? 'gold' : '#ccc'"
                    d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z" />
            </svg>
        </div>
        <img src="../assets/icons/review.png" class="rounded-circle" @click="goWriteReview">
        <div class="wordCloud mt-5">
            <WordCloud :items="ProsCons"/>
        </div>
        <div class="reviews">
            <div class="review p-3" v-for="review in reviews" :key="review.ReviewID">
                <div class="">
                    <div class="userInfo d-flex align-items-start text-start">
                        <img class="profile" :src="require('@/assets/icons/user.png')">
                        <div class="babyInfo mb-2">
                            <div class="userName">유저 {{ review.UserID }}</div>
                    <div class="baby">만 2세 <span>&#183;</span> 민감성 <span>&#183;</span> 여아</div>
                    <svg v-for="i in 5" :key="i" width="12" height="12" viewBox="0 0 24 24">
                        <path :fill="i <= review.Rating ? 'gold' : '#ccc'"
                            d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z" />
                    </svg>
                        </div>
                    </div>
                </div>
                <div class="reviewContainer mb-2">
                    <img class="reviewIcon" :src="require('@/assets/icons/good.png')"><div class="reviewText">{{ review.PositiveReviewText }}</div>
                </div>
                <div class="reviewContainer">
                    <img class="reviewIcon" :src="require('@/assets/icons/bad.png')"><div class="reviewText">{{ review.NegativeReviewText }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import WordCloud from './WordCloud.vue';
import axios from 'axios';
export default {
    name: "reviewPage",
    data() {
        return {
            itemId: this.$store.state.itemId,
            brand: '',
            productName: '',
            rating: 0,
            review: {},
            reviews: [],
            reviewCount: 0,
            ProsCons: [],
        };
    },
    mounted() {
        const getProductRating = `http://192.168.0.213:3000/api/item/getProductRating/${this.itemId}`;
        axios.get(getProductRating)
            .then((response) => {
                this.rating = response.data.rating;
            })
            .catch((error) => {
                console.error('API 요청 중 오류 발생:', error);
            });

        const getReviews = `http://192.168.0.213:3000/api/review/getReviewInfo/${this.itemId}`;
        axios.get(getReviews)
            .then((response) => {
                this.review = response.data.reviewInfo;
                this.reviews = this.review.productReviews;
                this.reviewCount = this.review.reviewCount;
                this.ProsCons = this.review.productProsCons;
            })
            .catch((error) => {
                console.error('API 요청 중 오류 발생:', error);
            });
    },
    methods: {
        goBack() {
            this.$router.go(-1);
        },
        goWriteReview() {
            this.$router.push({
                name: 'writeReview', // 라우트 이름
                query: {
                    ProductName: this.$route.query.ProductName,
                    Brand: this.$route.query.Brand
                }
            });
        }
    },
    components: { WordCloud }
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
    margin-top: 60px;
}

.rounded-circle {
    width: 50px;
    position: fixed;
    bottom: 60px;
    right: 30px;
}

.profile {
    width: 40px;
    border-radius: 100%;
    padding: 5px;
    background-color: #ccc;
    margin-right: 10px;
}
.review {
    border-bottom: 1px #ccc solid;
}

.reviewContainer {
    display: flex;
    align-items: flex-start;
}

.reviewIcon {
    width: 22px;
    margin-right: 10px;
}

.reviewText {
    flex: 1;
    text-align: start;
}

.userName {
    font-weight: bold;
}
</style>