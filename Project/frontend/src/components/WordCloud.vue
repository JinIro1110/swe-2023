<template>
    <div class="word-cloud-container">
        <div id="word-cloud-1">
            <div class="fs-1 fw-bold">장점</div>
        </div>
        <div id="word-cloud-2">
            <div class="fs-1 fw-bold">단점</div>
        </div>
    </div>
    <!-- <div class="modal-container" v-show="isModal" @click.self="close">
        <div class="headMenu container-fluid text-center p-3">
            <div class="row justify-content-evenly">
                <div class="col d-flex justify-content-start" @click="closeModal" @click.stop="">
                    <img src="../assets/icons/backward.png" class="iconWidth">
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
                <div class="reviewText">{{ consReview.NegativeReviewText }}</div>
            </div>
        </div>
    </div> -->

</template>

<script>

import * as d3 from 'd3';
import cloud from 'd3-cloud';

export default {
    props: {
        items: {
            type: Object,
            require: true,
        }
    },
    watch: {
        items: {
            handler() {
                this.createWordClouds();
            },
            deep: true
        }
    },
    methods: {
        createWordClouds() {
            this.createWordCloud('#word-cloud-1', this.items.map(item => ({ text: item.PositiveKeyword, size: item.PositiveRating * 2 })));
            this.createWordCloud('#word-cloud-2', this.items.map(item => ({ text: item.NegativeKeyword, size: item.NegativeRating * 2 })));
        },
        createWordCloud(containerId, words) {
            const width = window.innerWidth;
            const height = 400;
            const layout = cloud()
                .size([width, height])
                .words(words)
                .padding(10)
                .rotate(() => 0)
                .font("Impact")
                .fontSize(d => d.size * 10)
                .on("end", words => this.draw(containerId, words));
            layout.start();
        },
        draw(containerId, words) {
            d3.select(containerId).select("svg").remove();
            const width = window.innerWidth;
            const height = 400;
            const svg = d3.select(containerId).append("svg")
                .attr("width", width)
                .attr("height", height)
                .append("g")
                .attr("transform", `translate(${width / 2}, ${height / 2})`);
            svg.selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", d => d.size + "px")
                .style("font-family", "Impact")
                .style("fill", containerId === '#word-cloud-1' ? 'DodgerBlue' : 'Red')
                .attr("text-anchor", "middle")
                .attr("transform", d => `translate(${[d.x, d.y]})`)
                .text(function (d) { return d.text; })
                .style("border", "1px solid black")
                .on("click", (event, d) => {
                    if (containerId === '#word-cloud-1') {
                        this.$router.push({
                            name: 'similarItems',
                            query: { KeyWord: d.text }
                        });
                    } else {
                        this.$router.push({
                            name: 'negativeReviews',
                            query: { KeyWord: d.text, itemId: this.$store.state.itemId }
                        });
                    }
                })
        },
    }
};
</script>

<style scoped>
.word-cloud-1,
.word-cloud-2 {
    width: 100%;
}
</style>
