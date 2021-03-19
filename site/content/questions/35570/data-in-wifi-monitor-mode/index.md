+++
type = "question"
title = "Data in WiFi monitor mode"
description = '''I am using Ubuntu 14.04.1 with a TP-Link TL-WN722N WiFi adaptor. The network interface is configured in monitor mode by sudo airmon-ng start wlan1 so that I can capture all WiFi data. However I found that Wireshark only display the wireless packet as raw data, without analyse them to readable data. ...'''
date = "2014-08-19T04:43:00Z"
lastmod = "2014-08-19T11:24:00Z"
weight = 35570
keywords = [ "wifi", "analysis" ]
aliases = [ "/questions/35570" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Data in WiFi monitor mode](/questions/35570/data-in-wifi-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35570-score" class="post-score" title="current number of votes">1</div><span id="post-35570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Ubuntu 14.04.1 with a TP-Link TL-WN722N WiFi adaptor. The network interface is configured in monitor mode by <code>sudo airmon-ng start wlan1</code> so that I can capture all WiFi data.</p><p>However I found that Wireshark only display the wireless packet as raw data, without analyse them to readable data. (for example I do not know the detail in transport layer, TCP/UCP, IP address, etc)</p><p>How can I know the detail of the packet?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/d075420fd2ed7d78364856553fcbe705?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="garypty&#39;s gravatar image" /><p><span>garypty</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="garypty has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '14, 04:44</strong> </span></p></div></div><div id="comments-container-35570" class="comments-container"></div><div id="comment-tools-35570" class="comment-tools"></div><div class="clear"></div><div id="comment-35570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35591"></span>

<div id="answer-container-35591" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35591-score" class="post-score" title="current number of votes">0</div><span id="post-35591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is this a "protected" network, using WEP or WPA/WPA2?</p><p>If so, then the packets captured in monitor mode are encrypted, and <a href="http://wiki.wireshark.org/HowToDecrypt802.11">you will have to configure Wireshark to decrypt the traffic</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35591" class="comments-container"></div><div id="comment-tools-35591" class="comment-tools"></div><div class="clear"></div><div id="comment-35591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

