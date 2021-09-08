
#include <kata/lcd/Lcd.hpp>

#include <gtest/gtest.h>

using namespace com::murex::kata::lcd;

TEST(Lcd, DISABLED_acceptance_test)
{
	const auto expected =
		"    _  _     _  _     _  _ \n"
		"  | _|| |  | _|| |  | _|| |\n"
		"  ||_ |_|  ||_ |_|  ||_ |_|\n";
	EXPECT_EQ(expected, lcdConvert(120120120));
}
