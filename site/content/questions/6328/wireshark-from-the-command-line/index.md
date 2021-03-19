+++
type = "question"
title = "Wireshark from the command line"
description = '''We need to tracing at the same time every day until we can nail down a problem we are having with our system (which is intermittent). It is a machine with multiple interfaces but only one is involved in the problem. When we start up wireshark on the server and have it write to a file it locks up / d...'''
date = "2011-09-13T13:32:00Z"
lastmod = "2011-09-13T13:48:00Z"
weight = 6328
keywords = [ "line", "command", "file", "wireshark" ]
aliases = [ "/questions/6328" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark from the command line](/questions/6328/wireshark-from-the-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6328-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We need to tracing at the same time every day until we can nail down a problem we are having with our system (which is intermittent). It is a machine with multiple interfaces but only one is involved in the problem.</p><p>When we start up wireshark on the server and have it write to a file it locks up / dies after about 50 minutes. If I look at the memory on the box I can see that it climbs and climbs and climbs until there is no more memory for WS to grab.</p><p>Rather than try to fix wireshark we want to log on, run a batch file which will start wireshark for us, have it create files of 100MB each and just keep creating file after file until 45 minutes have passed, then it will shut down. (In the batch file it will then start up again but that is not the issue).</p><p>Currently I cannot get the app to create multiple files for X amount of time, here is the entire bat file, (below that is the line that starts the app):</p><p>**Note: this bat uses shorter times and smaller files to prove function before going for the full length:</p><pre><code>@echo on
set start=0
set /p end= Enter Number of times to loop, 6 loops of 10 minutes are 1 hour: 
:loop
if %start%==%end% goto stop
&quot;C:\Program Files\Wireshark\wireshark.exe&quot; -i \Device\NPF_{D6FB4DD7-AEBF-49B5-9409-6421DC62BC1F} -a duration:600 -b filesize:100 -w C:\TempWireShark\Results\IVR1.cap -k -Q
set /a start=%start%+1
goto loop
:stop</code></pre><p>this is my command line currently: <code> C:\Program Files\Wireshark\wireshark.exe" -i \Device\NPF_{D6FB4DD7-AEBF-49B5-9409-6421DC62BC1F} -a duration:600 -b filesize:100 -w C:\Temp\WireShark\Results\IVR1.cap -k -Q</code>. It creates one file of the specified filesize (I have made it larger and smaller to test with) then shuts down. The bat will re-start WS but it only wrote one file and did not run creating more files until the time specified in the -a is reached.</p><p>Any ideas how to fix this?</p><p>We are using WS because we periodically check what is happening and examine some of the packets as they are coming in so we want to be able to see them.</p></div><div id="question-tags" class="tags-container tags">line command file wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '11, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/2c796223426577bdbfc1608dd4c40311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandy%20Murdock&#39;s gravatar image" /><p>Sandy Murdock<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandy Murdock has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Sep '11, 04:00</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-6328" class="comments-container"></div><div id="comment-tools-6328" class="comment-tools"></div><div class="clear"></div><div id="comment-6328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6329"></span>

<div id="answer-container-6329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6329-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory" title="OutOfMemory">Out of Memory</a> bug is well-known. You should use <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolsdumpcap.html" title="dumpcap">dumpcap</a> for this task, although you <em>could</em> use <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html" title="tshark">tshark</a> if you want to watch the capture while it's in progress. Automating the Wireshark GUI is not a readily scriptable task. You can always review files created with dumpcap or tshark with Wireshark post-mortem for further in-depth analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '11, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-6329" class="comments-container"><span id="6330"></span><div id="comment-6330" class="comment"><div id="post-6330-score" class="comment-score"></div><div class="comment-text"><p>Note that, as TShark dissects packets, its memory usage will grow over time if you're running it to capture for a very long time.</p></div><div id="comment-6330-info" class="comment-info"><span class="comment-age">(13 Sep '11, 14:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6329" class="comment-tools"></div><div class="clear"></div><div id="comment-6329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

