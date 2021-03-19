+++
type = "question"
title = "Capturing messaged from a PLC"
description = '''My laptop is wired to a switch which is also wired to 2 Micrologix 1400 plc&#x27;s. About every 1/2 second one plc is getting data from the other via a message instruction over the ethernet/ip connection and I have verified that this is working properly online with the plc. I was trying to detect this in...'''
date = "2015-02-09T08:16:00Z"
lastmod = "2015-02-09T08:56:00Z"
weight = 39715
keywords = [ "bradley", "allen", "plc" ]
aliases = [ "/questions/39715" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing messaged from a PLC](/questions/39715/capturing-messaged-from-a-plc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39715-score" class="post-score" title="current number of votes">0</div><span id="post-39715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My laptop is wired to a switch which is also wired to 2 Micrologix 1400 plc's. About every 1/2 second one plc is getting data from the other via a message instruction over the ethernet/ip connection and I have verified that this is working properly online with the plc. I was trying to detect this information with wireshark but I'm not having any luck. I even tried a filter for the specific static plc address 10.250.0.130. I would be grateful for any suggestions to get me going in the proper direction.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bradley" rel="tag" title="see questions tagged &#39;bradley&#39;">bradley</span> <span class="post-tag tag-link-allen" rel="tag" title="see questions tagged &#39;allen&#39;">allen</span> <span class="post-tag tag-link-plc" rel="tag" title="see questions tagged &#39;plc&#39;">plc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/123339d8f5f40b450a8ae0d0827ffacd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wdfiller&#39;s gravatar image" /><p><span>wdfiller</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wdfiller has no accepted answers">0%</span></p></div></div><div id="comments-container-39715" class="comments-container"></div><div id="comment-tools-39715" class="comment-tools"></div><div class="clear"></div><div id="comment-39715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39716"></span>

<div id="answer-container-39716" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39716-score" class="post-score" title="current number of votes">0</div><span id="post-39716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wdfiller has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to have a look at <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p>(switches only forward frames to the port on which the destination mac address has been seen, so you need to take special action to see the frames in Wireshark)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '15, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39716" class="comments-container"><span id="39717"></span><div id="comment-39717" class="comment"><div id="post-39717-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that makes sense. I do have a managed switch so I will look into that solution.</p></div><div id="comment-39717-info" class="comment-info"><span class="comment-age">(09 Feb '15, 08:56)</span> <span class="comment-user userinfo">wdfiller</span></div></div></div><div id="comment-tools-39716" class="comment-tools"></div><div class="clear"></div><div id="comment-39716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

