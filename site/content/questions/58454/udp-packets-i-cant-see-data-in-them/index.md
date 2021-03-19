+++
type = "question"
title = "UDP packets - i cant see data in them?"
description = '''Hi all,  first of all, I am very new to this so what i am about to ask could be stupid - i hope not tho. I am slef teaching. Anyway, I am trying to capture some traffic on my wifi from a messaging app I have installed and what it does is send the message to everyone using UDP. I can tell that the UD...'''
date = "2017-01-01T16:06:00Z"
lastmod = "2017-01-02T02:31:00Z"
weight = 58454
keywords = [ "udp" ]
aliases = [ "/questions/58454" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP packets - i cant see data in them?](/questions/58454/udp-packets-i-cant-see-data-in-them)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58454-score" class="post-score" title="current number of votes">0</div><span id="post-58454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>first of all, I am very new to this so what i am about to ask could be stupid - i hope not tho. I am slef teaching.</p><p>Anyway, I am trying to capture some traffic on my wifi from a messaging app I have installed and what it does is send the message to everyone using UDP. I can tell that the UDP packet contains the message as the packet size increases inline with the size of the message, but I dont know how to access the data to see the message within the UDP packet data section. - OR if it is encrypted and how I would tell what type?</p><p>I cant tell if I am doing something wrong or it is a lack of knowledge on my part.</p><p>Any help is appreciated.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '17, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/3a66bff78b5b7247a056155172920f79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newshark&#39;s gravatar image" /><p><span>newshark</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newshark has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-58454" class="comments-container"></div><div id="comment-tools-58454" class="comment-tools"></div><div class="clear"></div><div id="comment-58454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58458"></span>

<div id="answer-container-58458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58458-score" class="post-score" title="current number of votes">1</div><span id="post-58458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can show you what the packet data is, and if it knows the protocol used and has the required parameters, it is able to dissect that data. So it seems that Wireshark doesn't know the protocol of this messaging app, or doesn't have the required decryption parameters to decrypt it. Either way, that knowledge has to come from elsewhere, this information is not contained in the network data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '17, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58458" class="comments-container"></div><div id="comment-tools-58458" class="comment-tools"></div><div class="clear"></div><div id="comment-58458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

