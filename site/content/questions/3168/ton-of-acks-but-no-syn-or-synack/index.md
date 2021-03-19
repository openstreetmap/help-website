+++
type = "question"
title = "ton of ACKs but no SYN or SYN/ACK"
description = '''I thought I&#x27;d try to learn WireShark but have a quick question. I started it up and went to a couple sites then stopped it. In 13 seconds, I had over 20,000 lines of ACK packets with no SYN or SYN/ACKs anywhere. Is this a DoS ACK attempt? Anything to be worried about? Thanks!'''
date = "2011-03-27T21:16:00Z"
lastmod = "2011-03-31T18:28:00Z"
weight = 3168
keywords = [ "syn" ]
aliases = [ "/questions/3168" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ton of ACKs but no SYN or SYN/ACK](/questions/3168/ton-of-acks-but-no-syn-or-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3168-score" class="post-score" title="current number of votes">0</div><span id="post-3168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I thought I'd try to learn WireShark but have a quick question. I started it up and went to a couple sites then stopped it. In 13 seconds, I had over 20,000 lines of ACK packets with no SYN or SYN/ACKs anywhere. Is this a DoS ACK attempt? Anything to be worried about?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '11, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/c1cf6fc7fd7dd213e1833084e20a4bcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cdnsupguy&#39;s gravatar image" /><p><span>cdnsupguy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cdnsupguy has no accepted answers">0%</span></p></div></div><div id="comments-container-3168" class="comments-container"><span id="3193"></span><div id="comment-3193" class="comment"><div id="post-3193-score" class="comment-score"></div><div class="comment-text"><p>Is this a workstation or a public facing server? 20,000 ACKs in 13 seconds isn't excessive per se, it depends on the how busy the server is. Are you saying that you only saw ACKs in one way? Were these to servers you visited? Were you using any capture filters? (or display filters at that).</p></div><div id="comment-3193-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:48)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-3168" class="comment-tools"></div><div class="clear"></div><div id="comment-3168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3216"></span>

<div id="answer-container-3216" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3216-score" class="post-score" title="current number of votes">0</div><span id="post-3216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is just my regular home computer. No capture filters and yes, it seemed to be only ACKs one-way (only one part of the 3 way handshake). I was expecting to see the 2 other parts of the handshake in the list but don't see them anywhere. These were not to any servers or sites I visit or know about.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '11, 16:09</strong></p><img src="https://secure.gravatar.com/avatar/c1cf6fc7fd7dd213e1833084e20a4bcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cdnsupguy&#39;s gravatar image" /><p><span>cdnsupguy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cdnsupguy has no accepted answers">0%</span></p></div></div><div id="comments-container-3216" class="comments-container"><span id="3220"></span><div id="comment-3220" class="comment"><div id="post-3220-score" class="comment-score">1</div><div class="comment-text"><p>If it's your home PC, you definitely have a problem! You better get it scanned pronto!</p></div><div id="comment-3220-info" class="comment-info"><span class="comment-age">(29 Mar '11, 19:51)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="3260"></span><div id="comment-3260" class="comment"><div id="post-3260-score" class="comment-score"></div><div class="comment-text"><p>So what could it be? Seems like a DoS of some kind or could it be something else? I ran an updated AV scanner in Safe Mode as well as Spyware scanner and Rootkit detector which came back clean.</p></div><div id="comment-3260-info" class="comment-info"><span class="comment-age">(31 Mar '11, 17:09)</span> <span class="comment-user userinfo">cdnsupguy</span></div></div></div><div id="comment-tools-3216" class="comment-tools"></div><div class="clear"></div><div id="comment-3216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3261"></span>

<div id="answer-container-3261" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3261-score" class="post-score" title="current number of votes">0</div><span id="post-3261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So you want to learn how to use wireshark and perform network analysis, you say? OK, then dig in to it a little bit.</p><p>Where are these ACK's originating from, the local or remote host? What ports are you seeing on the local and remote hosts? What does netstat show you?</p><p>The only way to learn it is to do it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '11, 18:28</strong></p><img src="https://secure.gravatar.com/avatar/bbb8df45b4d304408e6a3cea6cac2233?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joeqwerty&#39;s gravatar image" /><p><span>joeqwerty</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joeqwerty has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Apr '11, 18:07</strong> </span></p></div></div><div id="comments-container-3261" class="comments-container"></div><div id="comment-tools-3261" class="comment-tools"></div><div class="clear"></div><div id="comment-3261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

