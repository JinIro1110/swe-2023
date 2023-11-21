<template>
    <headMenu :menu="mainCategory" />
    <div class="subCategoryTab container-fluid align-items-center">
        <div class="row">
            <div class="col">
                <div class="bar">
                    <ul class="nav nav-pills nav-fill">
                        <li class="nav-item">
                            <div class="nav-link" :class="{ active: activeTab === 0 }"
                                @click="activeTab = 0">전체</div>
                        </li>
                        <li v-for="(subCategory, index) in subCategories" :key="index" class="nav-item">
                            <div class="nav-link" :class="{ active: activeTab === index + 1 }"
                                @click="activeTab = index + 1">{{
                                    subCategory.SubCategoryName }}</div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

    </div>
    <div class="content container-fluid p-3">
        <div class="row">
            <div v-for="item in items" :key="item.id" class="col-6 mb-3">
                <div class="lists text-center" @click="clickItem(item.ProductID)">
                    <img :src="require(`@/assets/photos/skincare/skincare1.png`)">
                    <div class="description">
                        <div class="brand">브랜드</div>
                        <div class="name">{{ item.ProductName }}</div>
                        <div class="info">
                            <span class="discount">{{ item.Discount }}%</span>
                            <span class="discountedPrice">{{ changeNum(item.Price * (1 - 0.01 * item.Discount)) }}원</span>
                            <span class="price">{{ changeNum(item.Price) }}원</span>
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
import headMenu from './headMenu.vue';
import axios from 'axios';
export default {
    components: {
        headMenu,
    },
    data() {
        return {
            mainCategory: '',
            subCategories: [],
            items: [],
            activeTab: 0,
        };
    },
    mounted() {
        const encodedMainCategory = encodeURIComponent(this.mainCategory);
        const getSubCategoryTab = `http://localhost:3000/api/category/subCategoryNavBar/${encodedMainCategory}`;
        axios.get(getSubCategoryTab)
            .then((response) => {
                this.subCategories = response.data.subcategories;
            })
            .catch((error) => {
                console.error('API 요청 중 오류 발생:', error);
            });
        
        const getMainCategoryItems = `http://localhost:3000/api/category/showEntireItem/${encodedMainCategory}`;
        axios.get(getMainCategoryItems)
            .then((response) => {
                this.items = response.data.mainCategoryItems;
            })
            .catch((error) => {
                console.error('API 요청 중 오류 발생:', error);
            });
    },
    created() {
        this.mainCategory = this.$store.state.mainCategory;
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
        }
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

.subCategoryTab {
    margin-top: 60px;
}
</style>
