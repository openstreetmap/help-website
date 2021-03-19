+++
type = "question"
title = "WLAN Traffic Statistics did not show SSID"
description = '''Hello, I am using debian and Wireshark Version 1.12.1. I see my wlan network traffic,but I would also like to see other SSID traffic. WLAN Traffic Statistics shows nothing. Is my wlan adapter not running in sniffer mode or what can I do?'''
date = "2017-06-25T11:29:00Z"
lastmod = "2017-06-25T12:17:00Z"
weight = 62286
keywords = [ "wlan", "ssid", "statistic" ]
aliases = [ "/questions/62286" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WLAN Traffic Statistics did not show SSID](/questions/62286/wlan-traffic-statistics-did-not-show-ssid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62286-score" class="post-score" title="current number of votes">0</div><span id="post-62286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am using debian and Wireshark Version 1.12.1. I see my wlan network traffic,but I would also like to see other SSID traffic. WLAN Traffic Statistics shows nothing. Is my wlan adapter not running in sniffer mode or what can I do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-ssid" rel="tag" title="see questions tagged &#39;ssid&#39;">ssid</span> <span class="post-tag tag-link-statistic" rel="tag" title="see questions tagged &#39;statistic&#39;">statistic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '17, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/2a286fc711918bda6278a6b7fe762651?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crankma&#39;s gravatar image" /><p><span>crankma</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crankma has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jun '17, 13:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span></p></div></div><div id="comments-container-62286" class="comments-container"></div><div id="comment-tools-62286" class="comment-tools"></div><div class="clear"></div><div id="comment-62286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62287"></span>

<div id="answer-container-62287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62287-score" class="post-score" title="current number of votes">0</div><span id="post-62287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are some requirements to capture other 802.11 traffic besides your own. There is a good starting point here:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p><p>There are many details that could come into play, but I would start with this link. If you need an easy way to get into, and out of, monitor mode, you can have a look at the scripts provided by the aircrack-ng suite of tools:</p><p><a href="http://www.aircrack-ng.org/doku.php?id=airmon-ng">http://www.aircrack-ng.org/doku.php?id=airmon-ng</a></p><p>This site has a lot of Q&amp;As regarding some of the finer points so when you are up and running you can search here to troubleshoot further.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '17, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-62287" class="comments-container"></div><div id="comment-tools-62287" class="comment-tools"></div><div class="clear"></div><div id="comment-62287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

