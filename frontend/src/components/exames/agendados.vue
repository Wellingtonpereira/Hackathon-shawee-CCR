<template>
    <q-list>
      <q-expansion-item expand-separator>
        <template v-slot:header>
                <q-item-section avatar>
                    <q-icon name="img:/statics/icons/sino.svg" />
                </q-item-section>
                <q-item-section>
                    Você tem {{qtd_exames}} exames agendados
                </q-item-section>
        </template>
        <q-card>
            <listagem />  
        </q-card>
      </q-expansion-item>
    </q-list>
</template>

<script>
import Listagem from 'components/exames/listagem'

export default {
    name: "agendados",
    components:{
        Listagem
    },
    data(){
        return {
            qtd_exames: 3
        }
    }
}
</script>
<style lang="sass" scoped>
    .q-list
        padding-top: 12px
        padding-bottom: 15px
        min-height: 35px
        border-bottom: 1px solid gainsboro

</style>