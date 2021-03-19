+++
type = "question"
title = "How can I check if there was a lot of interference on wireless channel?"
description = '''I have a cap file, and I want to check whether there actually was much interference in the wireless channel. Is there a way to do this using Wireshark? I guess there is no PPI information, because if I filter for PPI, I don&#x27;t get any information. Any other way to get some information about the inter...'''
date = "2017-04-19T11:43:00Z"
lastmod = "2017-04-19T13:18:00Z"
weight = 60896
keywords = [ "wireless", "filter", "wlan" ]
aliases = [ "/questions/60896" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I check if there was a lot of interference on wireless channel?](/questions/60896/how-can-i-check-if-there-was-a-lot-of-interference-on-wireless-channel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60896-score" class="post-score" title="current number of votes">0</div><span id="post-60896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a cap file, and I want to check whether there actually was much interference in the wireless channel. Is there a way to do this using Wireshark? I guess there is no PPI information, because if I filter for PPI, I don't get any information. Any other way to get some information about the interference in the wireless channel?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/beddb281beb413dd524bca66f5e99dc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whatever&#39;s gravatar image" /><p><span>whatever</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whatever has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Apr '17, 13:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-60896" class="comments-container"></div><div id="comment-tools-60896" class="comment-tools"></div><div class="clear"></div><div id="comment-60896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60901"></span>

<div id="answer-container-60901" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60901-score" class="post-score" title="current number of votes">1</div><span id="post-60901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you get from radiotap, PPI, or other radio metadata headers is information that the Wi-Fi adapter reports. I don't think they explicitly report "hey, there's a lot of interference"; you <em>might</em> be able to infer it from the rate of CRC errors, but CRC errors aren't necessarily due to interference, and I'm not sure that interference would always cause CRC errors instead of, for example, a failure to start receiving a packet.</p><p><a href="http://www.networkcomputing.com/wireless-infrastructure/wifi-spectrum-analysis-uncovering-rf-interference/210360782">This article in Network Computing</a> speaks of spectrum analyzers as being useful tools for detecting interference; it also says</p><blockquote><p>A common question regarding spectrum analysis is why can’t the built-in, or USB, WiFi adapter be used for spectrum analysis?</p><p>It boils down to the limitations of WiFi adapters; they’re unable to demodulate non-WiFi signals.</p><p>When a WiFi device wants to communicate, it will perform clear channel assessment (CCA) to determine whether the shared medium is busy -- basically, seeing if any RF energy is detected. The kicker is that WiFi adapters can only hear WiFi energy, meaning other WiFi devices such as laptops, tablets, mobile phones, and WiFi cameras. Built-in WiFi cards cannot understand microwave signals or cordless phones transmitting on 2.4 GHz.</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '17, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-60901" class="comments-container"></div><div id="comment-tools-60901" class="comment-tools"></div><div class="clear"></div><div id="comment-60901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

