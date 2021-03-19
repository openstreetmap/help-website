+++
type = "question"
title = "Large Packet Lengths"
description = '''I was contacted about a performance issue, so I setup Cisco SPANs in front of both end devices. The sending device has LSO enabled with the MTU set to 1500. Jumbo frames are enabled throughout the network up to ~9000 bytes. The devices send a MSS of 1460 in the TCP handshake. However, on BOTH sides ...'''
date = "2017-03-10T14:42:00Z"
lastmod = "2017-05-04T08:00:00Z"
weight = 59995
keywords = [ "jumbo", "lso", "mss", "mtu" ]
aliases = [ "/questions/59995" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Large Packet Lengths](/questions/59995/large-packet-lengths)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59995-score" class="post-score" title="current number of votes">0</div><span id="post-59995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was contacted about a performance issue, so I setup Cisco SPANs in front of both end devices. The sending device has LSO enabled with the MTU set to 1500. Jumbo frames are enabled throughout the network up to ~9000 bytes. The devices send a MSS of 1460 in the TCP handshake. However, on BOTH sides I am seeing packet lengths up to over 10,000 bytes in Wireshark. I've seen weird behavior like this before when capture ON the servers as many of you have as well. However, I'm capturing on the wire. I am trying to figure out if the sending server is not respecting the MTU size, Wireshark has a bug, I have some obscure option set incorrectly, or if one of our devices is altering packets. Has anyone else experienced this or have any ideas?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/TCP-options.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/frame_size.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jumbo" rel="tag" title="see questions tagged &#39;jumbo&#39;">jumbo</span> <span class="post-tag tag-link-lso" rel="tag" title="see questions tagged &#39;lso&#39;">lso</span> <span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span> <span class="post-tag tag-link-mtu" rel="tag" title="see questions tagged &#39;mtu&#39;">mtu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '17, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/37aeac42341cc42e5d10656094aa9139?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csereno&#39;s gravatar image" /><p><span>csereno</span><br />
<span class="score" title="69 reputation points">69</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csereno has one accepted answer">25%</span></p></img></div></div><div id="comments-container-59995" class="comments-container"><span id="60001"></span><div id="comment-60001" class="comment"><div id="post-60001-score" class="comment-score"></div><div class="comment-text"><p>It seems our packet capture server has offloading enabled. I disabled it and will test again Monday. Even a NIC in promiscuous mode doing the captures can be influenced by TSO/GSO/LSO.</p></div><div id="comment-60001-info" class="comment-info"><span class="comment-age">(10 Mar '17, 23:04)</span> <span class="comment-user userinfo">csereno</span></div></div><span id="60002"></span><div id="comment-60002" class="comment"><div id="post-60002-score" class="comment-score"></div><div class="comment-text"><p>I've never seen that happen in a capture setup, so I'm curious about your findings.</p></div><div id="comment-60002-info" class="comment-info"><span class="comment-age">(11 Mar '17, 02:44)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="60013"></span><div id="comment-60013" class="comment"><div id="post-60013-score" class="comment-score">1</div><div class="comment-text"><p>I've also had such packets when the capture device was configured for "Generic Receive Offload" resp. "Large Receive Offload".</p><p>An indication for this may several packets with increasing ACK numbers for "one" large packet.</p></div><div id="comment-60013-info" class="comment-info"><span class="comment-age">(12 Mar '17, 03:14)</span> <span class="comment-user userinfo">Uli</span></div></div><span id="60019"></span><div id="comment-60019" class="comment"><div id="post-60019-score" class="comment-score">1</div><div class="comment-text"><p>I have also witnessed this behavior on a Ubuntu laptop. Disabling all offload features of the NIC solved the issue for me...</p></div><div id="comment-60019-info" class="comment-info"><span class="comment-age">(12 Mar '17, 15:03)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="60022"></span><div id="comment-60022" class="comment"><div id="post-60022-score" class="comment-score"></div><div class="comment-text"><p>Uli, almost the entire stream looks like "one" large packet, so that had me curious as well. I'll let you all know tomorrow. Thanks for the confirmation!</p></div><div id="comment-60022-info" class="comment-info"><span class="comment-age">(12 Mar '17, 19:30)</span> <span class="comment-user userinfo">csereno</span></div></div></div><div id="comment-tools-59995" class="comment-tools"></div><div class="clear"></div><div id="comment-59995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61232"></span>

<div id="answer-container-61232" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61232-score" class="post-score" title="current number of votes">0</div><span id="post-61232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Disabling the offloads on the capture server worked. We rebuilt the servers awhile back and forgot to disable the offloads (it had been so long since the previous rebuild we forgot....lesson relearned!). Thank you Uli and SYN-bit for the confirmation!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '17, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/37aeac42341cc42e5d10656094aa9139?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csereno&#39;s gravatar image" /><p><span>csereno</span><br />
<span class="score" title="69 reputation points">69</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csereno has one accepted answer">25%</span></p></img></div></div><div id="comments-container-61232" class="comments-container"></div><div id="comment-tools-61232" class="comment-tools"></div><div class="clear"></div><div id="comment-61232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

