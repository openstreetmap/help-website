+++
type = "question"
title = "Is it possible to detect an inbound TCP association (ip address) if no socket is open..."
description = '''Is it possible to detect an inbound TCP association if no socket is open ? The title says it all. We need to detect an inbound association on port 2000 to detect the IP address before a socket to TCP is open. Is there a way to see the IP address under these conditions with WireShark..? Thank you, Ch...'''
date = "2010-11-14T01:01:00Z"
lastmod = "2010-11-14T05:08:00Z"
weight = 937
keywords = [ "association" ]
aliases = [ "/questions/937" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to detect an inbound TCP association (ip address) if no socket is open...](/questions/937/is-it-possible-to-detect-an-inbound-tcp-association-ip-address-if-no-socket-is-open)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-937-score" class="post-score" title="current number of votes">0</div><span id="post-937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to detect an inbound TCP association if no socket is open ? The title says it all. We need to detect an inbound association on port 2000 to detect the IP address before a socket to TCP is open. Is there a way to see the IP address under these conditions with WireShark..?</p><p>Thank you,</p><p>Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-association" rel="tag" title="see questions tagged &#39;association&#39;">association</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '10, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/65d3b76c73d5f2c87c69e192d3eee2e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrisxl&#39;s gravatar image" /><p><span>chrisxl</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrisxl has no accepted answers">0%</span></p></div></div><div id="comments-container-937" class="comments-container"></div><div id="comment-tools-937" class="comment-tools"></div><div class="clear"></div><div id="comment-937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="940"></span>

<div id="answer-container-940" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-940-score" class="post-score" title="current number of votes">0</div><span id="post-940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what you mean by association. But I assume you mean that you want to see which hosts are trying to connect to TCP port 2000, even though port 2000 is not open. Yes, you can see the incoming connections as long as you are using wireshark on the host that people connect too and there is no firewall in between blocking the packets.</p><p>You can also see these packets n your network if you are using a span or mirror port on the switch to which your host is connected. Or in case there is a blocking firewall, you can use a span/mirror port to look at the packets on the Internet facing interface of the firewall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '10, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-940" class="comments-container"></div><div id="comment-tools-940" class="comment-tools"></div><div class="clear"></div><div id="comment-940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

