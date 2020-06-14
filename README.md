## HACKATHON CCR SHAWEE ##


### FRONT-END

Desenvolvido em [quasar.dev](https://quasar.dev/start/pick-quasar-flavour), um framework para desenvolvimento de aplicativos em [Vuejs](https://vuejs.org/), a ideia do projeto é ganhar em produtividade e um maior volume de telas prototipadas.

Para visualizar o projeto, rode os comandos abaixo.

Acesse a pasta do front-end
```shell
cd frontend
```

_O projeto utiliza o `nodejs 12.16.1`, utilizamos o gerenciador de versões `asdf` caso não tenha instalado a versão do nodejs solicitada, veja mais nesse link [https://github.com/asdf-vm/asdf](https://github.com/asdf-vm/asdf) e [https://github.com/asdf-vm/asdf-nodejs](https://github.com/asdf-vm/asdf-nodejs)_ 


Instale as dependêncais
```script
asdf plugin-add yarn
asdf install yarn latest
yarn install
```

Execute o projeto em modo Desenvolvimento
```script
yarn global add @quasar/cli
quasar dev
```
_Certifique-se de que a porta `8080` esteja disponível, ou, altere o arquivo `frontend/quasar.conf.js`_
