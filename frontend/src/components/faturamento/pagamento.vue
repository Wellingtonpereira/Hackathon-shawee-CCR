<template>
    <div class="q-pa-md">
        <div class="flex flex-center name q-pa-md">
            Finalize sua compra
        </div>
        <div class="info q-pb-md">
            Estamos quase lá. Selecione a formade pagamento para finalizar a compra do exame. Confira seus dados.
        </div>

        <q-list>
            <q-item tag="label" v-ripple>
                <q-item-section avatar top>
                    <q-radio v-model="color" val="card" color="black" />
                </q-item-section>
                <q-item-section>
                    <q-item-label>Cartão de Crédito</q-item-label>
                    <q-item-label caption>3x de R$ 54,00 sem juros</q-item-label>
                </q-item-section>
            </q-item>

            <q-item tag="label" v-ripple>
                <q-item-section avatar top>
                    <q-radio v-model="color" val="boleto" color="black" />
                </q-item-section>
                <q-item-section>
                    <q-item-label>Boleto Bancário</q-item-label>
                    <q-item-label caption>
                        R$ 162,00 à vista
                        Confirmação em até 2 dias úteis
                    </q-item-label>
                </q-item-section>
            </q-item>
        </q-list>

        <div class="row">
            <div class="col text-center">
                <q-btn flat color="primary" @click="handlerPagamento('123')">
                    <q-icon name="shopping_cart" class="icon"/>
                    <span class="title">Finalizar Compra</span>
                </q-btn>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Pagamento",
    data(){
        return{
            color: 'card'
        }
    },
    methods:{
        handlerPagamento(id){
            this.$router.push('/exames/cartao/'+id)
        }
    }
}
</script>

<style lang="sass" scoped>
.name
    font-family: Roboto
    font-size: 24px
    font-weight: 500
    font-stretch: normal
    font-style: normal
    line-height: 1.21
    letter-spacing: normal
    text-align: left
    color: #424242

.info
    font-family: Roboto
    font-size: 14px
    font-weight: normal
    font-stretch: normal
    font-style: normal
    line-height: 1.43
    letter-spacing: normal
    text-align: left
    color: rgba(0, 0, 0, 0.87)    
</style>