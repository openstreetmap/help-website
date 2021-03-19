+++
type = "question"
title = "&quot;tcp previous segment not captured&quot;"
description = '''greetings, what does &quot;tcp previous segment not captured&quot; indicate? I am running wireshark when trying to connect to a wireless windows 7 vnc server from a wireless ubuntu laptop.'''
date = "2012-09-07T20:05:00Z"
lastmod = "2012-09-08T04:20:00Z"
weight = 14134
keywords = [ "windows7", "vnc", "captured" ]
aliases = [ "/questions/14134" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["tcp previous segment not captured"](/questions/14134/tcp-previous-segment-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14134-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>greetings, what does "tcp previous segment not captured" indicate? I am running wireshark when trying to connect to a wireless windows 7 vnc server from a wireless ubuntu laptop.</p></div><div id="question-tags" class="tags-container tags">windows7 vnc captured</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '12, 20:05</strong></p><img src="https://secure.gravatar.com/avatar/2d6ce717de105b2b2e3e64a4e92e1286?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bishop2001&#39;s gravatar image" /><p>bishop2001<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bishop2001 has no accepted answers">0%</span></p></div></div><div id="comments-container-14134" class="comments-container"></div><div id="comment-tools-14134" class="comment-tools"></div><div class="clear"></div><div id="comment-14134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14136"></span>

<div id="answer-container-14136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14136-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It means that Wireshark (or whatever program you used to capture the traffic) either wasn't fast enough to cope with the amount of data the NIC received (dropped frames due to performance problems or WiFi "half duplex" operation), or that the frame actually <em>wasn't</em> on the "wire" - meaning, that Wireshark detected packet loss. You usually can tell by looking for a retransmission of the missing packet - if you see it, you most likely didn't suffer dropped frames. Instead, you have packet loss or Out of Order arrivals.</p><p>Actually, this message is new replacement in version 1.8.x; in former versions of Wireshark it was "tcp previous segment lost".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '12, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Sep '12, 04:21</p></div></div><div id="comments-container-14136" class="comments-container"></div><div id="comment-tools-14136" class="comment-tools"></div><div class="clear"></div><div id="comment-14136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

