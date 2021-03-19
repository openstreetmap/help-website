+++
type = "question"
title = "Producing jitter values with tshark"
description = '''Hi all, is it at all possible with tshark to scan a pcap file, and like the -z rtp,streams flag, find the RTP streams, and then output the jitter and delta values for each packet? I basically want the same CSV that in wireshark you can get from telephony -&amp;gt; rtp -&amp;gt; Analysis -&amp;gt; save as CSV, b...'''
date = "2012-11-14T14:15:00Z"
lastmod = "2012-11-14T15:28:00Z"
weight = 15913
keywords = [ "jitter", "tshark", "voip", "rtp" ]
aliases = [ "/questions/15913" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Producing jitter values with tshark](/questions/15913/producing-jitter-values-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15913-score" class="post-score" title="current number of votes">0</div><span id="post-15913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, is it at all possible with tshark to scan a pcap file, and like the -z rtp,streams flag, find the RTP streams, and then output the jitter and delta values for each packet?</p><p>I basically want the same CSV that in wireshark you can get from telephony -&gt; rtp -&gt; Analysis -&gt; save as CSV, but from tshark, I'll be using tshark in a script to produce RRD graphs for VOIP monitoring purposes.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jitter" rel="tag" title="see questions tagged &#39;jitter&#39;">jitter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '12, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/59b893c7eed4cc041ce4a1679f5e85e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StrangeAttractor&#39;s gravatar image" /><p><span>StrangeAttra...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StrangeAttractor has no accepted answers">0%</span></p></div></div><div id="comments-container-15913" class="comments-container"></div><div id="comment-tools-15913" class="comment-tools"></div><div class="clear"></div><div id="comment-15913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15915"></span>

<div id="answer-container-15915" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15915-score" class="post-score" title="current number of votes">0</div><span id="post-15915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="StrangeAttractor has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hi all, is it at all possible with tshark ....</p></blockquote><p>Currently that functionality is not implemented in tshark.</p><p>Maybe the following tool can help you. It's written in Perl and will read pcap files.</p><blockquote><p><code>https://trac.uninett.no/qstream</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15915" class="comments-container"><span id="15917"></span><div id="comment-15917" class="comment"><div id="post-15917-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, I'll investigate qstream!</p></div><div id="comment-15917-info" class="comment-info"><span class="comment-age">(14 Nov '12, 15:28)</span> <span class="comment-user userinfo">StrangeAttra...</span></div></div></div><div id="comment-tools-15915" class="comment-tools"></div><div class="clear"></div><div id="comment-15915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

