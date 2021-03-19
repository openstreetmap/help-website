+++
type = "question"
title = "Trouble getting started with Windows build"
description = '''Hello, I believe I have followed the instructions to build Wireshark (Windows) but am stuck at the tool verification stage. When I run the following command: nmake -f Makefile.nmake verify_tools  I get the following output: C:&#92;DataRoot&#92;Projects&#92;Wireshark&amp;gt;nmake -f Makefile.nmake verify_tools  Micr...'''
date = "2014-11-23T16:11:00Z"
lastmod = "2014-11-24T00:52:00Z"
weight = 38084
keywords = [ "building", "verify_tools" ]
aliases = [ "/questions/38084" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Trouble getting started with Windows build](/questions/38084/trouble-getting-started-with-windows-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38084-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I believe I have followed the instructions to build Wireshark (Windows) but am stuck at the tool verification stage. When I run the following command:</p><pre><code>nmake -f Makefile.nmake verify_tools</code></pre><p>I get the following output:</p><pre><code>C:\DataRoot\Projects\Wireshark&gt;nmake -f Makefile.nmake verify_tools

Microsoft (R) Program Maintenance Utility Version 10.00.40219.01
Copyright (C) Microsoft Corporation.  All rights reserved.

&quot;C:/Program Files (x86)/Git/bin/bash.EXE&quot;: line 0: &quot;C:/Program Files (x86)/Git/b
in/bash.EXE&quot;: igncr: invalid option name
Can&#39;t find Qt. This will become a problem at some point.
&quot;C:/Program Files (x86)/Git/bin/bash.EXE&quot;: line 0: &quot;C:/Program Files (x86)/Git/b
in/bash.EXE&quot;: igncr: invalid option name
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Git\bin\bash.EXE&quot;&#39; : return
code &#39;0x2&#39;
Stop.

C:\DataRoot\Projects\Wireshark&gt;</code></pre><p>I hope someone can point me in the right direction to fix this. Thanks, Sid.</p></div><div id="question-tags" class="tags-container tags">building verify_tools</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '14, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/338cd4c75cfd2984c31cbc30708899d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid%20Price&#39;s gravatar image" /><p>sid Price<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid Price has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Nov '14, 00:53</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38084" class="comments-container"></div><div id="comment-tools-38084" class="comment-tools"></div><div class="clear"></div><div id="comment-38084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38092"></span>

<div id="answer-container-38092" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38092-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the issue is having "C:\Program Files (x86)\Git\bin on your PATH. My command prompt has ...\Git\cmd on the path which gives access to the git.exe which is all the Wireshark build requires, I can't remember if I did that manually, or (more likely) the chocolatey install of git did that.</p><p>config.nmake automagically adds ...\cygwin(64)\bin to the path for the build, so you'll just need to exclude ...\Git\bin from the path you use for your build command prompt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '14, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38092" class="comments-container"></div><div id="comment-tools-38092" class="comment-tools"></div><div class="clear"></div><div id="comment-38092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38086"></span>

<div id="answer-container-38086" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38086-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>&quot;C:/Program Files (x86)/Git/bin/bash.EXE&quot;: line 0: &quot;C:/Program Files (x86)/Git/b
in/bash.EXE&quot;: igncr: invalid option name</code></pre><p>The above indicates that Git bash is being used rather than cygwin bash.</p><p>I'm going to assume that you've installed cygwin.</p><p>Based upon the above, you'll need to adjust your PATH so that cygwin/bin appears before anything referring to Git.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '14, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-38086" class="comments-container"><span id="38105"></span><div id="comment-38105" class="comment"><div id="post-38105-score" class="comment-score"></div><div class="comment-text"><p>Excellent! For some reason cygwin\bin was not in my path so I added "cygwin64\bin" and now I am much closer. What I now see when I run the verify_tools "makefile" is:</p><p><code> C:\DataRoot\Projects\Wireshark&gt;nmake -f Makefile.nmake verify_tools</code></p><p><code></code></p><p><code>Microsoft (R) Program Maintenance Utility Version 10.00.40219.01 Copyright (C) Microsoft Corporation.  All rights reserved.</code></p><code></code><p>ERROR: The contents of 'C:\Wireshark-win32-libs\current_tag.txt' is (unknown). It should be 2014-10-01.</p></code><p><code>Can't find Qt. This will become a problem at some point. Checking for required applications:         cl: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bin/ cl         link: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/Bi n/link         nmake: /cygdrive/c/Program Files (x86)/Microsoft Visual Studio 10.0/VC/B in/nmake         bash: /usr/bin/bash         bison: /usr/bin/bison         flex: /usr/bin/flex         env: /usr/bin/env         grep: /usr/bin/grep         /usr/bin/find: /usr/bin/find         peflags: /usr/bin/peflags         perl: /usr/bin/perl         C:\Python27\python.exe: /cygdrive/c/Python27/python.exe         sed: /usr/bin/sed         unzip: /usr/bin/unzip         wget: /usr/bin/wget</code></p><p>Not finding "QT" is probably because I did not set that path in the "config.nmake" file.</p><p>I don't know about the error in file "current_tag.txt", both the Wireshark "libs" folders (win32 and win64) are empty. Is htis something I need to fix? Sid.</p></div><div id="comment-38105-info" class="comment-info"><span class="comment-age">(24 Nov '14, 07:28)</span> sid Price</div></div><span id="38106"></span><div id="comment-38106" class="comment"><div id="post-38106-score" class="comment-score"></div><div class="comment-text"><p>As I mentioned in my answer, config.nmake adds cygwin to your path, that's why there is no instruction to add it.</p><p>You are seeing the error about "current"tag" as you don't have the current versions of the 3rd party libraries. run <code>nmake -f makefile.nmake setup</code> to download and unpack them. See the Developers Guide 2.2.11 <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#_install_libraries">Install Libraries</a> step.</p><p>It also helps others if you format code or console output with the "&lt;code&gt;" "&lt;/code&gt;" tags to make the content more readable.</p></div><div id="comment-38106-info" class="comment-info"><span class="comment-age">(24 Nov '14, 08:08)</span> grahamb ♦</div></div><span id="38112"></span><div id="comment-38112" class="comment"><div id="post-38112-score" class="comment-score"></div><div class="comment-text"><p>grahamb, Many thanks for your help. running "make -f makefile.mak setup" is mentioned in the Developers' Guide AFTER the verify tools step, a note about the potential error I saw would be useful. So, I ran the "setup" makefile argument and it appeared to be running well until I got the following error:</p><p><code> Extracting '/cygdrive/c/Wireshark-win64-libs/nasm-2.09.08-win32.zip' into '/cygdrive/c/Wireshark-win64-libs/.' Verifying that the DLLs and EXEs in . are executable. 'C:\Program' is not recognized as an internal or external command, operable program or batch file. NMAKE : fatal error U1077: '"C:\Program Files (x86)\Git\bin\echo."' : return code '0x1' Stop.</code></p><p>This looks like a problem with a command in the makefile not being enclosed in quotes or maybe in a script, however I am not sure where to look for it. Sid.</p></div><div id="comment-38112-info" class="comment-info"><span class="comment-age">(24 Nov '14, 14:34)</span> sid Price</div></div><span id="38119"></span><div id="comment-38119" class="comment"><div id="post-38119-score" class="comment-score"></div><div class="comment-text"><p>Nope, looks like a problem with your environment having ..\Git\bin on the PATH before cygwin. The build script is picking up the git version of echo.</p></div><div id="comment-38119-info" class="comment-info"><span class="comment-age">(25 Nov '14, 03:09)</span> grahamb ♦</div></div><span id="38120"></span><div id="comment-38120" class="comment"><div id="post-38120-score" class="comment-score"></div><div class="comment-text"><p>grahamb, Thanks for the response, however that is not the case. Here is a dump of my "path" environmental variable:</p><p><code> PATH=c:\Windows\Microsoft.NET\Framework64\v4.0.30319; C:\Windows\Microsoft.NET\Framework\v4.0.30319;C:\Windows\Microsoft.NET\Framework64\v3.5; C:\Windows\Microsoft.NET\Framework\v3.5; ; C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE; C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\Tools; ; c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64; c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\VCPackages; ; C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\NETFX 4.0 Tools\x64; C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\x64; C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin; ; C:\Python27\; c:\cygwin64\bin; C:\Windows\system32; C:\Windows; C:\Windows\System32\Wbem; C:\Windows\System32\WindowsPowerShell\v1.0\; C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\; C:\Program Files\Microsoft SQL Server\110\Tools\Binn\; C:\Program Files\Microsoft Windows Performance Toolkit\; C:\Windows\System32\WindowsPowerShell\v1.0\; C:\Program Files (x86)\Git\cmd; C:\Program Files (x86)\Git\bin;C:\Chocolatey\bin;C:\Program Files (x86)\Git\cmd;</code></p><p>Note that the "cygwin" path is ahead of the "Git" entry. Since my error output appears to be referring to git there must be some other configuratkon that is wrong. Again, thanks, Sid</p></div><div id="comment-38120-info" class="comment-info"><span class="comment-age">(25 Nov '14, 07:15)</span> sid Price</div></div><span id="38121"></span><div id="comment-38121" class="comment not_top_scorer"><div id="post-38121-score" class="comment-score"></div><div class="comment-text"><p>grahamb, so I took your advice from elsewhere in this thread and removed the "git" paths form my PATH variable and the library installation now works. Thanks, Sid.</p></div><div id="comment-38121-info" class="comment-info"><span class="comment-age">(25 Nov '14, 07:38)</span> sid Price</div></div></div><div id="comment-tools-38086" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-38086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

