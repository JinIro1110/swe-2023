import { createRouter, createWebHistory } from 'vue-router'
import BeluvMall from '../components/BeluvMall'
import itemsMenu from '../components/itemsMenu'
import itemDescription from '../components/itemDescription'
import review from '../components/review'
import wordCloud from '../components/WordCloud'


const routes = [
    {
        path: '/',
        name: 'BeluvMall',
        component: BeluvMall
    },
    {
        path: '/itemsMenu',
        name: 'itemsMenu',
        component: itemsMenu,
    },
    {
        path: '/item',
        name: 'itemDescription',
        component: itemDescription
    },
    {
        path: '/reviews',
        name: 'reviews',
        component: review
    },
    {
        path: '/wordcloud',
        name: 'wordcloud',
        component: wordCloud
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;