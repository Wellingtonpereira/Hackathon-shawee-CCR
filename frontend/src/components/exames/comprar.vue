<template>
    <div class="detalhes">
        <div class="flex flex-center">
            <q-img class="rounded-borders" src="/statics/icons/sodre-full.png"  />
        </div>

        <div class="row ">
            <div class="col">
                <p class="laboratorio">
                    Exame Toxicológico
                    <br>
                    <span>Realizado por: <b>Sodré Laboratório</b></span> 
                </p>
                <p class="info">
                    Faça o exame toxicológico em qualquer posto de coleta CCR ou onde estiver.
                </p>
                <p class="info">
                    <ul>
                        <li>Parcelamento em 3x sem juros</li>
                        <li>Laudo com autenticação digital</li>
                    </ul>
                </p>
                <p class="preco">
                    R$ 162,20
                </p>
                <p class="info">
                    à vista no boleto<br>
                    no cartão de crédito 3x de R$54,00
                </p>
            </div>
        </div>

        <div class="row">
            <div class="col text-center">
                <q-btn flat color="primary" @click="handlerPagamento('123')">
                    <q-icon name="shopping_cart" class="icon"/>
                    <span class="title">Comprar</span>
                </q-btn>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "comprar_exame",
    data() {
        return {
        }
    },
    methods:{
        handlerPagamento(id){
            this.$router.push('/pagamento/123')
        }
    }
}
</script>

<style lang="sass" scoped>
    .icon
        padding-right: 15px

    .detalhes
        padding: 0px 20px 20px 20px 
        .laboratorio
            font-family: Roboto
            font-size: 24px
            font-weight: 500
            font-stretch: normal
            font-style: normal
            line-height: 1.21
            letter-spacing: normal
            text-align: left
            color: #424242

            span
                font-weight: 300
                font-size: 14px

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
            padding-bottom: 10px
        
        .preco
            font-family: Roboto
            font-size: 24px
            font-weight: bold
            font-stretch: normal
            font-style: normal
            line-height: 1.2
            letter-spacing: normal
            text-align: left
            color: rgba(0, 0, 0, 0.87)

        .q-btn
            width: 175px
            height: 48px
            border-radius: 4px
            box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16)
            background-color: #ffcc00
            span
                color: #000
        
</style>