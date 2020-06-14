
<template>
    <div class="detalhes">
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
                    <b>Resultado disponível</b>
                </p>
            </div>
        </div>

        <div class="row">
            <div class="col text-center">
                <q-btn flat>
                    <q-icon name="img:/statics/icons/resultados.svg" />
                    <span class="title">Verificar laudo</span>
                </q-btn>
                <q-btn flat>
                    <q-icon name="img:/statics/icons/resultados.svg" />
                    <span class="title">Relatório Médico</span>
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
        padding: 20px 20px 20px 20px 
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

        .q-btn
            margin-bottom: 20px
            width: 327px
            height: 48px
            border-radius: 4px
            box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16)
            background-color: #424242
            span
                color: #fff

        .title
            padding-left: 20px
        
</style>