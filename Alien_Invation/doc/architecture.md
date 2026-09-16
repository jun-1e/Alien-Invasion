# Architecture

## Current structure
Alien_Invation
 ┣ enemy
 ┃ ┣ aliens
 ┃ ┗ shooter 
 ┣ Events
 ┃ ┣ game_events
 ┃ ┗ hardware_event
 ┣ Public
 ┃ ┣ Bullets
 ┃ ┃ ┣ bullet
 ┃ ┃ ┗homing_bullet 
 ┃ ┣ button
 ┃ ┣ Game_Stats
 ┃ ┣ life_bar
 ┃ ┣ scoreboard
 ┃ ┗ settings  
 ┣ resource
 ┃┗ Images
 ┃  ┣ Gemini_Generated_Image_u2eywyu2eywyu2ey.png
 ┃  ┣ shiip.bmp
 ┃  ┣ shiip_1.bmp
 ┃  ┣ shiip_2 (2).bmp
 ┃  ┣ shiip_2.bmp
 ┃  ┣ Shooter.bmp
 ┃  ┗ Shooter.png    
 ┣ 123123123
 ┣ alien_invasion(main programme)
 ┣ architecture.md
 ┣ DEVELOPE.txt
 ┣ player_ship.py
 ┗ READ_ME.txt
    
## Known problems
*重新开始按钮无法正常工作，同时暂停界面的重新开始按钮无法正常显示
*homing_bullet没有实现
*高分系统无实际作用

## Future improvements
*增加子弹种类（实现跟踪，散射等效果）
*增加移动速度更快，目标为玩家飞船的敌人
*实现游戏存档功能
*优化玩家飞船操作手感，增加变向惯性