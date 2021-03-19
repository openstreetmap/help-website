+++
type = "question"
title = "TCP information segmented at NIC making wireshark capture less interesting"
description = '''I would like to see the &quot;normal&quot; behavior of TCP in wireshark, but I have discovered that (to save CPU) TCP sends large chunks of information to the NIC and the NIC actually performs the segmentation (based on MTU). From what I have read so far wireshark captures traffic data between TCP (the CPU) a...'''
date = "2013-01-21T16:00:00Z"
lastmod = "2013-01-21T16:11:00Z"
weight = 17835
keywords = [ "nic", "size", "packet", "tcp", "capture" ]
aliases = [ "/questions/17835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP information segmented at NIC making wireshark capture less interesting](/questions/17835/tcp-information-segmented-at-nic-making-wireshark-capture-less-interesting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17835-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to see the "normal" behavior of TCP in wireshark, but I have discovered that (to save CPU) TCP sends large chunks of information to the NIC and the NIC actually performs the segmentation (based on MTU). From what I have read so far wireshark captures traffic data between TCP (the CPU) and the NIC, so the "normal" behavior of TCP is lost. Is there a way to force the segmentation of information to be done by TCP (old school) or perhaps to capture the packets in the NIC? I'm using Linux.</p></div><div id="question-tags" class="tags-container tags">nic size packet tcp capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '13, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/98becf769507827238b27472da91323a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clod1977&#39;s gravatar image" /><p>clod1977<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clod1977 has no accepted answers">0%</span></p></div></div><div id="comments-container-17835" class="comments-container"></div><div id="comment-tools-17835" class="comment-tools"></div><div class="clear"></div><div id="comment-17835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17837"></span>

<div id="answer-container-17837" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17837-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The best way to see packets as they are on the wire is to use a network TAP. Next best thing would be to use the span port of a managed switch.</p><p>Have a look at my comment on your comment on <a href="http://ask.wireshark.org/questions/7659/tcp-packet-size">http://ask.wireshark.org/questions/7659/tcp-packet-size</a> for hints on how to disable TSO in linux.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '13, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17837" class="comments-container"><span id="17839"></span><div id="comment-17839" class="comment"><div id="post-17839-score" class="comment-score"></div><div class="comment-text"><p>basically, any method where you capture the packets somewhere <em>between</em> client and server (and not <strong>on</strong> any of them) will do the trick...</p></div><div id="comment-17839-info" class="comment-info"><span class="comment-age">(21 Jan '13, 16:19)</span> Jasper ♦♦</div></div><span id="17849"></span><div id="comment-17849" class="comment"><div id="post-17849-score" class="comment-score"></div><div class="comment-text"><p>I'm pretty sure Opnet's Ace analyst (now ATX) has the ability to recode it using MTU. You're kind of cheating since you don't see it on the wire, but when you're dealing with VMs and modern day servers, it does come in handy for quick troubleshooting. It would be like the anti-"allow subdissector to reassemble packets" feature! :)</p></div><div id="comment-17849-info" class="comment-info"><span class="comment-age">(21 Jan '13, 22:22)</span> hansangb</div></div></div><div id="comment-tools-17837" class="comment-tools"></div><div class="clear"></div><div id="comment-17837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

