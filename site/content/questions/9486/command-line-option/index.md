+++
type = "question"
title = "Command line option"
description = '''I am running the following command line to capture large files but I would like the logs to be created in my log folder under the Wireshark folder dumpcap -b files:10000 -b filesize:10000 -w logs.pcap I have tried all sorts of option to make it create the file in that folder but nothing seems to wor...'''
date = "2012-03-12T04:15:00Z"
lastmod = "2012-03-12T04:51:00Z"
weight = 9486
keywords = [ "command-line" ]
aliases = [ "/questions/9486" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Command line option](/questions/9486/command-line-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9486-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running the following command line to capture large files but I would like the logs to be created in my log folder under the Wireshark folder</p><p>dumpcap -b files:10000 -b filesize:10000 -w logs.pcap</p><p>I have tried all sorts of option to make it create the file in that folder but nothing seems to work</p></div><div id="question-tags" class="tags-container tags">command-line</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '12, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/a5fcee2171e02fecda0dd841a8c740df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DirtRider&#39;s gravatar image" /><p>DirtRider<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DirtRider has no accepted answers">0%</span></p></div></div><div id="comments-container-9486" class="comments-container"></div><div id="comment-tools-9486" class="comment-tools"></div><div class="clear"></div><div id="comment-9486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9488"></span>

<div id="answer-container-9488" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9488-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I read your question correctly you want to have the files containing the captured data in a sub directory of your Wireshark installation directory? And I assume you're running Windows Vista or Windows 7? In that case you're not allowed to write to the "program files" folders since the UAC (User Access Control) settings probably denies access to it. You can disabled UAC, but I advise against it - times are dangerous, and Worms/BotNets/Viruses (Virii?) never sleep. Better rethink your capture strategy save the files to a folder that you are allowed to write to.</p><p>If I'm not assuming the correct OS environment you'll need to elaborate ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '12, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '12, 04:52</p></div></div><div id="comments-container-9488" class="comments-container"><span id="9491"></span><div id="comment-9491" class="comment"><div id="post-9491-score" class="comment-score"></div><div class="comment-text"><p>(Converted to a comment in keeping with the format of <a href="http://ask.wireshark.org">ask.wireshark.org</a>; Please see the FAQ).</p><p>Ok not to worry I set it as this and it now works, thanks for the help. Made up a small bat file to run</p><pre><code>ECHO OFF
MKDIR c:\\IPECS_Log
dumpcap -b files:10000 -b filesize:10000 -w C:\\IPECS_Log\\ipecs.pcap
ECHO ON</code></pre></div><div id="comment-9491-info" class="comment-info"><span class="comment-age">(12 Mar '12, 05:28)</span> DirtRider</div></div></div><div id="comment-tools-9488" class="comment-tools"></div><div class="clear"></div><div id="comment-9488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9487"></span>

<div id="answer-container-9487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9487-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What is your OS? On Windows putting the path in the -w option works for me:</p><p>dumpcap.exe -i 2 -b files:1000 -b filesize:1000 -w C:\temp\caps\log.pcap</p><p>I get multiple files in the the C:\temp\caps directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '12, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '12, 04:53</p></div></div><div id="comments-container-9487" class="comments-container"><span id="9489"></span><div id="comment-9489" class="comment"><div id="post-9489-score" class="comment-score"></div><div class="comment-text"><p>It will be both Win7 and XP, I cannot get it to make it in the correct folder</p><pre><code>dumpcap -b files:10000 -b filesize:10000 -w C:\\Program Files\\Wireshark\\ipecslog\\ipecs.pcap</code></pre><p>It now makes a file in the root of c:</p><p><code>Program_00001_20120312125745</code></p></div><div id="comment-9489-info" class="comment-info"><span class="comment-age">(12 Mar '12, 05:01)</span> DirtRider</div></div><span id="9490"></span><div id="comment-9490" class="comment"><div id="post-9490-score" class="comment-score"></div><div class="comment-text"><p>As Jasper mentioned in his answer you don't normally have write access to the Program Files directory on Win 7. Create a directory somewhere else, e.g. C:\temp\caps and try that.</p></div><div id="comment-9490-info" class="comment-info"><span class="comment-age">(12 Mar '12, 05:05)</span> grahamb ♦</div></div></div><div id="comment-tools-9487" class="comment-tools"></div><div class="clear"></div><div id="comment-9487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

