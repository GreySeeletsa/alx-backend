#!/usr/bin/env node
// script that logs to the console "Redis client connected to the server"
//  OR
// logs console "Redis client not connected to the server: ERROR_MESSAGE"
import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
}
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
      return;
    }

    console.log(reply);
  });
}
// call displaySchoolValue with the Holberton key
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
