const brain = require('brain.js')
const data = require('./data.js')

const trainingData = [
  'Jane saw Doug.',
  'Doug saw Jane.',
  'Spot saw Doug and Jane looking at each other.',
  'It was love at first sight, and Spot had a frontrow seat. It was a very special moment for all.',
  'Hey, what up'
];

const lstm = new brain.recurrent.LSTM();
const result = lstm.train(data.data, {
  iterations: 1,
  log: details => console.log(details),
  errorThresh: 0.011
});
const run1 = lstm.run('News');

console.log('run 1: News' + run1);