+++
type = "question"
title = "order of packets in case of high data rate"
description = '''I am monitoring Eth3 of 2 machines.  1st machine is sending the RLP(Radio Link Protocol) messages. 2nd machine receives the RLP Messages. Data rate would ne 30-40 MBps Problem: Order of the packet on Machine 2 is not same as Machine 1. Is there any guarantee that wireshark will display the packets i...'''
date = "2011-03-24T10:05:00Z"
lastmod = "2011-03-24T10:05:00Z"
weight = 3086
keywords = [ "rlp", "out-of-order" ]
aliases = [ "/questions/3086" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [order of packets in case of high data rate](/questions/3086/order-of-packets-in-case-of-high-data-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3086-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am monitoring Eth3 of 2 machines. 1st machine is sending the RLP(Radio Link Protocol) messages. 2nd machine receives the RLP Messages. Data rate would ne 30-40 MBps</p><p>Problem: Order of the packet on Machine 2 is not same as Machine 1. Is there any guarantee that wireshark will display the packets in the same order as the order of the packets on the wire?</p><p>Thanks, Gp</p></div><div id="question-tags" class="tags-container tags">rlp out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '11, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/303a40c342cae0137f648288ec32c943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gforgurpreet&#39;s gravatar image" /><p>gforgurpreet<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gforgurpreet has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '12, 08:37</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3086" class="comments-container"><span id="14436"></span><div id="comment-14436" class="comment"><div id="post-14436-score" class="comment-score"></div><div class="comment-text"><p>are they in the same network (just a switch between them) or are there routers inbetween. If there are routers, the packets may be reordered.</p></div><div id="comment-14436-info" class="comment-info"><span class="comment-age">(21 Sep '12, 09:29)</span> Kurt Knochner ♦</div></div><span id="14440"></span><div id="comment-14440" class="comment"><div id="post-14440-score" class="comment-score"></div><div class="comment-text"><p>How are you capturing the traffic? If you're using a SPAN session, that may be skewing the results. If you can, try capturing using the same method (ie TX only SPAN,the RX only spans to rule out any issues with packets being re-ordered inside the switch)</p></div><div id="comment-14440-info" class="comment-info"><span class="comment-age">(21 Sep '12, 13:50)</span> hansangb</div></div></div><div id="comment-tools-3086" class="comment-tools"></div><div class="clear"></div><div id="comment-3086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

