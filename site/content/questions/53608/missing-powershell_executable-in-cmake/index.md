+++
type = "question"
title = "(missing:  POWERSHELL_EXECUTABLE) in cmake"
description = '''Hi, i don&#x27;t understand why and how but without any reasons my wireshark solution for creating a new heuristic dissector fails building.  Build error is  Error 1 error MSB6006: &quot;cmd.exe&quot; exited with code 9009. C:&#92;Program Files (x86)&#92;MSBuild&#92;Microsoft.Cpp&#92;v4.0&#92;V120&#92;Microsoft.CppCommon.targets 170 5 co...'''
date = "2016-06-22T08:17:00Z"
lastmod = "2016-06-23T02:54:00Z"
weight = 53608
keywords = [ "cmake", "powershell" ]
aliases = [ "/questions/53608" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [(missing: POWERSHELL\_EXECUTABLE) in cmake](/questions/53608/missing-powershell_executable-in-cmake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i don't understand why and how but without any reasons my wireshark solution for creating a new heuristic dissector fails building. Build error is Error 1 error MSB6006: "cmd.exe" exited with code 9009. C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets 170 5 copy_data_files</p><p>Cmake is a bit weird because it says:</p><p>Generating build using CMake 3.5.2 -- Could NOT find POWERSHELL (missing: POWERSHELL_EXECUTABLE) . . . . -- The following REQUIRED packages have not been found:</p><ul><li>PowerShell</li></ul><p>-- Configuring done -- Generating done -- Build files have been written to: C:/Development/wsbuild64</p><p>I'm tilting. Suggestions? Thanks in advance</p></div><div id="question-tags" class="tags-container tags">cmake powershell</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '16, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/39c90bff22b6fa58db657d5af50c7899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenhero&#39;s gravatar image" /><p>kenhero<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenhero has no accepted answers">0%</span></p></div></div><div id="comments-container-53608" class="comments-container"><span id="53609"></span><div id="comment-53609" class="comment"><div id="post-53609-score" class="comment-score"></div><div class="comment-text"><p>What version of Windows ate you building on?</p></div><div id="comment-53609-info" class="comment-info"><span class="comment-age">(22 Jun '16, 08:52)</span> Anders ♦</div></div><span id="53610"></span><div id="comment-53610" class="comment"><div id="post-53610-score" class="comment-score"></div><div class="comment-text"><p>the version is windows 8</p></div><div id="comment-53610-info" class="comment-info"><span class="comment-age">(22 Jun '16, 08:59)</span> kenhero</div></div><span id="53611"></span><div id="comment-53611" class="comment"><div id="post-53611-score" class="comment-score"></div><div class="comment-text"><p>Could it be an environment issue?</p></div><div id="comment-53611-info" class="comment-info"><span class="comment-age">(22 Jun '16, 09:00)</span> kenhero</div></div><span id="53612"></span><div id="comment-53612" class="comment"><div id="post-53612-score" class="comment-score"></div><div class="comment-text"><p>The Output of VS2013 is :</p><p>"POWERSHELL_COMMAND-NOTFOUND" non è riconosciuto come comando interno o esterno,un programma eseguibile o un file batch. (italian language)</p></div><div id="comment-53612-info" class="comment-info"><span class="comment-age">(22 Jun '16, 09:02)</span> kenhero</div></div><span id="53625"></span><div id="comment-53625" class="comment not_top_scorer"><div id="post-53625-score" class="comment-score"></div><div class="comment-text"><p>What happens if you type 'powershell' in a standard Windows command line? Do you get power shell prompt?</p><p>If yes, what's the output of the '$PSVersionTable' command?</p><p>If no, do you have in your PATH environment variable "C:/Windows/System32/WindowsPowerShell/v1.0/"? Does this folder even exist on your machine?</p></div><div id="comment-53625-info" class="comment-info"><span class="comment-age">(23 Jun '16, 01:54)</span> Pascal Quantin</div></div><span id="53805"></span><div id="comment-53805" class="comment not_top_scorer"><div id="post-53805-score" class="comment-score"></div><div class="comment-text"><p>omg i try to compile my wireshark dissector on my home pc and i still have powershell issue. is it normal this?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/powershell2.png" alt="alt text" /></p><pre><code>-- Generating build using CMake 3.5.2
-- Could NOT find POWERSHELL (missing:  POWERSHELL_EXECUTABLE) 
-- Building for win64 using Visual Studio 12 2013 Win64
-- No custom file found in C:/development2/wireshark
-- Configuration types: Debug;Release;MinSizeRel;RelWithDebInfo
-- CMAKE_C_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO: /MD /Zi /O2 /Ob1 /D NDEBUG
-- V: 2.1.1-git, MaV: 2, MiV: 1, PL: 1, EV: -git.
-- Checking for c-compiler flag: /MP
-- Checking for c-compiler flag: /Zo
-- Checking for c-compiler flag: /w34295 /w34189
-- Checking for c++-compiler flag: /MP
-- Checking for c++-compiler flag: /Zo
-- Checking for c++-compiler flag: /w34295 /w34189
-- Packagelist: AIRPCAP;CAP;CARES;GCRYPT;GEOIP;GLIB2;GMODULE2;GNUTLS;GTHREAD2;GTK2;Gettext;Git;KERBEROS;LEX;LIBSSH;LUA;M;PCAP;POD;PORTAUDIO;Perl;PythonInterp;Qt5Core;Qt5LinguistTools;Qt5Multimedia;Qt5PrintSupport;Qt5Svg;Qt5Widgets;Qt5WinExtras;SBC;SED;SETCAP;SH;SMI;WINSPARKLE;YACC;YAPP;ZLIB
-- Could NOT find AIRPCAP (missing:  AIRPCAP_INCLUDE_DIR AIRPCAP_LIBRARY) 
-- AIRPCAP NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;libcap&#39;
-- Could NOT find CAP (missing:  CAP_LIBRARY CAP_INCLUDE_DIR) 
-- CAP NOT FOUND
-- Could NOT find CARES (missing:  CARES_LIBRARY CARES_INCLUDE_DIR) 
-- CARES NOT FOUND
-- Could NOT find GCRYPT (missing:  GCRYPT_LIBRARY GCRYPT_INCLUDE_DIR) (Required is at least version &quot;1.4.2&quot;)
-- GCRYPT NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;geoip&#39;
-- Could NOT find GEOIP (missing:  GEOIP_LIBRARY GEOIP_INCLUDE_DIR) 
-- GEOIP NOT FOUND
-- Could NOT find PkgConfig (missing:  PKG_CONFIG_EXECUTABLE) 
-- Checking for one of the modules &#39;glib-2.0&gt;=2.14.0&#39;
-- Configuring incomplete, errors occurred!</code></pre></div><div id="comment-53805-info" class="comment-info"><span class="comment-age">(04 Jul '16, 07:17)</span> kenhero</div></div><span id="53806"></span><div id="comment-53806" class="comment not_top_scorer"><div id="post-53806-score" class="comment-score"></div><div class="comment-text"><p>The instruction from @Pascal Quantin to type <code>$PSversionTable</code> was to be run <strong>in</strong> a PowerShell prompt.</p><p>It looks as though Powershell isn't installed\enabled on that system.</p><p>Note that PowerShell is installed and enabled by default in Windows &gt;= Vista. Someone must have manually disabled it on your systems.</p></div><div id="comment-53806-info" class="comment-info"><span class="comment-age">(04 Jul '16, 07:47)</span> grahamb ♦</div></div><span id="53807"></span><div id="comment-53807" class="comment not_top_scorer"><div id="post-53807-score" class="comment-score"></div><div class="comment-text"><p>what should i do?</p></div><div id="comment-53807-info" class="comment-info"><span class="comment-age">(04 Jul '16, 08:09)</span> kenhero</div></div><span id="53808"></span><div id="comment-53808" class="comment not_top_scorer"><div id="post-53808-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/powershell3.png" alt="alt text" /></p><p>it seems it's installed</p></div><div id="comment-53808-info" class="comment-info"><span class="comment-age">(04 Jul '16, 08:11)</span> kenhero</div></div><span id="53810"></span><div id="comment-53810" class="comment not_top_scorer"><div id="post-53810-score" class="comment-score"></div><div class="comment-text"><p>CMake expects Powershell.exe to be on your path, usually with something such as <code>C:\WINDOWS\System32\WindowsPowerShell\v1.0\</code>. Is it on your path?</p></div><div id="comment-53810-info" class="comment-info"><span class="comment-age">(04 Jul '16, 09:42)</span> grahamb ♦</div></div><span id="53811"></span><div id="comment-53811" class="comment not_top_scorer"><div id="post-53811-score" class="comment-score"></div><div class="comment-text"><p>yes! Is it possible a wrong git installation?</p></div><div id="comment-53811-info" class="comment-info"><span class="comment-age">(04 Jul '16, 09:54)</span> kenhero</div></div><span id="53812"></span><div id="comment-53812" class="comment not_top_scorer"><div id="post-53812-score" class="comment-score"></div><div class="comment-text"><p>i found this on cmakecache.txt</p><p>//Command suitable for running PowerShell scripts. POWERSHELL_COMMAND:STRING=POWERSHELL_COMMAND-NOTFOUND</p><p>//PowerShell command POWERSHELL_EXECUTABLE:FILEPATH=POWERSHELL_EXECUTABLE-NOTFOUND</p></div><div id="comment-53812-info" class="comment-info"><span class="comment-age">(04 Jul '16, 10:03)</span> kenhero</div></div><span id="53813"></span><div id="comment-53813" class="comment not_top_scorer"><div id="post-53813-score" class="comment-score"></div><div class="comment-text"><p>Unlikely to be git. In your build directory, in the file CMakeCache.txt, what is recorded for the lines beginning with:</p><pre><code>POWERSHELL_COMMAND:STRING=
POWERSHELL_EXECUTABLE:FILEPATH=</code></pre></div><div id="comment-53813-info" class="comment-info"><span class="comment-age">(04 Jul '16, 10:04)</span> grahamb ♦</div></div><span id="53814"></span><div id="comment-53814" class="comment not_top_scorer"><div id="post-53814-score" class="comment-score"></div><div class="comment-text"><p>i solved ,error was on cmakechache.txt but i don't understand why</p></div><div id="comment-53814-info" class="comment-info"><span class="comment-age">(04 Jul '16, 10:54)</span> kenhero</div></div><span id="53815"></span><div id="comment-53815" class="comment not_top_scorer"><div id="post-53815-score" class="comment-score"></div><div class="comment-text"><p>What was the error?</p></div><div id="comment-53815-info" class="comment-info"><span class="comment-age">(04 Jul '16, 11:23)</span> grahamb ♦</div></div><span id="53816"></span><div id="comment-53816" class="comment not_top_scorer"><div id="post-53816-score" class="comment-score"></div><div class="comment-text"><p>In cmakecache.txt i have replaced</p><p>//Command suitable for running PowerShell scripts. POWERSHELL_COMMAND:STRING=POWERSHELL_COMMAND-NOTFOUND</p><p>//PowerShell command POWERSHELL_EXECUTABLE:FILEPATH=POWERSHELL_EXECUTABLE-NOTFOUND</p><p>with :</p><p>//Command suitable for running PowerShell scripts. POWERSHELL_COMMAND:STRING=C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe;-NoProfile;-NonInteractive;-executionpolicy;bypass;.</p><p>//PowerShell command POWERSHELL_EXECUTABLE:FILEPATH=C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe</p><p>found on my 32bit cmakecache.txt version . The point is :why there were POWERSHELL_COMMAND-NOTFOUND/POWERSHELL_EXECUTABLE-NOTFOUND ???</p></div><div id="comment-53816-info" class="comment-info"><span class="comment-age">(04 Jul '16, 11:47)</span> kenhero</div></div><span id="53817"></span><div id="comment-53817" class="comment"><div id="post-53817-score" class="comment-score">1</div><div class="comment-text"><p>The CMake module FindPowerShell.cmake (in the source tree in cmake\modules) locates PowerShell for the build. The module uses the standard CMake command <a href="https://cmake.org/cmake/help/v3.5/command/find_program.html">find_program()</a> looking for powershell.exe on the path. Yours is the first reported failure of this detection, so I think it's something local to your system.</p></div><div id="comment-53817-info" class="comment-info"><span class="comment-age">(04 Jul '16, 11:59)</span> grahamb ♦</div></div></div><div id="comment-tools-53608" class="comment-tools"><span class="comments-showing"> showing 5 of 17 </span> <a href="#" class="show-all-comments-link">show 12 more comments</a></div><div class="clear"></div><div id="comment-53608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53628"></span>

<div id="answer-container-53628" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53628-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ok,i solved. I had obv in path environment var the correct path and the version was until 4 but i solved going on windows control panel -&gt; program -&gt; enable/disable windows functionality and activate windows power shell there. Btw cmake actually has no error,build has the same error but i can debug my dissector on vs2013. Really weird issue</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '16, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/39c90bff22b6fa58db657d5af50c7899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenhero&#39;s gravatar image" /><p>kenhero<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenhero has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '16, 02:55</p></div></div><div id="comments-container-53628" class="comments-container"></div><div id="comment-tools-53628" class="comment-tools"></div><div class="clear"></div><div id="comment-53628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

