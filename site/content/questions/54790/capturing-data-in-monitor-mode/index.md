+++
type = "question"
title = "Capturing data in monitor mode"
description = '''Is there a way to capture data in monitor mode? When I try capturing in monitor mode, I only get beacon frames and some packets that say Null function (no data). Is there a way to see TCP or HTTP layer data while capturing in monitor mode? My OS is Fedora 24. Related question: I don&#x27;t really know mu...'''
date = "2016-08-14T04:52:00Z"
lastmod = "2016-08-14T05:47:00Z"
weight = 54790
keywords = [ "promiscuous-mode", "data", "monitor-mode" ]
aliases = [ "/questions/54790" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing data in monitor mode](/questions/54790/capturing-data-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54790-score" class="post-score" title="current number of votes">0</div><span id="post-54790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to capture data in monitor mode? When I try capturing in monitor mode, I only get beacon frames and some packets that say <code>Null function (no data)</code>.</p><p>Is there a way to see TCP or HTTP layer data while capturing in monitor mode? My OS is Fedora 24.</p><p>Related question: I don't really know much about adapters/drivers, but is it possible for monitor mode to work while promiscuous mode doesn't?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous-mode" rel="tag" title="see questions tagged &#39;promiscuous-mode&#39;">promiscuous-mode</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-monitor-mode" rel="tag" title="see questions tagged &#39;monitor-mode&#39;">monitor-mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '16, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/bf6e2a137be7b8bd13d1f8efec703554?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="devil0150&#39;s gravatar image" /><p><span>devil0150</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="devil0150 has no accepted answers">0%</span></p></div></div><div id="comments-container-54790" class="comments-container"></div><div id="comment-tools-54790" class="comment-tools"></div><div class="clear"></div><div id="comment-54790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54791"></span>

<div id="answer-container-54791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54791-score" class="post-score" title="current number of votes">0</div><span id="post-54791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><blockquote><p>I don't really know much about adapters/drivers, but is it possible for monitor mode to work while promiscuous mode doesn't?</p></blockquote></blockquote><p>Yes, this is common. Depends on wireless hardware you are using along with the driver. If in this mode, you would see all broadcast and multicast traffic, but no unicast traffic from other wireless clients. You mention Null - there are several types of Null frames, e.g. Null, QoS-Null, etc., but these are typically unicast. Since you don't provide a trace, I can't be sure exactly what you are seeing. So you may be seeing unicast traffic, but perhaps it is encrypted? Look for Data-type frames, like QoS Data and the like with a unicast destination MAC address to distinguish what state you are in.</p><p>It is also possible to see all WiFi traffic, though it may need to be decrypted for you to see TCP or HTTP traffic. First step is to make sure it is all present, i.e. you see unicast traffic along with broadcast/multicast and then work on a plan to decrypt. The Wireshark website has good notes on decryption if using WPA2-Personal, or, for a test, remove encryption altogether and then the IP, transport, and application layers should be apparent. I don't recommend to run like this for long, but only as a test.</p><p>These types of questions come up often here, so search and you will find lots of information.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '16, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-54791" class="comments-container"></div><div id="comment-tools-54791" class="comment-tools"></div><div class="clear"></div><div id="comment-54791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

