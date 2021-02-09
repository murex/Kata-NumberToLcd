#ifndef LCD_CONFIG
#define LCD_CONFIG

#ifdef _MSC_VER
#ifdef LCD_EXPORTS
#define LCD_API __declspec(dllexport)
#else
#define LCD_API __declspec(dllimport)
#endif
#else
#define LCD_API
#endif

#endif // LCD_CONFIG
