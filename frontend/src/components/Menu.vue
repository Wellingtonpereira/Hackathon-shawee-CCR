<template>
    <q-card>
      <q-card-section>
          <div class="row  justify-center">
            <div class="col text-center">
                <q-btn :class="pageActive == '/exames' ? 'active' : ''" flat @click="pushRouter('/exames')">
                  <q-icon name="img:/statics/icons/exames-30px.svg" />
                  <span class="title">Exames</span>
                </q-btn>
            </div>
            <div class="col text-center">
                <q-btn :class="pageActive == '/paradas' ? 'active' : ''" flat @click="pushRouter('/paradas')">
                  <q-icon name="img:/statics/icons/paradas-30px.svg" />
                  <span class="title">Paradas</span>
                </q-btn>
            </div>
            <div class="col text-center">
                <q-btn :class="pageActive == '/servicos' ? 'active' : ''" flat @click="pushRouter('/servicos')">
                  <q-icon name="img:/statics/icons/servicos-30px.svg" />
                  <span class="title">Serviços</span>
                </q-btn>
            </div>
          </div>
      </q-card-section>
    </q-card>
</template>

<script>
export default {
  name: 'Menu',
  data(){
    return {
      pageActive: '/exames',
    }
  },
  methods: {
    handerActice(){
      this.pageActive = '/'+this.$route.path.split('/')[1]
    },
    pushRouter(router){
      this.$router.push(router)
      this.handerActice()
    }
  },
  mounted(){
    this.handerActice()
  }
}
</script>

<style lang="sass" scoped>
  .q-card
    border-radius: 0 0px 15px 15px
    z-index: 100
    top: -20px
    background: #f2f2f2
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25)
    .q-card__section--vert
      height: 152px
      padding-top: 40px !important

      .active
        background: #ffcc00 !important
        .q-icon
          color: #424242 !important
        .title
          color: #424242 !important

      .q-btn    
        height: 88px      
        width: 97px
        border-radius: 5px
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1)
        background: #ffffff
        border: 0
        
        .q-icon
          width: 30px
          height: 30px
          object-fit: contain

        .title
          width: 50px
          height: 17px
          text-transform: capitalize
          -webkit-text-stroke: 1px rgba(0, 0, 0, 0)
          font-family: Roboto
          font-size: 14px
          font-weight: 500
          font-stretch: normal
          font-style: normal
          line-height: 1.14
          letter-spacing: normal
          text-align: center
          color: #7d7d7d
</style>