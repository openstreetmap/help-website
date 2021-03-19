+++
type = "question"
title = "Router solicitation in RFC 6788 context"
description = '''Hello,  I generated a customized router solicitation packet &quot;lio tunneled&quot;, following the context of RFC 6788 but Wireshark shows the packet as malformed. I would like to know if there is support for this Line-Identification Option (0x8C)?  Packet generated: 0000 33 33 00 00 00 02 AA BB CC DD EE FF ...'''
date = "2014-09-25T15:42:00Z"
lastmod = "2014-10-08T06:43:00Z"
weight = 36619
keywords = [ "icmpv6", "ipv6" ]
aliases = [ "/questions/36619" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Router solicitation in RFC 6788 context](/questions/36619/router-solicitation-in-rfc-6788-context)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36619-score" class="post-score" title="current number of votes">0</div><span id="post-36619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I generated a customized router solicitation packet "lio tunneled", following the context of RFC 6788 but Wireshark shows the packet as malformed. I would like to know if there is support for this Line-Identification Option (0x8C)?</p><p>Packet generated:</p><pre><code>0000   33 33 00 00 00 02 AA BB  CC DD EE FF 86 DD 60 00   33............`.
0010   00 00 00 08 3C FF FE 80  00 00 00 00 00 00 FA 1A   ....&lt;...........
0020   67 FF FE 04 9E EB FF 02  00 00 00 00 00 00 00 00   g...............
0030   00 00 00 00 00 02 3A 04  8C 02 01 55 85 00 7E 2C   ......:....U..~,
0040   00 00 00 00</code></pre><p>Thanks in advance<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmpv6" rel="tag" title="see questions tagged &#39;icmpv6&#39;">icmpv6</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '14, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/5a5bad3fbc165ab3cd06c06944422d98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willpz&#39;s gravatar image" /><p><span>willpz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willpz has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '14, 15:44</strong> </span></p></div></div><div id="comments-container-36619" class="comments-container"></div><div id="comment-tools-36619" class="comment-tools"></div><div class="clear"></div><div id="comment-36619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36917"></span>

<div id="answer-container-36917" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36917-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36917-score" class="post-score" title="current number of votes">0</div><span id="post-36917-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I take a look at packet IPv6 dissectors of 1.12.1 Wireshark version and these options seem not to be supported yet:</p><pre><code>0x08    SMF_DPD     [RFC6621]
0x8B    ILNP Nonce  [RFC6744]
0x8C    Line-Identification Option  [RFC6788]
0x6D    MPL Option  [draft-ietf-roll-trickle-mcast]
0xEE    IP_DFF  [RFC6971]</code></pre><p>The complete list of IPv6 Destination Options: <a href="http://www.iana.org/assignments/ipv6-parameters/ipv6-parameters.xhtml">http://www.iana.org/assignments/ipv6-parameters/ipv6-parameters.xhtml</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '14, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/5a5bad3fbc165ab3cd06c06944422d98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willpz&#39;s gravatar image" /><p><span>willpz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willpz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Oct '14, 06:43</strong> </span></p></div></div><div id="comments-container-36917" class="comments-container"></div><div id="comment-tools-36917" class="comment-tools"></div><div class="clear"></div><div id="comment-36917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

