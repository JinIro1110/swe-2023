import { createStore } from 'vuex';
const store = new createStore({
    state() {
        return {
            menu: null,
            mainCategory: null,
            subCategory: null,
            itemId: null
        };
    },
    mutations: {
        setMenu(state, menu) {
            state.menu = menu;
        },
        setMainCategory(state, mainCategory) {
            state.mainCategory = mainCategory;
        },
        setSubCategory(state, subCategory) {
            state.subCategory = subCategory;
        },
        setItemId(state, itemId) {
            state.itemId = itemId;
        }
    },
    actions: {
        updateMenu({ commit }, menu) {
            commit('setMenu', menu);
        },
        moveMainCategory({ commit }, mainCategory) {
            commit('setMainCategory', mainCategory);
        },
        moveSubCategory({ commit }, subCategory) {
            commit('setSubCategory', subCategory);
        },
        loadItemId({ commit }, itemId) {
            commit('setItemId', itemId);
        }
    }
});

export default store;
