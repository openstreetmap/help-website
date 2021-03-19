+++
type = "question"
title = "Closing Connections"
description = '''Is Wireshark capable of closing connections to certain ip address/urls from within the program?'''
date = "2015-11-23T14:01:00Z"
lastmod = "2015-11-24T07:08:00Z"
weight = 47890
keywords = [ "closing" ]
aliases = [ "/questions/47890" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Closing Connections](/questions/47890/closing-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47890-score" class="post-score" title="current number of votes">0</div><span id="post-47890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is Wireshark capable of closing connections to certain ip address/urls from within the program?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-closing" rel="tag" title="see questions tagged &#39;closing&#39;">closing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '15, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/f6f83639aa255e8440ba64545247950f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Benn&#39;s gravatar image" /><p><span>Benn</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Benn has no accepted answers">0%</span></p></div></div><div id="comments-container-47890" class="comments-container"></div><div id="comment-tools-47890" class="comment-tools"></div><div class="clear"></div><div id="comment-47890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47895"></span>

<div id="answer-container-47895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47895-score" class="post-score" title="current number of votes">1</div><span id="post-47895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark is a passive network analysis tool. It cant't send any data to the network, like TCP Resets or similar.</p><p>What are you trying to do? Maybe there are other ways to achieve that.</p><p>By any chance: Do you want to build some kind of IPS, based on the dissection capabilities of Wireshark?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '15, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47895" class="comments-container"><span id="47927"></span><div id="comment-47927" class="comment"><div id="post-47927-score" class="comment-score"></div><div class="comment-text"><p>I'm trying to find a program that can close the connection while it is running for telephone troubleshooting. I work in a phone service company and we are testing loss of connection from the ip address/url. Any programs that would be useful to me.</p></div><div id="comment-47927-info" class="comment-info"><span class="comment-age">(24 Nov '15, 05:50)</span> <span class="comment-user userinfo">Benn</span></div></div><span id="47928"></span><div id="comment-47928" class="comment"><div id="post-47928-score" class="comment-score"></div><div class="comment-text"><p>Please take a look at <strong>tcpkill</strong></p><blockquote><p><a href="https://en.wikipedia.org/wiki/Tcpkill">https://en.wikipedia.org/wiki/Tcpkill</a></p></blockquote><p>it's part of the <strong>dsniff</strong> suite, whhich should be part of all Linux distributions.</p></div><div id="comment-47928-info" class="comment-info"><span class="comment-age">(24 Nov '15, 05:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47930"></span><div id="comment-47930" class="comment"><div id="post-47930-score" class="comment-score"></div><div class="comment-text"><p>Great. Thank you for your help. I really appreciate it.</p></div><div id="comment-47930-info" class="comment-info"><span class="comment-age">(24 Nov '15, 06:34)</span> <span class="comment-user userinfo">Benn</span></div></div><span id="47931"></span><div id="comment-47931" class="comment"><div id="post-47931-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47931-info" class="comment-info"><span class="comment-age">(24 Nov '15, 07:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47895" class="comment-tools"></div><div class="clear"></div><div id="comment-47895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

