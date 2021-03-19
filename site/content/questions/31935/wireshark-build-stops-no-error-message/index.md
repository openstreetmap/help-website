+++
type = "question"
title = "Wireshark build stops, no error message"
description = '''I was trying to build the 1.11.3 development release from source (not from git but from the tarball in Download section of main web page) on Windows 7. I followed instructions in Win32/64: Step-by-Step Guide. Verify_tools went well: Checking for required applications:  cl: /cygdrive/c/Program Files/...'''
date = "2014-04-17T10:57:00Z"
lastmod = "2014-04-17T14:16:00Z"
weight = 31935
keywords = [ "error", "build", "stops", "no" ]
aliases = [ "/questions/31935" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark build stops, no error message](/questions/31935/wireshark-build-stops-no-error-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to build the 1.11.3 development release from source (not from git but from the tarball in Download section of main web page) on Windows 7. I followed instructions in Win32/64: Step-by-Step Guide.</p><p>Verify_tools went well:</p><p>Checking for required applications: cl: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/BIN/cl link: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/BIN/link</p><pre><code>    nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 10.0/VC/BIN/nmake
    bash: /usr/bin/bash
    bison: /usr/bin/bison
    flex: /usr/bin/flex
    env: /usr/bin/env
    grep: /usr/bin/grep
    /usr/bin/find: /usr/bin/find
    peflags: /usr/bin/peflags
    perl: /usr/bin/perl
    C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
    C:\Qt\Qt5.2.1\5.2.1\msvc2010_opengl\bin\qmake: /cygdrive/c/Qt/Qt5.2.1/5.2.1/msvc2010_opengl/bin/qmake
    sed: /usr/bin/sed
    unzip: /usr/bin/unzip
    wget: /usr/bin/wget</code></pre><p>nmake setup and distclean went well.<br />
</p><p>Build started OK and went for a long time. Then I suddenly got the prompt back with no declaration of either a success or a failure. I went to C drive and there is no wireshark directory created.</p><p>Here is a bit of the screen right before I got the prompt back:</p><p>C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\pibs\UMTS-PIB C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\pibs\UMTS-PIB-orig 38 File(s) copied xcopy "C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\yang*.yan g" wireshark-gtk2\snmp\mibs /d C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\yang\ietf-inet-types.yang</p><p>C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\yang\ietf-netconf-monitor ing.yang C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\yang\ietf-yang-types.yang</p><p>3 File(s) copied xcopy "C:\Wireshark-win32-libs\GeoIP-1.5.1-2-win32ws\bin\libGeoip-1.dll" wireshark-gtk2 /d C:\Wireshark-win32-libs\GeoIP-1.5.1-2-win32ws\bin\libGeoIP-1.dll 1 File(s) copied xcopy "C:\Wireshark-win32-libs\WinSparkle-0.3-44-g2c8d9d3-win32ws\WinSpa rkle.dll" wireshark-gtk2 /d C:\Wireshark-win32-libs\WinSparkle-0.3-44-g2c8d9d3-win32ws\WinSparkle.dll 1 File(s) copied cd wireshark-gtk2 peflags --dynamicbase=true --nxcompat=true <em>.dll peflags --dynamicbase=true --nxcompat=true lib/gtk-2.0/</em>/engines/<em>.dll peflags --dynamicbase=true --nxcompat=true lib/gtk-2.0/modules/</em>.dll cd ..</p><p>What's going on?</p></div><div id="question-tags" class="tags-container tags">error build stops no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p>YXI<br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-31935" class="comments-container"><span id="31937"></span><div id="comment-31937" class="comment"><div id="post-31937-score" class="comment-score"></div><div class="comment-text"><p>If you rerun nmake you might get a clearer error indication.</p></div><div id="comment-31937-info" class="comment-info"><span class="comment-age">(17 Apr '14, 11:37)</span> Anders ♦</div></div><span id="31940"></span><div id="comment-31940" class="comment"><div id="post-31940-score" class="comment-score"></div><div class="comment-text"><p>Just ran again, got the same result:</p><pre><code>0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\lua5.2.3\lua52.dll&quot; wireshark-gtk2 /d
 0 File(s) copied
        if not exist wireshark-gtk2\snmp mkdir wireshark-gtk2\snmp
        if not exist wireshark-gtk2\snmp\mibs mkdir wireshark-gtk2\snmp\mibs
        xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\bin\libsmi-2.dll&quot; wireshark-gtk2 /d
 0 File(s) copied
            xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\mibs\iana\*&quot; wireshark-gtk2\snmp\mibs /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\mibs\ietf\*&quot; wireshark-gtk2\snmp\mibs /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\mibs\irtf\*&quot; wireshark-gtk2\snmp\mibs /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\mibs\site\*&quot; wireshark-gtk2\snmp\mibs /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\mibs\tubs\*&quot; wireshark-gtk2\snmp\mibs /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\pibs\*&quot; wireshark-gtk2\snmp\mibs /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\yang\*.yang&quot; wireshark-gtk2\snmp\mibs /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\GeoIP-1.5.1-2-win32ws\bin\libGeoip-1.dll&quot; wireshark-gtk2 /d
 0 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\WinSparkle-0.3-44-g2c8d9d3-win32ws\WinSparkle.dll&quot; wireshark-gtk2 /d
 0 File(s) copied
        cd wireshark-gtk2
        peflags --dynamicbase=true --nxcompat=true *.dll
        peflags --dynamicbase=true --nxcompat=true lib/gtk-2.0/*/engines/*.dll
        peflags --dynamicbase=true --nxcompat=true lib/gtk-2.0/modules/*.dll
        cd ..</code></pre></div><div id="comment-31940-info" class="comment-info"><span class="comment-age">(17 Apr '14, 12:09)</span> YXI</div></div><span id="31941"></span><div id="comment-31941" class="comment"><div id="post-31941-score" class="comment-score"></div><div class="comment-text"><p>Maybe this build is not supposed to use nmake. I think it has both GTK+ and Qt, maybe this is beyond the ability of the nmake file in there? Well, I deleted QT5_BASE_DIR environmental variable and re-setup and rebuild, and I got premature build termination with no error again. Although this time it stopped at a different point.</p><pre><code> C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\share\yang\ietf-yang-types.yang
 3 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\GeoIP-1.5.1-2-win32ws\bin\libGeoip-1.dll&quot; wireshark-gtk2 /d
 C:\Wireshark-win32-libs\GeoIP-1.5.1-2-win32ws\bin\libGeoIP-1.dll
 1 File(s) copied
        xcopy &quot;C:\Wireshark-win32-libs\WinSparkle-0.3-44-g2c8d9d3-win32ws\WinSparkle.dll&quot; wireshark-gtk2 /d
 C:\Wireshark-win32-libs\WinSparkle-0.3-44-g2c8d9d3-win32ws\WinSparkle.dll
 1 File(s) copied
        cd wireshark-gtk2
        peflags --dynamicbase=true --nxcompat=true *.dll
        peflags --dynamicbase=true --nxcompat=true lib/gtk-2.0/*/engines/*.dll
        peflags --dynamicbase=true --nxcompat=true lib/gtk-2.0/modules/*.dll
        cd ..</code></pre></div><div id="comment-31941-info" class="comment-info"><span class="comment-age">(17 Apr '14, 12:11)</span> YXI</div></div><span id="31951"></span><div id="comment-31951" class="comment"><div id="post-31951-score" class="comment-score"></div><div class="comment-text"><p>OK, rebuild with Qt5_BASE_DIR defined. GTK+ executable is still good. See a wireshark-qt-release directory but no executable in it. My assumption is Qt version wireshark actually need one more step to build, as explained in README.qt.</p></div><div id="comment-31951-info" class="comment-info"><span class="comment-age">(17 Apr '14, 15:09)</span> YXI</div></div></div><div id="comment-tools-31935" class="comment-tools"></div><div class="clear"></div><div id="comment-31935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31947"></span>

<div id="answer-container-31947" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31947-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you really sure your compilation failed? Did you check the content of your wireshark-gtk2 subfolder?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-31947" class="comments-container"><span id="31948"></span><div id="comment-31948" class="comment"><div id="post-31948-score" class="comment-score"></div><div class="comment-text"><p>You are right!<br />
I was following the directions in the step by step guide and it says to check C:\wireshark\wireshark-gtk2 directory for the executable. I couldn't find it and since my build didn't say success I just assumed something went wrong. Now I went to the directory where the build was carried out, there it is the wireshark-gtk2 directory with the executable in it!<br />
Thank you so much!!<br />
Then my first build with Qt included worked too then. I will check.</p></div><div id="comment-31948-info" class="comment-info"><span class="comment-age">(17 Apr '14, 14:26)</span> YXI</div></div><span id="31961"></span><div id="comment-31961" class="comment"><div id="post-31961-score" class="comment-score"></div><div class="comment-text"><p>I've converted Pascal's comment to an answer as it seems to fit the bill. @YXI, can you accept the answer by clicking the checkmark icon on it for the benefit of others.</p></div><div id="comment-31961-info" class="comment-info"><span class="comment-age">(18 Apr '14, 01:46)</span> grahamb ♦</div></div></div><div id="comment-tools-31947" class="comment-tools"></div><div class="clear"></div><div id="comment-31947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

