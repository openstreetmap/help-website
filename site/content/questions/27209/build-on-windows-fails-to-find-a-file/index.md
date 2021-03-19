+++
type = "question"
title = "Build on Windows fails to find a file"
description = '''Hello, I&#x27;m trying to build Wireshark on a Windows 7 machine, but the build fails when I try to run the nmake -f Makefile.nmake all command. The error message is: sed -e s/@VERSION@/1.10.3kp/ -e s/@VERSION_MAJOR@/1/ -e s/@VERSION_MINOR@/10/ -e s/@VERSION_MICRO@/3/ -e &quot;s/@HAVE_C_ARES@/#define HAVE_C_A...'''
date = "2013-11-21T05:40:00Z"
lastmod = "2013-11-25T01:54:00Z"
weight = 27209
keywords = [ "windows7", "build", "error" ]
aliases = [ "/questions/27209" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Build on Windows fails to find a file](/questions/27209/build-on-windows-fails-to-find-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27209-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to build Wireshark on a Windows 7 machine, but the build fails when I try to run the nmake -f Makefile.nmake all command. The error message is:</p><pre><code>sed -e s/@[email protected]/1.10.3kp/  -e s/@[email protected]/1/  -e s/@[email protected]/10/  -e s/@[email protected]/3/  -e &quot;s/@[email protected]/#define HAVE_C_ARES 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBZ 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBPCAP 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_FINDALLDEVS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_DATALINK_NAME_TO_VAL 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_DATALINK_VAL_TO_NAME 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_DATALINK_VAL_TO_DESCRIPTION 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_REMOTE 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_REMOTE 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_OPEN 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_OPEN_DEAD 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_LIST_DATALINKS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_FREE_DATALINKS 1/&quot; -e &quot;s/@[email protected]/#define HAVE_PCAP_SET_DATALINK 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_PCAP_SETSAMPLING 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_BPF_IMAGE 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBGNUTLS 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBGCRYPT 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LUA1/&quot;  -e &quot;s/@[email protected]/#define HAVE_LUA 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_AIRPCAP 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBPORTAUDIO 1/&quot;  -e &quot;s/@[email protected]//&quot;  -e &quot;s/@[email protected]/#define HAVE_LIBSMI 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_GEOIP 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_GEOIP_V6 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_SOFTWARE_UPDATE 1/&quot;  -e &quot;s/@[email protected]/#define INET6 1/&quot;  -e &quot;s/@[email protected]/#define HAVE_NTDDNDIS_H 1/&quot;  -e &quot;s/@[email protected]/#define PCAP_NG_DEFAULT 1/&quot;  -e &quot;s/@[email protected]//&quot;  &lt; config.h.win32 &gt; config.h

The system cannot find the file specified.

NMAKE : fatal error U1077: &#39;sed&#39; : return code &#39;0x1&#39;
Stop.</code></pre><p>verify_tools and distclean work well, but now I'm unable to find what causes this problem. Which file is the one I'm missing? I have checked and the config.h.win32 is available and present in the directory I'm trying to build Wireshark.</p><p>My system is a 64-bit Windows 7 and I get this same error message whether I try to build a 32-bit or 64-bit version of Wireshark.</p></div><div id="question-tags" class="tags-container tags">windows7 build error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '13, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/fb67ff4db2597c29af7befc2fd6a9e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arttu%20Leinonen&#39;s gravatar image" /><p>Arttu Leinonen<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arttu Leinonen has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Nov '13, 04:48</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-27209" class="comments-container"><span id="27231"></span><div id="comment-27231" class="comment"><div id="post-27231-score" class="comment-score"></div><div class="comment-text"><p>Please post the output of verify_tools</p></div><div id="comment-27231-info" class="comment-info"><span class="comment-age">(21 Nov '13, 07:26)</span> Bill Meier ♦♦</div></div><span id="27256"></span><div id="comment-27256" class="comment"><div id="post-27256-score" class="comment-score"></div><div class="comment-text"><p>To my knowledge it follows what is usual:</p><p>C:\wiresharkdev&gt;nmake -f Makefile.nmake verify_tools<br />
</p><p>Microsoft (R) Program Maintenance Utility Version 10.00.40219.01<br />
Copyright (C) Microsoft Corporation. All rights reserved.<br />
</p><p>Checking for required applications:<br />
cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bin/cl<br />
link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bin/link<br />
nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bin/nmake<br />
bash: /usr/bin/bash<br />
bison: /usr/bin/bison<br />
flex: /usr/bin/flex<br />
env: /usr/bin/env<br />
grep: /usr/bin/grep<br />
/usr/bin/find: /usr/bin/find<br />
peflags: /usr/bin/peflags<br />
perl: /usr/bin/perl<br />
C:\Python27\python.exe: /cygdrive/c/Python27/python.exe<br />
sed: /usr/bin/sed<br />
unzip: /usr/bin/unzip<br />
wget: /usr/bin/wget<br />
<br />
I first ran into problems with unzip being found under TexLive, but I solved that by prepending the cygwin path instead of appending when I set the environment up.</p></div><div id="comment-27256-info" class="comment-info"><span class="comment-age">(21 Nov '13, 23:25)</span> Arttu Leinonen</div></div></div><div id="comment-tools-27209" class="comment-tools"></div><div class="clear"></div><div id="comment-27209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27333"></span>

<div id="answer-container-27333" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27333-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, I found the root cause of the problem.</p><p>At some point I had tried to ease my workflow by setting up command prompt to automatically change the directory to the one I needed. Of course I had forgotten this altogether, so when bash was running sed and tried to access config.h.win32, it could find it.</p><p>The problem was that the make process starts up many cmd processes and at some point the autorun commands were run which caused the working directory change so that the required file was nowhere to be found. Removing the autorun key from registry cleared up the problem.</p><p>So in the end this was a stupid mistake on my part. Sorry for the inconvenience to everybody.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '13, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/fb67ff4db2597c29af7befc2fd6a9e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arttu%20Leinonen&#39;s gravatar image" /><p>Arttu Leinonen<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arttu Leinonen has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-27333" class="comments-container"></div><div id="comment-tools-27333" class="comment-tools"></div><div class="clear"></div><div id="comment-27333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27232"></span>

<div id="answer-container-27232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27232-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer to a similar question (almost same error message)</p><blockquote><p><a href="http://ask.wireshark.org/questions/7991/nmake-fatal-error-u1077-sed-return-code-0x1">http://ask.wireshark.org/questions/7991/nmake-fatal-error-u1077-sed-return-code-0x1</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '13, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Nov '13, 07:34</p></div></div><div id="comments-container-27232" class="comments-container"><span id="27258"></span><div id="comment-27258" class="comment"><div id="post-27258-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately that question/answer was when sed wasn't being found properly. It did help solve a problem with bash finding a wrong version of unzip, but both cmd.exe and bash seem to find the sed-program as required.</p><p>It seems that the problem is that sed cannot find some file that it tries to find but as I'm able to see and if needed touch the config.h.win32 which to my understanding is the only file truly being used in that command, I don't know how to solve this.</p><p>Yours, Arttu</p></div><div id="comment-27258-info" class="comment-info"><span class="comment-age">(21 Nov '13, 23:32)</span> Arttu Leinonen</div></div><span id="27261"></span><div id="comment-27261" class="comment"><div id="post-27261-score" class="comment-score"></div><div class="comment-text"><p>O.K. please check:</p><ul><li>is there a config.h (generated by sed). If so: delete it and run nmake again</li><li>if there is no config.h, run sed manually (copy-paste from your question). What do you get?</li></ul><p>BTW: Do you have the standard windows cmd.exe or some 'enhancement tool' like 4DOS (or similar)?</p></div><div id="comment-27261-info" class="comment-info"><span class="comment-age">(22 Nov '13, 01:57)</span> Kurt Knochner ♦</div></div><span id="27263"></span><div id="comment-27263" class="comment"><div id="post-27263-score" class="comment-score"></div><div class="comment-text"><p>There wasn't a config.h file. I also tried creating an empty file and forcing make to regenerate it, but it didn't work.</p><p>Running the actual command straight off seems to work, as it generates a config.h file that seems to contain all the required parts, but now nmake is running to a different error about native-nmake.CMD not being a command, but that I believe I've seen as a question elsewhere, so I will try to find a solution to it.</p><p>Still a weird problem that invoking the command from the makefile fails, but invoking it outside works as it is supposed to.</p><p>P.S. Yes I have a native cmd.exe. At least it says it is cmd.exe and I don't remember installing anything that would supplant it.</p></div><div id="comment-27263-info" class="comment-info"><span class="comment-age">(22 Nov '13, 02:08)</span> Arttu Leinonen</div></div><span id="27265"></span><div id="comment-27265" class="comment"><div id="post-27265-score" class="comment-score"></div><div class="comment-text"><p>I still believe nmake does not find sed (for whatever reason).</p><p>Please try this: in Makefile.nmake replace the following line</p><pre><code>        sed -e s/@[email protected]/$(VERSION)/ \</code></pre><p>with</p><pre><code>        sed -xxx -e s/@[email protected]/$(VERSION)/ \</code></pre><p>then run nmake again. What is the error message?</p><p>If nmake finds sed, it should be a different error message/code (as sed does not know -xxx).</p><p>If it's the same error message/code, nmake does not find sed and probably other tools neither.</p></div><div id="comment-27265-info" class="comment-info"><span class="comment-age">(22 Nov '13, 02:19)</span> Kurt Knochner ♦</div></div><span id="27268"></span><div id="comment-27268" class="comment"><div id="post-27268-score" class="comment-score"></div><div class="comment-text"><p>I did that, and after first running distclean, to get rid of the config.h the error message did stay the same, with the added -xxx on the first row. It still complains about finding the file.</p><p>This would also be consistent with lemon compilation failing as it is unable to find the ../native-nmake.cmd or at least recognizing it as an executable.</p><p>Hummm...I think the next step would be reinstalling cygwin from scratch, if you do not have any better idea?</p></div><div id="comment-27268-info" class="comment-info"><span class="comment-age">(22 Nov '13, 02:33)</span> Arttu Leinonen</div></div><span id="27269"></span><div id="comment-27269" class="comment not_top_scorer"><div id="post-27269-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Hummm...I think the next step would be reinstalling cygwin from scratch, if you do not have any better idea?</p></blockquote><p>well, you could try to trace nmake with <a href="http://technet.microsoft.com/en-us/sysinternals/bb896653.aspx">process explorer</a> (set a filter on nmake.exe) to figure our where it looks for sed. However that output would be rather huge.</p></div><div id="comment-27269-info" class="comment-info"><span class="comment-age">(22 Nov '13, 02:36)</span> Kurt Knochner ♦</div></div><span id="27270"></span><div id="comment-27270" class="comment not_top_scorer"><div id="post-27270-score" class="comment-score"></div><div class="comment-text"><p>It seems that manually calling the correct sed executable with the correct command line does work, so I suspect some environment issue.</p><p>You also stated that you manually added cygwin to the path, that isn't normally necessary as config.nmake does that for you (look for <code># Construct the path</code>), although it does append cygwin, so any utils that are on the path will get picked up before cygwin.</p><p>Maybe you could try cleaning up your path in the command prompt you're using (remove cygwin and paths to other "bad" executables that get picked up) and try again?</p></div><div id="comment-27270-info" class="comment-info"><span class="comment-age">(22 Nov '13, 02:44)</span> grahamb ♦</div></div><span id="27271"></span><div id="comment-27271" class="comment not_top_scorer"><div id="post-27271-score" class="comment-score"></div><div class="comment-text"><p>Thank you Graham, by the way, for cleaning up my original question.</p><p>Actually I did it because it is mentioned as something that needs to be done in the Developer's Guide. I suspect that nmake verify_tools wouldn't be able to find the unix side tools without cygwin being added to the path before hand.</p><p>I'll look into cleaning up my path. I already uninstalled TexLive that had been first causing me some problems, but that did not help.</p><p>After running the toolchain setup that runs SetEnv.cmd and prepends cygwin and python27 to the path my PATH looks like:</p><p>C:\wiresharkdev&gt;echo %PATH%<br />
C:\windows\Microsoft.NET\Framework\v4.0.30319;C:\windows\Microsoft.NET\Framework\v3.5;;c:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE;c:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\Tools;;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\VCPackages;;C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\NETFX 4.0 Tools;C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin;;c:\cygwin\bin;c:\python27;C:\Program Files\Broadcom\Broadcom 802.11;;;C:\Python33\Lib\site-packages\PyQt4;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;;C:\Python33\;C:\Python33\Lib\;C:\windows\system32;C:\windows;C:\windows\System32\Wbem;C:\Program Files\WIDCOMM\Bluetooth Software\;C:\Program Files\WIDCOMM\Bluetooth Software\syswow64;C:\Program Files (x86)\Common Files\Roxio Shared\DLLShared\;C:\Program Files (x86)\Common Files\Roxio Shared\OEM\DLLShared\;C:\Program Files (x86)\Common Files\Roxio Shared\OEM\DLLShared\;C:\Program Files (x86)\Common Files\Roxio Shared\OEM\12.0\DLLShared\;C:\Program Files (x86)\Roxio\OEM\AudioCore\;C:\windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Hewlett-Packard\HP ProtectTools Security Manager\Bin\;C:\windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\Microsoft SQL Server\110\Tools\Binn\;c:\Program Files (x86)\Microsoft SQL Server\90\Tools\binn\;C:\Program Files (x86)\Intel\OpenCL SDK\3.0\bin\x86;C:\Program Files (x86)\Intel\OpenCL SDK\3.0\bin\x64;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Microsoft Windows Performance Toolkit\&lt;br&gt;</p><p>I think the python33 in the path could cause problems.</p></div><div id="comment-27271-info" class="comment-info"><span class="comment-age">(22 Nov '13, 04:08)</span> Arttu Leinonen</div></div><span id="27272"></span><div id="comment-27272" class="comment not_top_scorer"><div id="post-27272-score" class="comment-score"></div><div class="comment-text"><p>Well, that didn't really help.</p><p>With the PATH cleaned down to: C:\windows\Microsoft.NET\Framework\v4.0.30319;C:\windows\Microsoft.NET\Framework\v3.5;;c:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE;c:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\Tools;;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\VCPackages;;C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\NETFX 4.0 Tools;C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin;;c:\cygwin\bin;c:\python27;C:\Program Files\Broadcom\Broadcom 802.11;C:\windows\system32;C:\windows;C:\Program Files\WIDCOMM\Bluetooth Software\;C:\Program Files\WIDCOMM\Bluetooth Software\syswow64;C:\Program Files (x86)\Hewlett-Packard\HP ProtectTools Security Manager\Bin\;C:\Program Files\Microsoft SQL Server\110\Tools\Binn\;c:\Program Files (x86)\Microsoft SQL Server\90\Tools\binn\;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Microsoft Windows Performance Toolkit\</p><p>It still fails in the same point. Hmmm. I'll see if I'm able to get a virtual machine running to make a clean environment to build in. Otherwise I will move forward with uninstalling cygwin and reinstalling it without any additional components.</p></div><div id="comment-27272-info" class="comment-info"><span class="comment-age">(22 Nov '13, 04:21)</span> Arttu Leinonen</div></div><span id="27273"></span><div id="comment-27273" class="comment not_top_scorer"><div id="post-27273-score" class="comment-score"></div><div class="comment-text"><p>So, with a more readable layout:</p><pre><code>C:\windows\Microsoft.NET\Framework\v4.0.30319
C:\windows\Microsoft.NET\Framework\v3.5

c:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE
c:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\Tools

c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin
c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\VCPackages

C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\NETFX 4.0 Tools
C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin

c:\cygwin\bin
c:\python27
C:\Program Files\Broadcom\Broadcom 802.11

C:\Python33\Lib\site-packages\PyQt4
C:\Program Files (x86)\Intel\iCLS Client\
C:\Program Files\Intel\iCLS Client\

C:\Python33\
C:\Python33\Lib\
C:\windows\system32
C:\windows
C:\windows\System32\Wbem
C:\Program Files\WIDCOMM\Bluetooth Software\
C:\Program Files\WIDCOMM\Bluetooth Software\syswow64
C:\Program Files (x86)\Common Files\Roxio Shared\DLLShared\
C:\Program Files (x86)\Common Files\Roxio Shared\OEM\DLLShared\
C:\Program Files (x86)\Common Files\Roxio Shared\OEM\DLLShared\
C:\Program Files (x86)\Common Files\Roxio Shared\OEM\12.0\DLLShared\
C:\Program Files (x86)\Roxio\OEM\AudioCore\
C:\windows\System32\WindowsPowerShell\v1.0\
C:\Program Files (x86)\Hewlett-Packard\HP ProtectTools Security Manager\Bin\
C:\windows\System32\WindowsPowerShell\v1.0\
C:\Program Files\Microsoft SQL Server\110\Tools\Binn\
c:\Program Files (x86)\Microsoft SQL Server\90\Tools\binn\
C:\Program Files (x86)\Intel\OpenCL SDK\3.0\bin\x86
C:\Program Files (x86)\Intel\OpenCL SDK\3.0\bin\x64
C:\Program Files\Intel\Intel(R) Management Engine Components\DAL
C:\Program Files\Intel\Intel(R) Management Engine Components\IPT
C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL
C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT
C:\Program Files\Microsoft Windows Performance Toolkit</code></pre><p>Note you can use <code>($env:path).split(";")</code> in Powershell to "pretty-print" the path, I'm sure there is some cygwin awk equivalent.</p></div><div id="comment-27273-info" class="comment-info"><span class="comment-age">(22 Nov '13, 04:38)</span> grahamb ♦</div></div><span id="27274"></span><div id="comment-27274" class="comment not_top_scorer"><div id="post-27274-score" class="comment-score"></div><div class="comment-text"><p>Apart from the Python 3 entries, nothing really stands out. We can't use Python 3 in the build yet, so best make sure it's just not present.</p><p>My path (XP 32 bit) is pretty identical up until your entry for cygwin, and then all the other paths you have your installed stuff. My build env is XP in a VM that's only used for Wireshark.</p><p>My path:</p><p><code>C:\WINDOWS\Microsoft.NET\Framework\v4.0.30319 C:\WINDOWS\Microsoft.NET\Framework\v3.5</code></p><p><code></code></p><p><code>C:\Program Files\Microsoft Visual Studio 10.0\Common7\IDE C:\Program Files\Microsoft Visual Studio 10.0\Common7\Tools</code></p><code></code><p>C:\Program Files\Microsoft Visual Studio 10.0\VC\Bin C:\Program Files\Microsoft Visual Studio 10.0\VC\Bin\VCPackages</p><p>C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\NETFX 4.0 Tools C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin</p></code><p><code>C:\WINDOWS\system32 C:\WINDOWS C:\WINDOWS\System32\Wbem C:\WINDOWS\system32\WindowsPowerShell\v1.0 C:\Program Files\CMake 2.8\bin C:\Program Files\TortoiseSVN\bin</code></p><p>FWIW, I would still try to pare your path down first.</p></div><div id="comment-27274-info" class="comment-info"><span class="comment-age">(22 Nov '13, 04:47)</span> grahamb ♦</div></div></div><div id="comment-tools-27232" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-27232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

