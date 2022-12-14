# LANG: ENGLISH LANG_CODE: ENG                                      >>  copyright Β©οΈ 2021 nabilanavab  <<                                         fileName : lang/ENG.py
#                                        Thank: nabilanavab                                                   E-mail: nabilanavab@gmail.com

from configs.config import settings

# PM WELCOME MESSAGE (HOME A, B, C, D...)
HOME = {
    "HomeA" : """Hey [{}](tg://user?id={})..!!
This bot will help you to do many things with PDFs. π₯³

Some of the key features are:\nβ `Convert images to PDF`
β `Convert PDF to images`\nβ `Convert files to PDF`""",
    "HomeACB" : {
        "βοΈ SETTINGS βοΈ" : "Home|B", "β οΈ HELP β οΈ" : "Home|C",
        "π’ CHANNEL π’" : f"{str(settings.OWNED_CHANNEL)}",
        "π SOURCE CODE π" : f"{str(settings.SOURCE_CODE)}",
        "πΆ CLOSE πΆ" : "close|mee"
    },
    "HomeAdminCB" : {
        "βοΈ SETTINGS βοΈ" : "Home|B", "β οΈ HELP β οΈ" : "Home|C",
        "π’ CHANNEL π’" : f"{str(settings.OWNED_CHANNEL)}",
        "π SOURCE CODE π" : f"{str(settings.SOURCE_CODE)}",
        "π½ STATUS π½" : f"status|home", "πΆ CLOSE πΆ" : "close|mee"
    },
    "HomeB" : """SETTINGS PAGE βοΈ\n\nUSER NAME   : {}
USER ID           : {}\nUSERNAME    : {}\nJOIN DATE      : {}\n
LANGUAGE    : {}\nAPI                    : {}
THUMB            : {}\nCAPTION         : {}\nFILE NAME      : {}""",
    "HomeBCB" : {
        "π LANG π" : "set|lang", "π THUMB π" : "set|thumb",
        "π NAME π" : "set|fname", "π© API π©" : "set|api",
        "π CAPTION π" : "set|capt", "Β« BACK TO HOME Β«" : "Home|B2A"
    },
    "HomeC" : """πͺ **HELP MESSAGE** πͺ:

```Some of the main features are:
 β Convert Images to PDF\n β PDF Manupultions\n β Many popular codecs to PDF
 
Modify the PDF file:
 β PDFβ₯IMAGES [all,range,pages]\n β DOCS to PDF [png, jpg, jpeg]\n β IMAGESβ₯PDF\n β PDF METADATA\n β PDFβ₯TEXT\n β TEXTβ₯PDF\n β Compress pdf file
 β SPLIT PDF [range, pages]\n β MERGE PDF\n β ADD STAMP\n β RENAME PDF\n β ROTATE PDF\n β ENCRYPT/DECRYPT PDF\n β PDF FORMATTER \n β PDFβ₯JSON/TXT FILE
 β PDFβ₯HTML [web view]\n β URLβ₯PDF\n β PDFβ₯ZIP/TAR/RAR [all, range, pages]\nAnd Much More.. ```""",
    "HomeCCB" : {"Β« BACK HOME Β«" : "Home|A", "π INSTRUCTIONS π" : "Home|D"},
    "HomeD" : """`As you know, this is a free service, I cannot guarantee how long I can maintain this service..`π
 
β οΈ INSTRUCTIONS β οΈ:
π __Please don't try to abuse Bot Admins__ π
π __Don't spam here, may lead to a permanent ban π²__.
π __Porn Contents too will gives you PERMANENT BAN π―__

**Send any image to start:** π""",
    "HomeDCB" : {"β οΈ HELP β οΈ" : "Home|C", "Β» BACK HOME Β»" : "Home|A"}  
}

SETTINGS = {
    "default" : ["DEFAULT β", "CUSTOM β"], "chgLang" : {"SETTING βοΈ Β» CHANGE LANG π" : "nabilanavab"},
    "error" : "Something went wrong while retrieving data from the database", "lang" : "Now, Select any language..",
    "ask" : ["Now, Send me..", "Now, Send me.. π\n\nFast.! I have no more time to go over the text.. π\n\n/cancel: to cancel"],
    "askApi" : "\n\nOpen the **Below** link and Send me the secret code:", "waitApi" : {"Open link β" : "https://www.convertapi.com/a/signin"},
    "wait" : {"Waiting.. π₯±" : "nabilanavab"}, "back" : {"Β« BACK TO HOME Β«" : "Home|B2S"}, "errorCB" : {"Β« BACK TO HOME Β«" : "Home|B2A"},
    "result" : ["Settings cannot be updated β", "Settings Updated Successfully β"], "cant" : "This feature cannot be used β",
    "feedback" : "Reviews from Awesome Customers like you help Other.\n@nabilanavab"
                 "\n\nReport a BUG in {} Lang:\n`β’ Specify Lang\nβ’ Error Message\nβ’ New Message`",
    "feedbtn" : {"Report Lang Error" : settings.REPORT},
    "thumb" : [
        {"SETTING βοΈ Β» THUMBNAIL π·" : "nabilanavab", "β» ADD β»" : "set|thumb+", "Β« BACK TO HOME Β«" : "Home|B"},
        {"SETTING βοΈ Β» THUMBNAIL π·" : "nabilanavab", "β» CHANGE β»" : "set|thumb+", "π DELETE π" : "set|thumb-", "Β« BACK TO HOME Β«" : "Home|B2S"}
    ],
    "fname" : [
        {"SETTING βοΈ Β» FNAME π·" : "nabilanavab", "β» ADD β»" : "set|fname+", "Β« BACK TO HOME Β«" : "Home|B2S"},
        {"SETTING βοΈ Β» FNAME π·" : "nabilanavab", "β» CHANGE β»" : "set|fname+", "π DELETE π" : "set|fname-", "Β« BACK TO HOME Β«" : "Home|B2S"}
    ],
    "api" : [
        {"SETTING βοΈ Β» API π·" : "nabilanavab", "β» ADD β»" : "set|api+", "Β« BACK TO HOME Β«" : "Home|B2S"},
        {"SETTING βοΈ Β» API π·" : "nabilanavab", "β» CHANGE β»" : "set|api+", "π DELETE π" : "set|api-", "Β« BACK TO HOME Β«" : "Home|B2S"}
    ],
    "capt" : [
        {"SETTING βοΈ Β» CAPTION π·" : "nabilanavab", "β» ADD β»" : "set|capt+", "Β« BACK TO HOME Β«" : "Home|B2S"},
        {"SETTING βοΈ Β» CAPTION π·" : "nabilanavab", "β» CHANGE β»" : "set|capt+", "π DELETE π" : "set|capt-", "Β« BACK TO HOME Β«" : "Home|B2S"}
    ]
}

BOT_COMMAND = {"start" : "Welcome message..", "txt2pdf" : "Create text PDF's"}

HELP_CMD = {
    "userHELP" : """[USER COMMAND MESSAGES]:\n
/start: To check whether bot is alive or not\n/cancel: To cancel current work
/delete: Clear image to PDF **queue**\n/txt2pdf: Text to PDF""",
    "adminHelp" : """\n\n\n[ADMIN COMMAND MESSAGES]:\n
/send: To broadcast, PM message""",
    "footerHelp" : f"""\n\n\nSource-Code: [i π PDF]({str(settings.SOURCE_CODE)})
Bot: @complete_pdf_bot π\n[Support Channel]({settings.OWNED_CHANNEL})""",
    "CB" : {"β οΈ CLOSE β οΈ" : "close|all"}
}

STATUS_MSG = {
    "HOME" : "`Now, select any option below to get current STATUS π±.. `",
    "_HOME" : {
        "π β SERVER β π" : "nabilanavab", "πΆ STORAGE πΆ" : "status|server",
        "π₯₯ DATABASE π₯₯" : "status|db", "π β GET LIST β π": "nabilanavab",
        "π ADMIN π" : "status|admin", "π€ USERS π€" : "status|users",
        "Β« BACK Β«" : "Home|A"
    },
    "DB" : """π DATABASE :\n\n**β Database Users :** `{}` π\n**β Database Chats :** `{}` π""",
    "SERVER" : """**β Total Space     :** `{}`
**β Used Space     :** `{}({}%)`\n**β Free Space      :** `{}`
**β CPU Usage      :** `{}`%\n**β RAM Usage     :** `{}`%
**β Current Work  :** `{}`\n**β Message Id     :** `{}`""",
    "BACK" : {"Β« BACK Β«" : "status|home"}, "ADMIN" : "**Total ADMIN:** __{}__\n",
    "USERS" : "Users saved In DB Are:\n\n", "NO_DB" : "No dataBASE set Yet π©"
}

feedbackMsg = f"[Write a FEEDBACK π]({settings.FEEDBACK})"

# GROUP WELCOME MESSAGE
HomeG = {
    "HomeA" : """Hello There.! π\nI'm new here {message.chat.title}\n
Let me introduce myself..\nMy Name is **iLovePDF,** and I can help you to do **many
things** with @telegram PDF files.\n\nThanks @nabilanavab for this AWESOME Bot π""",
    "HomeACB" : {
        "π€  BOT OWNER π€ ": f"https://telegram.dog/{settings.OWNER_USERNAME}",
        "π‘οΈ UPDATE CHANNEL π‘οΈ": f"{settings.OWNED_CHANNEL}", "π SOURCE CODE π": f"{settings.SOURCE_CODE}"
    }
}

# BANNED USER UI
BAN = {
    "cbNotU" : "Message IS NOT for You.. π",
    "banCB" : {
        "Create your Own Bot": f"{settings.SOURCE_CODE}", "Tutorial": f"{settings.SOURCE_CODE}",
        "Update Channel": "https://telegram.dog/ilovepdf_bot"
    },
    "UCantUse" : """Hey {}\n\nFOR SOME REASON YOU CANT USE THIS BOT :(""",
    "UCantUseDB" : """Hey {}\n\nFOR SOME REASON YOU CANT USE THIS BOT :(\n\nREASON: {}""",
    "GroupCantUse" : """{} NEVER EXPECT A GOOD RESPONSE FROM ME\n
ADMINS RESTRICTED ME FROM WORKING HERE.. π€­""",
    "GroupCantUseDB" : """{} NEVER EXPECT A GOOD RESPONSE FROM ME\n
ADMINS RESTRICTED ME FROM WORKING HERE.. π€­\n\nREASON: {}""",
    "Force" : """Wait [{}](tg://user?id={})..!!\n
Due To The Huge Traffic Only **Channel Members** Can Use this Bot πΆ\n
This Means That You Need To **Join** The Below Mentioned Channel for Using Me!\n
Hit on `"β»οΈretryβ»οΈ"` after joining.. π""",
    "ForceCB" : {"π JOIN CHANNEL π" : "{}", "β»οΈ Refresh β»οΈ" : "refresh"},
    "Fool" : "ΰ΄΅ΰ΄Ώΰ΄³ΰ΄ΰ΅ΰ΄ΰ΄Ώΰ΄²ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅ΰ΄ΰ΄²ΰ΅ΰ΄²ΰ΅ ΰ΄ΰ΅ΰ΄ΰ΅ΰ΄ΰ΅.. π€­"
}

checkPdf = {
    "pg" : "`Number of Pages: β’{}β’` π",
    "pdf" : """`What should I do with this file.?`\n\nFile Name : `{}`\nFile Size : `{}`""",
    "pdfCB" : {
        "β­ METAΒ£ATA β­" : "metaData", "π³οΈ PREVIEW π³οΈ" : "preview",
        "πΌοΈ IMAGES πΌοΈ" : "pdf|img", "βοΈ TEXT βοΈ" : "pdf|txt",
        "π ENCRYPT π" : "work|encrypt", "π DECRYPT π" : "work|decrypt",
        "ποΈ COMPRESS ποΈ" : "work|compress", "π€Έ ROTATE π€Έ" : "pdf|rotate",
        "βοΈ SPLIT βοΈ" : "pdf|split", "π§¬ MERGE π§¬" : "merge", "β’οΈ STAMP β’οΈ" : "pdf|stp",
        "βοΈ RENAME βοΈ" : "work|rename", "π OCR π" : "work|ocr",
         "π₯· A4 FORMAT π₯·" : "work|format", "π« CLOSE π«" : "close|all"
    },
    "error" : """__I can't do anything with this file.__ π\n\nπ  `CODEC ERROR`  π""",
    "errorCB" : {"β ERROR IN CODEC β" : "error", "πΈ CLOSE πΈ" : "close|all"},
    "encrypt" : """`FILE IS ENCRYPTED` π\n\nFile Name: `{}`\nFile Size: `{}`""",
    "encryptCB" : {"π DECRYPT π" : "work|decrypt"}
}

PROGRESS = {
    "progress" : """**\nDone β : **{0}/{1}\n**Speed π:** {2}/s\n**Estimated Time β³:** {3}""",
    "dlImage" : "`Downloading your Image..β³`", "upFile" : "`Started Uploading..`π€",
    "dlFile" : "`Downloading your file..` π₯", "upFileCB" : {"π€ .. UPLOADING.. π€" : "nabilanavab"},
    "workInP" : "WORK IN PROGRESS.. π", "refresh" : {"β»οΈ Refresh β»οΈ" : "{}"},
    "takeTime" : """```βοΈ Work in Progress..`\n`It might take some time..```π""",
    "cbPRO_D" : ["π€ DOWNLOAD: {:.2f}% π€", "π― CANCEL π―"], "cbPRO_U" : ["π€ UPLOADED: {:.2f}% π€", "π― CANCEL π―"]
}

GENERATE = {
    "deleteQueue" : "`Queue deleted Successfully..`π€§", "noQueue" : "`No Queue found..`π²",
    "noImages" : "No image found.!! π", "getFileNm" : "Now Send Me a File Name π: ",
    "geting" : "File Name: `{}`\nPages: `{}`", "getingCB" : {"π GENERATING PDF.." : "nabilanavab"},
    "currDL" : "Downloaded {} Images π₯±"
}

document = {
    "refresh" : PROGRESS['refresh'], "inWork" : PROGRESS['workInP'], "reply" : checkPdf['pdf'],
    "replyCB" : checkPdf['pdfCB'], "download" : PROGRESS['dlFile'], "process" : "βοΈ Processing..",
    "takeTime" : PROGRESS['takeTime'], "upFile" : PROGRESS['upFile'], "dlImage" : PROGRESS['dlImage'],
    "big" : """Due to Overload, Owner limits {}mb for pdf files π
\n`please Send me a file less than {}mb Size` π""",
    "bigCB" : {"π Create 2Gb Support Bot π" : "https://github.com/nabilanavab/ilovepdf"},
    "imageAdded" : """`Added {} pages to your PDF..`π€\n\nfileName: `{}.pdf`""",
    "setHdImg" : """Now Image To PDF is in HD mode π""",
    "setDefault" : {"Β« Back to Default Quality Β«" : "close|hd"},
    "error" : """SOMETHING went WRONG.. π\n\nERROR: `{}`""",
    "noAPI" : "`Please add convert API.. π©\n\nstart Β» settings Β» api Β» add/change`",
    "useDOCKER" : "`File Not Supported, deploy bot using docker`",
    "fromFile" : "`Converted: {} to {}`", "unsupport" : "Unsupported file..π`",
    "generateRN" : {"GENERATE π" : "generate", "RENAME βοΈ" : "generateREN"},
    "generate" : {"GENERATE π" : "generate"}, "cancelCB" : {"β¨ Cancel β©" : "close|me"}
}

noHelp = f"`No one gonna help you` π"

split = {
    "inWork" : PROGRESS['workInP'], "cancelCB" : document['cancelCB'],
    "download" : PROGRESS['dlFile'], "exit" : "`Process Cancelled..` π",
    "button" : {
        "βοΈ PDF Β» SPLIT β" : "nabilanavab", "With In Range π¦" : "split|R",
        "Single Page π" : "split|S", "Β« BACK Β«" : "pdf"
    },
    "work" : ["Range", "Single"], "over" : "`5 attempts over.. Process cancelled..`π",
    "pyromodASK_1" : """__PDF Split Β» By Range\nNow, Enter the range (start:end) :__
\n/exit __to cancel__""",
    "completed" : "`Downloading Completed..` β",
    "error_1" : "`Syntax Error: justNeedStartAndEnd `πΆ",
    "error_2" : "`Syntax Error: errorInEndingPageNumber `πΆ",
    "error_3" : "`Syntax Error: errorInStartingPageNumber `πΆ",
    "error_4" : "`Syntax Error: pageNumberMustBeADigit` π§ ",
    "error_5" : "`Syntax Error: noEndingPageNumber Or notADigit` πΆ",
    "error_6" : "`Can't find any number..`π",
    "error_7" : "`Something went Wrong..`π", "error_8" : "`Enter Numbers less than {}..`π",
    "error_9" : "`1st Check Number of pages` π", "upload" : "βοΈ `Started Uploading..` π€"
}

pdf2IMG = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "uploadfile" : split["upload"],
    "toImage" : {
        "βοΈ PDF Β» IMAGES β" : "nabilanavab", "πΌ IMG πΌ" : "pdf|img|img",
        "π DOC π" : "pdf|img|doc", "π€ ZIP π€" : "pdf|img|zip",
        "π― TAR π―" : "pdf|img|tar","Β« BACK Β«" : "pdf" 
    },
    "imgRange" : {
        "βοΈ PDF Β» IMAGES Β» {} β" : "nabilanavab", "π ALL π" : "p2img|{}A",
        "π€§ RANGE π€§" : "p2img|{}R", "π PAGES π" : "p2img|{}S", "Β« BACK Β«" : "pdf|img"
    },
    "over" : "`5 attempt over.. Process canceled..`π",
    "pyromodASK_1" : """__Pdf - ImgβΊDoc Β» Pages:\nNow, Enter the range (start:end) :__
\n/exit __to cancel__""",
    "pyromodASK_2" : """"__Pdf - ImgβΊDoc Β» Pages:\nNow, Enter the Page Numbers seperated by__ (,) :
\n/exit __to cancel__""",
    "exit" : "`Process Canceled..` π",
    "error_1" : "`Syntax Error: justNeedStartAndEnd `πΆ",
    "error_2" : "`Syntax Error: errorInEndingPageNumber `πΆ",
    "error_3" : "`Syntax Error: errorInStartingPageNumber `πΆ",
    "error_4" : "`Syntax Error: pageNumberMustBeADigit` π§ ",
    "error_5" : "`Syntax Error: noEndingPageNumber Or notADigit` πΆ",
    "error_6" : "`Can't find any number..`π", "error_7" : "`Something went Wrong..`π",
    "error_8" : "`PDF only have {} pages` π©", "error_9" : "`1st Check Number of pages` π",
    "error_10" : "__Due to Some restrictions Bot Sends Only 50 pages as ZIP..__π",
    "total" : "`Total pages: {}..β³`", "upload" : "`Uploading: {}/{} pages.. π¬`",
    "current" : "`Converted: {}/{} pages.. π€`", "complete" : "`Uploading Completed.. `ποΈ",
    "canceledAT" : "`Canceled at {}/{} pages..` π", "cbAns" : "βοΈ okDA, Canceling.. ",
    "cancelCB" : {"π€ CANCEL π€" : "close|P2I"},     # EDITABLE: β
    "canceledCB" : {"π CANCELLED π" : "close|P2IDONE"},
    "completed" : {"π COMPLETED π" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "upload" : PROGRESS['upFile'],
    "load" : "__Due to Overload you can only merge 5 PDFs at a time__",
    "sizeLoad" : "`Due to Overload Bot Only Support %sMb PDFs..", # removing %s show error
    "pyromodASK" : """__MERGE pdfs Β» Total PDFs in queue: {}__

/exit __to cancel__
/merge __to merge__""",
    "exit" : "`Process Cancelled..` π", "total" : "`Total PDFs : {} π‘",
    "current" : "__Started Downloading PDF : {} π₯__", "cancel" : "`Merging Process Cancelled.. π`",
    "started" : "__Merging Started.. __ πͺ", "caption" : "`Merged PDF π`",
    "error" : "`May be File Encrypted..`\n\nReason: {}"
}

metaData = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "download" : PROGRESS['dlFile'],   # [β]
    "read" : "Please read this message again.. π₯΄"
}

preview = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "error" : document['error'],
    "download" : PROGRESS['dlFile'], "_" : "PDF only have {} pages π€\n\n",
    "__" : "PDF pages: {}\n\n", "total" : "`Total pages: {}..` π€",
    "album" : "`Preparing an Album..` π€Ή", "upload" : f"`Uploading: preview pages.. π¬`"
}

stamp = {
    "stamp" : {
        "βοΈ PDF Β» STAMP β" : "nabilanavab",
        "Not For Public Release π€§" : "pdf|stp|10",
        "For Public Release π₯±" : "pdf|stp|8",
        "Confidential π€«" : "pdf|stp|2", "Departmental π€" : "pdf|stp|3",
        "Experimental π¬" : "pdf|stp|4", "Expired π" : "pdf|stp|5",
        "Final π§" : "pdf|stp|6", "For Comment π―οΈ" : "pdf|stp|7",
        "Not Approved π" : "pdf|stp|9", "Approved π₯³" : "pdf|stp|0",
        "Sold β" : "pdf|stp|11", "Top Secret π·" : "pdf|stp|12",
        "Draft π" : "pdf|stp|13", "AsIs π€" : "pdf|stp|1",
        "Β« BACK Β«" : "pdf"
    },
    "stampA" : {
        "βοΈ PDF Β» STAMP Β» COLOR β" : "nabilanavab",
        "Red β€οΈ" : "spP|{}|r", "Blue π" : "spP|{}|b",
        "Green π" : "spP|{}|g", "Yellow π" : "spP|{}|c1",
        "Pink π" : "spP|{}|c2", "Hue π" : "spP|{}|c3",
        "White π€" : "spP|{}|c4", "Black π€" : "spP|{}|c5",
        "Β« Back Β«" : "pdf|stp"
    },
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "upload" : PROGRESS['upFile'],
    "stamping" : "`Started Stamping..` π ", "caption" : """stamped pdf\ncolor : `{}`\nannot : `{}`"""
}

work = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "takeTime" : PROGRESS['takeTime'],
    "upload" : PROGRESS['upFile'], "button" : document['cancelCB'],
    "rot360" : "You have some **big problem..π**", "ocrError" : "Owner Restricted ππ€",
    "largeNo" : "Send a PDF file less than 5 pages.. π",
    "pyromodASK_1" : """__PDF {} Β»\nNow, please enter the PASSWORD :__\n\n/exit __to cancel__""",
    "pyromodASK_2" : """__Rename PDF Β»\nNow, please enter the NEW NAME:__\n\n/exit __to cancel__""",
    "exit" : "`process canceled.. `π", "ren_caption" : "__New Name:__ `{}`", 
    "notENCRYPTED" : "`File is Not Encrypted..` π",
    "compress" : "βοΈ `Started Compressing.. π‘οΈ\nIt might take some time..`π",
    "decrypt" : "βοΈ `Started Decrypting.. π\nIt might take some time..`π",
    "encrypt" : "βοΈ `Started Encrypting.. π\nIt might take some time..`π",
    "ocr" : "βοΈ `Adding OCR Layer.. βοΈ\nIt might take some time..`π",
    "format" : "βοΈ `Started Formatting.. π€\nIt might take some time..`π",
    "rename" : "βοΈ `Renameing PDf.. βοΈ\nIt might take some time..`π",
    "rot" : "βοΈ `Rotating PDf.. π€Έ\nIt might take some time..`π",
    "pdfTxt" : "βοΈ `Extracting Text.. πΎ\nIt might take some time..`π",
    "fileNm" : "Old Filename: {}\nNew Filename: {}",
    "rotate" : {
        "βοΈ PDF Β» ROTATE β" : "nabilanavab", "90Β°" : "work|rot90", "180Β°" : "work|rot180",
        "270Β°" : "work|rot270", "360Β°" : "work|rot360", "Β« BACK Β«" : "pdf"
    },
    "txt" : {
        "βοΈ PDF Β» TXT β" : "nabilanavab", "π MESSAGE π" : "work|M", "π§Ύ TXT FILE π§Ύ" : "work|T",
        "π HTML π" : "work|H", "π JSON π" : "work|J", "Β« BACK Β«" : "pdf"
    }
}

PROCESS = {
    "ocr" : "OCR added", "decryptError" : "__Cannot Decrypt the file with__ `{}` πΈοΈ",
    "decrypted" : "__Decrypted File__", "encrypted" : "__Page Number__: {}\n__key__ π: ||{}||",
    "compressed" : """`Original Size : {}\nCompressed Size : {}\n\nRatio : {:.2f} %`""",
    "cantCompress" : "File Can't be Compressed More..π€",
    "pgNoError" : """__For Some Reason A4 FORMATTING Supports only for PDFs with less than 5 Pages__\n\nTotal Pages: {} β­""",
    "ocrError" : "`Already Have A Text Layer.. `π",
    "90" : "__Rotated 90Β°__", "180" : "__Rotated 180Β°__", "270" : "__Rotated 270Β°__",
    "formatted" : "A4 Formatted File", "M" : "β» Extracted {} Pages β»",
    "H" : "HTML File", "T" : "TXT File", "J" : "JSON File"
}

pdf2TXT = {
    "upload" : PROGRESS["upFile"], "exit" : split['exit'], "nothing" : "Nothing to create.. π",
    "TEXT" : "`Create PDF From Text Messages Β»`", "start" : "Started Converting txt to Pdf..π",
    "font_btn" : {
        "TXT@PDF Β» SET FONT" : "nabilanavab", "Times" : "pdf|font|t", "Courier" : "pdf|font|c", "Helvetica (Default)" : "pdf|font|h",
        "Symbol" : "pdf|font|s", "Zapfdingbats" : "pdf|font|z", "π« CLOSE π«" : "close|me"
    },
    "size_btn" : { "TXT@PDF Β» {} Β» SET SCALE" : "nabilanavab", "Portarate" : "t2p|{}|p", "Landscape" : "t2p|{}|l", "Β« Back Β«": "pdf|T2P"},
    "askT" : "__TEXT TO PDF Β» Now, please enter a TITLE:__\n\n/exit __to cancel__\n/skip __to skip__",
    "askC" : "__TEXT TO PDF Β» Now, please enter paragraph {}:__\n\n/exit __to cancel__\n/create __to create__"
}

URL = {
    "get" : {"π§­ Get PDF File π§­" : "getFile"}, "close" : HELP_CMD['CB'], "notPDF" : "`Not a PDF File",
    "error" : "π SOMETHING WENT WRONG π\n\nERROR: `{}`\n\nNB: In Groups, Bots Can Only fetch documents Send After Joining Group =)",
    "done" : "```Almost Done.. β\nNow, Started Uploading.. π€```", "_error_" : "send me any url or direct telegram pdf links",
    "openCB" : {"Open In Browser" : "{}"}, "_error" : "`Some Thing Went Wrong =(`\n\n`{}`",
    "_get" : "[Open Chat]({})\n\n**ABOUT CHAT β**\nChat Type   : {}\nChat Name : {}\nChat Usr    : @{}\n"
             "Chat ID        : {}\nDate : {}\n\n**ABOUT MEDIA β**\nMedia       : {}\nFile Name : {}\nFile Size   : {}\n\nFile Type : {}"
}

getFILE = {
    "inWork" : PROGRESS['workInP'], "big" : "Send PDF url less than {}mb", "wait" : "Wait.. Let me.. π",
    "dl" : {"π₯ ..DOWNLOADING.. π₯" : "nabilanavab"}, "up" : {"π€ ..UPLOADING..  π€" : "nabilanavab"},
    "complete" : {"π COMPLETED π" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "This feature is Under Development β·οΈ", "Error annenn paranjille.. then what.. π",
    "Process Canceled.. π", "File Not Encrypted.. π", "Nothing Official About it.. π", "π Completed.. π"
]

inline_query = {
    "TOP" : { "Now, Select Language β?·" : "nabilanavab" }, "capt" : "SET LANGUAGE βοΈ", "des" : "By: @nabilanavab β€"
}

# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
