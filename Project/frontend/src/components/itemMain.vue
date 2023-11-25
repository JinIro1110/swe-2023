<template>
    <div class="thisInfo container-fluid">
        <div class="category row">
            <div class="col text-start">
                <span style="font-size: 14px; color: rgb(221, 221, 221)">{{ mainCategory }}><span style="color: gray">{{
                    item.SubCategoryName }}</span></span>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <img :src="require(`@/assets/photos/bebeluna_mild_lotion.jpg`)" class="img-fluid">
            </div>
        </div>
        <div class="aboutPrice row text-start p-2">
            <div class="brandInfo d-flex justify-content-between">
                <div class="" style="font-size: 16px; color: rgb(150, 150, 150)">브랜드 > {{ item.Brand }}</div>
                <div class=""><img src="../assets/icons/share.png" width="20px"></div>
            </div>
            <div class="nameInfo">
                <div style="font-weight: bold; font-size: 20px;">{{ item.ProductName }}</div>
            </div>
            <div class="reviewInfo mb-3 d-flex align-items-center">
                <span class="photo d-flex align-items-center">
                    <svg v-for="i in 5" :key="i" width="15" height="15" viewBox="0 0 24 24">
                        <path :fill="i <= Rating ? 'gold' : '#ccc'"
                            d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z" />
                    </svg>
                    <span style="font-size:20px; font-weight: bold; margin-left:10px;">{{ Rating }}</span>
                </span>
                <span style="font-size: 14px; color: rgb(150, 150, 150); text-decoration: underline; margin-left: 10px;"
                    @click="goReview">{{ reviewCount }}개 리뷰보기</span>
            </div>
            <div class="priceInfo">
                <span class="discount">{{ item.Discount }}%</span>
                <span class="discountedPrice fw-bold">{{ changeNum(discountedPrice) }}<span
                        style="font-size:18px; margin-right:5px; margin-left:5px;">원</span></span>
                <span class="price">{{ changeNum(item.Price) }}</span>
            </div>
            <div class="resultPrice">

            </div>
            <div class="coupon">

            </div>
        </div>
        <div class="deliver p-2">
            <div class="cont text-start">
                <div class="free">
                    <span class="contLabel">배송</span>
                    <span v-if=item.FreeShipping class="delivery ms-4">무료배송</span> <!-- item.freeDelivery -->
                    <span v-else class="delivery ms-4">3000원</span>
                </div>
                <div class="mileage">
                    <span class="contLabel">적립</span>
                    <span class="ms-4">최대 {{ changeNum(item.Price * 0.05) }}+P적립</span>
                </div>
            </div>
        </div>
    </div>
    <div class="descriptionTab container-fluid">
        <div class="bar">
            <ul class="nav nav-pills nav-fill">
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: activeTab === 1 }" @click="activeTab = 1">성분정보</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: activeTab === 2 }" @click="activeTab = 2">상품소개</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: activeTab === 3 }" @click="activeTab = 3">리뷰({{ reviewCount
                    }})</a>
                </li>
            </ul>
        </div>
        <div v-if="activeTab === 1">

        </div>
        <div v-if="activeTab === 2">

        </div>
        <div v-if="activeTab === 3" class="p-3">
            <div class="photo d-flex align-items-center p-3">
                <span style="font-size:25px; font-weight: bold; margin-right:5px;">{{ Rating }}</span>
                <svg v-for="i in 5" :key="i" width="22" height="22" viewBox="0 0 30 30">
                    <path :fill="i <= Rating ? 'gold' : '#ccc'"
                        d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z" />
                </svg>
            </div>
            <img src="../assets/icons/review.png" class="rounded-circle" @click="goWriteReview">
            <div class="wordCloud mt-5">
                <WordCloud :items="ProsCons"/>
            </div>
            <div class="reviews">
                <div class="review p-3" v-for="review in reviews" :key="review.ReviewID">
                    <div>
                        <div class="userInfo d-flex align-items-start text-start">
                            <img class="profile" :src="require('@/assets/icons/user.png')">
                            <div class="babyInfo">
                                <div class="userName">유저{{ review.UserID }}</div>
                                <div class="baby">만 2세 <span>&#183;</span> 민감성 <span>&#183;</span> 여아</div>
                                <svg v-for="i in 5" :key="i" width="12" height="12" viewBox="0 0 24 24">
                                    <path :fill="i <= review.Rating ? 'gold' : '#ccc'"
                                        d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z" />
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="reviewContainer">
                        <img class="reviewIcon" :src="require('@/assets/icons/good.png')">
                        <div class="reviewText">{{ review.PositiveReviewText }}</div>
                    </div>
                    <div class="reviewContainer">
                        <img class="reviewIcon" :src="require('@/assets/icons/bad.png')">
                        <div class="reviewText">{{ review.NegativeReviewText }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import WordCloud from './WordCloud.vue';
import axios from 'axios';
export default {
    name: "itemMain",
    data() {
        return {
            itemId: this.$store.state.itemId,
            mainCategory: this.$store.state.mainCategory,
            item: {},
            Rating: 2,
            reviewCount: 0,
            reviews: [],
            activeTab: 3,
            ProsCons: [],
        };
    },
    mounted() {
        const getProductInfo = `http://192.168.0.213:3000/api/item/getProductInfo/${this.itemId}`;
        axios.get(getProductInfo)
            .then((response) => {
                this.item = response.data.productInfo;
                this.Rating = this.item.Rating;
            })
            .catch((error) => {
                console.error('API 요청 중 오류 발생:', error);
            });

        const getReviews = `http://192.168.0.213:3000/api/review/getReviewInfo/${this.itemId}`;
        axios.get(getReviews)
            .then((response) => {
                this.review = response.data.reviewInfo;
                this.reviews = this.review.productReviews.slice(0, 5);
                this.reviewCount = this.review.reviewCount;
                this.ProsCons = this.review.productProsCons;
            })
            .catch((error) => {
                console.error('API 요청 중 오류 발생:', error);
            });
    },
    methods: {
        goReview() {
            this.$router.push({
                name: "reviews",
                query: {
                    ProductName: this.item.ProductName,
                    Brand: this.item.Brand
                }
            });
        },
        updateStarWidth() {
            for (let i = 1; i <= 5; i++) {
                const starWidth = this.getStarWidth(i);
                // 여기에서 어떻게 활용하려는지에 따라 적절한 작업을 수행합니다.
                console.log(`Star ${i} Width: ${starWidth}`);
            }
        },
        changeNum(value) {
            if (value != null) {
                // 숫자를 문자열로 변환
                let valueStr = value.toString();

                // 소수점 이하의 숫자 제거
                valueStr = valueStr.split('.')[0];

                // 천 단위마다 쉼표 추가
                return valueStr.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,");
            } else {
                return "";
            }
        },
        goWriteReview() {
            this.$router.push({
                name: 'writeReview', // 라우트 이름
                query: {
                    ProductName: this.item.ProductName,
                    Brand: this.item.Brand
                }
            });
        },
    },
    created() {
        this.mainCategory = this.$store.state.mainCategory;
    },
    computed: {
        discountedPrice() {
            return this.item.Price * (1 - this.item.Discount / 100);
        },
    },
    components: { WordCloud }
}
</script>

<style scoped>
.thisInfo {
    margin-top: 60px;
}

.descriptionTab {
    margin-bottom: 60px;
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
    font-size: 20px;
    font-weight: bold;
    margin-right: 5px;
    color: rgb(150, 150, 150);
}

.aboutPrice {
    border-bottom: 1px #ccc solid;
}

.discountedPrice {
    font-size: 30px;
}

.cont {
    font-size: 14px;
}

.contLabel {
    color: gray;
}

.delivery {
    color: dodgerblue;
}

.free {
    margin-top: 10px;
    margin-bottom: 10px;
}

.mileage {
    margin-top: 10px;
    margin-bottom: 10px;
}

.thisInfo {
    border-bottom: 5px #edebeb solid;
}

.nav-link {
    color: gray;
    border-bottom: 3px solid transparent;
    border-radius: 0;
}

.nav-link:hover {
    color: darkgray;
}

.nav-link.active {
    color: #5BF52F;
    border-bottom: 3px solid #5BF52F;
    background-color: transparent;
}

.rounded-circle {
    width: 50px;
    position: fixed;
    bottom: 60px;
    right: 30px;
}

.review {
    border-bottom: 1px #ccc solid;
}

.reviewContainer {
    display: flex;
    align-items: flex-start;
}

.reviewIcon {
    width: 25px;
    margin-right: 10px;
}

.reviewText {
    flex: 1;
    text-align: start;
}
</style>