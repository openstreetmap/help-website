+++
type = "question"
title = "Link-layer header unknown"
description = '''I have the Nordic BLE sniffer that connects to WireShark with &#92;.&#92;pipe&#92;wireshark_nordic_ble:(null). This had been working. Now WireShark doesn&#x27;t show any ble traffic that it did in the past even though the Nordic tool opens WireShark. I am looking in Capture Options and see the Link-layer header for ...'''
date = "2017-03-28T05:01:00Z"
lastmod = "2017-04-06T04:57:00Z"
weight = 60384
keywords = [ "link-layer", "blesniffer" ]
aliases = [ "/questions/60384" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Link-layer header unknown](/questions/60384/link-layer-header-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60384-score" class="post-score" title="current number of votes">0</div><span id="post-60384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the Nordic BLE sniffer that connects to WireShark with \.\pipe\wireshark_nordic_ble:(null). This had been working. Now WireShark doesn't show any ble traffic that it did in the past even though the Nordic tool opens WireShark.</p><p>I am looking in Capture Options and see the Link-layer header for the pipe is unknown. The pipe is enabled and there is no capture filter associated with it. So I have two questions,</p><p>What should the Link-layer header be and should there be a capture filter associated with this pipe?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-link-layer" rel="tag" title="see questions tagged &#39;link-layer&#39;">link-layer</span> <span class="post-tag tag-link-blesniffer" rel="tag" title="see questions tagged &#39;blesniffer&#39;">blesniffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '17, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/7ed6c9315b75f9e0f177249aa81d0e5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rbmisc&#39;s gravatar image" /><p><span>rbmisc</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rbmisc has no accepted answers">0%</span></p></div></div><div id="comments-container-60384" class="comments-container"></div><div id="comment-tools-60384" class="comment-tools"></div><div class="clear"></div><div id="comment-60384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60391"></span>

<div id="answer-container-60391" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60391-score" class="post-score" title="current number of votes">0</div><span id="post-60391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found that Cygwin64 installed something that caused the communications between ble-sniffer and WireShark to not occur. I removed Cygwin64 completely and the communications between these two devices is working again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '17, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/7ed6c9315b75f9e0f177249aa81d0e5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rbmisc&#39;s gravatar image" /><p><span>rbmisc</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rbmisc has no accepted answers">0%</span></p></div></div><div id="comments-container-60391" class="comments-container"><span id="60612"></span><div id="comment-60612" class="comment"><div id="post-60612-score" class="comment-score"></div><div class="comment-text"><p>Actually it was a limit of the sniffer I am using.</p></div><div id="comment-60612-info" class="comment-info"><span class="comment-age">(06 Apr '17, 04:57)</span> <span class="comment-user userinfo">rbmisc</span></div></div></div><div id="comment-tools-60391" class="comment-tools"></div><div class="clear"></div><div id="comment-60391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

