+++
type = "question"
title = "TCP Acknowledgement and Sequence number"
description = '''I am using iperf to send a traffic for 60 seconds (i.e. i have an iperf client and iperf server). When I capture the traffic using both Wireshark and tcpdump, almost all of the packets have the same acknowledgement number but different sequence numbers. This is worrying me and is this healthy? Is it...'''
date = "2017-04-21T14:09:00Z"
lastmod = "2017-04-21T15:27:00Z"
weight = 60952
keywords = [ "iperf", "tcpdump", "packets", "wireshark" ]
aliases = [ "/questions/60952" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Acknowledgement and Sequence number](/questions/60952/tcp-acknowledgement-and-sequence-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60952-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using iperf to send a traffic for 60 seconds (i.e. i have an iperf client and iperf server). When I capture the traffic using both Wireshark and tcpdump, almost all of the packets have the same acknowledgement number but different sequence numbers. This is worrying me and is this healthy? Is it OK to have thousands of packets to have the same ack number?</p></div><div id="question-tags" class="tags-container tags">iperf tcpdump packets wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '17, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div></div><div id="comments-container-60952" class="comments-container"></div><div id="comment-tools-60952" class="comment-tools"></div><div class="clear"></div><div id="comment-60952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60954"></span>

<div id="answer-container-60954" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60954-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two Sequence numbers and two ACK numbers - one for each node in the conversation. So if you look at the sequence of the first node going up (which it does during sending data), you should see the ACK numbers of the other node doing the same (acknowledging the sent data).</p><p>The node not sending anything will not increase it's sequence number, and so also the ACK number will not increase of the other node. So, in short, what you see is not unusual at all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '17, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60954" class="comments-container"></div><div id="comment-tools-60954" class="comment-tools"></div><div class="clear"></div><div id="comment-60954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

