+++
type = "question"
title = "Does wireshark have a BSON dissector?"
description = '''I&#x27;ve got a network protocol that uses BSON over TLS, and I&#x27;d like to dissect the BSON. I can decrypt the TLS session correctly, but the only protocol option I can use successfully is &quot;data&quot;, which displays just the hex. Is there a BSON dissector that I can use to decrypt the &quot;Application Data&quot; insid...'''
date = "2013-11-20T12:16:00Z"
lastmod = "2013-11-20T16:17:00Z"
weight = 27178
keywords = [ "dissector" ]
aliases = [ "/questions/27178" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does wireshark have a BSON dissector?](/questions/27178/does-wireshark-have-a-bson-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27178-score" class="post-score" title="current number of votes">0</div><span id="post-27178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got a network protocol that uses BSON over TLS, and I'd like to dissect the BSON. I can decrypt the TLS session correctly, but the only protocol option I can use successfully is "data", which displays just the hex.</p><p>Is there a BSON dissector that I can use to decrypt the "Application Data" inside a TLS session?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/8f9c683775bfbe76ed4855a19b73dc81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roger%20Lipscombe&#39;s gravatar image" /><p><span>Roger Lipscombe</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roger Lipscombe has no accepted answers">0%</span></p></div></div><div id="comments-container-27178" class="comments-container"></div><div id="comment-tools-27178" class="comment-tools"></div><div class="clear"></div><div id="comment-27178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27183"></span>

<div id="answer-container-27183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27183-score" class="post-score" title="current number of votes">0</div><span id="post-27183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does wireshark have a BSON dissector?</p></blockquote><p>Yes and No.</p><p>There is a BSON dissector, however it's (only) part of the dissector for the MongoDB wire protocol.</p><p>So, if you're using BSON directly over TLS, you won't be able to dissect that with Wireshark as it's not structured like the MongoDB wire protocol.</p><p>If you need a 'generic' BSON dissector these are your options:</p><ul><li>Take a look at the MongoDB dissector (packet-mongo.c) and try to build your own BSON dissector based on the that code</li><li>File an enhancement 'bug' at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and add a sample capture file.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 16:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27183" class="comments-container"></div><div id="comment-tools-27183" class="comment-tools"></div><div class="clear"></div><div id="comment-27183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

