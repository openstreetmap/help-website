+++
type = "question"
title = "Does wireshark capture the packet if the packet was dropped at ethernet layer?"
description = '''If suppose two parties are involved in a network communication over UDP/IP say P1 and P2. For a query made by P2, P1 responds with the response. If for some reason, the response was dropped by P2 at ethernet layer, does the wireshark running on P2&#x27;s machine capture the response? Thanks in advance.'''
date = "2012-11-28T22:58:00Z"
lastmod = "2012-11-29T01:27:00Z"
weight = 16411
keywords = [ "packet-capture" ]
aliases = [ "/questions/16411" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does wireshark capture the packet if the packet was dropped at ethernet layer?](/questions/16411/does-wireshark-capture-the-packet-if-the-packet-was-dropped-at-ethernet-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16411-score" class="post-score" title="current number of votes">0</div><span id="post-16411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If suppose two parties are involved in a network communication over UDP/IP say P1 and P2. For a query made by P2, P1 responds with the response. If for some reason, the response was dropped by P2 at ethernet layer, does the wireshark running on P2's machine capture the response?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '12, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/17f793d4032c6825b28b621d7e713874?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SantoshB&#39;s gravatar image" /><p><span>SantoshB</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SantoshB has no accepted answers">0%</span></p></div></div><div id="comments-container-16411" class="comments-container"></div><div id="comment-tools-16411" class="comment-tools"></div><div class="clear"></div><div id="comment-16411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16412"></span>

<div id="answer-container-16412" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16412-score" class="post-score" title="current number of votes">1</div><span id="post-16412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, if wireshark is running on P2, it will only see the packets that the NIC forwards to the OS, so if the NIC already drops the packet, then Wireshark won't see it.</p><p>That's one of the reasons why using a TAP or a spanport are preferred when analyzing network problems :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '12, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-16412" class="comments-container"><span id="16413"></span><div id="comment-16413" class="comment"><div id="post-16413-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYN-bit for the information.</p></div><div id="comment-16413-info" class="comment-info"><span class="comment-age">(29 Nov '12, 01:27)</span> <span class="comment-user userinfo">SantoshB</span></div></div></div><div id="comment-tools-16412" class="comment-tools"></div><div class="clear"></div><div id="comment-16412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

