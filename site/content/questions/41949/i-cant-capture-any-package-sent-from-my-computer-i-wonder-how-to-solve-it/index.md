+++
type = "question"
title = "I can&#x27;t capture any package sent from my computer; I wonder how to solve it?"
description = '''I can&#x27;t capture any package sent from my computer; I didn&#x27;t set any filter and I&#x27;m sure the interface captured was right. For example, I ping another IP from my PC, a REPLY package can be captured, but the REQUEST package sent from my PC cannot be captured.Any packages sent from my PC cannot be capt...'''
date = "2015-04-29T12:28:00Z"
lastmod = "2015-05-07T07:07:00Z"
weight = 41949
keywords = [ "icmp", "http", "tcp", "package" ]
aliases = [ "/questions/41949" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I can't capture any package sent from my computer; I wonder how to solve it?](/questions/41949/i-cant-capture-any-package-sent-from-my-computer-i-wonder-how-to-solve-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41949-score" class="post-score" title="current number of votes">0</div><span id="post-41949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't capture any package sent from my computer; I didn't set any filter and I'm sure the interface captured was right. For example, I ping another IP from my PC, a REPLY package can be captured, but the REQUEST package sent from my PC cannot be captured.Any packages sent from my PC cannot be captured,such as ICMP,TCP,HTTP, and so on. Look forward to your reply soon. Thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-package" rel="tag" title="see questions tagged &#39;package&#39;">package</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '15, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/35d2d692288e4c4d06cac37a8ab7fc4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ncu1121zhb&#39;s gravatar image" /><p><span>ncu1121zhb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ncu1121zhb has no accepted answers">0%</span></p></div></div><div id="comments-container-41949" class="comments-container"><span id="42182"></span><div id="comment-42182" class="comment"><div id="post-42182-score" class="comment-score"></div><div class="comment-text"><p>It sounds like you have more than one interface to the outside world and for whatever reason you are capturing on the one that the reply is returning on. If it were me, I would first capture on the "any" interface to see if there is some asymmetric signaling going on.</p></div><div id="comment-42182-info" class="comment-info"><span class="comment-age">(07 May '15, 07:07)</span> <span class="comment-user userinfo">tiger762</span></div></div></div><div id="comment-tools-41949" class="comment-tools"></div><div class="clear"></div><div id="comment-41949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41952"></span>

<div id="answer-container-41952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41952-score" class="post-score" title="current number of votes">0</div><span id="post-41952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How do you capture, wireless or wired? When wireless, you can't capture your outgoing packets with the same WiFi card because it can either send or receive (=capture). If wired, check/disable your local firewall/security software which may omit packets from the capture process.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '15, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41952" class="comments-container"></div><div id="comment-tools-41952" class="comment-tools"></div><div class="clear"></div><div id="comment-41952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

