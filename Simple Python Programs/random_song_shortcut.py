'''
This script combines with the Pythonista and Shortcuts iPad apps.

When the user pushes the 'Random Song' Shortcuts button 3 things happen;
    1) This script copies one random string from the list to the clipboard.
    2) Shortcuts opens Spotify and 'Platinum Song List' in the Notes app.
    3) Shortcuts sends a notification containing the contents of the clipboard 
    number to the user.
 
The user should be able to use the Siri voice command "Random Song" to activate
this but it doesn't work!
'''

import random, clipboard

songlist = []
songlist.append("1. Highway Star - Deep Purple")
songlist.append("2. Won't Get Fooled Again - The Who'")
songlist.append("3. Comfortably Numb - Pink Floyd")
songlist.append("4. Jump - Van Halen")
songlist.append("5. Radar Love - White Lion")
songlist.append("6. Keep on Rockin’ in the Free World - Bon Jovi")
songlist.append("7. Black Night - Deep Purple")
songlist.append("8. Just Like Paradise - David Lee Roth")
songlist.append("9. Live and Let Die - Guns and Roses")
songlist.append("10. Raise Your Hands - Bon Jovi")
songlist.append("11. Start Talking Love - Magnum")
songlist.append("12. One Night Love Affair - Bryan Adams")
songlist.append("13. Doctor Doctor - UFO")
songlist.append("14. Mr. Blue Sky - ELO")
songlist.append("15. Wanted Dead or Alive - Bon Jovi")
songlist.append("16. Out in the Fields - Gary Moore")
songlist.append("17. Run To You - Bryan Adams")
songlist.append("18. Feels Like The First Time - Foreigner")
songlist.append("19. Animal - Def Leppard")
songlist.append("20. Starlight - Muse")
songlist.append("21. Blinded by the Light - Manfred Mann")
songlist.append("22. Separate Ways (Worlds Apart) - Journey")
songlist.append("23. Give Me All Your Love Tonight - Whitesnake")
songlist.append("24. Where the Streets Have No Name - U2")
# songlist.append("25. Space Oddity - David Bowie") # ABANDONED
songlist.append("26. Starman - David Bowie")
songlist.append("27. Rain - The Cult")
songlist.append("28. Bat Out of Hell - Meatloaf")
songlist.append("29. Hold the Line - Toto")
songlist.append("30. Anyway You Want It - Journey")
songlist.append("31. Elouise - The Damned")
songlist.append("32. Rebel Yell - Billy Idol")
songlist.append("33. Run to the Hills - Iron Maiden")
songlist.append("34. Smoke on the Water - Deep Purple")
songlist.append("35. Wishing Well - Free")
songlist.append("36. Sweet Child O’ Mine - Guns ‘n’ Roses")
songlist.append("37. Whole Lotta Rosie - AC/DC")
songlist.append("38. Highway to Hell - AC/DC")
songlist.append("39. Coming Back to Life - Pink Floyd")
songlist.append("40. In the Flesh/The Happiest Days of Our Lives/Another " +
                "Brick in the Wall - Pink Floyd")
songlist.append("41. Boys Are Back in Town - Thin Lizzy")
songlist.append("42. It’s My Life - Bon Jovi")
songlist.append("43. Stairway to Heaven - Led Zeppelin")
songlist.append("44. Bed of Roses - Bon Jovi")
songlist.append("45. Free Bird - Lynyrd Skynyrd")
songlist.append("46. She Sells Sanctuary - The Cult")
songlist.append("47. Whiskey in the Jar - Thin Lizzy")
songlist.append("48. Run Like Hell - Pink Floyd")
songlist.append("49. In These Arms - Bon Jovi")
songlist.append("50. Lazy Sunday Afternoon - Thunder")
songlist.append("51. Pinball Wizard - The Who")
songlist.append("52. Ships in the Night - Be Bop Deluxe")
songlist.append("53. Born to be Wild - Steppenwolf")
songlist.append("54. Enter Sandman - Metallica")
songlist.append("55. Rock and Roll - Led Zeppelin")
songlist.append("56. Livin' On A Prayer - Bon Jovi")
songlist.append("57. Runaway - Bon Jovi")
songlist.append("58. In A Broken Dream - Thunder")
songlist.append("59. Bohemian Rhapsody - Queen")
songlist.append("60. St. Elmos Fire - John Parr")
# songlist.append("53. Little Devil - The Cult")
# songlist.append("54. 747 Strangers in the Night - Saxon")
# songlist.append("55. Can’t Get Enough - Bad Company")
# songlist.append("56. Paranoid - Black Sabbath")
# songlist.append("57. Ain’t No Talking Bout Love - Van Halen")
# songlist.append("58. Feel Like Making Love - Bad Company")
# songlist.append("59. Ziggy Stardust - David Bowie")
# songlist.append("60. Over the Hills n Far Away - Gary Moore")
# songlist.append("61. Perfect Strangers - Deep Purple")
# songlist.append("62. Kayleigh and Lavender - Marrilion")
# songlist.append("63. Hotel California - The Eagles")
# songlist.append("64. November Rain - GnR")

clipboard.set(str(random.sample(songlist, 1)))
