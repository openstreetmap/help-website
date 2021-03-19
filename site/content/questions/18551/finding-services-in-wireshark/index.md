+++
type = "question"
title = "Finding services in Wireshark?"
description = '''Hi all, I&#x27;m a Wireshark beginner and I have a question about it: How does one go about finding services in Wireshark, specifically, the question is asking &#x27;What services are running in the network capture?&#x27; Would this relate to the application layer and services that run within it? Any help would be...'''
date = "2013-02-12T07:00:00Z"
lastmod = "2013-02-12T07:22:00Z"
weight = 18551
keywords = [ "question", "beginner", "wireshark" ]
aliases = [ "/questions/18551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Finding services in Wireshark?](/questions/18551/finding-services-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18551-score" class="post-score" title="current number of votes">0</div><span id="post-18551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm a Wireshark beginner and I have a question about it:</p><p>How does one go about finding services in Wireshark, specifically, the question is asking 'What services are running in the network capture?'</p><p>Would this relate to the application layer and services that run within it? Any help would be greatly appreciated</p><p>Lambert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/18040f0433490722cf29121cead91571?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lambert84&#39;s gravatar image" /><p><span>Lambert84</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lambert84 has no accepted answers">0%</span></p></div></div><div id="comments-container-18551" class="comments-container"></div><div id="comment-tools-18551" class="comment-tools"></div><div class="clear"></div><div id="comment-18551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18553"></span>

<div id="answer-container-18553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18553-score" class="post-score" title="current number of votes">0</div><span id="post-18553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>'What services are running in the network capture?'</p></blockquote><p>'services' is not the right term in case of Wireshark. What you see in Wireshark is (mostly) TCP and UDP conversations. Some TCP/UDP ports (mail:25, http:80,ssh:22, etc.) are tied to 'services' (by convention). So, you need to know what TCP/UDP port your service/application is using and then you can filter for that.</p><p>You get a brief overview of protocols/ports/services by this:</p><blockquote><p><code>Statistics -&gt; Potocol Hierarchy</code><br />
</p></blockquote><p>If you need a more detailed view, you need to actually look at packets and <a href="http://wiki.wireshark.org/DisplayFilters">filter for whatever</a> you need.</p><p>If you need just an overview what is going on in your network, a network forensic tool may be better suited for you (e.g. <a href="http://sourceforge.net/projects/networkminer/">Network Miner</a>, <a href="http://www.xplico.org/">Xplico</a> or <a href="http://www.forensicswiki.org/wiki/Tools:Network_Forensics">similar</a>).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18553" class="comments-container"></div><div id="comment-tools-18553" class="comment-tools"></div><div class="clear"></div><div id="comment-18553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

