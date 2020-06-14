<template>
  <q-layout view="hhh ipr fff">
    <tool-bar />
    <info-user />
    <my-menu />

    <div class="q-container">
      <router-view />
    </div>
  </q-layout>
</template>

<script>
import ToolBar from 'components/ToolBar'
import MyMenu from 'components/Menu'
import InfoUser from 'components/InfoUser'

export default {
  name: 'MainLayout',
  components: {
    ToolBar,
    InfoUser,
    MyMenu
  }
}
</script>

<style lang="sass" scoped>
  .q-header
    position: relative !important

  .q-container
      top: -12px
      position: relative
  
</style>