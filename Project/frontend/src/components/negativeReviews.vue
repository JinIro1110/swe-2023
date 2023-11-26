<template>
    <div class="headMenu container-fluid text-center p-3">
        <div class="row justify-content-evenly">
            <div class="col d-flex justify-content-start">
                <img src="../assets/icons/backward.png" class="iconWidth" @click="goBack">
            </div>
            <div class="col d-flex justify-content-center" style="font-size: 17px; font-weight: lighter;">
                {{ keyWord }} 포함 리뷰
            </div>
            <div class="col">
            </div>
        </div>
    </div>
    <div class="review p-3" v-for="consReview in consReviews" :key="consReview.ReviewID">
        <div class="">
            <div class="userInfo d-flex align-items-start text-start">
                <img class="profile" :src="require('@/assets/icons/user.png')">
                <div class="babyInfo mb-2">
                    <div class="userName">유저 {{ consReview.UserID }}</div>
                    <div class="baby">만 2세 <span>&#183;</span> 민감성 <span>&#183;</span> 여아</div>
                    <svg v-for="i in 5" :key="i" width="12" height="12" viewBox="0 0 24 24">
                        <path :fill="i <= consReview.Rating ? 'gold' : '#ccc'"
                            d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z" />
                    </svg>
                </div>
            </div>
        </div>
        <div class="reviewContainer">
            <img class="reviewIcon" :src="require('@/assets/icons/bad.png')">
            <div class="reviewText" v-html="highlightKeyWord(consReview.NegativeReviewText)"></div>
        </div>
    </div>
</template>

<script scoped>
import axios from 'axios';
export default {
    data() {
        return {
            consReviews: [],
            consKeyWord: '',
        };
    },
    created() {
        this.consKeyWord = this.$route.query.KeyWord;
    },
    mounted() {
        const getConsKeyWordReviews = `http://192.168.0.213:3000/api/review/getConsKeyWordReviews/`;
            axios.get(getConsKeyWordReviews, {
                params: {
                    "itemId": this.$store.state.itemId,
                    "keyWord": this.consKeyWord
                }
            })
                .then((response) => {
                    this.consReviews = response.data.results;
                })
                .catch((error) => {
                    console.error('API 요청 중 오류 발생:', error);
                });
    },
    methods: {
        highlightKeyWord(text) {
            if (!this.consKeyWord) return text;
            const regex = new RegExp(`(${this.consKeyWord})`, 'gi');
            return text.replace(regex, '<span class="highlight">$1</span>');
        },
        goBack() {
            this.$router.go(-1);
        },
    }
}
</script>

<style>
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

.highlight {
    color: red;
}
</style>