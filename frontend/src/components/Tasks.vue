<template>
    <v-row class="justify-center">
      <v-col sm="10">
        <h1>Task</h1>
        <hr><br><br>
        <v-btn>
          Add Task
        </v-btn>
        <br><br>

        <v-data-table
          :headers="headers"
          :items="myList"
          :items-per-page="5"
          item-key="oid"
          class="elevation-1"
        >
          <template v-slot:item.oid="props">
            <v-btn>
              {{ props.item.oid }}
            </v-btn>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
</template>

<script>
export default {
  name: 'Tasks',
  data: () => ({
    headers: [
      { text: 'Owner', value: 'username' },
      { text: 'Category', value: 'category' },
      { text: 'Created At', value: 'createdAt' },
      { text: '', value: 'oid' },
    ],
    myList: [
      {
        username: 'Frozen Yogurt',
        category: 159,
        createdAt: 24,
        oid: 0,
      },
      {
        username: 'Ice cream sandwich',
        category: 237,
        createdAt: 37,
        oid: 1,
      },
      {
        username: 'Eclair',
        category: 262,
        createdAt: 23,
        oid: 2,
      },
      {
        username: 'Cupcake',
        category: 305,
        createdAt: 67,
        oid: 3,
      },
      {
        username: 'Gingerbread',
        category: 356,
        createdAt: 49,
        oid: 4,
      },
      {
        username: 'Jelly bean',
        category: 375,
        createdAt: 94,
        oid: 5,
      },
      {
        username: 'Lollipop',
        category: 392,
        createdAt: 98,
        oid: 6,
      },
      {
        username: 'Honeycomb',
        category: 408,
        createdAt: 87,
        oid: 0,
      },
      {
        username: 'Donut',
        category: 452,
        createdAt: 51,
        oid: 0,
      },
      {
        username: 'KitKat',
        category: 518,
        createdAt: 65,
        oid: 7,
      },
    ],
  }),
};
</script>
