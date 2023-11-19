import { createStore } from 'vuex';
const store = new createStore({
    state() {
        return {
            menu: null,
            bigCategory: null,
            smallCategory: null,
            item: null
        };
    },
    mutations: {
        setMenu(state, menu) {
            state.menu = menu;
        },
        setBigCategory(state, bigCategory) {
            state.bigCategory = bigCategory;
        },
        setSmallCategory(state, smallCategory) {
            state.smallCategory = smallCategory;
        },
        setItem(state, item) {
            state.item = item;
        }
    },
    actions: {
        updateMenu({ commit }, menu) {
            commit('setMenu', menu);
        },
        moveBigCategory({ commit }, bigCategory) {
            commit('setBigCategory', bigCategory);
        },
        moveSmallCategory({ commit }, smallCategory) {
            commit('setSmallCategory', smallCategory);
        },
        loadItem({ commit }, item) {
            commit('setItem', item);
        }
    }
});

export default store;
