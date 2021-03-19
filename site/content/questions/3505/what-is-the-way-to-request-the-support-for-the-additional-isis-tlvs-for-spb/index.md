+++
type = "question"
title = "What is the way to request the support for the additional ISIS TLVs for SPB?"
description = '''IANA just resgiter a new series of ISIS TLVs to support SPB based on the draft: http://tools.ietf.org/html/draft-ietf-isis-ieee-aq-05 The SPB tlvs are listed under IANA ISIS codepoints at http://www.iana.org/assignments/isis-tlv-codepoints/isis-tlv-codepoints.xml Please advise the procedure to reque...'''
date = "2011-04-14T18:47:00Z"
lastmod = "2011-04-16T15:04:00Z"
weight = 3505
keywords = [ "isis", "tlv" ]
aliases = [ "/questions/3505" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the way to request the support for the additional ISIS TLVs for SPB?](/questions/3505/what-is-the-way-to-request-the-support-for-the-additional-isis-tlvs-for-spb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3505-score" class="post-score" title="current number of votes">0</div><span id="post-3505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>IANA just resgiter a new series of ISIS TLVs to support SPB based on the draft: http://tools.ietf.org/html/draft-ietf-isis-ieee-aq-05</p><p>The SPB tlvs are listed under IANA ISIS codepoints at http://www.iana.org/assignments/isis-tlv-codepoints/isis-tlv-codepoints.xml</p><p>Please advise the procedure to request the support of those within wireshark.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-isis" rel="tag" title="see questions tagged &#39;isis&#39;">isis</span> <span class="post-tag tag-link-tlv" rel="tag" title="see questions tagged &#39;tlv&#39;">tlv</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '11, 18:47</strong></p><img src="https://secure.gravatar.com/avatar/64171163f8e6bbcb03b6c3498389db51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edgard&#39;s gravatar image" /><p><span>Edgard</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edgard has no accepted answers">0%</span></p></div></div><div id="comments-container-3505" class="comments-container"></div><div id="comment-tools-3505" class="comment-tools"></div><div class="clear"></div><div id="comment-3505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3506"></span>

<div id="answer-container-3506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3506-score" class="post-score" title="current number of votes">2</div><span id="post-3506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>All enhancement requests can be done on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>. Please mark your request as an enhancement request (severity) and provide the link towards the protocol specification (just like you did in this Question). It will be of great help if you can attach a capture file showing the new TLV's.</p><p>Please note that there is no guarantee to if and when the new TLV's will be added, as all work is done on a voluntary basis. If you really need this functionality, you might consider finding someone to write the dissector code for you (and preferably submit it to the Wireshark repository).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '11, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3506" class="comments-container"><span id="3531"></span><div id="comment-3531" class="comment"><div id="post-3531-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I'll do</p></div><div id="comment-3531-info" class="comment-info"><span class="comment-age">(16 Apr '11, 07:35)</span> <span class="comment-user userinfo">Edgard</span></div></div><span id="3535"></span><div id="comment-3535" class="comment"><div id="post-3535-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", that's the way this Q&amp;A site works best, see also the FAQ. Please also accept an "answer" if it did indeed answer your question so that your question will not be listed on the unanswered questions list anymore)</p></div><div id="comment-3535-info" class="comment-info"><span class="comment-age">(16 Apr '11, 15:04)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-3506" class="comment-tools"></div><div class="clear"></div><div id="comment-3506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

