
import Layout from 'layouts/MainLayout'
import Error404 from 'pages/Error404'
import Index from 'pages/Index'
import Pagina from 'pages/Pagina'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      { path: '', component: Index }
    ]
  },
  {
    path: '/pagina',
    component: Layout,
    children: [
      { path: '', component: Pagina }
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
