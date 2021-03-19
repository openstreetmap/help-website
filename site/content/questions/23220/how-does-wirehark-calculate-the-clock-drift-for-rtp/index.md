+++
type = "question"
title = "How does Wirehark calculate the clock drift for RTP?"
description = '''Hi, I made an rtp capture and obtained the following statistics : Max delta = 26,74 ms at packet no. 482  Max jitter = 0,94 ms. Mean jitter = 0,38 ms. Max skew = -6,65 ms. Total RTP packets = 92 (expected 92) Lost RTP packets = 0 (0,00%) Sequence errors = 0  Duration 8,20 s (-1842 ms clock drift, co...'''
date = "2013-07-22T03:58:00Z"
lastmod = "2013-07-22T03:58:00Z"
weight = 23220
keywords = [ "drift", "rtp", "clock" ]
aliases = [ "/questions/23220" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does Wirehark calculate the clock drift for RTP?](/questions/23220/how-does-wirehark-calculate-the-clock-drift-for-rtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23220-score" class="post-score" title="current number of votes">0</div><span id="post-23220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I made an rtp capture and obtained the following statistics :</p><pre><code>Max delta = 26,74 ms at packet no. 482 
Max jitter = 0,94 ms. Mean jitter = 0,38 ms.
Max skew = -6,65 ms.
Total RTP packets = 92   (expected 92)   Lost RTP packets = 0 (0,00%)   Sequence errors = 0 
Duration 8,20 s (-1842 ms clock drift, corresponding to 6203 Hz (-22,47%)</code></pre><p>I do not understand how it calculates -1842 ms clock drift since in the trace there is no difference between the timestamp of wireshark and the timestamp of the RTP stream. Both shows 8200 ms (8,20 s).</p><p>regards Bruno Scornet</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-drift" rel="tag" title="see questions tagged &#39;drift&#39;">drift</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-clock" rel="tag" title="see questions tagged &#39;clock&#39;">clock</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/77cdc7d79899b924448a9b8d8d7c7e19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruno&#39;s gravatar image" /><p><span>Bruno</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruno has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jul '13, 14:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-23220" class="comments-container"></div><div id="comment-tools-23220" class="comment-tools"></div><div class="clear"></div><div id="comment-23220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

