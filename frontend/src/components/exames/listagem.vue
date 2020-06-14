<template>
    <div>
        <q-list v-for="item in items" :key="item.voucher">
            <q-item clickable v-ripple @click="pushRouter('/exames/detalhes/' + item.id)">
                <q-item-section avatar class="avatar">
                    <q-icon :name="item.laboratorio.imagem" />
                </q-item-section>
                <q-item-section>
                    <span class="nome">
                        {{item.exame.nome}}<br>
                    </span>
                    <span class="info">
                        {{item.exame.base_coletada}}<br>
                        {{item.exame.data_agendada}}
                    </span>

                </q-item-section>
                <q-item-section side>
                    <q-icon name="img:/statics/icons/more.svg" />
                </q-item-section>
            </q-item>
             <q-separator spaced inset />
        </q-list>
    </div>
</template>

<script>
export default {
    name:"Listagem_Meus_Exames",
    data(){
        return {
            items: [
                {
                    id: 123,
                    voucher: "123",
                    laboratorio: {
                        imagem: "img:/statics/icons/labet.jpg",
                        id: "",
                        nome: ""
                    },
                    exame: {
                        id: "",
                        nome:"Exame 1",
                        base_coletada: "BSO km20 SP-280 (Limeira)",
                        data_agendada: "13/07/20 18:30"
                    }
                },
                {
                    id: 1234,
                    voucher: "1234",
                    laboratorio: {
                        imagem: "img:/statics/icons/sodre.jpg",
                        id: "",
                        nome: ""
                    },
                    exame: {
                        id: "",
                        nome:"Exame 2",
                        base_coletada: "BSO km20 SP-280 (Limeira)",
                        data_agendada: "13/07/20 18:30"
                    }
                },
                {
                    id: 12345,
                    voucher: "1235",
                    laboratorio: {
                        imagem: "img:/statics/icons/labet.jpg",
                        id: "",
                        nome: ""
                    },
                    exame: {
                        id: "",
                        nome:"Exame 3",
                        base_coletada: "BSO km20 SP-280 (Limeira)",
                        data_agendada: "13/07/20 18:30"
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
    .avatar
        img
            width: 33px !important
            height: 19px !important
            object-fit: contain !important
    
    .nome
        font-weight: bold
    
    .info
        font-weight: 300
</style>