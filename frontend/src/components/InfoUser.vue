<template>
    <q-card>
        <q-card-section>
            <div class="row">
                <div class="col-3">
                    <q-img :src="url"/>
                </div>

                <div class="col-9">
                    <div class="column justify-center info">
                        <div class="col-auto">
                            <div class="col-12">
                                <span class="name">
                                    {{name}}
                                </span>
                            </div>

                            <div class="col-12">
                                <span class="cnh">
                                    <b>CNH: </b>{{cnh}}
                                </span>
                                <br>
                                <span class="proximo-exame">
                                    <b>{{pontos}} </b> pontos ccr
                                </span>
                            </div>
                        </div>                        
                    </div>
                </div>
            </div>
        </q-card-section>
    </q-card>
</template>

<script>
export default {
  name: 'InfoUser',
  data(){
      return {
          url: "/statics/icons/caminho-114.svg",
          name: "Fernando dos Santos",
          cnh: "12345678900",
          pontos: 350
      }
  }
}
</script>

<style lang="sass" scoped>
    .q-card
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.25);
        border-radius: 0 0px 15px 15px;
        z-index: 200;
        height: 108px;

        .q-img
            width: 78px;
            height: 71px;
            border-radius: 5px;
            box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
            .q-img__image
                background-size: contain !important;

        .info
            height: 100%;
            padding-left: 20px;
            .name
                width: 151px;
                height: 19px;
                font-family: Roboto;
                font-size: 16px;
                font-weight: 500;
                font-stretch: normal;
                font-style: normal;
                line-height: 1.25;
                letter-spacing: normal;
                text-align: left;
                color: #424242;

            .cnh
                width: 174px;
                height: 40px;
                font-family: Roboto;
                font-size: 14px;
                font-weight: normal;
                font-stretch: normal;
                font-style: normal;
                line-height: 1.43;
                letter-spacing: normal;
                text-align: left;
                color: #424242;
                
            .proximo-exame
                font-weight: 500;
        
            
</style>