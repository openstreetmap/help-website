+++
type = "question"
title = "Find which port Identified the protocol (find calling direction of a packet)"
description = '''I want to determine the connection direction from a single packet data. The only way I can think about is - if I can know which is the known port number Wireshark used to determine the protocol name. Is there a way to get this information from the pdml ?  for example: SNMP packet uses port 161.  so ...'''
date = "2016-02-06T21:04:00Z"
lastmod = "2016-02-10T00:23:00Z"
weight = 49938
keywords = [ "directions", "pdml" ]
aliases = [ "/questions/49938" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Find which port Identified the protocol (find calling direction of a packet)](/questions/49938/find-which-port-identified-the-protocol-find-calling-direction-of-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49938-score" class="post-score" title="current number of votes">0</div><span id="post-49938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to determine the connection direction from a single packet data. The only way I can think about is - if I can know which is the known port number Wireshark used to determine the protocol name.</p><p>Is there a way to get this information from the pdml ?</p><p>for example: SNMP packet uses port 161. so if I have a packet that src is 161 and dest is 4567 I can detemine this is server to client packet. It will not always be truth, but I think in general 95% of the packets I'll get it right.</p><p>How can I tell which is the known port in a pdml ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '16, 21:04</strong></p><img src="https://secure.gravatar.com/avatar/b50e05a5f1954d250dd908dacce081c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kdani&#39;s gravatar image" /><p><span>kdani</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kdani has no accepted answers">0%</span></p></div></div><div id="comments-container-49938" class="comments-container"></div><div id="comment-tools-49938" class="comment-tools"></div><div class="clear"></div><div id="comment-49938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50042"></span>

<div id="answer-container-50042" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50042-score" class="post-score" title="current number of votes">1</div><span id="post-50042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kdani has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't directly do that from the PDML. The <em>only</em> thing you can do is see which of the two port numbers is lower; that number is <em>probably</em> the right one. However, note that not all servers have port numbers assigned to them; in that case, you're out of luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '16, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50042" class="comments-container"><span id="50044"></span><div id="comment-50044" class="comment"><div id="post-50044-score" class="comment-score"></div><div class="comment-text"><p>you confirm my feats ;-) but wireshark does know which port defines the selected protocol, it just doesn't export it to the pdml. If I had this knowledge I can easily guess and usually guess right the packet direction. (it decides it's http, based on the fact that one of the ports is 80....)</p></div><div id="comment-50044-info" class="comment-info"><span class="comment-age">(10 Feb '16, 00:23)</span> <span class="comment-user userinfo">kdani</span></div></div></div><div id="comment-tools-50042" class="comment-tools"></div><div class="clear"></div><div id="comment-50042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49944"></span>

<div id="answer-container-49944" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49944-score" class="post-score" title="current number of votes">0</div><span id="post-49944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have look at <code>packet_info.match_uint</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '16, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-49944" class="comments-container"><span id="50038"></span><div id="comment-50038" class="comment"><div id="post-50038-score" class="comment-score"></div><div class="comment-text"><p>I have no such value in my pdml</p></div><div id="comment-50038-info" class="comment-info"><span class="comment-age">(09 Feb '16, 21:44)</span> <span class="comment-user userinfo">kdani</span></div></div></div><div id="comment-tools-49944" class="comment-tools"></div><div class="clear"></div><div id="comment-49944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

