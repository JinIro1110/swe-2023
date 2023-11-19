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
        <div class="aboutPrice row text-start p-2">
            <div class="brandInfo d-flex justify-content-between">
                <div class="" style="font-size: 16px; color: rgb(150, 150, 150)">브랜드 ></div>
                <div class=""><img src="../assets/icons/share.png" width="20px"></div>
            </div>
            <div class="nameInfo">
                <div style="font-weight: bold; font-size: 20px;">드시모네 베이비 스텝 1 1+1</div>
            </div>
            <div class="reviewInfo mb-3 d-flex align-items-center">
                <span class="photo d-flex align-items-center">
                    <svg v-for="i in 5" :key="i" width="15" height="15" viewBox="0 0 24 24">
                        <defs>
                            <clipPath :id="'clip-star-' + i">
                                <rect :width="getStarWidth(i)" height="24" />
                            </clipPath>
                        </defs>
                        <path
                            d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z"
                            fill="#ccc" />
                        <path
                            d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z"
                            fill="gold" :clip-path="'url(#' + 'clip-star-' + i + ')'" />
                    </svg>
                    <span style="font-size:20px; font-weight: bold; margin-left:10px;">{{ rating }}</span>
                </span>
                <span style="font-size: 14px; color: rgb(150, 150, 150); text-decoration: underline; margin-left: 10px;"
                    @click="goReview">count개 리뷰보기</span>
            </div>
            <div class="priceInfo">
                <span class="discount">30%</span>
                <span class="discountedPrice fw-bold">{{ changeNum(discountedPrice) }}<span
                        style="font-size:18px; margin-right:5px; margin-left:5px;">원</span></span>
                <span class="price">{{ changeNum(item.price) }}원</span>
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
                    <span v-if=item.freeDelivery class="delivery ms-4">무료배송</span>
                    <span v-else class="delivery ms-4">3000원</span>
                </div>
                <div class="mileage">
                    <span class="contLabel">적립</span>
                    <span class="ms-4">최대+{{ changeNum(item.price * 0.05) }}P적립</span>
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
                    <a class="nav-link" :class="{ active: activeTab === 3 }" @click="activeTab = 3">리뷰({{ item.reviewCount
                    }})</a>
                </li>
            </ul>
        </div>
        <div v-if="activeTab === 1">
            
        </div>
        <div v-if="activeTab === 2">
            
        </div>
        <div v-if="activeTab === 3">
            <ReviewTemplate />
        </div>
    </div>
</template>

<script>
import ReviewTemplate from './reviewTemplate.vue';

export default {
    name: "itemMain",
    props: {},
    data() {
        return {
            bigCategory: "",
            smallCategory: "",
            brand: "",
            rating: 4.2,
            item: {
                price: 10000,
                discount: 10,
                freeDelivery: true,
                reviewCount: 15,
            },
            activeTab: 1,
        };
    },
    methods: {
        goReview() {
            this.$router.push({
                name: "reviews",
            });
        },
        getStarWidth(starIndex) {
            const fullStars = Math.floor(this.rating);
            const hasHalfStar = (this.rating % 1 >= 0.5);
            const partialStarIndex = fullStars + (hasHalfStar ? 1 : 0);
            if (starIndex <= fullStars) {
                return 24; // 전체 별
            }
            else if (starIndex === partialStarIndex) {
                return 12; // 반 별 (별의 절반 크기)
            }
            return 0; // 빈 별
        },
        changeNum: function (value) {
            if (typeof value !== "string") {
                value = value.toString();
            }
            return value.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,");
        },
    },
    created() {
        this.bigCategory = this.$store.state.bigCategory;
        this.smallCategory = this.$store.state.smallCategory;
    },
    computed: {
        discountedPrice() {
            return this.item.price * (1 - this.item.discount / 100);
        },
    },
    components: { ReviewTemplate }
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

</style>