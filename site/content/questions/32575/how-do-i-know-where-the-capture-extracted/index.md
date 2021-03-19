+++
type = "question"
title = "How do i know where the capture extracted?"
description = '''Given a capture how can i figure out where the trace is taken from(who is the originator of the flow) if the capture contains 3 packets (SYN,SYN/ACK and ACK)?'''
date = "2014-05-06T19:57:00Z"
lastmod = "2014-05-07T09:41:00Z"
weight = 32575
keywords = [ "capture" ]
aliases = [ "/questions/32575" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do i know where the capture extracted?](/questions/32575/how-do-i-know-where-the-capture-extracted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32575-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Given a capture how can i figure out where the trace is taken from(who is the originator of the flow) if the capture contains 3 packets (SYN,SYN/ACK and ACK)?</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 19:57</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 May '14, 19:58</p></div></div><div id="comments-container-32575" class="comments-container"><span id="32597"></span><div id="comment-32597" class="comment"><div id="post-32597-score" class="comment-score"></div><div class="comment-text"><p>"Where the trace is taken from?" and "Who is the originator of the flow?" are 2 entirely different questions. Which do you want to know? Or are you assuming that the trace is being taken from the originator? Which class is this question for, by the way?</p></div><div id="comment-32597-info" class="comment-info"><span class="comment-age">(07 May '14, 07:13)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-32575" class="comment-tools"></div><div class="clear"></div><div id="comment-32575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32576"></span>

<div id="answer-container-32576" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32576-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To determine where the capture was taken you can use following clues</p><ul><li>Look at the delta time betweem SYN and SYN_ACK</li><li>Compare it to the delta time between SYN_ACK and ACK</li><li>Look at the ip.ttl of SYN and SYN_ACK packet (even TTLS are 255,128,64)</li><li>Look at the manufacturer prefix of the MAC addresses</li><li>Look at the Statistics - Summary</li></ul><p>The larger delta time has the external RTT of the connection indicating the sender of the packet is remote host (if there is a notable difference).</p><p>Most IP stacks have a hexadecimal 'even' TTL. Windows uses 128, most other stacks 64, some 255. So unless client and server are on the same LAN you should see an 'odd' TTL, this is a packet from the remote host.</p><p>MAC addresses give a clue as to what manufacturer the sender of an IP packet is</p><p>Statistics Summary contains general information about the capture</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '14, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 May '14, 21:19</p></div></div><div id="comments-container-32576" class="comments-container"></div><div id="comment-tools-32576" class="comment-tools"></div><div class="clear"></div><div id="comment-32576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32610"></span>

<div id="answer-container-32610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32610-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer to <a href="http://ask.wireshark.org/questions/21297/ip-of-machine-where-wireshark-is-running">this question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-32610" class="comments-container"></div><div id="comment-tools-32610" class="comment-tools"></div><div class="clear"></div><div id="comment-32610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

