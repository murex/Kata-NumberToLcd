import { convert } from '../src/Lcd';

describe('lcd', () => {
  // Remove the ".skip" below to enable this test case
  test.skip('acceptance test', () => {
    let input: number = 120120120;
    let expected: string
      = '    _  _     _  _     _  _ \n'
      + '  | _|| |  | _|| |  | _|| |\n'
      + '  ||_ |_|  ||_ |_|  ||_ |_|\n';
    expect(convert(input)).toEqual(expected);
  });
});
