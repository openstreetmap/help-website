+++
type = "question"
title = "Why retransmission occured before duplicated ACK ?"
description = '''Hi everyone,  I&#x27;m struggling with TCP analysis from my home lan network. I tried to understand which TCP version is implemented in my OS (Windows 8.1 in two computers) and how it&#x27;s working. I generated 7 TCP streams to get retransmissions. I think that my TCP version is TCP SACK. First of all, I got...'''
date = "2015-06-19T04:37:00Z"
lastmod = "2015-06-22T12:36:00Z"
weight = 43361
keywords = [ "dup-ack", "sack", "tcp", "retransmissions" ]
aliases = [ "/questions/43361" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why retransmission occured before duplicated ACK ?](/questions/43361/why-retransmission-occured-before-duplicated-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43361-score" class="post-score" title="current number of votes">0</div><span id="post-43361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I'm struggling with TCP analysis from my home lan network. I tried to understand which TCP version is implemented in my OS (Windows 8.1 in two computers) and how it's working. I generated 7 TCP streams to get retransmissions. I think that my TCP version is TCP SACK.</p><p>First of all, I got first retransmission because of the timeout elapsed (probably). <a href="http://pl.tinypic.com/r/2rra0lc/8">Picture</a> Next, I got duplicated ACK(1) and in this segment I got information about SLE = 1595113 and SRE = 1596573. SLE is a seq number of first TCP retransmission. Did I get information that retransmission was correct ?</p><p>This duplicated ACK(1) occured because there was one or more segments lost. After that I got another retransmission but not connected with that lost segment. Why I did not get retransmission connected with that loose ?</p><p>Finally, I got another duplicated ACK and there was not any reaction for that.</p><p>Could anybody tell me if I am thinking on the right way ?</p><p>Cheers !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-sack" rel="tag" title="see questions tagged &#39;sack&#39;">sack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '15, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/30da7d33d2decf0b14f4ca33b140c0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kub4ss&#39;s gravatar image" /><p><span>kub4ss</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kub4ss has no accepted answers">0%</span></p></div></div><div id="comments-container-43361" class="comments-container"><span id="43363"></span><div id="comment-43363" class="comment"><div id="post-43363-score" class="comment-score"></div><div class="comment-text"><p>Your questions aren't clear, probably due to the lack of a capture file.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox?</p><p>Also your picture link doesn't seem to show anything useful and then traps my browser in some AliExpress hell.</p></div><div id="comment-43363-info" class="comment-info"><span class="comment-age">(19 Jun '15, 05:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43417"></span><div id="comment-43417" class="comment"><div id="post-43417-score" class="comment-score"></div><div class="comment-text"><p>Here is a capture file: <a href="https://drive.google.com/open?id=0B_Xiotgqtz2Kck9GcEg1d09zM0k&amp;authuser=0">link</a></p></div><div id="comment-43417-info" class="comment-info"><span class="comment-age">(21 Jun '15, 14:14)</span> <span class="comment-user userinfo">kub4ss</span></div></div><span id="43418"></span><div id="comment-43418" class="comment"><div id="post-43418-score" class="comment-score">1</div><div class="comment-text"><p><span>@kub4ss</span>: I converted your answer to a comment, as that's how this Q&amp;A site works. Please read the FAQ!</p></div><div id="comment-43418-info" class="comment-info"><span class="comment-age">(21 Jun '15, 14:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-43361" class="comment-tools"></div><div class="clear"></div><div id="comment-43361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43458"></span>

<div id="answer-container-43458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43458-score" class="post-score" title="current number of votes">0</div><span id="post-43458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do I understnad you correct, that you are wondering about the DUP ACK of FRAME 10824? It is D-SACK for Frame 10456. But also it has the same SEQ und ACK number as the ACK 10638, but with the additional D-SACK options, so Wireshark interpreted it as a DUP ACK. (Maybe this could irritated you.)</p><p>There has been a quite similar thread here: <a href="https://ask.wireshark.org/questions/42878/tcp-sack-in-capture-shows-range-of-previous-segments-instead-of-subsequent">TCP SACK in capture shows range of previous segments instead of subsequent</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '15, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-43458" class="comments-container"></div><div id="comment-tools-43458" class="comment-tools"></div><div class="clear"></div><div id="comment-43458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

