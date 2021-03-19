+++
type = "question"
title = "Implementing an stream dissector for an Packet-DataPackets-Response stream"
description = '''Hi,  I&#x27;m implementing an LUA dissector for an protocol that is implemented with   RequestPacket, {RequestDataPacket} * n, {ResponseDataPacket} * n , ResponsePacket.  Requests / Responses might be interleaved with different Transaction-IDs. To dissect the Response correctly I need to access the match...'''
date = "2016-05-15T03:51:00Z"
lastmod = "2016-05-30T07:53:00Z"
weight = 52588
keywords = [ "dissector" ]
aliases = [ "/questions/52588" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Implementing an stream dissector for an Packet-DataPackets-Response stream](/questions/52588/implementing-an-stream-dissector-for-an-packet-datapackets-response-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52588-score" class="post-score" title="current number of votes">0</div><span id="post-52588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm implementing an LUA dissector for an protocol that is implemented with</p><pre><code>  RequestPacket, {RequestDataPacket} * n, {ResponseDataPacket} * n , ResponsePacket.</code></pre><p>Requests / Responses might be interleaved with different Transaction-IDs.</p><p>To dissect the Response correctly I need to access the matching Request type.</p><p>How can I pass on the request types?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '16, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/4875dbde2eebdc54b43edef7b9c29473?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20E&#39;s gravatar image" /><p><span>Thomas E</span><br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas E has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '16, 03:52</strong> </span></p></div></div><div id="comments-container-52588" class="comments-container"></div><div id="comment-tools-52588" class="comment-tools"></div><div class="clear"></div><div id="comment-52588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52589"></span>

<div id="answer-container-52589" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52589-score" class="post-score" title="current number of votes">0</div><span id="post-52589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Thomas E has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to use a global (i.e. not local to the dissection function) table holding the translations of the transaction ID (possibly combined with some additional information if the transaction IDs may roll over in a short time) to the associated request type. When dissecting requests, your dissection function would fill this table; when dissecting responses, it would use it to fetch the request type for the known transaction id. You would declare the table in the part of your Lua script where you create the protocol fields (i.e. before describing the dissector function itself).</p><p>The name of such table should begin with the name of the protocol (like <code>MyProto_Request_Type_by_TxnID</code>) merely to avoid conflicts in the common namespace shared by all Lua scripts.</p><p>Unfortunately, you cannot save space (which would be desirable) by dropping each item from the table as soon as it has been used once, because after the initial first-to-last dissection pass, a dissector for any packet may be invoked multiple times and in random order.</p><p>And the part of your dissecting function dealing with responses has to handle gracefully the situation when no request matching the response has been captured (due to mid-transaction start of capture, packet loss, ...).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '16, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '16, 05:26</strong> </span></p></div></div><div id="comments-container-52589" class="comments-container"><span id="53052"></span><div id="comment-53052" class="comment"><div id="post-53052-score" class="comment-score"></div><div class="comment-text"><p>The number of streams is kind of limited compared to todays computing resources, so the approach worked fine. Used in <a href="https://github.com/tengelmeier/mtp-tools/.">https://github.com/tengelmeier/mtp-tools/.</a></p></div><div id="comment-53052-info" class="comment-info"><span class="comment-age">(30 May '16, 07:53)</span> <span class="comment-user userinfo">Thomas E</span></div></div></div><div id="comment-tools-52589" class="comment-tools"></div><div class="clear"></div><div id="comment-52589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

