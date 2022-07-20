<template>
  <div class="home">
    <h1 class="title">Todo Project</h1>

    <hr>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
          <h2 class="subtitle">Добавить задачу</h2>

          <div class="field">
            <label class="label">Описание</label>
            <div class="control">
              <input class="input" type="text" v-model="description">
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-link">Подтвердить</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="columns">
      <div class="column is-6"style="margin-left: 6px">
        <h2 class="subtitle">Задачи</h2>

        <div class="todo">
          <div class="card" v-for="task in tasks" v-if="task.status === 'todo'" v-bind:key="task.id">
            <div class="card-content">
              <div style="display: block">
                {{ task.description }}
              </div>
              <div style="text-align: right;">
                {{task.time_create}}
              </div>
            </div>
            <footer class="card-footer">
              <a class="card-footer-item" @click="setStatus(task.id, 'done')">Выполнено!</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">Выполненные задачи</h2>

        <div >
          <div class="card" v-for="task in tasks" v-if="task.status === 'done'" v-bind:key="task.id">
            <div class="card-content done">{{ task.description }}</div>

            <footer class="card-footer" >
              <a class="card-footer-item" @click="setStatus(task.id, 'todo')">В список задач</a>
            </footer>
            <footer class="card-footer" >
              <a class="card-footer-item" @click="deleteTask(task.id)" style="color: red">Удалить</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000/'

import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      tasks: [],
      description: '',
      status: 'todo'
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks() {
      axios({
        method: 'get',
        url: API_URL + 'tasks/',
        // auth: {
        //   username: 'admin',
        //   password: 'admin'
        // }
      }).then(response => this.tasks = response.data)
    },
    addTask() {
      if (this.description) {
        axios({
          method: 'post',
          url: API_URL + 'tasks/',
          data: {
            description: this.description,
            status: this.status,
            // time_create:this.time_create
          },
          // auth: {
          //   username: 'admin',
          //   password: 'admin'
          // }
        }).then((response) => {
          let newTask = {
            'id': response.data.id,
            'description': this.description,
            'status': this.status,
          }
          this.getTasks();
          this.tasks.push(newTask)

          this.description = ''
          this.status = 'todo'
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    setStatus(task_id, status) {
      const task = this.tasks.filter(task => task.id === task_id)[0]
      const description = task.description

      axios({
        method: 'put',
        url: API_URL + 'tasks/' + task_id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          status: status,
          description: description,
        },
      }).then(() => {
        task.status = status
      })
    },
    deleteTask(task_id) {
      axios.delete(API_URL + 'tasks/' + task_id + '/', {
      }).then(()=>{
        this.getTasks();
      })
    }
  }
}
</script>

<style lang="scss">
.select, select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  text-decoration: line-through;
}
</style>
