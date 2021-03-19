+++
type = "question"
title = "Understanding PING (reply in XXXX) Packets"
description = '''Hi, I get following response on Wireshark while running ping 195.8.215.136 on windows PC: 6007 11.928578000 58.65.XXX.XXX 195.8.215.136 ICMP 74 Echo (ping) request id=0x000c, seq=17134/60994, ttl=128 (reply in 6014) 6341 12.929617000 58.65.XXX.XXX 195.8.215.136 ICMP 74 Echo (ping) request id=0x000c,...'''
date = "2015-07-17T07:40:00Z"
lastmod = "2015-07-17T09:10:00Z"
weight = 44243
keywords = [ "firewall3229", "icmp", "ping" ]
aliases = [ "/questions/44243" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding PING (reply in XXXX) Packets](/questions/44243/understanding-ping-reply-in-xxxx-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44243-score" class="post-score" title="current number of votes">0</div><span id="post-44243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I get following response on Wireshark while running ping 195.8.215.136 on windows PC:</p><p>6007 11.928578000 58.65.XXX.XXX 195.8.215.136 ICMP 74 Echo (ping) request id=0x000c, seq=17134/60994, ttl=128 (reply in 6014)</p><p>6341 12.929617000 58.65.XXX.XXX 195.8.215.136 ICMP 74 Echo (ping) request id=0x000c, seq=17136/61506, ttl=128 (reply in 6353)</p><p>6430 13.930676000 58.65.XXX.XXX 195.8.215.136 ICMP 74 Echo (ping) request id=0x000c, seq=17137/61762, ttl=128 (no response found!)</p><p>As per my findings (no response found!) is due to firewall blocking but I dont understand first two messages. Any help in this regard would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firewall3229" rel="tag" title="see questions tagged &#39;firewall3229&#39;">firewall3229</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '15, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/a44cbaa05bac7375b9425625e67cf847?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noman4ever&#39;s gravatar image" /><p><span>noman4ever</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noman4ever has no accepted answers">0%</span></p></div></div><div id="comments-container-44243" class="comments-container"></div><div id="comment-tools-44243" class="comment-tools"></div><div class="clear"></div><div id="comment-44243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44244"></span>

<div id="answer-container-44244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44244-score" class="post-score" title="current number of votes">1</div><span id="post-44244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first two ping requests were answered in packets 6014 and 6353, respectively. The third was either blocked, or Wireshark just doesn't have the response packet in the capture file and thus could not match it to the request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44244" class="comments-container"><span id="44247"></span><div id="comment-44247" class="comment"><div id="post-44247-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply.</p></div><div id="comment-44247-info" class="comment-info"><span class="comment-age">(17 Jul '15, 09:10)</span> <span class="comment-user userinfo">noman4ever</span></div></div></div><div id="comment-tools-44244" class="comment-tools"></div><div class="clear"></div><div id="comment-44244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

