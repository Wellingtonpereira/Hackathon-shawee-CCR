
<template>
    <div class="detalhes">
        <div class="flex flex-center">
            <q-img class="rounded-borders" src="/statics/icons/sodre-full.png"  />
        </div>

        <div class="row ">
            <div class="col">
                <div class="laboratorio">
                    Exame Toxicológico
                    <br>
                    <span>Realizado por: <b>Sodré Laboratório</b></span> 

                    <br>

                    <div class="row info">
                        <div class="col-6">13/06/20 - 18:30</div>
                        <div class="col-6">
                            <q-icon name="local_offer" />
                                ID A002219101
                        </div>
                    </div>
                    
                </div>

                <p class="info">
                    Dirija-se ao posto de coleta selecionado. 
                    Durante o exame, através de cabelos ou pelos do corpo, é 
                    feita uma análise capaz de detectar o uso em uma janela 
                    retroativa mínima de 90 dias. A coleta de material não é 
                    invasiva, contagiosa ou indolor.
                </p>

                <p class="info">
                    <b>Resultado em até 14 dias</b>
                </p>

                <p class="info_exames">
                    O resultado do exame estará disponível na seção "Exames" ou no seu histórico em "Perfil".
                </p>

            </div>
        </div>

        <div class="row">
            <div class="col text-center">
                <q-btn flat color="primary">
                    <q-icon name="library_books" class="icon"/>
                    <span class="title">Alterar agendamento</span>
                </q-btn>
                <q-btn flat color="primary">
                    <q-icon name="library_books" class="icon"/>
                    <span class="title">Alterar lugar do exame</span>
                </q-btn>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "detalhes_exame",
    data() {
        return {
        }
    }
}
</script>

<style lang="sass" scoped>

    .material-icons
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

            .material-icons
                color: #ffcc00 !important
                padding-right: 2px

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
            padding-bottom: 30px
        
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
            height: 48px
            border-radius: 4px
            box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16)
            background-color: #ffcc00
            margin-bottom: 20px
            span
                color: #000

        .info_exames
            font-family: Roboto
            font-size: 14px
            font-weight: normal
            font-stretch: normal
            font-style: italic
            line-height: 1.67
            letter-spacing: normal
            text-align: left
            color: #191919
        
</style>