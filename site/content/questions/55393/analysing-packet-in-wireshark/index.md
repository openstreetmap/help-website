+++
type = "question"
title = "Analysing packet in wireshark"
description = '''Is wireshark included application layer attachment.Basically I want to ask is it attaching the information above the network layer ? If it is so how to analyze it ? Ultimately How do we come to know that there are other headers are attacked with packet on wireshark ?'''
date = "2016-09-08T07:18:00Z"
lastmod = "2016-09-11T22:49:00Z"
weight = 55393
keywords = [ "wirepack", "packets", "analysis" ]
aliases = [ "/questions/55393" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Analysing packet in wireshark](/questions/55393/analysing-packet-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55393-score" class="post-score" title="current number of votes">0</div><span id="post-55393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Is wireshark included application layer attachment.Basically I want to ask is it attaching the information above the network layer ?</p><p>If it is so how to analyze it ?</p><p>Ultimately How do we come to know that there are other headers are attacked with packet on wireshark ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wirepack" rel="tag" title="see questions tagged &#39;wirepack&#39;">wirepack</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '16, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/fe46f9a9147da796d172745b5d4fe71d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avani%20badheka&#39;s gravatar image" /><p><span>avani badheka</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avani badheka has no accepted answers">0%</span></p></div></div><div id="comments-container-55393" class="comments-container"></div><div id="comment-tools-55393" class="comment-tools"></div><div class="clear"></div><div id="comment-55393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55397"></span>

<div id="answer-container-55397" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55397-score" class="post-score" title="current number of votes">0</div><span id="post-55397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="avani badheka has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes there is. Above the network layer (eg. IP) there are transport layer protocols which are dissected (eg. TCP, UDP, etc). Even layers above that are dissected (eg. SMB, FTP, HTTP, etc.), and in some cases even above that, allowing you to export objects and streams communicated with these protocols (eg. SMB, RTP voice, etc.). As soon as Wireshark knows about these protocols it tries to dissect them, given that dissection is properly configured. This varies per protocol and dissector.</p><p>In short, the higher you come in the network stack, the less complete Wireshark is. It main strengths lay in the lower layer protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '16, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55397" class="comments-container"><span id="55477"></span><div id="comment-55477" class="comment"><div id="post-55477-score" class="comment-score"></div><div class="comment-text"><p>thank you , Is there any probability that OS is going to attached some headers with packets ? like at kernel side is it attach some own headers ?</p></div><div id="comment-55477-info" class="comment-info"><span class="comment-age">(11 Sep '16, 22:49)</span> <span class="comment-user userinfo">avani badheka</span></div></div></div><div id="comment-tools-55397" class="comment-tools"></div><div class="clear"></div><div id="comment-55397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

