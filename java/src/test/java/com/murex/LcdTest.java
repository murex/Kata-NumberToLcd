package com.murex;

import org.junit.Ignore;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class LcdTest {
    @Ignore
    @Test
    public void acceptance_test() {
        int input = 120120120;
        String expected
                = "    _  _     _  _     _  _ \n"
                + "  | _|| |  | _|| |  | _|| |\n"
                + "  ||_ |_|  ||_ |_|  ||_ |_|\n";
        assertEquals(expected, Lcd.convert(input));
    }
}
