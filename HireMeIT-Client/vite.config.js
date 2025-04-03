// import { defineConfig } from 'vite'
// import react from '@vitejs/plugin-react'

// // https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [react()],
//   server: {
//     port: 3000,
//     proxy: {
//       '/api': {
//         target: 'http://localhost:5000',
//         changeOrigin: true,
//       }
//     },
//     headers: {
//       "Content-Type": "application/javascript",
//     }
//   }
// })


import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: process.env.PORT || 3000,
    proxy: {
      '/api': {
        target: process.env.BACKEND_URL || 'https://hireme-it.onrender.com' || 'http://127.0.0.1:10000' || 'http://10.204.189.63:10000',
        changeOrigin: true,
        secure: false
      }
    },
    headers: {
      "Content-Type": "application/javascript",
    }
  }
})