+++
type = "question"
title = "Associating synchrophasor config2 frame with data frame"
description = '''I am using wireshark to capture synchrophasor data. However, the config2 frame is sent over a separate TCP port, and the data frame is sent over a separate UDP port. Is it possible to associate the config2 frame with the data frame(s) in this situation? I have seen it work when the two are sent over...'''
date = "2012-11-29T14:04:00Z"
lastmod = "2012-11-30T08:06:00Z"
weight = 16442
keywords = [ "synchrophasor" ]
aliases = [ "/questions/16442" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Associating synchrophasor config2 frame with data frame](/questions/16442/associating-synchrophasor-config2-frame-with-data-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16442-score" class="post-score" title="current number of votes">0</div><span id="post-16442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark to capture synchrophasor data. However, the config2 frame is sent over a separate TCP port, and the data frame is sent over a separate UDP port.</p><p>Is it possible to associate the config2 frame with the data frame(s) in this situation?</p><p>I have seen it work when the two are sent over the same port.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-synchrophasor" rel="tag" title="see questions tagged &#39;synchrophasor&#39;">synchrophasor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '12, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/ccb3d212d1e69518e87ab49f737bb55f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vgharpure&#39;s gravatar image" /><p><span>vgharpure</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vgharpure has no accepted answers">0%</span></p></div></div><div id="comments-container-16442" class="comments-container"></div><div id="comment-tools-16442" class="comment-tools"></div><div class="clear"></div><div id="comment-16442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16468"></span>

<div id="answer-container-16468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16468-score" class="post-score" title="current number of votes">0</div><span id="post-16468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like you are using TCP/UDP for your synchrophasor stream, where command frames from the receiving end start and stop the stream at the sending end.</p><p>In my experience, when using TCP/UDP for synchrophasor streaming, the config2 frame is only sent once by the sending end, over TCP, in response to the command frame from the receiving end. Wireshark needs to be listening before the receiving end sends the command frame to the sending end.</p><p>In contrast to TCP/UDP, spontaneous UDP includes the config2 frame in the data stream once per minute (in my experience), which makes it easy to use the Wireshark synchrophasor decoder.</p><p>My experience is limited, so there's probably a better answer to be had, but I think that unless you are at the receiving end, and can turn the stream off and then back on while Wireshark listens, you're probably out of luck. Even then, I don't know about telling the synchrophasor decoder to look in the TCP stream for the config2 frame. The synchrophasor decoder may not work that way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '12, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/660a9e09a8d894eb57457f8c39087d4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slsturgi&#39;s gravatar image" /><p><span>slsturgi</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slsturgi has no accepted answers">0%</span></p></div></div><div id="comments-container-16468" class="comments-container"></div><div id="comment-tools-16468" class="comment-tools"></div><div class="clear"></div><div id="comment-16468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

