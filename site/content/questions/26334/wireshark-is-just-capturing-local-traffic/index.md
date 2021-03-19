+++
type = "question"
title = "Wireshark is just capturing local traffic"
description = '''Hi, I am using Wireshark on Mac OSX and it is justing capturing the local traffic (so, what happening on my computer, not on the others). I have tried it with Ethernet (LAN) Connection and with a WiFi Connection. It is still not working... Thank you Florian Traun'''
date = "2013-10-23T13:19:00Z"
lastmod = "2013-10-25T10:17:00Z"
weight = 26334
keywords = [ "not", "traffic", "local", "external", "loopback" ]
aliases = [ "/questions/26334" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark is just capturing local traffic](/questions/26334/wireshark-is-just-capturing-local-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26334-score" class="post-score" title="current number of votes">0</div><span id="post-26334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using Wireshark on Mac OSX and it is justing capturing the local traffic (so, what happening on my computer, not on the others). I have tried it with Ethernet (LAN) Connection and with a WiFi Connection. It is still not working...</p><p>Thank you Florian Traun</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-external" rel="tag" title="see questions tagged &#39;external&#39;">external</span> <span class="post-tag tag-link-loopback" rel="tag" title="see questions tagged &#39;loopback&#39;">loopback</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/c5ececd524b62fb4f90a12616269c668?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Florian%20Traun&#39;s gravatar image" /><p><span>Florian Traun</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Florian Traun has no accepted answers">0%</span></p></div></div><div id="comments-container-26334" class="comments-container"></div><div id="comment-tools-26334" class="comment-tools"></div><div class="clear"></div><div id="comment-26334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26338"></span>

<div id="answer-container-26338" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26338-score" class="post-score" title="current number of votes">0</div><span id="post-26338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I hate to belabor the obvious, but is your capture NIC in promiscuous mode? I am not familiar with Apple products, so this might not be the answer.</p><p>You will only capture "local" traffic on your WiFi connection unless you get an AirPcap adapter or a NIC that will go into RFMON mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/3d1f94fd059d26805abac57ed6299bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randyp&#39;s gravatar image" /><p><span>randyp</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randyp has no accepted answers">0%</span></p></div></div><div id="comments-container-26338" class="comments-container"><span id="26339"></span><div id="comment-26339" class="comment"><div id="post-26339-score" class="comment-score"></div><div class="comment-text"><p>Also, are you on a mirrored port or using a TAP? You will need to do this to see all traffic on the wire.</p></div><div id="comment-26339-info" class="comment-info"><span class="comment-age">(23 Oct '13, 16:04)</span> <span class="comment-user userinfo">randyp</span></div></div></div><div id="comment-tools-26338" class="comment-tools"></div><div class="clear"></div><div id="comment-26338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26407"></span>

<div id="answer-container-26407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26407-score" class="post-score" title="current number of votes">0</div><span id="post-26407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ethernet traffic nowadays work mostly with switches instead of hubs. This means traffic is not sent to all ports. Hence your ethernet port will only see broadcasts and your own traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '13, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/fa842ad48d99c642a22081fcacada9c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="easterman&#39;s gravatar image" /><p><span>easterman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="easterman has no accepted answers">0%</span></p></div></div><div id="comments-container-26407" class="comments-container"></div><div id="comment-tools-26407" class="comment-tools"></div><div class="clear"></div><div id="comment-26407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

