<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="flex justify-center min-h-screen">
      <div
        class="hidden bg-cover lg:block lg:w-2/5"
        style="
          background-image: url('https://images.unsplash.com/photo-1494621930069-4fd4b2e24a11?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=715&q=80');
        "
      ></div>

      <div class="flex items-center w-full max-w-3xl p-8 mx-auto lg:px-12 lg:w-3/5">
        <div class="w-full">
          <h1
            class="text-4xl font-semibold tracking-wider text-gray-800 capitalize dark:text-white"
          >
            Prediksi Penyakit Diabetes.
          </h1>

          <p class="mt-4 text-gray-500 dark:text-gray-400">
            Mohon lengkapi formulir di bawah ini untuk membantu kami dalam memprediksi risiko
            diabetes.
          </p>

          <form class="grid grid-cols-1 gap-6 mt-8 md:grid-cols-2">
            <div>
              <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">Umur Pasien</label>
              <input
                v-model.trim="parameter.a"
                type="number"
                id="a"
                min="1"
                max="120"
                placeholder="Masukkan Umur Pasien (1 th - 120 th)"
                :class="{ 'border-red-500': error && error.field === 'age' }"
                class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
              />
              <p v-if="error && error.field === 'age'" class="text-red-500 mt-1 text-sm">
                {{ error.message }}
              </p>
            </div>
            <div>
              <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">BMI</label>
              <input
                v-model.trim="parameter.b"
                type="number"
                id="b"
                placeholder="BMI dalam range 12 - 98"
                :class="{ 'border-red-500': error && error.field === 'bmi' }"
                class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
              />
              <p v-if="error && error.field === 'bmi'" class="text-red-500 mt-1 text-sm">
                {{ error.message }}
              </p>
            </div>

            <div>
              <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200"
                >Kadar Kolestrol</label
              >
              <select
                v-model.trim="parameter.c"
                id="c"
                placeholder="HighChol"
                :class="{ 'border-red-500': error && error.field === 'highchol' }"
                class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
              >
                <option value="1">Tinggi Kolestrol (Lebih dari 200mg/dL)</option>
                <option value="0">Rendah Kolestrol (kurang dari 200mg/dL)</option>
              </select>
              <p v-if="error && error.field === 'highchol'" class="text-red-500 mt-1 text-sm">
                {{ error.message }}
              </p>
            </div>

            <div>
              <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200"
                >Riwayat Kesehatan</label
              >
              <input
                v-model.trim="parameter.d"
                type="number"
                id="d"
                min="1"
                max="30"
                placeholder="Jumlah hari sakit dalam 30 hari"
                :class="{ 'border-red-500': error && error.field === 'phy' }"
                class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
              />
              <p v-if="error && error.field === 'phy'" class="text-red-500 mt-1 text-sm">
                {{ error.message }}
              </p>
            </div>

            <div>
              <label class="block mb-2 text-sm text-gray-600 dark:text-gray-200">HighBP</label>
              <select
                v-model.trim="parameter.e"
                id="e"
                placeholder="HighBP"
                :class="{ 'border-red-500': error && error.field === 'highbp' }"
                class="block w-full px-5 py-3 mt-2 text-gray-700 placeholder-gray-400 bg-white border border-gray-200 rounded-md dark:placeholder-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-700 focus:border-blue-400 dark:focus:border-blue-400 focus:ring-blue-400 focus:outline-none focus:ring focus:ring-opacity-40"
              >
                <option value="1">Tekanan darah tinggi (lebih dari 140 mmHg)</option>
                <option value="0">Tekanan darah normal (kurang dari 140 mmHg)</option>
              </select>
              <p v-if="error && error.field === 'highbp'" class="text-red-500 mt-1 text-sm">
                {{ error.message }}
              </p>
            </div>

            <button
              @click="predict"
              type="button"
              class="flex items-center justify-between w-full px-6 py-3 text-sm tracking-wide text-white capitalize transition-colors duration-300 transform bg-blue-500 rounded-md hover:bg-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-50"
            >
              <span> Predict </span>

              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-5 h-5 rtl:-scale-x-100"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </button>

            <!-- <p v-if="!APIResult.length">Isi data-data diatas untuk melakukan prediksi</p>
            <p v-else class="text-lg text">{{ APIResult }}</p> -->
          </form>
          <div class="text-xl font-bold mt-20">
            <div v-if="APIResult == null">Isi data-data di atas untuk melakukan prediksi</div>
            <div v-else>
              <div class="outline outline-2 outline-offset-2 outline-cyan-500 rounded-md p-5">
                <!-- Animated Counting untuk APIResult -->
                <div class="text-black font-bold pb-9 text-center">Decision Tree Classifier</div>
                <div class="text-blue-600 font-semibold">
                  Probabilitas Pasien Tidak Terkena Diabetes
                </div>
                <div class="text-xl">
                  <span id="count1" class="text-blue-600 font-bold" ref="countElement">{{
                    animatedCountdt
                  }}</span
                  >%
                </div>

                <!-- Animated Counting untuk APIResult2 -->
                <div class="text-green-600 font-semibold">Probabilitas Pasien Terkena Diabetes</div>
                <div class="text-xl">
                  <span id="count2" class="text-green-600 font-bold">{{ animatedCountdt2 }}</span
                  >%
                </div>

                <!-- APIResult3 di baris baru -->
                <br />
                <span class="text-blue-600 font-semibold">Kesimpulan:</span> Dengan melihat hasil
                probabilitas di atas, dapat dikatakan bahwa pasien memiliki kemungkinan untuk
                <b>{{ APIResult3 }}</b>
              </div>
            </div>
          </div>

          <div class="text-xl font-bold mt-20">
            <p v-if="APIResult == null"></p>
            <div v-else>
              <div class="outline outline-2 outline-offset-2 outline-cyan-500 rounded-md p-5">
                <!-- Animated Counting untuk APIResult4 -->
                <div class="text-black font-bold pb-9 text-center">
                  K-Nearest Neighbors Classifier
                </div>
                <div class="text-blue-600 font-semibold">
                  Probabilitas Pasien Tidak Terkena Diabetes
                </div>
                <div class="text-xl">
                  <span id="count1" class="text-blue-600 font-bold" ref="countElement">{{
                    animatedCountknn
                  }}</span
                  >%
                </div>

                <!-- Animated Counting untuk APIResult5 -->
                <div class="text-green-600 font-semibold">Probabilitas Pasien Terkena Diabetes</div>
                <div class="text-xl">
                  <span id="count2" class="text-green-600 font-bold">{{ animatedCountknn2 }}</span
                  >%
                </div>

                <!-- APIResult3 di baris baru -->
                <br />
                <span class="text-blue-600 font-semibold">Kesimpulan:</span> Dengan melihat hasil
                probabilitas di atas, dapat dikatakan bahwa pasien memiliki kemungkinan untuk
                <b>{{ APIResult3 }}</b>
              </div>
            </div>
          </div>

          <div class="text-xl font-bold mt-20">
            <div v-if="APIResult == null"></div>
            <div v-else>
              <!-- Animated Counting untuk APIResult7 -->
              <div class="outline outline-2 outline-offset-2 outline-cyan-500 rounded-md p-5">
                <div class="text-black font-bold pb-9 text-center">Naive Bayes Classifier</div>
                <div class="text-blue-600 font-semibold">
                  Probabilitas Pasien Tidak Terkena Diabetes
                </div>
                <div class="text-xl">
                  <span id="count1" class="text-blue-600 font-bold" ref="countElement">{{
                    animatedCountnb
                  }}</span
                  >%
                </div>

                <!-- Animated Counting untuk APIResult8 -->
                <div class="text-green-600 font-semibold">Probabilitas Pasien Terkena Diabetes</div>
                <div class="text-xl">
                  <span id="count2" class="text-green-600 font-bold">{{ animatedCountnb2 }}</span
                  >%
                </div>

                <!-- APIResult3 di baris baru -->
                <br />
                <span class="text-blue-600 font-semibold">Kesimpulan:</span> Dengan melihat hasil
                probabilitas di atas, dapat dikatakan bahwa pasien memiliki kemungkinan untuk
                <b>{{ APIResult3 }}</b>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { getAPI } from '@/axios'
export default {
  name: 'Posts',
  data() {
    return {
      parameter: {
        a: '',
        b: '',
        c: '',
        d: '',
        e: ''
      },
      APIResult: null,
      APIResult2: null,
      APIResult3: null,
      APIResult4: null,
      APIResult5: null,
      APIResult6: null,
      APIResult7: null,
      APIResult8: null,
      APIResult9: null,
      animatedCountdt: 0,
      animatedCountdt2: 0,
      animatedCountknn: 0,
      animatedCountknn2: 0,
      animatedCountnb: 0,
      animatedCountnb2: 0,

      error: null
    }
  },
  watch: {
    APIResult(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.animateCountdt()
      }
    }
  },
  methods: {
    animateCountdt() {
      const duration = 3000 // Animation duration in milliseconds
      const steps = 100 // Number of steps
      const stepDuration = duration / steps
      const finalCountdt = this.APIResult
      const finalCountdt2 = this.APIResult2
      const finalCountknn = this.APIResult4
      const finalCountknn2 = this.APIResult5
      const finalCountnb = this.APIResult7
      const finalCountnb2 = this.APIResult8

      let step = 0

      const update = () => {
        this.animatedCountdt = Math.round((finalCountdt / steps) * step)
        this.animatedCountdt2 = Math.round((finalCountdt2 / steps) * step)
        this.animatedCountknn = Math.round((finalCountknn / steps) * step)
        this.animatedCountknn2 = Math.round((finalCountknn2 / steps) * step)
        this.animatedCountnb = Math.round((finalCountnb / steps) * step)
        this.animatedCountnb2 = Math.round((finalCountnb2 / steps) * step)
        step++
        if (step <= steps) {
          requestAnimationFrame(update)
        }
      }

      update()
    },

    predict() {
      if (this.parameter.a < 1 || this.parameter.a > 120) {
        this.error = {
          field: 'age',
          message: 'Age must be between 1 and 120.'
        }
        return
      }
      if (this.parameter.b < 12 || this.parameter.b > 98) {
        this.error = {
          field: 'bmi',
          message: 'BMI must be between 12 and 98.'
        }
        return
      }
      if (this.parameter.c == '') {
        this.error = {
          field: 'highchol',
          message: 'Cholesterol level cant be empty'
        }
        return
      }
      if (this.parameter.d < 1 || this.parameter.d > 30) {
        this.error = {
          field: 'phy',
          message: 'Input must be within 30 days.'
        }
        return
      }
      if (this.parameter.e == '') {
        this.error = {
          field: 'highbp',
          message: 'Blood Pressure level cant be empty'
        }
        return
      }
      this.error = null

      getAPI
        .get('/diabetes', {
          params: {
            Age: this.parameter.a,
            BMI: this.parameter.b,
            HighChol: this.parameter.c,
            PhysHlth: this.parameter.d,
            HighBP: this.parameter.e
          }
        })
        .then((response) => {
          console.log('Received data successfully')
          this.APIResult = response.data.prediction_proba_dt[0][0] * 100
          this.APIResult2 = response.data.prediction_proba_dt[0][1] * 100
          this.APIResult3 = response.data.prediction_result_dt
          this.APIResult4 = response.data.prediction_proba_knn[0][0] * 100
          this.APIResult5 = response.data.prediction_proba_knn[0][1] * 100
          this.APIResult6 = response.data.prediction_result_knn
          this.APIResult7 = response.data.prediction_proba_nb[0][0] * 100
          this.APIResult8 = response.data.prediction_proba_nb[0][1] * 100
          this.APIResult9 = response.data.prediction_result_nb
          console.log(response.data)
          console.log(response)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
