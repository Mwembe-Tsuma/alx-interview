// File: 1-calcul.test.js

const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  describe('SUM operation', () => {
    it('should add rounded numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
      assert.strictEqual(calculateNumber('SUM', 2.0, 2.0), 4);
      assert.strictEqual(calculateNumber('SUM', -2.0, -2.0), -4);
      assert.strictEqual(calculateNumber('SUM', -2.0, 2.0), 0);
      assert.strictEqual(calculateNumber('SUM', 0.0, 0.0), 0);
    });
  });

  describe('SUBTRACT operation', () => {
    it('should subtract rounded b from a', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
      assert.strictEqual(calculateNumber('SUBTRACT', 2.0, 2.0), 0);
      assert.strictEqual(calculateNumber('SUBTRACT', -2.0, -2.0), 0);
      assert.strictEqual(calculateNumber('SUBTRACT', -2.0, 2.0), -4.0);
      assert.strictEqual(calculateNumber('SUBTRACT', 2.0, -2.0), 4.0);
      assert.strictEqual(calculateNumber('SUBTRACT', 0.0, 0.0), 0);
    });
  });

  describe('DIVIDE operation', () => {
    it('should divide rounded a by rounded b', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should handle division by 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 8.0, 2.0), 4.0);
      assert.strictEqual(calculateNumber('DIVIDE', -7.0, 2.0), -3.5);
      assert.strictEqual(calculateNumber('DIVIDE', 7.0, -2.0), -3.5);
      assert.strictEqual(calculateNumber('DIVIDE', 7.0, -2.0), -3.5);
      assert.strictEqual(calculateNumber('DIVIDE', -7.0, -2.0), 3.5);
      assert.strictEqual(calculateNumber('DIVIDE', 2.0, 2.0), 1);
      assert.strictEqual(calculateNumber('DIVIDE', -2.0, -2.0), 1);
      assert.strictEqual(calculateNumber('DIVIDE', 2.6, 3.0), 1);
      assert.strictEqual(calculateNumber('DIVIDE', 2.4, 2.0), 1);
      assert.strictEqual(calculateNumber('DIVIDE', 0.0, 5.0), 0);
      assert.strictEqual(calculateNumber('DIVIDE', 0.0, -5.0), -0);
      assert.strictEqual(calculateNumber('DIVIDE', 5.0, 0), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 5.0, 0.2), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 5.0, -0.2), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', -5.0, 0), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', -5.0, 0.2), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', -5.0, -0.2), 'Error');
      assert.strictEqual(calculateNumber('DIVIDE', 0.0, 0.0), 'Error');
    });
  });
});
