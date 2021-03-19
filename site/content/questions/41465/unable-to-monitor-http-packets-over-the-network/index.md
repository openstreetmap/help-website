+++
type = "question"
title = "Unable to monitor http packets over the network"
description = '''Hello, I have used WireShark to monitor our network for about 2 years now. Normally when we are at a very high bandwidth peak I will logon to my remote machine and do some packet capturing. Recently when I have loged in and tried to do some monitoring I am not able to see the HTTP address. I just se...'''
date = "2015-04-15T13:19:00Z"
lastmod = "2015-04-17T07:43:00Z"
weight = 41465
keywords = [ "capture", "http", "network", "packet", "monitor" ]
aliases = [ "/questions/41465" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to monitor http packets over the network](/questions/41465/unable-to-monitor-http-packets-over-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41465-score" class="post-score" title="current number of votes">0</div><span id="post-41465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have used WireShark to monitor our network for about 2 years now. Normally when we are at a very high bandwidth peak I will logon to my remote machine and do some packet capturing. Recently when I have loged in and tried to do some monitoring I am not able to see the HTTP address. I just see one IP now.</p><p>Under HTTP Requests by Server Address I see 239.255.255.250 which I see is used for UPNP.</p><p>How come I was able to look through all the web addresses before but I no longer can?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '15, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/96452beac7951e359dbe8a29b430403c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bohlingj&#39;s gravatar image" /><p><span>bohlingj</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bohlingj has no accepted answers">0%</span></p></div></div><div id="comments-container-41465" class="comments-container"></div><div id="comment-tools-41465" class="comment-tools"></div><div class="clear"></div><div id="comment-41465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41492"></span>

<div id="answer-container-41492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41492-score" class="post-score" title="current number of votes">1</div><span id="post-41492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How come I was able to look through all the web addresses before but I no longer can?</p></blockquote><p>I don't know, but if I had to guess, I would say: because somebody changed the capture setup, which led to the situation where your capturing system does not see the traffic any longer. Example: Somebody modified (or restored) the switch configuration, which disabled the port mirroring, or somebody replaced the switch altogether, etc.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '15, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41492" class="comments-container"><span id="41539"></span><div id="comment-41539" class="comment"><div id="post-41539-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, I figured out that one of the ports changed on the switch and I had to redo the port mirroring. Once I changed that and fixed that back up things were good to go.</p><p>THanks for the help!</p></div><div id="comment-41539-info" class="comment-info"><span class="comment-age">(17 Apr '15, 07:23)</span> <span class="comment-user userinfo">bohlingj</span></div></div><span id="41541"></span><div id="comment-41541" class="comment"><div id="post-41541-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41541-info" class="comment-info"><span class="comment-age">(17 Apr '15, 07:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41492" class="comment-tools"></div><div class="clear"></div><div id="comment-41492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

