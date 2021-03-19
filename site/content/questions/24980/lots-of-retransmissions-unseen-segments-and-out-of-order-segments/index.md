+++
type = "question"
title = "Lots of retransmissions, unseen segments and out of order segments"
description = '''Hi I am capturing some traffic from multiple 10G interfaces to a laptop connected at 1Gbs. If applied a capture filter to specifically look for the IPs I need to investgate. In my capture files I see a lot of retransmissions, unseen segments and out-of-order segements. Is it possible that wireshark ...'''
date = "2013-09-20T00:38:00Z"
lastmod = "2013-09-22T16:36:00Z"
weight = 24980
keywords = [ "unseen_segment", "retransmissions", "out-of-order" ]
aliases = [ "/questions/24980" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lots of retransmissions, unseen segments and out of order segments](/questions/24980/lots-of-retransmissions-unseen-segments-and-out-of-order-segments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24980-score" class="post-score" title="current number of votes">0</div><span id="post-24980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am capturing some traffic from multiple 10G interfaces to a laptop connected at 1Gbs. If applied a capture filter to specifically look for the IPs I need to investgate. In my capture files I see a lot of retransmissions, unseen segments and out-of-order segements. Is it possible that wireshark is seeing these due to packets getting lost to to the overload of the 1GBs connection? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unseen_segment" rel="tag" title="see questions tagged &#39;unseen_segment&#39;">unseen_segment</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '13, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/6389c211ec05b85529186bd45d63fd6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="murawai&#39;s gravatar image" /><p><span>murawai</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="murawai has no accepted answers">0%</span></p></div></div><div id="comments-container-24980" class="comments-container"></div><div id="comment-tools-24980" class="comment-tools"></div><div class="clear"></div><div id="comment-24980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24983"></span>

<div id="answer-container-24983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24983-score" class="post-score" title="current number of votes">2</div><span id="post-24983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most certainly you have lost frames due to</p><ul><li>the device that's aggregateing several 10G links to one 1G link is unable to do that (way too much traffic)</li><li>your laptop gets all frames, but is unable to write everything to disk</li></ul><p>Your capture setup seems to be kind of under-sized for that kind of environment!</p><p>You could try to add filters on the aggregating device (n x 10G -&gt; 1G) to limit the amount of traffic. However, that is no guarantee to overrun the 1G link.</p><p>If the laptop is the source of the problem, the only option is to get a device that is capable to handle a fully utilized 1G link.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Sep '13, 01:02</strong> </span></p></div></div><div id="comments-container-24983" class="comments-container"><span id="25081"></span><div id="comment-25081" class="comment"><div id="post-25081-score" class="comment-score"></div><div class="comment-text"><p>Hi - thanks it does sound likely &amp; would make sense for the "TCP ACKed unseen segment" - however just to be sure can you confirm this would also explains why wireshark is seeing so many retransmissions, also out-of-order packets? If it makes sense for all these then thats great, I just did't want to ignore these "errors" if there was no sensible reason. Much appreciate your assistance Cheers</p></div><div id="comment-25081-info" class="comment-info"><span class="comment-age">(22 Sep '13, 16:23)</span> <span class="comment-user userinfo">murawai</span></div></div><span id="25082"></span><div id="comment-25082" class="comment"><div id="post-25082-score" class="comment-score"></div><div class="comment-text"><blockquote><p>however just to be sure can you confirm this would also explains why wireshark is seeing so many retransmissions, also out-of-order packets?</p></blockquote><p>without looking at the capture file neither can I confirm that nor can I decline it. Can you post a small sample capture file somewhere (google docs, dropbox, cloudshark)?</p></div><div id="comment-25082-info" class="comment-info"><span class="comment-age">(22 Sep '13, 16:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24983" class="comment-tools"></div><div class="clear"></div><div id="comment-24983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

