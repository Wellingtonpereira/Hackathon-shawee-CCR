<template>
    <div>
        <q-btn outline rounded style="color: #424242;" @click="alert = true"  >
            <q-icon name="img:/statics/icons/comment.svg"/>
            Denunciar fraude
        </q-btn>

        <q-dialog v-model="alert">
            <q-card>
                <q-card-section>
                <div class="text-h6 alert">Aviso</div>
                </q-card-section>

                <q-card-section class="q-pt-none info">
                    Você será redirecionado ao site do Ministério do 
                    Trabalho para continuar a sua denúncia. <br>
                    Caso não queira continuar, ligue para <b>{{telefone}}</b>.
                </q-card-section>

                <q-card-actions align="right">
                    <q-btn flat label="Continuar" color="primary" v-close-popup />
                    <q-btn flat label="Cancelar" color="primary" v-close-popup />
                </q-card-actions>
            </q-card>
        </q-dialog>

    </div>
</template>

<script>
export default {
  data () {
    return {
      alert: false,
      telefone: "xxxx xxxx"
    }
  }
}
</script>
<style lang="sass" scoped>
    .alert
        font-family: Roboto;
        font-size: 20px;
        font-weight: 500;
        font-stretch: normal;
        font-style: normal;
        line-height: 1.2;
        letter-spacing: normal;
        text-align: left;
        color: #424242;
    .info
        font-family: Roboto;
        font-size: 16px;
        font-weight: normal;
        font-stretch: normal;
        font-style: normal;
        line-height: 1.5;
        letter-spacing: normal;
        text-align: left;
        color: rgba(0, 0, 0, 0.54);

    .q-btn__content
        span
            font-weight: bold;
</style>