<template>
    <div class="word-cloud-container">
        <div id="word-cloud-1">
            <div class="fs-1 fw-bold">장점</div>
        </div>
        <div id="word-cloud-2">
            <div class="fs-1 fw-bold">단점</div>
        </div>
    </div>
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
            this.createWordCloud('#word-cloud-1', this.items.map(item => ({ text: item.PositiveKeyword, size: item.PositiveRating })));
            this.createWordCloud('#word-cloud-2', this.items.map(item => ({ text: item.NegativeKeyword, size: item.NegativeRating })));
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
