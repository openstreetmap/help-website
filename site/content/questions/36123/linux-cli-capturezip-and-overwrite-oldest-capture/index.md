+++
type = "question"
title = "Linux cli capture,zip and overwrite oldest capture"
description = '''I am attempting to capture packets, gzip and overwritten oldest file when about to run of disk space: tcpdump -ni eth0 -G 180 -w &#x27;trace_%Y-%m-%d_%H:%M:%S.pcap&#x27; -z gzip The one liner is capturing packets and zipping them but I am unable to setup a script to overwriting part.'''
date = "2014-09-09T13:04:00Z"
lastmod = "2014-09-10T03:50:00Z"
weight = 36123
keywords = [ "rotating", "gzip", "capturing" ]
aliases = [ "/questions/36123" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Linux cli capture,zip and overwrite oldest capture](/questions/36123/linux-cli-capturezip-and-overwrite-oldest-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36123-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to capture packets, gzip and overwritten oldest file when about to run of disk space:</p><p>tcpdump -ni eth0 -G 180 -w 'trace_%Y-%m-%d_%H:%M:%S.pcap' -z gzip</p><p>The one liner is capturing packets and zipping them but I am unable to setup a script to overwriting part.</p></div><div id="question-tags" class="tags-container tags">rotating gzip capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '14, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/4160a58d396514245632f8e8d286edd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ksudi&#39;s gravatar image" /><p>ksudi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ksudi has no accepted answers">0%</span></p></div></div><div id="comments-container-36123" class="comments-container"></div><div id="comment-tools-36123" class="comment-tools"></div><div class="clear"></div><div id="comment-36123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36144"></span>

<div id="answer-container-36144" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36144-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should look into using <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> i.s.o. tcpdump. It's the capture engine {wire|t}shark uses to capture network traffic and write it to disk. It has multiple capture file option (-b) which can cycle files based on time, size and number of files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-36144" class="comments-container"></div><div id="comment-tools-36144" class="comment-tools"></div><div class="clear"></div><div id="comment-36144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

