<template>
    <div class="row">
        <div class="col-6 " v-for="item in items" :key="item.exame_labortorio">
            <q-card class="grade" flat bordered @click="pushRouter('/exames/comprar/' + item.id)">

                <q-card-section class="flex flex-center">
                    <q-img class="rounded-borders" :src="item.laboratorio.imagem"  />
                </q-card-section>

                <q-card-section>
                    <div class="nome">Exame Toxicológico</div>
                </q-card-section>

                <q-card-actions align="around">
                    <q-btn flat color="dark" class="money" label="R$ 150,00" />
                    <q-btn rounded color="primary" icon="shopping_cart" class="img"/>  
                </q-card-actions>
            </q-card>
        </div>
    </div>
</template>

<script>
export default {
    name: "grade_exames",
    data() {
        return {
            items: [
                {
                    id: 123,
                    exame_labortorio: 1,
                    laboratorio: {
                        nome: "Labet",
                        imagem: "/statics/icons/labet.jpg",
                        id: ""
                    },
                    exame: {
                        preco: "125,30",
                        tempo_exame: "2 dias",
                        id: 123
                    }
                },
                {
                    id: 1234,
                    exame_labortorio: 3,
                    laboratorio: {
                        nome: "Labet",
                        imagem: "/statics/icons/labet.jpg",
                        id: ""
                    },
                    exame: {
                        preco: "125,30",
                        tempo_exame: "2 dias",
                        id: 123
                    }
                },
                {
                    id: 12345,
                    exame_labortorio: 4,
                    laboratorio: {
                        nome: "Labet",
                        imagem: "/statics/icons/labet.jpg",
                        id: ""
                    },
                    exame: {
                        preco: "125,30",
                        tempo_exame: "2 dias",
                        id: 123
                    }
                },
                {
                    id: 123456,
                    exame_labortorio: 7,
                    laboratorio: {
                        nome: "Labet",
                        imagem: "/statics/icons/labet.jpg",
                        id: ""
                    },
                    exame: {
                        preco: "125,30",
                        tempo_exame: "2 dias",
                        id: 123
                    }
                },
                {
                    id: 1234567,
                    exame_labortorio: 2,
                    laboratorio: {
                        nome: "Sodré",
                        imagem: "/statics/icons/sodre.jpg",
                        id: ""
                    },
                    exame: {
                        preco: "125,30",
                        tempo_exame: "2 dias",
                        id: 123
                    }
                },
                {
                    id: 1234568,
                    exame_labortorio: 5,
                    laboratorio: {
                        nome: "Sodré",
                        imagem: "/statics/icons/sodre.jpg",
                        id: ""
                    },
                    exame: {
                        preco: "125,30",
                        tempo_exame: "2 dias",
                        id: 123
                    }
                }
            ]
        }
    },
    methods:{
        pushRouter(router){
            this.$router.push(router)
        }
    }
}
</script>

<style lang="sass" scoped>

    .q-card
        border-radius: 5px !important
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25) !important
        background-color: #ffffff !important

    .grade
        margin: 9px !important
        .nome
            font-family: Roboto
            font-size: 12px
            font-weight: normal
            font-stretch: normal
            font-style: normal
            line-height: 1.67
            letter-spacing: normal
            text-align: left
            color: #191919
        
        .money
            font-family: Roboto
            font-size: 13px
            font-weight: bold
            font-stretch: normal
            font-style: normal
            line-height: 1.67
            letter-spacing: normal
            text-align: left
            color: #424242

        .img
            width: 32px
            height: 32px
            object-fit: contain
            color: #7d7d7d !important
</style>