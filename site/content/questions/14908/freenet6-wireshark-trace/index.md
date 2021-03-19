+++
type = "question"
title = "Freenet6 Wireshark Trace"
description = '''I connected to IPv6 via Freenet6, logged into ipv6.google.com and captured the Wireshark trace. In the trace it does not show any IPv4 address. Connection mode is IPv6-in-UDP-IPv4 Tunnel (NAT Traversal). My question is,  shouldn&#x27;t the tunnel be going through my IPv4 network? If it is not so how is t...'''
date = "2012-10-10T20:58:00Z"
lastmod = "2012-10-11T05:58:00Z"
weight = 14908
keywords = [ "tunnel", "ipv6", "freenet6" ]
aliases = [ "/questions/14908" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Freenet6 Wireshark Trace](/questions/14908/freenet6-wireshark-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14908-score" class="post-score" title="current number of votes">0</div><span id="post-14908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I connected to IPv6 via Freenet6, logged into <a href="http://ipv6.google.com">ipv6.google.com</a> and captured the Wireshark trace.</p><p>In the trace it does not show any IPv4 address. Connection mode is IPv6-in-UDP-IPv4 Tunnel (NAT Traversal). My question is,</p><ol><li>shouldn't the tunnel be going through my IPv4 network?</li><li>If it is not so how is the connection established with remote server?</li></ol><p>If anyone knows please help me.</p><p>Thank You</p><p>Shreehari M</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span> <span class="post-tag tag-link-freenet6" rel="tag" title="see questions tagged &#39;freenet6&#39;">freenet6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '12, 20:58</strong></p><img src="https://secure.gravatar.com/avatar/72f5b05e12b88360c19063f377d8c312?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shreehari%20M&#39;s gravatar image" /><p><span>Shreehari M</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shreehari M has no accepted answers">0%</span></p></div></div><div id="comments-container-14908" class="comments-container"></div><div id="comment-tools-14908" class="comment-tools"></div><div class="clear"></div><div id="comment-14908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14916"></span>

<div id="answer-container-14916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14916-score" class="post-score" title="current number of votes">0</div><span id="post-14916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure that there is no IPv4 layer in your packets? Keep in mind that looking at the <em>packet list</em> won't help since Wireshark will always show the "highest" IP address found in a packet, so if you transport IPv6 over IPv4 it will always show the IPv6 address. If you take a look at the decode of the packet you will see the real layers, usually: Ethernet -&gt; IPv4 -&gt; IPv6 -&gt; TCP/UDP/ICMP... or (in your case) Ethernet -&gt; IPv4 -&gt; UDP -&gt; IPv6 -&gt; TCP/UDP/ICMP...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14916" class="comments-container"><span id="14926"></span><div id="comment-14926" class="comment"><div id="post-14926-score" class="comment-score"></div><div class="comment-text"><p>Thank You very much Jasper</p></div><div id="comment-14926-info" class="comment-info"><span class="comment-age">(11 Oct '12, 05:58)</span> <span class="comment-user userinfo">Shreehari M</span></div></div></div><div id="comment-tools-14916" class="comment-tools"></div><div class="clear"></div><div id="comment-14916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

