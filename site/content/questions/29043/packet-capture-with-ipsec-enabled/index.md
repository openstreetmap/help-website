+++
type = "question"
title = "PACKET CAPTURE with IPSEC ENABLED"
description = '''Hi, If IPSEC is enabled , can PCAP traces be captured and decoded using wireshark? Thanks'''
date = "2014-01-20T22:36:00Z"
lastmod = "2014-01-21T04:06:00Z"
weight = 29043
keywords = [ "pcap", "ipsec" ]
aliases = [ "/questions/29043" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PACKET CAPTURE with IPSEC ENABLED](/questions/29043/packet-capture-with-ipsec-enabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29043-score" class="post-score" title="current number of votes">0</div><span id="post-29043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, If IPSEC is enabled , can PCAP traces be captured and decoded using wireshark? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '14, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/276dd2e60fd9f342b8fc2d3bd102886e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Surajitm&#39;s gravatar image" /><p><span>Surajitm</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Surajitm has no accepted answers">0%</span></p></div></div><div id="comments-container-29043" class="comments-container"></div><div id="comment-tools-29043" class="comment-tools"></div><div class="clear"></div><div id="comment-29043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29051"></span>

<div id="answer-container-29051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29051-score" class="post-score" title="current number of votes">0</div><span id="post-29051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>well, it depends....</p><p>.... on the OS and the way the IPSEC subsystem is integrated into the kernel. On some systems there is a virtual ipsec interface (like Linux KLIPS). If you capture traffic on that virtual interface, you will see the traffic in clear. On other systems (Linux 'native' IPSEC stack since kernel 2.6) you will see parts of the traffic in clear and other parts only encrypted (strange thing, but that's due to the internal architecture of the IPSEC stack and the way libpcap hooks into the kernel). Again on other systems (e.g. Windows) it might be totally different <strong>and</strong> dependent on the VPN software in use (we have had several reports about problems with WinPcap and VPN clients ).</p><p>So, there is no clear answer to you question, as you did not tell us the system (OS and VPN software) you are talking about.</p><p>Even if you add that information, it's hard to answer the question, unless one of the members here has the same 'configuration' and is able to test it. But then, why don't you test it yourself?</p><p>Simply try to capture traffic</p><ul><li>without IPSEC tunnel</li><li>with an established IPSEC tunnel</li></ul><p>and see what you get on <strong>your system</strong> with <strong>your IPSEC</strong> configuration ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '14, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29051" class="comments-container"></div><div id="comment-tools-29051" class="comment-tools"></div><div class="clear"></div><div id="comment-29051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

