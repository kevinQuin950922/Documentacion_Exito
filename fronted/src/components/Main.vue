<template>
  <div>
    <p>{{ mensaje }}</p>
  </div>
</template>

z<script>
import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      mensaje: 'Sin mensaje!'
    }
  },
  methods: {
    getMensaje () {
      const path = 'http://localhost:5000/projects/klczb7u4f5ombypc7t5zxeknhlvf3cthjd4kmkh7nawfo6ac42pq/juancho270'
      axios.get(path).then((respuesta) => {
        this.mensaje = respuesta.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created () {
    this.getMensaje()
  }
}
</script>
