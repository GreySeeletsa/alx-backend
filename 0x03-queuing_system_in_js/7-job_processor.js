#!/usr/bin/env node
// Create an array that will contain the blacklisted phone numbers
// Create a function sendNotification that takes 4 arguments
// Create a queue with Kue that will proceed job of the queue 
// push_notification_code_2 with two jobs at a time.

import { createQueue, Job } from 'kue';

// Create a new Kue queue
const queue = createQueue();

// Define an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Sends a notification to a phone number with a given message
 * @throws {Error} Will throw an error if the phone number is blacklisted.
 * @returns {void}
 */
const sendNotification = (phoneNumber, message, job, done) => {
  // Track the progress of the job
  job.progress(0, 100);
  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // If the phone number is blacklisted, fail the job with an error
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    // If the phone number is not blacklisted, continue processing the job
    // Track the progress of the job
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
