#!/usr/bin/env node
'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const calls = [];
let consent = false;
let clickHandler;
const context = {
  console,
  URL,
  Number,
  Object,
  String,
  window: {
    location: { origin: 'https://wheeloflist.com', pathname: '/' },
    gtag: (...args) => calls.push(args)
  },
  localStorage: { getItem: () => consent ? 'accepted' : null },
  document: {
    addEventListener: (name, handler) => {
      if (name === 'click') clickHandler = handler;
    }
  }
};

const source = fs.readFileSync(path.join(__dirname, '..', 'engagement.js'), 'utf8');
vm.runInNewContext(source, context, { filename: 'engagement.js' });

assert.equal(context.window.wolAnalytics.track('wheel_spin_start', { item_count: 4 }), false);
assert.equal(calls.length, 0, 'events must be blocked before consent');

consent = true;
assert.equal(context.window.wolAnalytics.track('unknown_event', { item_count: 4 }), false);
assert.equal(calls.length, 0, 'unknown events must be blocked');

assert.equal(context.window.wolAnalytics.track('wheel_result', {
  item_count: 4.4,
  remaining_count: 3,
  winner: 'Private Name',
  free_text: 'must not leave the browser'
}), true);
assert.equal(calls.length, 1);
assert.equal(calls[0][0], 'event');
assert.equal(calls[0][1], 'wheel_result');
assert.deepEqual(Object.keys(calls[0][2]).sort(), ['item_count', 'remaining_count', 'send_to']);
assert.equal(calls[0][2].item_count, 4);
assert.equal(calls[0][2].remaining_count, 3);

assert.equal(context.window.wolAnalytics.track('wheel_share', { method: 'Contains spaces' }), true);
assert.deepEqual(Object.keys(calls[1][2]), ['send_to'], 'unsafe categorical values must be dropped');

context.window.location.pathname = '/coin-flip/';
clickHandler({
  target: {
    closest: (selector) => selector === 'button[id]' ? { id: 'flip-btn' } : null
  }
});
assert.equal(calls[2][1], 'tool_action');
assert.equal(calls[2][2].action, 'flip');
assert.equal(calls[2][2].tool, 'coin_flip');

const templateLink = {
  href: 'https://wheeloflist.com/wheels/what-to-eat/',
  closest: (selector) => selector === '.tool-card' ? {} : null
};
clickHandler({
  target: {
    closest: (selector) => selector === 'a[href]' ? templateLink : null
  }
});
assert.equal(calls[3][1], 'template_open');
assert.equal(calls[3][2].template, 'what_to_eat');
assert.equal(calls[3][2].source, 'card');

console.log('Analytics privacy tests passed.');
