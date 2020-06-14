
import Layout from 'layouts/MainLayout'
import Error404 from 'pages/Error404'
import Exames from 'pages/Exames'
import Paradas from 'pages/Paradas'
import Servicos from 'pages/Servicos'
import DetalhesExames from 'pages/DetalhesExames'
import ComprarExames from 'pages/ComprarExames'
import HistoricoExames from 'pages/HistoricoExames'
import RealizadoExames from 'pages/RealizadoExames'
import PagamentoExames from 'pages/PagamentoExames'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      { path: '', component: Exames }
    ]
  },
  {
    path: '/exames',
    component: Layout,
    children: [
      { path: '', component: Exames },
      { path: 'detalhes/:id', component: DetalhesExames },
      { path: 'comprar/:id', component: ComprarExames },
      { path: 'historico', component: HistoricoExames },
      { path: 'realizado/:id', component: RealizadoExames }
    ]
  },
  {
    path: '/pagamento',
    component: Layout,
    children: [
      { path: ':id', component: PagamentoExames }
    ]
  },
  {
    path: '/paradas',
    component: Layout,
    children: [
      { path: '', component: Paradas }
    ]
  },
  {
    path: '/servicos',
    component: Layout,
    children: [
      { path: '', component: Servicos }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: Error404
  })
}

export default routes
