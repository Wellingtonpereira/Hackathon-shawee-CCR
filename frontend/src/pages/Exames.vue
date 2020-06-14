<template>  
<div>
  <div class="row">
    <div class="col-12">
      <agendados />
    </div>
  </div>
  <div class="row">
    <div class="col-12">
      <disponiveis />
    </div>
  </div>
  </div>
</template>

<script>

import Agendados from 'components/exames/agendados'
import Disponiveis from 'components/exames/disponiveis'

export default {
  name: 'Exames',
  components:{
    Agendados,
    Disponiveis
  }
}
</script>
