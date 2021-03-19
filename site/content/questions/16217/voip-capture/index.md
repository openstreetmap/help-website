+++
type = "question"
title = "Voip Capture"
description = '''Hi, I made this capture and i want to understand it: Max delta = 35.92 ms at packet no. 83135  Max jitter = 3.91 ms. Mean jitter = 1.03 ms. Max skew = 26.09 ms. Total RTP packets = 1436 (expected 1436) Lost RTP packets = -2872 (-200.00%) Sequence errors = 2872  Duration 28.68 s (-17389 ms clock drif...'''
date = "2012-11-22T07:56:00Z"
lastmod = "2012-11-23T04:27:00Z"
weight = 16217
keywords = [ "rtp", "voip" ]
aliases = [ "/questions/16217" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Voip Capture](/questions/16217/voip-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16217-score" class="post-score" title="current number of votes">0</div><span id="post-16217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I made this capture and i want to understand it:</p><pre><code>Max delta = 35.92 ms at packet no. 83135 
Max jitter = 3.91 ms. Mean jitter = 1.03 ms.
Max skew = 26.09 ms.
Total RTP packets = 1436 (expected 1436) Lost RTP packets = -2872 (-200.00%) Sequence errors = 2872 
Duration 28.68 s (-17389 ms clock drift, corresponding to 3149 Hz (-60.63%),</code></pre>what does it mean this?? why is -200.00%, and why sequence error? Cuz previously capture from another side, percent represent the amount of lost, but positive not negative like in this case. VoIP quality is good. So i just wanna know what this means.</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '12, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/fcf0bcb2aff6ee8c5d98906e2fa9b72c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asantana&#39;s gravatar image" /><p><span>asantana</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asantana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '12, 22:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-16217" class="comments-container"></div><div id="comment-tools-16217" class="comment-tools"></div><div class="clear"></div><div id="comment-16217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16234"></span>

<div id="answer-container-16234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16234-score" class="post-score" title="current number of votes">0</div><span id="post-16234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It means that you spanned a vlan and you captured the media packets twice, once in ingress, once on egress.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 22:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16234" class="comments-container"><span id="16242"></span><div id="comment-16242" class="comment"><div id="post-16242-score" class="comment-score"></div><div class="comment-text"><p>ok. There's a way to obtain normal results, i mean average over 0%? cuz i really wish to know the lost of voip packets</p></div><div id="comment-16242-info" class="comment-info"><span class="comment-age">(23 Nov '12, 04:27)</span> <span class="comment-user userinfo">asantana</span></div></div></div><div id="comment-tools-16234" class="comment-tools"></div><div class="clear"></div><div id="comment-16234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

