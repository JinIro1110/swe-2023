<template>
    <div class="photo d-flex align-items-center">
        <span style="font-size:25px; font-weight: bold; margin-right:5px;">{{ selectedRating }}</span>
        <svg v-for="i in 5" :key="i" @click="setRating(i)" width="24" height="24" viewBox="0 0 24 24">
            <path
                d="M23.836,8.794a3.179,3.179,0,0,0-3.067-2.226H16.4L15.073,2.432a3.227,3.227,0,0,0-6.146,0L7.6,6.568H3.231a3.227,3.227,0,0,0-1.9,5.832L4.887,15,3.535,19.187A3.178,3.178,0,0,0,4.719,22.8a3.177,3.177,0,0,0,3.8-.019L12,20.219l3.482,2.559a3.227,3.227,0,0,0,4.983-3.591L19.113,15l3.56-2.6A3.177,3.177,0,0,0,23.836,8.794Z"
                :fill="i <= selectedRating ? 'gold' : '#ccc'" />
        </svg>
    </div>
</template>

<script>
export default {
    name: 'writeReview',
    data() {
        return {
            selectedRating: 0,
            item: {
                id: 1,
                image: 'skincare/skincare1.png',
                price: 50000,
                discount: 20,
                brand: '브랜드1',
                name: '브랜드1의 제품1',
                freeDelivery: true,
            },
        };
    },
    methods: {
        setRating(rating) {
            this.selectedRating = rating;
            // 여기에 Axios를 사용하여 서버에 데이터를 전송하는 로직을 추가할 수 있습니다.
        },
    },
};
</script>
