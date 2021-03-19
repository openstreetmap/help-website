+++
type = "question"
title = "Duplicated packets in a 6to4 tunnel ping"
description = '''I&#x27;ve configured a 6to4 tunnel in Ubuntu and works like a charm. But when I research into a ping to ping6.google.com I see all the packets twice; duplicated. I left here a CAPTURE IMAGE Why happens this?'''
date = "2015-12-05T07:27:00Z"
lastmod = "2015-12-09T08:34:00Z"
weight = 48283
keywords = [ "wireshark", "ping", "6to4" ]
aliases = [ "/questions/48283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicated packets in a 6to4 tunnel ping](/questions/48283/duplicated-packets-in-a-6to4-tunnel-ping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48283-score" class="post-score" title="current number of votes">0</div><span id="post-48283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've configured a 6to4 tunnel in Ubuntu and works like a charm. But when I research into a ping to ping6.google.com I see all the packets twice; duplicated. I left here a <a href="http://s30.postimg.org/7zjtpd3ch/Screenshot_from_2015_12_05_15_57_33.png">CAPTURE IMAGE</a></p><p>Why happens this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-6to4" rel="tag" title="see questions tagged &#39;6to4&#39;">6to4</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/b848be277ee3b2ac25fd9f88c97a222a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssoomm&#39;s gravatar image" /><p><span>ssoomm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssoomm has no accepted answers">0%</span></p></div></div><div id="comments-container-48283" class="comments-container"><span id="48383"></span><div id="comment-48383" class="comment"><div id="post-48383-score" class="comment-score"></div><div class="comment-text"><p>Can you post a capture file?</p></div><div id="comment-48383-info" class="comment-info"><span class="comment-age">(09 Dec '15, 08:34)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-48283" class="comment-tools"></div><div class="clear"></div><div id="comment-48283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48287"></span>

<div id="answer-container-48287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48287-score" class="post-score" title="current number of votes">1</div><span id="post-48287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check the protocol layers in the decode - my guess is that you see the IPv6 packet with and without the IPv4 tunneling layer. Wireshark decodes the top addresses for the packet list, so you always see the IPv6 addresses (twice, in this case).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '15, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-48287" class="comments-container"><span id="48288"></span><div id="comment-48288" class="comment"><div id="post-48288-score" class="comment-score"></div><div class="comment-text"><p>To me <span>@Jasper</span>'s explanation makes sense only if the gate to the tunnel is a virtual IPv6 interface, and the capture has been taken at both the physical ipv4 interface and the virtual ipv6 interface simultaneously. Is it the case?</p><p>(posting the capture instead of the screenshot would have removed all doubts)</p></div><div id="comment-48288-info" class="comment-info"><span class="comment-age">(05 Dec '15, 08:51)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48289"></span><div id="comment-48289" class="comment"><div id="post-48289-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span> I think this is not the case. The capture corresponds to the main IPv4 interface. By the way, is there anyway to show the interface of the captured packet in Wireshark?</p></div><div id="comment-48289-info" class="comment-info"><span class="comment-age">(05 Dec '15, 09:19)</span> <span class="comment-user userinfo">ssoomm</span></div></div><span id="48290"></span><div id="comment-48290" class="comment"><div id="post-48290-score" class="comment-score"></div><div class="comment-text"><p>Weird, it goes against my understanding of principles of Wireshark that a single captured packet could be shown twice in the packet list.</p><blockquote><p>is there any way to show the interface of the captured packet in Wireshark?</p></blockquote><p>Yes, there is: the topmost line of the packet dissection pane (the one in the middle) reads "138 bytes captured on interface 0" for frame No. 1; for frame No. 2, I guess you should see "104 bytes captured on interface 1". If you unfold the "frame" line, you'll see a dissection of the frame label fields (which are not part of the captured frame but a collection of additional information added during capture); there, you should see a more detailed description what interface 0 and interface 1 are.</p></div><div id="comment-48290-info" class="comment-info"><span class="comment-age">(05 Dec '15, 09:35)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48311"></span><div id="comment-48311" class="comment"><div id="post-48311-score" class="comment-score"></div><div class="comment-text"><p>6to4 probably tunnels it virtually on the same physical NIC, it's a translation technique. You get both IPv6 and IPv4 address on the same interface and see IPv6 packets twice. Native, and then tunneled.</p></div><div id="comment-48311-info" class="comment-info"><span class="comment-age">(06 Dec '15, 06:21)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-48287" class="comment-tools"></div><div class="clear"></div><div id="comment-48287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

