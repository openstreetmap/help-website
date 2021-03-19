+++
type = "question"
title = "Improving performance"
description = '''Hi all, I am using tshark to sniff HTTP content on a very busy server and I see that the CPU usage of the tshark process is very high. This is the command line I am using: tshark.exe -i3 -l -f &quot;tcp port 80&quot; -O http -d tcp.port==80,http -o &quot;ip.use_geoip:FALSE&quot; -R &quot;not tcp.analysis.duplicate_ack&quot; -T f...'''
date = "2013-03-04T11:34:00Z"
lastmod = "2013-03-05T12:48:00Z"
weight = 19135
keywords = [ "performance" ]
aliases = [ "/questions/19135" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Improving performance](/questions/19135/improving-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19135-score" class="post-score" title="current number of votes">0</div><span id="post-19135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am using tshark to sniff HTTP content on a very busy server and I see that the CPU usage of the tshark process is very high.</p><p>This is the command line I am using:</p><p>tshark.exe -i3 -l -f "tcp port 80" -O http -d tcp.port==80,http -o "ip.use_geoip:FALSE" -R "not tcp.analysis.duplicate_ack" -T fields -e ip.host -e tcp.port -e http.request.full_uri -e http.request.method -e http.response.code -e http.response.phrase -e http.content_length -e data -e text -E separator=;2&gt;&amp;0</p><p>Is there anything I can do to get the same result - but with better performance? Can anyone point to any part of the command line that might be the reason for the high CPU usage?</p><p>Thanks</p><p>David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '13, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/0b0ac57ffe8e8e5747c4b0f5595a521f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Sackstein&#39;s gravatar image" /><p><span>David Sackstein</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Sackstein has no accepted answers">0%</span></p></div></div><div id="comments-container-19135" class="comments-container"></div><div id="comment-tools-19135" class="comment-tools"></div><div class="clear"></div><div id="comment-19135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19138"></span>

<div id="answer-container-19138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19138-score" class="post-score" title="current number of votes">0</div><span id="post-19138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wow, this is some tshark command line. I assume you need the <code>-l</code> because you pipe the output to another tool or script? I think you can leave out the <code>-O http</code> bit, since you later on as for specific fields using <code>-T</code>. I also think you can leave out the <code>-d tcp.port==80,http</code> bit, it's rather obvious tcp port 80 traffic is HTTP, at least that's what the HTTP dissector assumes. I'm not sure these would improve performance though. I recon taking out the <code>-R</code> filter would.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '13, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19138" class="comments-container"></div><div id="comment-tools-19138" class="comment-tools"></div><div class="clear"></div><div id="comment-19138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19174"></span>

<div id="answer-container-19174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19174-score" class="post-score" title="current number of votes">0</div><span id="post-19174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there anything I can do to get the same result - but with better performance?</p></blockquote><p>please try this:</p><blockquote><p><code>tshark.exe -n -i3</code><br />
</p></blockquote><p>instead of</p><blockquote><p><code>tshark.exe -i3</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-19174" class="comments-container"><span id="19177"></span><div id="comment-19177" class="comment"><div id="post-19177-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Thanks for this tip. Is the order of the options actually important too? Must -n be before -i3? Thanks David</p></div><div id="comment-19177-info" class="comment-info"><span class="comment-age">(05 Mar '13, 12:41)</span> <span class="comment-user userinfo">David Sackstein</span></div></div><span id="19179"></span><div id="comment-19179" class="comment"><div id="post-19179-score" class="comment-score"></div><div class="comment-text"><p>The order does not matter.</p></div><div id="comment-19179-info" class="comment-info"><span class="comment-age">(05 Mar '13, 12:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-19174" class="comment-tools"></div><div class="clear"></div><div id="comment-19174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

