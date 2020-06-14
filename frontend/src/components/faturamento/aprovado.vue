<template>
    <div class="q-pa-md">
        <div class="flex flex-center name q-pa-md">
            Compra confirmada
        </div>

        <div class="info flex flex-center q-pa-md">
            <q-icon name="credit_card" class="icon"/>
        </div>

        <div class="info flex flex-center q-pa-md">
            <b>Pronto!</b>
        </div>

        <div class="info q-pb-md">
            Compra realizada com sucesso. Seu vale-exame estará disponível em Exames em instantes, você poderá alterar data ou local do exame até 4 vezes.
        </div>

        <div class="row q-pt-md">
            <div class="col text-center">
                <q-btn color="primary" @click="handlerPagamento('/exames')">
                    <q-icon name="library_books" class="icon"/>
                    <span class="title">Voltar para Exames</span>
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
        handlerPagamento(rota){
            this.$router.push(rota)
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

    .material-icons
        font-size: 60px
        color: #ffcc00 !important

.q-btn
    width: 315px
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