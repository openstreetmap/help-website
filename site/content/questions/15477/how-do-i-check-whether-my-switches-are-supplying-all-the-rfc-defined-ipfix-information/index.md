+++
type = "question"
title = "How do I check whether my switches are supplying all the RFC-defined IPFIX information"
description = '''Okay, so to fine-tune my add-on &quot;me too&quot; reply, I&#x27;m not looking for a &quot;Follow ___ stream&quot; capability, so much as being able to decipher the IETF IPFIX implementation. In my situation today, I&#x27;m needing to detect whether my Nortel Ethernet switches are, in fact, providing info for all the rfc-defined...'''
date = "2012-11-01T12:18:00Z"
lastmod = "2012-11-01T13:50:00Z"
weight = 15477
keywords = [ "ipfix" ]
aliases = [ "/questions/15477" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I check whether my switches are supplying all the RFC-defined IPFIX information](/questions/15477/how-do-i-check-whether-my-switches-are-supplying-all-the-rfc-defined-ipfix-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15477-score" class="post-score" title="current number of votes">0</div><span id="post-15477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Okay, so to fine-tune my add-on "me too" reply, I'm not looking for a "Follow ___ stream" capability, so much as being able to decipher the IETF IPFIX implementation. In my situation today, I'm needing to detect whether my Nortel Ethernet switches are, in fact, providing info for all the rfc-defined/formatted fields.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipfix" rel="tag" title="see questions tagged &#39;ipfix&#39;">ipfix</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '12, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/84bb605805bd40c918befa510e126541?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BWB8771&#39;s gravatar image" /><p><span>BWB8771</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BWB8771 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>01 Nov '12, 12:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-15477" class="comments-container"><span id="15479"></span><div id="comment-15479" class="comment"><div id="post-15479-score" class="comment-score"></div><div class="comment-text"><p>"Decipher" in the sense of "understand the RFCs" or "decipher" in the sense of "decode the packets"? Wireshark can't help you much with the former; does its dissection of IPFIX packets not sufficiently decode the packets?</p></div><div id="comment-15479-info" class="comment-info"><span class="comment-age">(01 Nov '12, 12:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-15477" class="comment-tools"></div><div class="clear"></div><div id="comment-15477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15480"></span>

<div id="answer-container-15480" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15480-score" class="post-score" title="current number of votes">0</div><span id="post-15480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, As far as I know, Nortel only uses Netflow v9 and calls it IPFIX. The reason for this is that they legally could not use the term NetFlow as it is a Cisco trademark. Unless something has changed very recently, Nortel switches are NOT RFC compliant IPFIX exporters. More proof here: <a href="http://www.plixer.com/blog/netflow/nortel-switches-and-ipfix-a-mixed-message/">http://www.plixer.com/blog/netflow/nortel-switches-and-ipfix-a-mixed-message/</a></p><p>-Mike Krygeris</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/2e0d708e65e4859b35d15d7ee56f5522?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkrygeri&#39;s gravatar image" /><p><span>mkrygeri</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkrygeri has no accepted answers">0%</span></p></div></div><div id="comments-container-15480" class="comments-container"></div><div id="comment-tools-15480" class="comment-tools"></div><div class="clear"></div><div id="comment-15480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

