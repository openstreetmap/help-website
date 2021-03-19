+++
type = "question"
title = "SSH connection, web browser and TTL"
description = '''Hello, I haven&#x27;t been unable to figure out the following: a) If there was an SSH connection. b) If a web browser was used ( like which one ) c)How many packages have a TTL ( time to Live) in a certain range. d) How do I find out if there was a peer-to-peer file sharing ? Does anyone know ? I can&#x27;t f...'''
date = "2015-01-26T05:59:00Z"
lastmod = "2015-01-26T23:58:00Z"
weight = 39399
keywords = [ "ssh", "homework" ]
aliases = [ "/questions/39399" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSH connection, web browser and TTL](/questions/39399/ssh-connection-web-browser-and-ttl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39399-score" class="post-score" title="current number of votes">0</div><span id="post-39399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I haven't been unable to figure out the following:</p><p>a) If there was an SSH connection.</p><p>b) If a web browser was used ( like which one )</p><p>c)How many packages have a TTL ( time to Live) in a certain range.</p><p>d) How do I find out if there was a peer-to-peer file sharing ?</p><p>Does anyone know ? I can't find this anywhere.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span> <span class="post-tag tag-link-homework" rel="tag" title="see questions tagged &#39;homework&#39;">homework</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '15, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/d33eb2b57ff4dc439fa8f9b3b8eceba6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xandi&#39;s gravatar image" /><p><span>Xandi</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xandi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jan '15, 06:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-39399" class="comments-container"></div><div id="comment-tools-39399" class="comment-tools"></div><div class="clear"></div><div id="comment-39399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39410"></span>

<div id="answer-container-39410" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39410-score" class="post-score" title="current number of votes">1</div><span id="post-39410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Xandi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some hints (we usually don't solve homework assignments):</p><p>a) determine the TCP or UDP port SSH runs on. Filter for that port, check if anything shows up. If it does, you found one. b) web browsers use HTTP. Find the port for that. Filter on it. Check user agent strings. c) easiest would be to add a column for this. Find a TTL field, use pop up menu to "Apply as column" d) check if there is SMB/CIFS in the capture (find the port, filter, yada yada yada)</p><p>If you "can't find this anywhere" you haven't really put any time into it, so take the hints and use them. It takes probably 15-30 minutes to do all this if starting from scratch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '15, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39410" class="comments-container"><span id="39421"></span><div id="comment-39421" class="comment"><div id="post-39421-score" class="comment-score"></div><div class="comment-text"><p>Just need get familiar with the program. Thank you</p></div><div id="comment-39421-info" class="comment-info"><span class="comment-age">(26 Jan '15, 23:58)</span> <span class="comment-user userinfo">Xandi</span></div></div></div><div id="comment-tools-39410" class="comment-tools"></div><div class="clear"></div><div id="comment-39410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

