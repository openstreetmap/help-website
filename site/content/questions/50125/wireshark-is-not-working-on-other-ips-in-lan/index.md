+++
type = "question"
title = "wireshark is not working on other IPs in LAN?"
description = '''i used the filter http.proxy_authorization and it does tell me credentials, but only mine when i log in, not of other persons on same LAN network? what is the solution to this?'''
date = "2016-02-12T02:22:00Z"
lastmod = "2016-02-12T06:07:00Z"
weight = 50125
keywords = [ "wlan" ]
aliases = [ "/questions/50125" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark is not working on other IPs in LAN?](/questions/50125/wireshark-is-not-working-on-other-ips-in-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50125-score" class="post-score" title="current number of votes">0</div><span id="post-50125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i used the filter http.proxy_authorization and it does tell me credentials, but only mine when i log in, not of other persons on same LAN network? what is the solution to this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '16, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/fbb41474dd035e39f565313db8eff0a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vinayak&#39;s gravatar image" /><p><span>vinayak</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vinayak has no accepted answers">0%</span></p></div></div><div id="comments-container-50125" class="comments-container"></div><div id="comment-tools-50125" class="comment-tools"></div><div class="clear"></div><div id="comment-50125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50127"></span>

<div id="answer-container-50127" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50127-score" class="post-score" title="current number of votes">0</div><span id="post-50127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For that you would need to capture the packets of the other persons, which requires a SPAN port or TAP in front of the proxy. For that you need to have admin access to the switch or the ability to insert a TAP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-50127" class="comments-container"><span id="50140"></span><div id="comment-50140" class="comment"><div id="post-50140-score" class="comment-score">1</div><div class="comment-text"><p>In other words, see the <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet</a> CaptureSetup page.</p></div><div id="comment-50140-info" class="comment-info"><span class="comment-age">(12 Feb '16, 06:07)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-50127" class="comment-tools"></div><div class="clear"></div><div id="comment-50127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

