import { createStore } from 'vuex';
const store = new createStore({
    state() {
        return {
            menu: null,
            mainCategory: null,
            subCategory: null,
            itemId: null,
            prosKeyword: null,
            consKeyword: null,
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
        },
        setProsKeyword(state, prosKeyword) {
            state.prosKeyword = prosKeyword;
        },
        setConsKeyword(state, consKeyword) {
            state.consKeyword = consKeyword;
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
        },
        loadProsKeyword({ commit }, prosKeyword) {
            commit('setProsKeyword', prosKeyword);
        },
        loadConsKeyword({ commit }, consKeyword) {
            commit('setConsKeyword', consKeyword);
        }
    }
});

export default store;
