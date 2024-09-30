// Настройки внешнего вида 
{  
  "window.density.editorTabHeight": "compact", // Устанавливает высоту вкладок в редакторе на компактную 
  "workbench.activityBar.location": "top",  // Устанавливает местоположение панели действий VS Code вверху  
  "editor.tabSize": 4, // Устанавливает размер табуляции в редакторе на 4 пробела  
  "editor.minimap.enabled": false, // Отключает мини-карту в редакторе  
  "editor.fontSize": 14,  // Устанавливает размер шрифта в редакторе на 14 пикселей  
  "window.commandCenter": false, // Отключает центр команд VS Code  
  "editor.scrollbar.vertical": "hidden", // Скрывает вертикальную полосу прокрутки в редакторе  
  "editor.scrollbar.horizontal": "hidden", // Скрывает горизонтальную полосу прокрутки в редакторе  
  "editor.folding": false, // Отключает возможность сворачивания кода в редакторе  
  "editor.glyphMargin": false, // Отключает область с иконками в редакторе  
} 

// Настройки курсора 
{  
  "editor.cursorBlinking": "expand", // Устанавливает стиль мигания курсора на расширение  
  "editor.cursorStyle": "line-thin", // Устанавливает стиль курсора на тонкую линию  
  "editor.cursorSmoothCaretAnimation": "explicit", // Включает плавную анимацию курсора  
  "editor.suggest.showIcons": true, // Включает показ иконок в подсказках  
} 

// Настройки подсказок 
{  
  "editor.quickSuggestions": {  
    "other": false, // Отключает подсказки для прочих элементов (def: on - включено по умолчанию)  
    "comments": false, // Отключает подсказки для комментариев (def: off - отключено по умолчанию)  
    "strings": false // Отключает подсказки для строк (def: off - отключено по умолчанию)  
  },  
} 

// Настройки подключений к базам данных 
{  
  "sqltools.connections": [  
    {  
      "mysqlOptions": {  
        "authProtocol": "default", // Устанавливает протокол аутентификации на "default"  
        "enableSsl": "Disabled" // Отключает SSL для соединения  
      },  
      "previewLimit": 50, // Ограничивает количество строк для предварительного просмотра результатов запроса до 50  
      "server": "localhost", // Устанавливает сервер на локальный хост  
      "port": 3306, // Устанавливает порт на 3306  
      "driver": "MySQL", // Устанавливает тип драйвера на "MySQL"  
      "name": "MySQL Local", // Устанавливает имя соединения на "MySQL Local"  
      "username": "root", // Устанавливает имя пользователя на "root"  
      "database": "hioganesdb", // Устанавливает имя базы данных на "hioganesdb"  
      "password": "Di16ser-Piero03" // Устанавливает пароль на "Di16ser-Piero03"  
    }  
  ],  
} 

// Настройки для Python (комментированные) 
{  
  // https://stackoverflow.com/questions/41115285/how-can-i-disable-hover-tooltip-hints-in-vs-code  
  //"editor.parameterHints.enabled": true, // Включает подсказки параметров (комментировано)  
  //"editor.suggest.snippetsPreventQuickSuggestions":false, // Отключает отключение подсказок из-за сниппетов (комментировано)  
  //"html.suggest.html5": true, // Включает HTML5 подсказки (комментировано)  
  //"editor.snippetSuggestions": "inline", // Устанавливает расположение подсказок сниппетов на "inline" (комментировано)  
  "python.REPL.enableREPLSmartSend": false, // Отключает умную отправку в REPL для Python  
  "python.testing.pytestEnabled": false, // Отключает pytest для тестирования Python  
  "python.testing.unittestEnabled": false // Отключает unittest для тестирования Python  
}  