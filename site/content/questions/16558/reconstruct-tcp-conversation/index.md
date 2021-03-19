+++
type = "question"
title = "Reconstruct TCP conversation"
description = '''I am trying to reconstruct a TCP conversation from the first SYN to the FIN in order to troubleshoot an application response issue. If I use &quot;Follow TCP Stream&quot; in Wireshark, it starts from the first packet captured always. It doesn&#x27;t list time or number packets: it is very difficult to figure out I...'''
date = "2012-12-04T16:51:00Z"
lastmod = "2012-12-05T10:13:00Z"
weight = 16558
keywords = [ "tcp.stream" ]
aliases = [ "/questions/16558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reconstruct TCP conversation](/questions/16558/reconstruct-tcp-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16558-score" class="post-score" title="current number of votes">0</div><span id="post-16558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to reconstruct a TCP conversation from the first SYN to the FIN in order to troubleshoot an application response issue.</p><p>If I use "Follow TCP Stream" in Wireshark, it starts from the first packet captured always. It doesn't list time or number packets: it is very difficult to figure out</p><p>I need to be able to select a SYN packet from with the capture and then see all subsequent packets in the exchange. I am specifically looking at times of response, because ACKs seem to be losing ground and transmissions are slowing.</p><p>There must be an easier way to do this: any advice would be great.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 16:51</strong></p><img src="https://secure.gravatar.com/avatar/6291a08897e1cb21f4b194ebbb012766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Silas1066&#39;s gravatar image" /><p><span>Silas1066</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Silas1066 has no accepted answers">0%</span></p></div></div><div id="comments-container-16558" class="comments-container"></div><div id="comment-tools-16558" class="comment-tools"></div><div class="clear"></div><div id="comment-16558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16564"></span>

<div id="answer-container-16564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16564-score" class="post-score" title="current number of votes">1</div><span id="post-16564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Follow TCP Stream is basically a forensic feature, while also doing the filtering for the specific TCP conversation you are interested in.</p><p>I'd always recommend locating the SYN packet for the connection you're interested in, right-clicking on that SYN packet and then go for Conversation Filter -&gt; TCP.</p><p>This applies the same filter like follow TCP Steam does, without reconstructing payload data which in terms of network analysis should not be needed, except you're troubleshooting application issues within the layer +4 protocols.</p><p>Then in the filtered conversation set the time-reference on the first packet which is your SYN and then your relative times are nicely readable for that specific conversation. Be sure to apply the coloumn delta time displayed as well to quickly lookup inter-packet timings -&gt; this should fit your needs to analyse whats going on inside your TCP Session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-16564" class="comments-container"><span id="16594"></span><div id="comment-16594" class="comment"><div id="post-16594-score" class="comment-score"></div><div class="comment-text"><p>Landi:</p><p>If I select the SYN packet and go to Analyze--&gt;Conversation Filter</p><p>I don't see anything in there except two "greyed out" options: PN-AO etc.</p><p>Am I in the right place?</p></div><div id="comment-16594-info" class="comment-info"><span class="comment-age">(05 Dec '12, 07:29)</span> <span class="comment-user userinfo">Silas1066</span></div></div><span id="16600"></span><div id="comment-16600" class="comment"><div id="post-16600-score" class="comment-score"></div><div class="comment-text"><p><span>@Silas1066</span>: I converted your answer to a comment due to the rules of this Q&amp;A site.</p><p>You right-click on the SYN packet right at where you spot in in the packet list and in the context menu you find Conversation Filter -&gt; TCP</p></div><div id="comment-16600-info" class="comment-info"><span class="comment-age">(05 Dec '12, 10:13)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-16564" class="comment-tools"></div><div class="clear"></div><div id="comment-16564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

