<template>
    <headMenu :menu="bigCategory" />
    <div class="content container-fluid p-3">
        <div class="row">
            <div v-for="item in items" :key="item.id" class="col-6 mb-5">
                <div class="lists text-center" @click="clickItem(item.id)">
                    <img :src="require(`@/assets/photos/${item.image}`)">
                    <div class="description">
                        <div class="brand">{{ item.brand }}</div>
                        <div class="name">{{ item.name }}</div>
                        <div class="info">
                            <span class="discount">{{ item.discount }}%</span>
                            <span class="discountedPrice">{{ changeNum(item.price * (1 - 0.01 * item.discount)) }}원</span>
                            <span class="price">{{ changeNum(item.price) }}원</span>
                        </div>
                        <div class="freeShipping text-start">
                            <div v-if="item.freeDelivery" class="text-center">무료배송</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script scoped>
import headMenu from './headMenu.vue'
import { skincares } from '@/assets/items/skincare'
export default {
    components: {
        headMenu,
    },
    data() {
        return {
            bigCategory: '',
            items: [],
        };
    },
    created() {
        this.items = skincares;
        this.bigCategory = this.$store.state.bigCategory;
    },
    methods : {
        changeNum: function(value) {
            if (typeof value !== 'string') {
                value = value.toString();
            }
            return value.replace(/(\d)(?=(?:\d{3})+(?!\d))/g, '$1,');
        },
        clickItem(item) {
            this.$store.dispatch('updateItem', item);
            this.$router.push({
                name: "itemDescription",
            });
        }
    },
}
</script>

<style scoped>
.content {
    width: 100%;
    overflow-x: hidden;
    text-align: start;
}

.freeShipping {
    background-color: rgb(224, 224, 224);
    width: 60px;
    font-size: 14px;
    border-radius: 20%;
    color: gray;
}
.brand, .name, .info {
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
