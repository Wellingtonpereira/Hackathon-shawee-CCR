<template>
<div>
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
                        
                        <span class="cnh" v-if="exibir">
                            <br>
                            <b>Tel.: </b>{{telefone}}
                        </span>
                        
                        <span class="proximo-exame" v-if="!exibir">
                            <br>
                            <b>{{pontos}} </b> pontos ccr
                        </span>
                    </div>

                </div>
            </div>
        </div>
    </div>
    <div v-if="exibir" class="wrapper-profile">
        <div class="row">
            <div class="col-12 situacao">
                <b>Situação: </b>{{situacao}}<br>
                <b>Empresa: </b>{{empresa.nome}}
            </div>
            <div class="col-12 situacao">
                <b>
                    <q-icon name="img:/statics/icons/perfil-historico.svg"/>
                    Informações Gerais
                </b>
                <br>
                <b>CNH: </b>{{cnh}}<br>
                <b>Prazo de Expiração da CNH: <br></b>{{empresa.nome}}
            </div>
            <div class="col-12 situacao">
                <b>
                    <q-icon name="img:/statics/icons/perfil-pontos.svg"/>
                    Programa de Pontos Trecho CCR
                </b>
                <div class="row">
                    <div class="col-12 text-center pontos">
                        {{pontos}} pontos
                    </div>
                </div>
                <div class="row justify-between">
                    <q-linear-progress :value="progress" class="q-mt-md" />
                    <div class="col-3">Iniciado em 12 jan</div>
                    <div class="col-3 text-right">{{pontos}} de 1000  pontos</div>

                    <div class="row">
                        <div class="col-12 dicas">
                            Acumule pontos para <b>trocar por brindes</b> ou <b>usar em cabines de pedágio</b> e serviços de empresas parceiras.
                        </div>
                    </div>
                </div>

                <div class="row">
                    <div class="col-12 text-center">
                        <q-btn outline rounded style="color: #424242;" >
                            <q-icon name="img:/statics/icons/pontos-preenchido.svg"/>
                            Trocar pontos
                        </q-btn>
                    </div>
                </div>
            </div>
            <div class="col-12 situacao">
                <b>
                    <q-icon name="img:/statics/icons/perfil-historico.svg"/>
                    Histórico de exames
                </b>
                <div class="col-12 dicas">
                    Confira informações sobre sua saúde e todos os exames realizados anteriormente.
                </div>
                <div class="col-12 text-center">
                    <q-btn outline rounded style="color: #424242;" @click="handlerHistorico()">
                        <q-icon name="img:/statics/icons/historico.svg"/>
                        Consultar histórico
                    </q-btn>
                </div>
            </div>
            <div class="col-12 situacao">
                <b>
                    <q-icon name="img:/statics/icons/perfil-historico.svg"/>
                    Fraudes e denúncias
                </b>
                <div class="col-12 dicas">
                    Use os botões abaixo para registrar denúncias sobre fraudes em exames toxicológicos ou descumprimento dos direitos de leis trabalhistas .
                </div>
                <div class="col-12 text-center">
                    <denuncia />
                </div>
            </div>

        </div>
    </div>

    <div class="row">
        <div class="col-12 text-center arrow_down" @click="handlerPerfil()">
            <q-icon name="keyboard_arrow_down" v-if="!exibir"/>
            <q-icon name="keyboard_arrow_up" v-else/>
        </div>
    </div>
</div>
</template>

<script>
import Denuncia from 'components/dialogs/denuncia'
export default {
    name: 'InfoUser',
    components: {
        Denuncia
    },
    data(){
        return {
            exibir: false,
            url: "/statics/icons/usuario.jpeg",
            name: "Fernando dos Santos",
            cnh: "12345678900",
            pontos: 430,
            telefone: "(14) 9914318703",
            situacao: "Contratado",
            progress:  430/1000,
            empresa: {
                nome: "XPTO Transportadora"
            }
        }
    },
    methods:{
        handlerPerfil(){
            if (this.exibir){
                this.exibir = false
            }else{
                this.exibir = true
            }
        },
        handlerHistorico(){
            this.exibir = false
            this.$router.push('/exames/historico')
        }
    }
}
</script>

<style lang="sass" scoped>

    .arrow_down
        .material-icons
            color: #000 !important

    .q-img
        width: 78px
        height: 71px
        border-radius: 5px
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1)
        .q-img__image
            background-size: contain !important

    .info
        height: 100%
        padding-left: 20px
        .name
            width: 151px
            height: 19px
            font-family: Roboto
            font-size: 16px
            font-weight: 500
            font-stretch: normal
            font-style: normal
            line-height: 1.25
            letter-spacing: normal
            text-align: left
            color: #424242

        .cnh
            width: 174px
            height: 40px
            font-family: Roboto
            font-size: 14px
            font-weight: normal
            font-stretch: normal
            font-style: normal
            line-height: 1.43
            letter-spacing: normal
            text-align: left
            color: #424242
            
        .proximo-exame
            font-weight: 500

    .wrapper-profile
        padding-top: 10px
        .situacao
            font-family: Roboto;
            font-size: 14px;
            font-weight: 500;
            font-stretch: normal;
            font-style: normal;
            line-height: 2;
            letter-spacing: normal;
            text-align: left;
            color: #424242;
            border-bottom: 1px solid #cacaca;
            padding-top: 10px;
            padding-bottom: 15px;

            img
                width: 24px;
                height: 24px;
                object-fit: contain;

            .q-linear-progress
                height: 14px;
                border-radius: 50px;

            .dicas
                padding: 20px 0
                font-size: 14px;
                font-weight: normal;
                font-stretch: normal;
                font-style: normal;
                line-height: 1.43;
                letter-spacing: normal;
                text-align: left;
                color: #424242;

            .pontos
                font-weight: bold
                font-size: 20px
        
</style>