+++
type = "question"
title = "Viewing connection issues with Wireshark"
description = '''Hi all, I have tried to use WireShark to view traffic on certain connections to help identify why connections seemingly randomly reset. The issue seems to be, that if a connection becomes idle, no data is sent or received for some time (for example sitting idle on an irc server and only ping/ponging...'''
date = "2013-05-30T08:39:00Z"
lastmod = "2013-05-30T08:52:00Z"
weight = 21604
keywords = [ "connection", "out-of-order", "wireshark" ]
aliases = [ "/questions/21604" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Viewing connection issues with Wireshark](/questions/21604/viewing-connection-issues-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21604-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have tried to use WireShark to view traffic on certain connections to help identify why connections seemingly randomly reset. The issue seems to be, that if a connection becomes idle, no data is sent or received for some time (for example sitting idle on an irc server and only ping/ponging) the connection "dies" and the client will disconnect the next time it tries to write to the connection. In order to check this, I looked at traffic on http, irc and also for the online game WoW.</p><p>In the trace, WireShark frequently informs me that packets were sent out-of-order, previous tcp segments were not captured and packets marked with TCP retransmission. There is not enough traffic on the nic or lack of processing power for wireshark to warrant not capturing previous segments so often. Does this indicate a connection problem? If so, does this indicate a problem with my hardware?</p><p>Edit: <a href="http://www.cloudshark.org/captures/ab029483e244">IRC</a> <a href="http://www.cloudshark.org/captures/5e19a8168f07">Bnetgame</a>. My HTTP capture had many, many more marked packets however it likely contains personal information and is very large. The spikes in bnetgame correspond to when the client informed me I was disconnected and reconnected. The IRC capture shows me connecting, joining and then having my connection disconnected several times.</p></div><div id="question-tags" class="tags-container tags">connection out-of-order wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '13, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/5474328b0379fdf51855e92ae1fa5e67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joshx00&#39;s gravatar image" /><p>Joshx00<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joshx00 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '13, 09:59</p></div></div><div id="comments-container-21604" class="comments-container"></div><div id="comment-tools-21604" class="comment-tools"></div><div class="clear"></div><div id="comment-21604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21605"></span>

<div id="answer-container-21605" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21605-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on your capture setup whether the symptoms you're describing are really part of a problem with your connection or hardware, or just a flawed way of recording packets. For example you might loose packets on a switch SPAN session, or writing to disk is too slow to write all captured packets to disk in time.</p><p>You should try to find out if you have drops (shown in the status bar right after stopping the capture). If there are none, your capturing machine was fast enough to write all captured packets to disk. Next thing is to find out if there are really retransmissions or just duplicate packets in the trace. Also, you will have to determine if the combination of "previous segment not captured, Out-of-Order, retransmission" isn't just an out-of-order cluster of packets. To do that you need to understand how retransmission works in regard to round trip time - could the sender have known that the packet is lost when it was sent or not? If the retransmissions comes in too fast it is probably just normal Out-of-Order behavior.</p><p>Maybe you can post a sample capture at <a href="http://www.cloudshark.org"></a><a href="http://www.cloudshark.org">http://www.cloudshark.org</a> so we can take a look (only if it does not contain sensitive information).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '13, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21605" class="comments-container"><span id="21613"></span><div id="comment-21613" class="comment"><div id="post-21613-score" class="comment-score"></div><div class="comment-text"><p>Since Akismet believes my comment is spam here, I have edited my question.</p></div><div id="comment-21613-info" class="comment-info"><span class="comment-age">(30 May '13, 09:59)</span> Joshx00</div></div><span id="21620"></span><div id="comment-21620" class="comment"><div id="post-21620-score" class="comment-score">1</div><div class="comment-text"><p>You've got bidirectional packet loss, so it looks like your connection to the internet is loosing packets both ways. In the IRC case it also leads to a RESET termination due to the fact that the other node doesn't reply anymore (Stream Index 0) and your local PC gives up in packet 88.</p><p>This may be caused by some other PC/node in your network performing massive downloads which clog the line.</p></div><div id="comment-21620-info" class="comment-info"><span class="comment-age">(30 May '13, 12:17)</span> Jasper ♦♦</div></div><span id="21623"></span><div id="comment-21623" class="comment"><div id="post-21623-score" class="comment-score"></div><div class="comment-text"><p>Hi, no packet loss shows up in ping tests to these servers. Would there be a reason for this? Also, if I spam the connection with requests (such as ping/ponging every 3 seconds) it is stable. Is this because there are more replies to indicate the server is still alive?</p></div><div id="comment-21623-info" class="comment-info"><span class="comment-age">(30 May '13, 14:18)</span> Joshx00</div></div><span id="21644"></span><div id="comment-21644" class="comment"><div id="post-21644-score" class="comment-score">1</div><div class="comment-text"><p>Ping tests are not really accurate since the packet frequency is quite low (usually with 1 second delay) and they're pretty small (usually 64 byte), so they have a high chance of getting through. Packet loss usually happens with high packet volume (meaning: delta times between packets in the millisecond or microsecond range) and with larger payload.</p></div><div id="comment-21644-info" class="comment-info"><span class="comment-age">(31 May '13, 02:42)</span> Jasper ♦♦</div></div></div><div id="comment-tools-21605" class="comment-tools"></div><div class="clear"></div><div id="comment-21605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

