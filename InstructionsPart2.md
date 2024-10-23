# Number to LCD

## Instructions - Part 2

Change your program to support variable width or height of the digits.

For example for width = 3 and height = 2 the digit 2 will be:

```
 ___
    |
 ___|
|
|___
```

## Scaling Acceptance Test

Add the below acceptance test to your list of test cases.

### C++ Version

```cpp
TEST(Lcd, acceptance_test_scaling)
{
    const auto expected =
        "      ___  ___ \n"
        "    |    ||   |\n"
        "    | ___||   |\n"
        "    ||    |   |\n"
        "    ||___ |___|\n";
    EXPECT_EQ(expected, lcdConvert(120, 3, 2));
}
```

### Java Version

```java
@Test
public void acceptance_test_scaling() {
    int input = 120;
    String expected
            = "      ___  ___ \n"
            + "    |    ||   |\n"
            + "    | ___||   |\n"
            + "    ||    |   |\n"
            + "    ||___ |___|\n";
    assertEquals(expected, Lcd.convert(input, 3, 2));
}
```

### Typescript Version

```typescript
test('acceptance test with scaling', () => {
    const input = 120;
    const expected: string
      = ''
      + '      ___  ___ \n'
      + '    |    ||   |\n'
      + '    | ___||   |\n'
      + '    ||    |   |\n'
      + '    ||___ |___|\n';
    expect(convert(input, 3, 2)).toEqual(expected);
});
```
