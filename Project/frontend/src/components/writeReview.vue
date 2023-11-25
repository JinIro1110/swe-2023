<!-- 리뷰 등록 시 데이터베이스에 저장, 삭제 시 제거 -> 각각 fastapi(?) or aws 요청 -> 새로운 키워드 추출(저장)-->

<template>
    <div class="headMenu container-fluid text-center p-3">
        <div class="row justify-content-evenly">
            <div class="col d-flex justify-content-start" @click="goBack">
                <img :src="require(`@/assets/icons/backward.png`)" class="iconWidth">
            </div>
            <div class="col d-flex justify-content-center" style="font-size: 18px; font-weight: bold;">
                리뷰쓰기
            </div>
            <div class="col d-flex justify-content-end me-3" style="color: gray;" @click="writeReview">
                등록
            </div>
        </div>
    </div>
    <div class="box row d-flex align-items-center p-2 text-start">
        <div class="productImg img-fluid col-2 ms-2 ">
            <img :src="require(`@/assets/photos/skincare/skincare1.png`)">
        </div>
        <div class="itemText col-auto">
            <div class="itemBrand fw-bold">{{ brand }}</div>
            <div class="itemName fw-bold">{{ productName }}</div>
        </div>
    </div>

    <div class="photo container-fluid d-inline-block align-items-center">
        <div class="row">
            <div class="col fw-bold p-2 mb-2 mt-2">
                얼마나 만족하셨나요?
            </div>
        </div>
        <div class="row">
            <div class="col mb-2">
                <svg v-for="i in 5" :key="i" @click="setRating(i)" width="40" height="40" viewBox="0 0 30 30">
                    <path
                        d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z"
                        :fill="i <= selectedRating ? 'gold' : '#e9ebf0'" />
                </svg>
            </div>
        </div>
        <div class="row">
            <div class="col message fw-bold mb-2">
                {{ selectedMessage }}
            </div>
        </div>
    </div>
    <div class="reviewInput container-fluid">
        <div class="row d-flex jusfify-content-between p-3">
            <div class="col fw-bold">
                제품에 대해 알려주세요
            </div>
            <div class="strLen col text-end">
                <span v-if="stringLength > 30" style="color: #5BF52F;">{{ stringLength }}</span>
                <span v-else>{{ stringLength }}</span>
                <span> / 30자 이상</span>
            </div>
        </div>
        <div class="row text-start p-4">
            <div class="inputLabel d-flex align-items-center mb-1">
                <img class="thumb me-1 mb-2" :src="require(`@/assets/icons/good.png`)"><span class="fw-bold">칭찬할 점</span>
            </div>
            <div class="inputBox">  
                <textarea v-model="pros" class="inputText" :placeholder="prosPlaceHolder"/>
            </div>
            <div class="inputLabel d-flex align-items-center mb-1 mt-4">
                <img class="thumb me-1 mb-1" :src="require(`@/assets/icons/bad.png`)"><span class="fw-bold">아쉬운 점</span>
            </div>
            <div class="inputBox">  
                <textarea v-model="cons" class="inputText" :placeholder="consPlaceHolder"/>
            </div>
        </div>
    </div>
    <button
    :class="stringLength >= 30 && selectedRating !== 0 ? 'submitButton' : 'justsubmitButton'"
    @click="writeReview">
    {{ stringLength > 30 && selectedRating !== 0 ? stringLength : '등록하기' }}
</button>
</template>

<script>
import axios from 'axios';

export default {
    name: 'writeReview',
    data() {
        return {
            selectedRating: 0,
            userId: 1000,
            productId: 0,
            productName: 'dd',
            brand: 'dd',
            selectedMessage: '-',
            stringLen: 0,
            pros: '',
            itemId: this.$store.state.itemId,
            cons: '',
            prosPlaceHolder: `제형 / 사용감 / 트러블 유무 / 향 / 가성비 등\n칭찬할 점에 대해 자유롭게 작성해주세요 :)`,
            consPlaceHolder: `제형 / 사용감 / 트러블 유무 / 향 / 가성비 등\n아쉬운 점에 대해 자유롭게 작성해주세요 :)`
        };
    },
    created() {
        this.productName = this.$route.query.ProductName;
        this.brand = this.$route.query.Brand;
    },
    methods: {
        setRating(rating) {
            this.selectedRating = rating;
            if (this.selectedRating == 1) { this.selectedMessage = '별로에요' }
            else if (this.selectedRating == 2) { this.selectedMessage = '아쉬워요' }
            else if (this.selectedRating == 3) { this.selectedMessage = '보통이에요' }
            else if (this.selectedRating == 4) { this.selectedMessage = '맘에 들어요' }
            else { this.selectedMessage = '최고에요' }
        },
        goBack() {
            this.$router.go(-1);
        },
        writeReview() {
            if(this.stringLength >= 30 && this.selectedRating !== 0) {
                const getReviews = `http://192.168.0.213:3000/api/review/writeReview/${this.itemId}`;
                axios.post(getReviews, {
                    "userId": this.userId,
                    "prosReview": this.pros,
                    "consReview": this.cons,
                    "rating": this.selectedRating,
                }, {"Content-Type": 'application/json'})
                    .then((response) => {
                        alert(response.data.message);
                        this.$router.push("/item");
                    })
                    .catch((error) => {
                        console.error('API 요청 중 오류 발생:', error.response);
                    });
            }
        },
    },
    computed: {
        stringLength() {
            return this.pros.length + this.cons.length;
        }
    }
};
</script>

<style scoped>
.headMenu {
    border-bottom: 1px solid #ccc;
}

.productImg img {
    width: 60px;
}

.box {
    border-bottom: 10px #edebeb solid;
}

.photo {
    border-bottom: 10px #edebeb solid;
}

.itemBrand {
    color: #5BF52F;
}

.reviewInput {
    padding: 0;
}

.strLen {
    font-size: 14px;
    color: gray;
}

.inputLabel {
    display: f
}
.thumb {
    width: 25px;
}

.inputText {
    width: 100%;
    height: 160px;
    border-radius: 10px;
    border: 1px #ccc solid;
    padding: 10px;
}

.justsubmitButton {
    width: 100%;
    color: white;
    background-color: #ccc;
    border: 0;
    height: 40px;
}

.submitButton {
    width: 100%;
    color: white;
    background-color: #5BF52F;
    border: 0;
    height: 40px;
}

.submitButton:active {
    background-color: green;
}
</style>
