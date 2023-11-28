<template>
    <headMenu :menu="keyWord" />
    <div class="content container-fluid p-3">
        <div class="row">
            <div v-for="item in items" :key="item.id" class="col-6 mb-3">
                <div class="lists text-center" @click="clickItem(item.ProductID)">
                    <img class="img-fluid" :src="require(`@/assets/photos/items/${item.ProductID}.jpg`)">
                    <div class="description">
                        <div class="brand">{{ item.Brand }}</div>
                        <div class="name">{{ item.ProductName }}</div>
                        <div class="info">
                            <span class="discount">{{ item.Discount }}%</span>
                            <span class="discountedPrice">{{ changeNum(item.Price * (1 - 0.01 * item.Discount)) }}원</span>
                            <span class="price">{{ changeNum(item.Price) }}원</span>
                        </div>
                        <div class="freeShipping text-start">
                            <div v-if="item.FreeShipping" class="text-center">무료배송</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script scoped>
import headMenu from './headMenu.vue';
import axios from 'axios';
export default {
    components: {
        headMenu,
    },
    data() {
        return {
            mainCategory: '',
            items: [],
            keyWord: ''
        };
    },
    mounted() {
        const getSameProsProduct = `http://${this.$store.state.port}:3000/api/item/getSameProsProduct`;
        axios.get(getSameProsProduct, {
            params: {
                "itemId": this.$store.state.itemId,
                "keyWord": this.keyWord,
            }
        })
            .then((response) => {
                this.items = response.data;
                console.log(response.data);
            })
            .catch((error) => {
                console.error('API 요청 중 오류 발생:', error);
            });

    },
    created() {
        this.keyWord = this.$route.query.KeyWord;
        console.log(this.keyWord);
    },
    methods: {
        changeNum(value) {
            if (value != null) {
                let valueStr = value.toString();
                valueStr = valueStr.split('.')[0];
                return valueStr.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, "$1,");
            } else {
                return "";
            }
        },
        clickItem(item) {
            this.$store.dispatch('loadItemId', item);
            this.$router.push({
                name: "itemDescription",
            });
        },
    },
}
</script>

<style scoped>
.content {
    width: 100%;
    overflow-x: hidden;
    text-align: start;
    margin-top: 40px;
    height: 100%;
}

.freeShipping {
    background-color: rgb(224, 224, 224);
    width: 60px;
    font-size: 14px;
    border-radius: 20%;
    color: gray;
}

.brand,
.name,
.info {
    text-align: start;
}

.brand {
    color: rgb(150, 150, 150);
}

.discount {
    font-size: 18px;
    color: rgb(125, 157, 214);
    font-weight: bold;
    margin-right: 3px;
}

.discountedPrice {
    font-size: 18px;
    font-weight: bold;
    margin-right: 3px;
}

.price {
    text-decoration: line-through;
    color: rgb(150, 150, 150);
    font-size: 12px;
}
</style>
