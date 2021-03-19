+++
type = "question"
title = "Can not open file over 2GB,there is an error ."
description = '''Hello all  When I open a pcap file about 2GB on Win2008 R2 (4 CPU 16GB RAM) ，the program crash and there is an error,I have tried wireshark 1.46 64bit &amp;amp; wireshark 1.50 64bit &amp;amp; wireshar 1.61rc1 64bit， Can you help me to fix it ,thank u very much! '''
date = "2011-05-22T03:05:00Z"
lastmod = "2011-05-22T07:14:00Z"
weight = 4171
keywords = [ "windows", "crash", "filesize", "error" ]
aliases = [ "/questions/4171" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can not open file over 2GB,there is an error .](/questions/4171/can-not-open-file-over-2gbthere-is-an-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4171-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all When I open a pcap file about 2GB on Win2008 R2 (4 CPU 16GB RAM) ，the program crash and there is an error,I have tried wireshark 1.46 64bit &amp; wireshark 1.50 64bit &amp; wireshar 1.61rc1 64bit， Can you help me to fix it ,thank u very much!</p><p><img src="http://www.imeefan.com/error.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">windows crash filesize error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '11, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/c3d9c23f8ea8b44dc13a230100d31e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cybluesky&#39;s gravatar image" /><p>cybluesky<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cybluesky has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>retagged 25 May '11, 21:46</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4171" class="comments-container"></div><div id="comment-tools-4171" class="comment-tools"></div><div class="clear"></div><div id="comment-4171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4172"></span>

<div id="answer-container-4172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4172-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your 16GB memory do not help since Wireshark has other limitations that might cause a crash when loading really huge trace files, see:</p><p><a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a></p><p>To get around that problem you might take a look at my answer here:</p><p><a href="http://ask.wireshark.org/questions/2947/dump-very-large-stream-capture-to-raw-file-wireshark-crashes">http://ask.wireshark.org/questions/2947/dump-very-large-stream-capture-to-raw-file-wireshark-crashes</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '11, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '11, 07:16</p></div></div><div id="comments-container-4172" class="comments-container"></div><div id="comment-tools-4172" class="comment-tools"></div><div class="clear"></div><div id="comment-4172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

