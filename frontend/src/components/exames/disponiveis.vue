<template>
    <div class="exames">
        <span class="disponiveis">Exames disponíveis</span>
        <p class="info">
            Mostramos todos os exames disponíveis para você e com os melhores preços
        </p>
        <grade />
    </div>
</template>

<script>
import Grade from 'components/exames/grade'

export default {
    name: "agendados",
    components:{
        Grade
    },
    data(){
        return {
            qtd_exames: 3
        }
    }
}
</script>
<style lang="sass" scoped>
    .exames
        padding: 30px 20px 20px 20px 

        .info
            padding-top: 10px
            font-family: Roboto
            font-size: 14px
            font-weight: normal
            font-stretch: normal
            font-style: normal
            line-height: 1.43
            letter-spacing: normal
            text-align: left
            color: #424242

        .disponiveis
            font-family: Roboto
            font-size: 16px
            font-weight: 500
            font-stretch: normal
            font-style: normal
            line-height: 1.25
            letter-spacing: normal
            text-align: left
            color: rgba(0, 0, 0, 0.87)
</style>