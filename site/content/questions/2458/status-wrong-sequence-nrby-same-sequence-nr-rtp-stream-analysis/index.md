+++
type = "question"
title = "Status: Wrong Sequence Nr.by Same Sequence Nr. = RTP Stream Analysis"
description = '''Hi guys, I really apprictae, if you can support me with my challenge. I am capturing RTPs and analyse the stream, I am facing the issue getting 2 sequences with the same nr., which has one the status &quot;OK&quot; and the next status`&quot;wrong sequence nr.&quot;. How can I sort them only on &quot;OK&quot; sequences? Thx'''
date = "2011-02-21T13:09:00Z"
lastmod = "2011-02-22T06:23:00Z"
weight = 2458
keywords = [ "wireshark" ]
aliases = [ "/questions/2458" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Status: Wrong Sequence Nr.by Same Sequence Nr. = RTP Stream Analysis](/questions/2458/status-wrong-sequence-nrby-same-sequence-nr-rtp-stream-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2458-score" class="post-score" title="current number of votes">0</div><span id="post-2458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I really apprictae, if you can support me with my challenge. I am capturing RTPs and analyse the stream, I am facing the issue getting 2 sequences with the same nr., which has one the status "OK" and the next status`"wrong sequence nr.".</p><p>How can I sort them only on "OK" sequences?</p><p>Thx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '11, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/3057867f6aaee6adcac69f83d02c42d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza666&#39;s gravatar image" /><p><span>reza666</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza666 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Feb '11, 13:09</strong> </span></p></div></div><div id="comments-container-2458" class="comments-container"></div><div id="comment-tools-2458" class="comment-tools"></div><div class="clear"></div><div id="comment-2458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="2461"></span>

<div id="answer-container-2461" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2461-score" class="post-score" title="current number of votes">0</div><span id="post-2461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have to trace to try it at the moment, but you can try to highlight the line in the decode where it is saying "Sequence OK" and using the popup menu to select "Apply as filter -&gt; selected". That should give you just the packets where the sequence is OK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '11, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2461" class="comments-container"></div><div id="comment-tools-2461" class="comment-tools"></div><div class="clear"></div><div id="comment-2461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2467"></span>

<div id="answer-container-2467" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2467-score" class="post-score" title="current number of votes">0</div><span id="post-2467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hey man Thx for anwer,</p><p>I am in the Wireshark:RTP Stream Anylysis windows. I have following schama:</p><h2 id="packet-sequence-delat-filtered-jitter-skew-ip-bw-status">Packet sequence Delat Filtered Jitter Skew IP BW Status</h2><p>53 2729 0,00 0,00 0,00 2,24 [ok] 54 2729 0,25 0,02 -0,25 4,48 Wrong sequence nr. 55 2730 29,96 0,02 -0,21 6,72 [ok] 56 2730 0,21 0,03 -0,42 8,96 Wrong sequence nr. .... ..... .... ....</p><p>So I have not the possibility to apply [ok] as a filter and sort all OKs. I can just Save palyload, Save as CSV, ...., Graf, Player,....</p><p>Where do you mean to apply the filter for good OKs?</p><p>Rezzzaa<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '11, 21:36</strong></p><img src="https://secure.gravatar.com/avatar/3057867f6aaee6adcac69f83d02c42d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza666&#39;s gravatar image" /><p><span>reza666</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza666 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-2467" class="comments-container"></div><div id="comment-tools-2467" class="comment-tools"></div><div class="clear"></div><div id="comment-2467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2469"></span>

<div id="answer-container-2469" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2469-score" class="post-score" title="current number of votes">0</div><span id="post-2469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>These packets with wrong seq. are packet loss. Now how can I filter a capture without packet loss? Thx</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '11, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/3057867f6aaee6adcac69f83d02c42d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza666&#39;s gravatar image" /><p><span>reza666</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza666 has no accepted answers">0%</span></p></div></div><div id="comments-container-2469" class="comments-container"></div><div id="comment-tools-2469" class="comment-tools"></div><div class="clear"></div><div id="comment-2469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2476"></span>

<div id="answer-container-2476" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2476-score" class="post-score" title="current number of votes">0</div><span id="post-2476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>how can i upload a file here?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/3057867f6aaee6adcac69f83d02c42d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza666&#39;s gravatar image" /><p><span>reza666</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza666 has no accepted answers">0%</span></p></div></div><div id="comments-container-2476" class="comments-container"></div><div id="comment-tools-2476" class="comment-tools"></div><div class="clear"></div><div id="comment-2476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

