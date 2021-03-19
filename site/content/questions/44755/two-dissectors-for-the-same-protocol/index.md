+++
type = "question"
title = "two dissectors for the same protocol"
description = '''hi, I want to know if it is possible to use two dissectors with the same protocol for different messages? These two messages are different but having the same protocol. so i am supposed to use the same dissector for both the messages or is it possible to create two different dissectors for the same ...'''
date = "2015-08-03T00:51:00Z"
lastmod = "2015-08-03T23:16:00Z"
weight = 44755
keywords = [ "ask.wireshark.org" ]
aliases = [ "/questions/44755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [two dissectors for the same protocol](/questions/44755/two-dissectors-for-the-same-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44755-score" class="post-score" title="current number of votes">0</div><span id="post-44755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I want to know if it is possible to use two dissectors with the same protocol for different messages? These two messages are different but having the same protocol. so i am supposed to use the same dissector for both the messages or is it possible to create two different dissectors for the same protocol for two different messages??</p><p>thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ask.wireshark.org" rel="tag" title="see questions tagged &#39;ask.wireshark.org&#39;">ask.wireshark.org</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '15, 00:51</strong></p><img src="https://secure.gravatar.com/avatar/4f516d44975f0778735c91ae9f71624b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zombimind&#39;s gravatar image" /><p><span>zombimind</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zombimind has no accepted answers">0%</span></p></div></div><div id="comments-container-44755" class="comments-container"></div><div id="comment-tools-44755" class="comment-tools"></div><div class="clear"></div><div id="comment-44755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44756"></span>

<div id="answer-container-44756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44756-score" class="post-score" title="current number of votes">1</div><span id="post-44756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just do as all the other dissectors for protocols that have more than one message type do, and just have one dissector for the protocol that somehow determines the type of the message (for example, by looking at a message type field if there is one) and dissects all the different types of messages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44756" class="comments-container"><span id="44757"></span><div id="comment-44757" class="comment"><div id="post-44757-score" class="comment-score"></div><div class="comment-text"><p>thanks form your time harris,, so its not possible to have two dissectors for the same protocol..??</p></div><div id="comment-44757-info" class="comment-info"><span class="comment-age">(03 Aug '15, 01:11)</span> <span class="comment-user userinfo">zombimind</span></div></div><span id="44796"></span><div id="comment-44796" class="comment"><div id="post-44796-score" class="comment-score"></div><div class="comment-text"><p>No, it is not. As per my response, you don't <em>need</em> to have two dissectors for the same protocol, you just have one dissector that dissects all the messages for the protocol.</p></div><div id="comment-44796-info" class="comment-info"><span class="comment-age">(03 Aug '15, 10:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="44810"></span><div id="comment-44810" class="comment"><div id="post-44810-score" class="comment-score"></div><div class="comment-text"><p>I got it , thanks..</p></div><div id="comment-44810-info" class="comment-info"><span class="comment-age">(03 Aug '15, 23:16)</span> <span class="comment-user userinfo">zombimind</span></div></div></div><div id="comment-tools-44756" class="comment-tools"></div><div class="clear"></div><div id="comment-44756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

