+++
type = "question"
title = "Fatal Error U1077 Cannot Find the Path Specified"
description = '''I&#x27;m building Wireshark for Windows 7 from source. I succeeded earlier this week, but ended up deleting my repository and cloning it again to get rid of all the changes from a bad attempt to install a custom plugin. However, now when I build something seems to have gone wrong. I&#x27;m not sure what could...'''
date = "2015-01-16T12:57:00Z"
lastmod = "2015-01-16T13:14:00Z"
weight = 39223
keywords = [ "windows", "u1077", "nmake", "wireshark" ]
aliases = [ "/questions/39223" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fatal Error U1077 Cannot Find the Path Specified](/questions/39223/fatal-error-u1077-cannot-find-the-path-specified)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39223-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm building Wireshark for Windows 7 from source. I succeeded earlier this week, but ended up deleting my repository and cloning it again to get rid of all the changes from a bad attempt to install a custom plugin. However, now when I build something seems to have gone wrong. I'm not sure what could have changed.</p><p>During the build, I get a U1077 fatal error saying that it can't find the path specified. I'm having trouble telling exactly which path they're talking about, as the printout is massive. If I'm reading it right, it starts happening at the wireshark-tap-register.c file? But I could be wrong.</p><p>This is the relevant portion of the log:</p><blockquote>moc_recent_file_status.cpp moc_sequence_diagram.cpp moc_sequence_dialog.cpp moc_simple_dialog.cpp moc_syntax_line_edit.cpp moc_time_shift_dialog.cpp moc_wireshark_application.cpp moc_wireshark_dialog.cpp cl -c -nologo -Zm200 -Zc:wchar_t /DWINPCAP_VERSION=4_1_3 /Zi /W3 /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600 /D_CRT_SECURE_NO_DEPRECATE /D_CRT _NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w3 4295 /w34189 /DNOMINMAX -GR -W3 -w34100 -w34189 -EHsc -DUNICODE -DWIN32 -DINET6 -DREENTRANT -DHAVE_PCAP_REMOTE -DHAVE_PCAP_SETSAMPLING -DQT_NO_DEBUG -DQT_MULTIM EDIAWIDGETS_LIB -DQT_PRINTSUPPORT_LIB -DQT_MULTIMEDIA_LIB -DQT_WINEXTRAS_LIB -DQ T_WIDGETS_LIB -DQT_NETWORK_LIB -DQT_GUI_LIB -DQT_CORE_LIB -DNDEBUG -I"..\.." -I" ..\..\wiretap" -I"..\..\..\Wireshark-win32-libs\gtk2\include\glib-2.0" -I"..\..\ ..\Wireshark-win32-libs\gtk2\lib\glib-2.0\include" -I"C:\Development\Wireshark-w in32-libs\gtk3\include\glib-2.0" -I"C:\Development\Wireshark-win32-libs\gtk3\lib \glib-2.0\include" -I"..\..\..\Wireshark-win32-libs\WpdPack\Include" -I"..\..\.. \Wireshark-win32-libs\AirPcap_Devpack_4_1_0_1622\Airpcap_Devpack\include" -I"..\ ..\..\Wireshark-win32-libs\gnutls-3.2.15-2.7-win32ws\include" -I"..\..\..\Wiresh ark-win32-libs\GeoIP-1.5.1-2-win32ws\include" -I"..\..\..\Wireshark-win32-libs\z lib125\include" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include" -I"..\..\..\..\Qt \5.3\msvc2010_opengl\include\QtMultimediaWidgets" -I"..\..\..\..\Qt\5.3\msvc2010 _opengl\include\QtPrintSupport" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include\Qt Multimedia" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include\QtWinExtras" -I"..\..\ ..\..\Qt\5.3\msvc2010_opengl\include\QtWidgets" -I"..\..\..\..\Qt\5.3\msvc2010_o pengl\include\QtNetwork" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include\QtGui" -I "..\..\..\..\Qt\5.3\msvc2010_opengl\include\QtCore" -I"." -I"." -I"..\..\..\..\Q t\5.3\msvc2010_opengl\mkspecs\win32-msvc2010" -Fo @C:\Users\mihubbar\AppData\Loc al\Temp\nm33A0.tmp wireshark-qt.cpp cl -c -nologo -Zm200 -Zc:wchar_t /DWINPCAP_VERSION=4_1_3 /Zi /W3 /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600 /D_CRT_SECURE_NO_DEPRECATE /D_CRT _NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w3 4295 /w34189 -W3 -DUNICODE -DWIN32 -DINET6 -DREENTRANT -DHAVE_PCAP_REMOTE -DHAVE _PCAP_SETSAMPLING -DQT_NO_DEBUG -DQT_MULTIMEDIAWIDGETS_LIB -DQT_PRINTSUPPORT_LIB -DQT_MULTIMEDIA_LIB -DQT_WINEXTRAS_LIB -DQT_WIDGETS_LIB -DQT_NETWORK_LIB -DQT_G UI_LIB -DQT_CORE_LIB -DNDEBUG -I"..\.." -I"..\..\wiretap" -I"..\..\..\Wireshark- win32-libs\gtk2\include\glib-2.0" -I"..\..\..\Wireshark-win32-libs\gtk2\lib\glib -2.0\include" -I"C:\Development\Wireshark-win32-libs\gtk3\include\glib-2.0" -I"C :\Development\Wireshark-win32-libs\gtk3\lib\glib-2.0\include" -I"..\..\..\Wiresh ark-win32-libs\WpdPack\Include" -I"..\..\..\Wireshark-win32-libs\AirPcap_Devpack _4_1_0_1622\Airpcap_Devpack\include" -I"..\..\..\Wireshark-win32-libs\gnutls-3.2 .15-2.7-win32ws\include" -I"..\..\..\Wireshark-win32-libs\GeoIP-1.5.1-2-win32ws\ include" -I"..\..\..\Wireshark-win32-libs\zlib125\include" -I"..\..\..\..\Qt\5.3 \msvc2010_opengl\include" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include\QtMultim ediaWidgets" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include\QtPrintSupport" -I".. \..\..\..\Qt\5.3\msvc2010_opengl\include\QtMultimedia" -I"..\..\..\..\Qt\5.3\msv c2010_opengl\include\QtWinExtras" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include\ QtWidgets" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\include\QtNetwork" -I"..\..\..\ ..\Qt\5.3\msvc2010_opengl\include\QtGui" -I"..\..\..\..\Qt\5.3\msvc2010_opengl\i nclude\QtCore" -I"." -I"." -I"..\..\..\..\Qt\5.3\msvc2010_opengl\mkspecs\win32-m svc2010" -Fo @C:\Users\mihubbar\AppData\Local\Temp\nm4231.tmp wireshark-tap-register.c link /NOLOGO /DYNAMICBASE /NXCOMPAT /LARGEADDRESSAWARE /INCREMENTAL:NO / DEBUG /MACHINE:x86 /RELEASE /SafeSEH /FIXED:no /SUBSYSTEM:WINDOWS "/MANIFESTDEPE NDENCY:type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' p ublicKeyToken='6595b64144ccf1df' language='*' processorArchitecture='*'" /VERSIO N:1.992 /OUT:..\..\wireshark-qt-release\Wireshark.exe @C:\Users\mihubbar\AppData \Local\Temp\nm4435.tmp copy /y ..\..\epan\wslua\console.lua ..\..\wireshark-qt-release\ 1 file(s) copied. copy /y "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\redist\x 86\Microsoft.VC100.CRT\*.*" ..\..\wireshark-qt-release\ The system cannot find the path specified. NMAKE : fatal error U1077: 'copy' : return code '0x1' Stop. NMAKE : fatal error U1077: '"c:\Program Files (x86)\Microsoft Visual Studio 10.0 \VC\BIN\nmake.EXE"' : return code '0x2'</blockquote></div><div id="question-tags" class="tags-container tags">windows u1077 nmake wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '15, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p>mehubb985<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div></div><div id="comments-container-39223" class="comments-container"></div><div id="comment-tools-39223" class="comment-tools"></div><div class="clear"></div><div id="comment-39223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39225"></span>

<div id="answer-container-39225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39225-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you building with MSVC2010 Express Edition? If yes, edit config.nmake file and remove the # from the following line:</p><pre><code>#MSVC_VARIANT=MSVC2010EE</code></pre><p>Also download the MSVC2010 redistributable installer and copy it in your WIRESHARK_LIB_DIR folder</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '15, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '15, 13:25</p></div></div><div id="comments-container-39225" class="comments-container"></div><div id="comment-tools-39225" class="comment-tools"></div><div class="clear"></div><div id="comment-39225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

