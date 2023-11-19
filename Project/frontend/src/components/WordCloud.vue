<template>
    <div class="word-cloud-container">
        <div id="word-cloud-1"></div>
        <div id="word-cloud-2"></div>
    </div>
</template>

<script>
import * as d3 from 'd3';
import cloud from 'd3-cloud';

export default {
    name: 'WordCloud',
    mounted() {
        this.createWordCloud('#word-cloud-1', [
            { text: 'Hello', size: 20 },
            { text: 'Vue', size: 20 },
            { text: 'Hello', size: 20 },
            { text: 'Vue', size: 20 },
            { text: 'Hello', size: 20 },
            { text: 'Vue', size: 20 },
            { text: 'Hello', size: 40 },
            { text: 'Vue', size: 50 },
        ]);
        this.createWordCloud('#word-cloud-2', [
            { text: 'World', size: 30 },
            { text: 'JavaScript', size: 60 },
            // 추가 단어들...
        ]);
    },
    methods: {
        createWordCloud(containerId, words) {
            const layout = cloud()
                .size([200, 200]) // 클라우드 크기를 줄임
                .words(words)
                .padding(10) // 겹침 방지를 위해 패딩 증가
                .rotate(() => 0) // 모든 단어를 가로 방향으로
                .font("Impact")
                .fontSize(d => d.size)
                .on("end", words => this.draw(containerId, words));

            layout.start();
        },
        draw(containerId, words) {
            const svg = d3.select(containerId).append("svg")
                .attr("width", 200)
                .attr("height", 200)
                .append("g")
                .attr("transform", "translate(100,100)");

            svg.selectAll("text")
                .data(words)
                .enter().append("text")
                .style("font-size", d => d.size + "px")
                .style("font-family", "Impact")
                .attr("text-anchor", "middle")
                .attr("transform", d => `translate(${[d.x, d.y]})`)
                .text(d => d.text);
        }
    }
};
</script>

<style scoped>
.word-cloud-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

#word-cloud-1 svg, #word-cloud-2 svg {
    border: 1px solid black; /* 테두리 설정 */
}
</style>
