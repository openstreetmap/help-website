+++
type = "question"
title = "Can&#x27;t execute /usr/bin/pod2html error in Wireshark-2.0.2 Build"
description = '''Hi Wireshark Version: 2.0.2, I tried building latest wireshark code on my Windows 7, MSVC2013 Compiler Text from for the above Error cd doc  &quot;C:&#92;Program Files (x86)&#92;Microsoft Visual Studio 12.0&#92;VC&#92;BIN&#92;nmake.exe&quot; /  -f Makefile.nmake  Microsoft (R) Program Maintenance Utility Version 12.00.21005.1 Co...'''
date = "2016-04-25T23:10:00Z"
lastmod = "2016-04-27T05:09:00Z"
weight = 51944
keywords = [ "build_error", "pod2html", "wireshark" ]
aliases = [ "/questions/51944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't execute /usr/bin/pod2html error in Wireshark-2.0.2 Build](/questions/51944/cant-execute-usrbinpod2html-error-in-wireshark-202-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51944-score" class="post-score" title="current number of votes">0</div><span id="post-51944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Wireshark Version: 2.0.2, I tried building latest wireshark code on my Windows 7, MSVC2013 Compiler</p><h2 id="text-from-for-the-above-error">Text from for the above Error</h2><pre><code>cd doc
    &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\nmake.exe&quot; /
                   -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 12.00.21005.1
Copyright (C) Microsoft Corporation.  All rights reserved.

        bash -o igncr pod2html   --title=&quot;The Wireshark Network Analyzer 2.0.2&quot;  -css=ws.css -noindex                                  wireshark.pod &gt; wireshark.html
Can&#39;t execute /usr/bin/pod2html.
NMAKE : fatal error U1077: &#39;bash&#39; : return code &#39;0x1d&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0
\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>Please Help.</p><p>Thanks Dinesh Sadu</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-pod2html" rel="tag" title="see questions tagged &#39;pod2html&#39;">pod2html</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '16, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/04334c27cb629065a13d61a61b611038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinesh%20Babu%20Sadu&#39;s gravatar image" /><p><span>Dinesh Babu ...</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinesh Babu Sadu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Apr '16, 23:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51944" class="comments-container"></div><div id="comment-tools-51944" class="comment-tools"></div><div class="clear"></div><div id="comment-51944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51947"></span>

<div id="answer-container-51947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51947-score" class="post-score" title="current number of votes">0</div><span id="post-51947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a duplicate of <a href="https://ask.wireshark.org/questions/7572/compile-error-in-windows">this</a> question which unfortunately wasn't resolved as the questioner didn't come back.</p><p>Does pod2html exist in the Cygwin install of /usr/bin?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '16, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51947" class="comments-container"><span id="51948"></span><div id="comment-51948" class="comment"><div id="post-51948-score" class="comment-score"></div><div class="comment-text"><p>I did changes to CYGWIN_PATH in config.nmake in Wireshark base code CYGWIN_PATH=D:\Cygwin-Cust\bin</p><p>Path: Pod2html file is present in “D:\Cygwin-Cust\bin” &lt;d:\\cygwin-cust\\bin\\pod2html&gt;</p></div><div id="comment-51948-info" class="comment-info"><span class="comment-age">(26 Apr '16, 00:28)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="51953"></span><div id="comment-51953" class="comment"><div id="post-51953-score" class="comment-score"></div><div class="comment-text"><p>And what happens if you temporarily add Cygwin to the path and try to execute the command, e.g.</p><pre><code>set PATH=%PATH%;D:\Cygwin-Cust\bin
bash -o igncr pod2html   --title=&quot;The Wireshark Network Analyzer 2.0.2&quot;  -css=ws.css -noindex wireshark.pod &gt; wireshark.html</code></pre><p>Note there are only two lines, the set and the bash, the display might wrap them.</p></div><div id="comment-51953-info" class="comment-info"><span class="comment-age">(26 Apr '16, 03:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51959"></span><div id="comment-51959" class="comment"><div id="post-51959-score" class="comment-score"></div><div class="comment-text"><p>Cygwin Path setup is done in System Environment Varaibles but even though i tried in setting path in command, but it didn't work I got the same error. Error: Can't execute /usr/bin/pod2html.</p><p>So i did two below changes in config.namke and build is sucessful</p><p>POD2MAN=$(SH) /usr/bin/pod2man</p><p>POD2HTML=$(SH) /usr/bin/pod2html</p></div><div id="comment-51959-info" class="comment-info"><span class="comment-age">(26 Apr '16, 05:42)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="51960"></span><div id="comment-51960" class="comment"><div id="post-51960-score" class="comment-score"></div><div class="comment-text"><p>The above command works as expected on my Build VM. As this is an infrequent issue I think there's something odd in your Cygwin setup.</p><p>What does the Cygwin mount command show when called form DOS (as you have Cygwin already on your path)? I get:</p><pre><code>c:\&gt;mount
C:/Cygwin/bin on /usr/bin type ntfs (binary,auto)
C:/Cygwin/lib on /usr/lib type ntfs (binary,auto)
C:/Cygwin on / type ntfs (binary,auto)
C: on /cygdrive/c type ntfs (binary,posix=0,user,noumount,auto)</code></pre></div><div id="comment-51960-info" class="comment-info"><span class="comment-age">(26 Apr '16, 06:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51962"></span><div id="comment-51962" class="comment"><div id="post-51962-score" class="comment-score"></div><div class="comment-text"><p>Please find as below what does Cygwin mount gave in my build.env</p><pre><code>E:\Packages\Software\Dinesh\wireshark-2.0.2&gt;mount

D:/Cygwin-Cust/bin on /usr/bin type ntfs (binary,auto)
D:/Cygwin-Cust/lib on /usr/lib type ntfs (binary,auto)
D:/Cygwin-Cust on / type ntfs (binary,auto)
C: on /cygdrive/c type ntfs (binary,posix=0,user,noumount,auto)
D: on /cygdrive/d type ntfs (binary,posix=0,user,noumount,auto)
E: on /cygdrive/e type ntfs (binary,posix=0,user,noumount,auto)</code></pre></div><div id="comment-51962-info" class="comment-info"><span class="comment-age">(26 Apr '16, 06:59)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="51964"></span><div id="comment-51964" class="comment not_top_scorer"><div id="post-51964-score" class="comment-score"></div><div class="comment-text"><p>OK, looks good, odd then that bash can't execute pod2html which is in the directory mounted as /usr/bin.</p><p>Try these lines from a command prompt:</p><pre><code>C:\&gt;bash

[email protected] /cygdrive/c
$ which pod2html

[email protected] /cygdrive/c
$ echo $PATH</code></pre></div><div id="comment-51964-info" class="comment-info"><span class="comment-age">(26 Apr '16, 07:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51987"></span><div id="comment-51987" class="comment not_top_scorer"><div id="post-51987-score" class="comment-score"></div><div class="comment-text"><p>Tried running bash command. Please find the below</p><pre><code>E:\Pac~\Soft~\Dinesh\wireshark-2.0.2&gt;bash 
bash-3.2# /cygdrive/c/ 
bash: /cygdrive/c/: is a directory 
bash-3.2# cd /cygdrive/c/ 
bash-3.2# which pod2html 
/usr/bin/pod2html 
bash-3.2# echo $PATH
{ /cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Common7/IDE/CommonExtensions/Microsoft/TestWindow:/cygdrive/c/Prg~Files (x86)/Microsoft SDKs/F#/3.1/Framework/v4.0/:/cygdrive/c/Prg~Files (x86)/MSBuild/12.0/bin:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Common7/IDE/:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/VC/BIN:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Common7/Tools:/cygdrive/c/Windows/Microsoft.NET/Framework/v4.0.30319:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/VC/VCPackages:/cygdrive/c/Prg~Files (x86)/HTML Help Workshop:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Team Tools/Performance Tools:/cygdrive/c/Prg~Files (x86)/Windows Kits/8.1/bin/x86:/cygdrive/c/Prg~Files (x86)/Microsoft SDKs/Windows/v8.1A/bin/NETFX 4.5.1 Tools/:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Common7/IDE/CommonExtensions/Microsoft/TestWindow:/cygdrive/c/Prg~Files (x86)/Microsoft SDKs/F#/3.1/Framework/v4.0/:/cygdrive/c/Prg~Files (x86)/MSBuild/12.0/bin:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Common7/IDE/:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/VC/BIN:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Common7/Tools:/cygdrive/c/Windows/Microsoft.NET/Framework/v4.0.30319:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/VC/VCPackages:/cygdrive/c/Prg~Files (x86)/Mic~Vis~Stud 12.0/Team Tools/Performance Tools:/cygdrive/c/Prg~Files (x86)/Windows Kits/8.1/bin/x86:/cygdrive/c/Prg~Files (x86)/Microsoft SDKs/Windows/v8.1A/bin/NETFX 4.5.1 Tools/:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0/:/cygdrive/c/Prg~Files/Intel/Intel(R) Management Engine Components/DAL:/cygdrive/c/Prg~Files/Intel/Intel(R) Management Engine Components/IPT:/cygdrive/c/Prg~Files (x86)/Intel/Intel(R) Management Engine Components/DAL:/cygdrive/c/Prg~Files (x86)/Intel/Intel(R) Management Engine Components/IPT:/cygdrive/c/Prg~Files (x86)/Windows Kits/8.1/Windows Performance Toolkit/:/cygdrive/c/Prg~Files/Microsoft SQL Server/110/Tools/Binn/:/cygdrive/c/Prg~Files (x86)/Microsoft SDKs/Windows/v7.1A/Include:/cygdrive/c/Prg~Files (x86)/Microsoft SDKs/Windows/v7.1A/Bin:/cygdrive/e/Packages/Software:/cygdrive/c/Prg~Files (x86)/Microsoft SDKs/Windows/v7.1A/Lib:/cygdrive/c/Windows/System32/WindowsPowerShell/v1.0:/usr/bin:/usr/include }</code></pre></div><div id="comment-51987-info" class="comment-info"><span class="comment-age">(27 Apr '16, 01:38)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="51990"></span><div id="comment-51990" class="comment not_top_scorer"><div id="post-51990-score" class="comment-score"></div><div class="comment-text"><p>Apart from the odd shortening of paths with "~" that all looks OK. pod2html is on the path which includes /usr/bin as the which command shows.</p><p>I'm at a loss why the nmake command fails to execute pod2html.</p></div><div id="comment-51990-info" class="comment-info"><span class="comment-age">(27 Apr '16, 02:15)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51991"></span><div id="comment-51991" class="comment not_top_scorer"><div id="post-51991-score" class="comment-score"></div><div class="comment-text"><p>Grahamb, Due to character constraint in Comment section, I did them shorten</p><p>Program Files = Prg~Files</p><p>Microsoft Visual Studio = Mic~Vis~Stud</p></div><div id="comment-51991-info" class="comment-info"><span class="comment-age">(27 Apr '16, 02:24)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="51994"></span><div id="comment-51994" class="comment not_top_scorer"><div id="post-51994-score" class="comment-score"></div><div class="comment-text"><p>OK, I was a bit confused by that.</p><p>So the issue is that from a DOS CMD prompt, you can't execute the pod2html command via bash.</p><p>Can you try <code>bash -o igncr pod2html --help</code> from your build command prompt?</p></div><div id="comment-51994-info" class="comment-info"><span class="comment-age">(27 Apr '16, 02:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51996"></span><div id="comment-51996" class="comment not_top_scorer"><div id="post-51996-score" class="comment-score"></div><div class="comment-text"><p>Tried</p><pre><code>E:\Packages\Software\Dinesh\wireshark-2.0.2&gt;bash -o igncr pod2html --help

Can&#39;t execute /usr/bin/pod2html.
but with command /usr/bin/pod2html it worked.</code></pre></div><div id="comment-51996-info" class="comment-info"><span class="comment-age">(27 Apr '16, 02:55)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="51998"></span><div id="comment-51998" class="comment not_top_scorer"><div id="post-51998-score" class="comment-score"></div><div class="comment-text"><p>Your installation of bash appears to be ignoring the path it has. When you supply the path then it works.</p><p>Just to rule out the fact that somehow we're picking up the wrong bash, what does <code>where bash</code> show?</p></div><div id="comment-51998-info" class="comment-info"><span class="comment-age">(27 Apr '16, 03:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="52002"></span><div id="comment-52002" class="comment not_top_scorer"><div id="post-52002-score" class="comment-score"></div><div class="comment-text"><h2 id="command-where-bash">Command Where Bash:</h2><pre><code>E:\Packages\Software\Dinesh\wireshark-2.0.2&gt;where bash
E:\Packages\Software\Dinesh\wireshark-2.0.2\bash
D:\Cygwin-Cust\bin\bash.exe</code></pre><p>It shows the correct path of Cygwin Bin Directory</p></div><div id="comment-52002-info" class="comment-info"><span class="comment-age">(27 Apr '16, 04:43)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="52005"></span><div id="comment-52005" class="comment not_top_scorer"><div id="post-52005-score" class="comment-score"></div><div class="comment-text"><p>I'm guessing it's a path issue of some sort, but I don't know what.</p><p>In your path you showed earlier, there are a lot of duplicate entries and none of the standard Windows directories, although I don't think that has anything to do with the problem.</p><p>I'm stumped, I can't think of what to look at next. Sorry about that.</p></div><div id="comment-52005-info" class="comment-info"><span class="comment-age">(27 Apr '16, 05:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51947" class="comment-tools"><span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a></div><div class="clear"></div><div id="comment-51947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

