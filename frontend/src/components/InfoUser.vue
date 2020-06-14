<template>
    <q-card>
        <q-card-section>
            <perfil />
        </q-card-section>
    </q-card>
</template>

<script>
import Perfil from 'components/usuario/perfil'
export default {
  name: 'InfoUser',
  components:{
      Perfil
  }
}
</script>

<style lang="sass" scoped>
    .q-card
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25)
        border-radius: 0 0px 15px 15px
        z-index: 200
        min-height: 108px

        .q-card__section--vert
            padding-bottom: 7px !important
            
</style>