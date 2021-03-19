+++
type = "question"
title = "how to convert .dump format file to a text file in windows?"
description = '''i would like to convert a tcpdump file to a text file in windows.'''
date = "2014-06-26T09:40:00Z"
lastmod = "2014-06-26T09:47:00Z"
weight = 34228
keywords = [ "tcpdump" ]
aliases = [ "/questions/34228" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to convert .dump format file to a text file in windows?](/questions/34228/how-to-convert-dump-format-file-to-a-text-file-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34228-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i would like to convert a tcpdump file to a text file in windows.</p></div><div id="question-tags" class="tags-container tags">tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '14, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/2e0dea7eb4dcca39cde6601fbabaa907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="veni&#39;s gravatar image" /><p>veni<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="veni has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '14, 09:42</p></div></div><div id="comments-container-34228" class="comments-container"></div><div id="comment-tools-34228" class="comment-tools"></div><div class="clear"></div><div id="comment-34228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34230"></span>

<div id="answer-container-34230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34230-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Install Wireshark, start Wireshark, open the tcpdump file with Wireshark, then from the file menu, 'Export Packet Dissections | as "Plain Text" file ...', type in a filename and click Save.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '14, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34230" class="comments-container"><span id="34258"></span><div id="comment-34258" class="comment"><div id="post-34258-score" class="comment-score"></div><div class="comment-text"><p>thanks for the answer..but it crashes when i tried to open the file (5.44 GB). is there a way to solve this problem? please guide me because i am still new.</p></div><div id="comment-34258-info" class="comment-info"><span class="comment-age">(28 Jun '14, 00:10)</span> veni</div></div><span id="34259"></span><div id="comment-34259" class="comment"><div id="post-34259-score" class="comment-score">1</div><div class="comment-text"><p>Ah, you forgot to mention that you're dealing with a very large capture.</p><p>Have a look at the <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory</a> page on the wiki for tips, the <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">blog</a> entry from @Jasper discussing the issue.</p><p>Basically you can:</p><ol><li>Try using tshark.</li><li>Chop the file into smaller chunks with editcap and then process each chunk</li><li>Use a 64 bit OS and 64 bit Wireshark\tshark and buy more RAM.</li></ol></div><div id="comment-34259-info" class="comment-info"><span class="comment-age">(28 Jun '14, 04:33)</span> grahamb ♦</div></div></div><div id="comment-tools-34230" class="comment-tools"></div><div class="clear"></div><div id="comment-34230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

