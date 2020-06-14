<template>
    <q-header>
      <q-toolbar>
        <q-btn flat round dense>
            <q-icon name="arrow_back" v-if="paginas > 1"/>
        </q-btn>
        <q-toolbar-title class="TrechoApp">
          TrechoApp
        </q-toolbar-title>
        <q-btn flat round dense>
            <q-icon v-if="usuario" name="power_settings_new" />
        </q-btn>
      </q-toolbar>
    </q-header>
</template>

<script>
export default {
    name: "ToolBar",
    data() {
        return {
            paginas: 1,
            usuario: null
        }
    },
    methods:{
        handlerCallback(){
            // this.paginas = this.$route.path.split('/').length - 1
        }
    },
    mounted(){
        //this.$root.$on('set_callback_menu', res => { 
            //if (res) {
          //      this.handlerCallback()
            //} 
        //})
    }
}
</script>