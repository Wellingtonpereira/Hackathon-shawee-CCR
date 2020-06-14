<template>
    <div class="q-pa-md">
        <div class="flex flex-center name q-pa-md">
            Confirme seus dados
        </div>
        <div class="info q-pb-md">
            Digite os números e o nome que aparece em seu cartão de crédito corretamente e depois clique no botão "Finalizar Compra".
        </div>

        <div class="q-gutter-md q-pb-lg">
            <q-input v-model="num_card" label="Número do cartão de crédito" />


            <q-input v-model="nome" label="Nome impresso no cartão" />

            <div class="row justify-between">
                <div class="col-5">
                    <q-input v-model="vencimento" mask="##/##" label="Vencimento" />
                </div>
                <div class="col-5">
                    <q-input v-model="cs" label="Cód. de segurança" type="password" />
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col text-center">
                <q-btn color="primary" @click="handlerPagamento('123')">
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
            color: 'card',
            num_card: null,
            nome: null,
            vencimento: null,
            cs: null
        }
    },
    methods:{
        handlerPagamento(id){
            this.$router.push('/cartao/aprovado')
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

.q-btn
    width: 215px
    height: 48px
    border-radius: 4px
    box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16)
    background-color: #ffcc00
    span
        color: #424242

    .material-icons
        color: #424242 !important
        padding-right: 15px
</style>