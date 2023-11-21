<template>
    <div class="topBar row justify-content-between align-items-center p-2">
        <div class="Logo col d-flex justify-content-start ms-1">Beluv MALL</div>
        <div class="col d-flex justify-content-end me-1">
            <img src="../assets/icons/cart.png" alt="" class="iconWidth">
        </div>
    </div>
    <div class="container-fluid content">
        <div class="images row">
            <img src="../assets/photos/main/babyFoot.jpg" alt="" class="img-fluid">
        </div>
        <div class="row border-top">
            <div class="col border-top rounded-top p-4">
                <input type="search" class="form-control rounded" placeholder="어떤 상품이 필요하신가요?">
            </div>
        </div>
        <div class="row mt-3">
            <ul class="list-unstyled d-flex flex-wrap text-center">
                <li v-for="(item, index) in items" :key="index" class="col-4 mb-4" @click="clickCategory(item.text)">
                    <img :src="item.image" class="img-fluid">
                    <p class="mt-2">{{ item.text }}</p>
                </li>
            </ul>
        </div>
    </div>
    <div class="underBar border-top-shadow p-1 pt-2">
        <ul class="list-unstyled d-flex justify-content-around">
            <li v-for="(item, index) in underItems" :key="index" @click="selectItem(index)"
                :class="{ selected: selectedItemIndex === index }">
                <img :src="item.image" class="img-fluid">
                <p class="mt-2">{{ item.text }}</p>
            </li>
        </ul>
    </div>
</template>

<script>

export default {
    data() {
        return {
            selectedItemIndex: 2,
            items: [
                {
                    image: require('../assets/icons/bodyLotion.png'),
                    id: 1,
                    text: '스킨케어'
                },
                {
                    image: require('../assets/icons/snack.png'),
                    id: 2,
                    text: '간식'
                },
                {
                    image: require('../assets/icons/bathTub.png'),
                    id: 3,
                    text: '바스/클렌징'
                },
                {
                    image: require('../assets/icons/detergent.png'),
                    id: 4,
                    text: '세정제'
                },
                {
                    image: require('../assets/icons/babyDiaper.png'),
                    id: 5,
                    text: '기저귀'
                },
                {
                    image: require('../assets/icons/wetWipes.png'),
                    id: 6,
                    text: '물티슈'
                },
            ],
            underItems: [
                {
                    image: require('../assets/icons/home.png'),
                    text: '홈'
                },
                {
                    image: require('../assets/icons/book.png'),
                    text: '가이드'
                },
                {
                    image: require('../assets/icons/store.png'),
                    text: '베럽몰'
                },
                {
                    image: require('../assets/icons/heart1.png'),
                    text: '찜'
                },
                {
                    image: require('../assets/icons/profile.png'),
                    text: '마이베럽'
                },
            ]
        }
    },
    methods: {
        selectItem(index) {
            this.selectedItemIndex = index;
        },
        clickCategory(category) {
            this.$store.dispatch('moveMainCategory', category);
            this.$router.push({
                name: "itemsMenu",
            });
        }
    },
}
</script>

<style>
@font-face {
    font-family: 'Beluv';
    src: url('../assets/fonts/나눔손글씨\ 아인맘\ 손글씨.ttf')
}

.iconWidth {
    width: 25px;
}

.Logo {
    font-family: 'Beluv';
    font-size: 30px;
    font-weight: bold;
    color: #5BF52F;
}

.topBar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background-color: white;
    height: 60px;
}

.content {
    padding: 0;
    margin-top: 60px;
    margin-bottom: 80px;
    overflow-y: scroll;
    height: calc(100vh - 120px);
}

.underBar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: white;
    height: 80px;
    /* 최소 높이 설정 */
}

.underBar li img {
    filter: opacity(0.2) drop-shadow(0 0 0 rgb(221, 221, 221));
}

.underBar li p {
    color: rgb(221, 221, 221);
}

.underBar li.selected img {
    filter: grayscale(100%) brightness(50%);
}

.underBar li.selected p {
    color: black;
}
.border-top-shadow {
    box-shadow: 0px -5px 5px -3px rgba(0, 0, 0, 0.2);
}
</style>