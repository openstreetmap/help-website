+++
type = "question"
title = "Unencrypted HTTP protocol detected over encrypted port?"
description = '''I see in my witeshark the below msg. Unencrypted HTTP protocol detected over encrypted port, could indicate a dangerous misconfiguration. What does it mean?'''
date = "2017-05-19T02:33:00Z"
lastmod = "2017-05-19T02:56:00Z"
weight = 61504
keywords = [ "ssl_error" ]
aliases = [ "/questions/61504" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unencrypted HTTP protocol detected over encrypted port?](/questions/61504/unencrypted-http-protocol-detected-over-encrypted-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61504-score" class="post-score" title="current number of votes">0</div><span id="post-61504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see in my witeshark the below msg. Unencrypted HTTP protocol detected over encrypted port, could indicate a dangerous misconfiguration.</p><p>What does it mean?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl_error" rel="tag" title="see questions tagged &#39;ssl_error&#39;">ssl_error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '17, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/b5ef9e11a802a93a8f8a3991698e0f1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronaldmabini&#39;s gravatar image" /><p><span>ronaldmabini</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronaldmabini has no accepted answers">0%</span></p></div></div><div id="comments-container-61504" class="comments-container"></div><div id="comment-tools-61504" class="comment-tools"></div><div class="clear"></div><div id="comment-61504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61505"></span>

<div id="answer-container-61505" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61505-score" class="post-score" title="current number of votes">0</div><span id="post-61505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Port 443 has been <a href="https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&amp;page=8">assigned by IANA</a> for transport of HTTPS traffic. When detecting unencrypted HTTP this is a possible sign that the intention was to use HTTPS, but possibly a misconfiguration, or some other reason, lead to serving unencrypted HTTP over port 443. As people somewhat expect port 443 to carry encrypted traffic this warning is generated to alert the network or system administrator of possible problems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '17, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61505" class="comments-container"></div><div id="comment-tools-61505" class="comment-tools"></div><div class="clear"></div><div id="comment-61505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

