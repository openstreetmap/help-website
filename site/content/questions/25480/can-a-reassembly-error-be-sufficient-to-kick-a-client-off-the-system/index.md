+++
type = "question"
title = "Can a Reassembly error be sufficient to kick a client off the system"
description = '''We have over 50,000 users on an enterprise application and on occasion users submit a request and the spinning wheel commences and after some time they are kicked out. This is a datacentric databases application that is several tiers deep. The common thread seems to be   This would not be enough to ...'''
date = "2013-10-01T10:13:00Z"
lastmod = "2013-10-07T16:53:00Z"
weight = 25480
keywords = [ "reassembly", "error" ]
aliases = [ "/questions/25480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can a Reassembly error be sufficient to kick a client off the system](/questions/25480/can-a-reassembly-error-be-sufficient-to-kick-a-client-off-the-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25480-score" class="post-score" title="current number of votes">0</div><span id="post-25480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have over 50,000 users on an enterprise application and on occasion users submit a request and the spinning wheel commences and after some time they are kicked out. This is a datacentric databases application that is several tiers deep. The common thread seems to be <img src="https://osqa-ask.wireshark.org/upfiles/10-1-2013_12-58-21_PM.jpg" alt="alt text" /> This would not be enough to kick someone off the system?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/10-1-2013_1-10-46_PM.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '13, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/16c80ca493c77f3486cbb7ff38cc5d3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoberist&#39;s gravatar image" /><p><span>Zoberist</span><br />
<span class="score" title="0 reputation points">0</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoberist has no accepted answers">0%</span></p></img></div></div><div id="comments-container-25480" class="comments-container"></div><div id="comment-tools-25480" class="comment-tools"></div><div class="clear"></div><div id="comment-25480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25739"></span>

<div id="answer-container-25739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25739-score" class="post-score" title="current number of votes">0</div><span id="post-25739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>This would not be enough to kick someone off the system?</p></blockquote><p>hard/impossible to tell, just by looking at a screenshot of a single frame ;-) Can you please post a capture file (anonymized with <a href="http://www.tracewrangler.com/">tracewrangler</a>) somewhere (google docs, dropbox, cloudshark)?</p><p>Wireshark seems to see a retransmission and thinks it has seen the same data before, possibly in some fragmented frames (at least that's how I interpret the message).</p><p>If that's really the case, that could (or could not) cause problems in the TCP stack of your server and/or client. If it causes problems, you should see a RESET or FIN shortly after that error message. If however, the TCP conversation (that single tcp stream) continues to exchange data, you can (most certainly) ignore the error message, at least for the problem you are describing.</p><blockquote><p>and on occasion users submit a request and the spinning wheel commences and after some time they are kicked out.</p></blockquote><p>There might be other systems that kick a connection, like Firewalls (state table time out) and Load Balancers (state table time out or session persistence time out). I guess you have both in place for that kind of application. If so, you'll need parallel captures in front of the clients and in front of the server(s). With those capture files, you'll be able to figure out if any intermediate device tampers with your connections.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 16:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-25739" class="comments-container"></div><div id="comment-tools-25739" class="comment-tools"></div><div class="clear"></div><div id="comment-25739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

