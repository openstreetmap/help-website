+++
type = "question"
title = "Fragment Overlap: True , Via UDP"
description = '''Hi After IP Fragmentation two times (UDP not TCP ), I get the error Fragment Overlap: True , and then the host does not respond anymore. Can you tell me please what can cause the fragment overlap in general ? Thanks alot'''
date = "2017-10-13T08:53:00Z"
lastmod = "2017-10-14T02:18:00Z"
weight = 63866
keywords = [ "fragmentation", "udp", "overlapping" ]
aliases = [ "/questions/63866" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fragment Overlap: True , Via UDP](/questions/63866/fragment-overlap-true-via-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi After IP Fragmentation two times (UDP not TCP ), I get the error Fragment Overlap: True , and then the host does not respond anymore.</p><p>Can you tell me please what can cause the fragment overlap in general ?</p><p>Thanks alot</p></div><div id="question-tags" class="tags-container tags">fragmentation udp overlapping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '17, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/d4d86ff8a9a663eba8ebbbbb4241f9e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="webtuto&#39;s gravatar image" /><p>webtuto<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="webtuto has no accepted answers">0%</span></p></div></div><div id="comments-container-63866" class="comments-container"><span id="63873"></span><div id="comment-63873" class="comment"><div id="post-63873-score" class="comment-score"></div><div class="comment-text"><p>Can you upload the PCAP? If you need to sanitize it first, use this tutorial: <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-63873-info" class="comment-info"><span class="comment-age">(13 Oct '17, 12:40)</span> Jasper ♦♦</div></div></div><div id="comment-tools-63866" class="comment-tools"></div><div class="clear"></div><div id="comment-63866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63893"></span>

<div id="answer-container-63893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63893-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without having looked at the specifics, the theory is that the sending host is chopping up the UDP packet into smaller parts to be able to transport is over the network to the other IP endpoint. For that purpose the IP header contains a payload length and offset, which allows the receiver's IP layer to put all pieces back together, like a jigsaw puzzle, into a complete UDP packet. When the sending host's IP layer miscalculates the offsets and/or lengths, the receiver will have jigsaw pieces that don't fit together, in this case there are overlapping parts. That will raise this error. So the cause is usually found in either the sending host's IP stack or any intervening network device which interacts at the IP layer, eg. NAT's.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '17, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Oct '17, 07:01</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-63893" class="comments-container"></div><div id="comment-tools-63893" class="comment-tools"></div><div class="clear"></div><div id="comment-63893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

