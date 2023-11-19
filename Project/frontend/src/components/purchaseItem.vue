<template>
    <div class="purchaseItem container-fluid text-center">
        <div class="row justify-content-center">
            <div class="col-auto">
                <button
                    style="background-color: white; outline: none; border: 1px solid gray; border-radius: 10%; padding: 7px; height: 40px; line-height: 1.5; font-size: 16px; margin-right: -10px;"><img
                        src="../assets/icons/heart2.png" alt="" width="22"></button>
            </div>
            <div class="col-auto">
                <button type="button" class="btn"
                    style="width: 320px; height: 40px; line-height: 1.5; font-size: 16px;">구매하기</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container-fluid {
    padding: 0px;
}

/* purchase_item.vue의 스타일 */
.purchaseItem {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    padding: 10px;
    background-color: white;
}

.btn {
    background-color: rgb(39, 202, 151);
    color: white;
}
</style>
