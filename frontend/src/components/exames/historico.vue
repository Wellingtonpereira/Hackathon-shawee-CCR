<template>
    <div class="detalhes">
        <div class="row ">
            <div class="col">
                <p class="laboratorio">
                    <span>
                        <q-icon name="img:/statics/icons/perfil-historico.svg"/>
                        <b>Histórico de exames</b>
                    </span>
                    <br>
                    <span> Última atualização: 14 jul 2020</span>
                </p>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <q-table :data="data" :columns="columns" row-key="name" hide-bottom>
                    <template v-slot:body="props">
                        <q-tr :props="props">
                            <q-td key="data" :props="props">
                                {{ props.row.data }}
                            </q-td>
                            <q-td key="id" :props="props">
                                {{ props.row.id }}
                            </q-td>
                            <q-td key="actions" :props="props">
                                <q-btn round color="primary" style="color: #424242;" icon="remove_red_eye" @click="handlerResultado(props.row.id)" />
                                <q-btn round color="primary" style="color: #424242;" icon="share" />
                            </q-td>
                        </q-tr>
                    </template>
                </q-table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "detalhes_exame",
    data() {
        return {
            columns: [
                { name: 'data', align: 'center', label: 'Data', field: 'data', sortable: true },
                { name: 'id', align: 'center', label: 'ID', field: 'id', sortable: true },
                { name: 'actions', align: 'center', label: 'Ações', field: 'actions', sortable: true }
            ],
            data: [
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                },
                {
                    data: '12/03/20',
                    id: 123987547,
                    actions: '#'
                }
            ]
        }
    },
    methods:{
        handlerResultado(id){
            this.$router.push('/exames/realizado/' + id)
        }
    }
}
</script>

<style lang="sass" scoped>
    .icon
        padding-right: 15px

    .q-icon
        font-size: 24px

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
            margin-left: 5px
            border-radius: 30px
            box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16)
            background-color: #ffcc00
            span
                color: #000

        .q-table__container
            box-shadow: none
        
</style>