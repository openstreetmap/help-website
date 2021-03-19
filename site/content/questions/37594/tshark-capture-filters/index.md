+++
type = "question"
title = "TShark Capture Filters"
description = '''Is it possible to set a Capture Filter for a specific MAC address destination and for only frames that contain HTTP data? When I try the filter &quot;-f wlan.da==XX:XX:XX:XX:XX:XX&quot; tshark returns the error &quot;Invalid capture filter &quot;wlan.da==68:9C:70:28:FF:C0&quot; for interface&quot;. This works as a Display Filter...'''
date = "2014-11-05T09:57:00Z"
lastmod = "2014-11-06T05:32:00Z"
weight = 37594
keywords = [ "capture-filter", "display-filter" ]
aliases = [ "/questions/37594" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TShark Capture Filters](/questions/37594/tshark-capture-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37594-score" class="post-score" title="current number of votes">0</div><span id="post-37594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to set a Capture Filter for a specific MAC address destination and for only frames that contain HTTP data?</p><p>When I try the filter "-f wlan.da==XX:XX:XX:XX:XX:XX" tshark returns the error "Invalid capture filter "wlan.da==68:9C:70:28:FF:C0" for interface".</p><p>This works as a Display Filter. Is there an advantage to a Capture Filter over a Display Filter?</p><p>I haven't been able to find anything for the HTTP Data filter.</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '14, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/cd84182756c41ff09be94e2961752880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdDickens&#39;s gravatar image" /><p><span>EdDickens</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdDickens has no accepted answers">0%</span></p></div></div><div id="comments-container-37594" class="comments-container"></div><div id="comment-tools-37594" class="comment-tools"></div><div class="clear"></div><div id="comment-37594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37601"></span>

<div id="answer-container-37601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37601-score" class="post-score" title="current number of votes">1</div><span id="post-37601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to set a Capture Filter for a specific MAC address destination and for only frames that contain HTTP data?</p></blockquote><p>No, but</p><pre><code>wlan dst 68:9C:70:28:FF:C0 and tcp port 80</code></pre><p>will get you all traffic to or from TCP port 80 and to MAC address 68:9C:70:28:FF:C0. You can add other ports, e.g.</p><pre><code>wlan dst 68:9C:70:28:FF:C0 and (tcp port 80 or tcp port 8080 or tcp port 443 or ...)</code></pre><blockquote><p>Is there an advantage to a Capture Filter over a Display Filter?</p></blockquote><p>The packets are discarded very early in the capture process, so that if the network on which you're capturing is a very high-traffic network, you're less likely to drop packets, as the packets deemed un-interesting are discarded before they take up space in the system's packet capture buffer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '14, 21:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37601" class="comments-container"><span id="37616"></span><div id="comment-37616" class="comment"><div id="post-37616-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy.</p><p>That seems to have done the trick.</p></div><div id="comment-37616-info" class="comment-info"><span class="comment-age">(06 Nov '14, 05:32)</span> <span class="comment-user userinfo">EdDickens</span></div></div></div><div id="comment-tools-37601" class="comment-tools"></div><div class="clear"></div><div id="comment-37601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

