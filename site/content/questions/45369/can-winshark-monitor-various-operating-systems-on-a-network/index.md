+++
type = "question"
title = "Can Winshark monitor various operating systems on a network?"
description = '''I have Wireshark installed on a windows 7 computer in my home network. Is there a way to monitor the traffic coming from an Apple computer on the same network?'''
date = "2015-08-26T11:08:00Z"
lastmod = "2015-08-27T01:14:00Z"
weight = 45369
keywords = [ "applewindows" ]
aliases = [ "/questions/45369" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can Winshark monitor various operating systems on a network?](/questions/45369/can-winshark-monitor-various-operating-systems-on-a-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45369-score" class="post-score" title="current number of votes">0</div><span id="post-45369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark installed on a windows 7 computer in my home network. Is there a way to monitor the traffic coming from an Apple computer on the same network?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-applewindows" rel="tag" title="see questions tagged &#39;applewindows&#39;">applewindows</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '15, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/4dc7dc078f986caad55102642c634cc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ulman%20Zittof&#39;s gravatar image" /><p><span>Ulman Zittof</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ulman Zittof has no accepted answers">0%</span></p></div></div><div id="comments-container-45369" class="comments-container"></div><div id="comment-tools-45369" class="comment-tools"></div><div class="clear"></div><div id="comment-45369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45370"></span>

<div id="answer-container-45370" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45370-score" class="post-score" title="current number of votes">1</div><span id="post-45370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ulman Zittof has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can only capture the traffic that flows through the network interfaces in the capture machine.</p><p>If the devices in your home network are connected via WiFi, then you could capture that traffic using monitor mode, but unfortunately Windows (of any variety) is not a good platform for WiFi capture due to driver issues.</p><p>You could possibly capture on the router through which all traffic would normally flow in a home network, however most home routers are not able to capture traffic with the standard firmware, although some alternative firmwares do offer this capability.</p><p>See the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup">Capture Setup</a> for a starter on capturing traffic, along with its sub-pages for specific network types.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '15, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45370" class="comments-container"><span id="45373"></span><div id="comment-45373" class="comment"><div id="post-45373-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. Just one more question, would Ubuntu (or any other Linux platform)be better than Windows? Thanks in advance</p></div><div id="comment-45373-info" class="comment-info"><span class="comment-age">(26 Aug '15, 14:48)</span> <span class="comment-user userinfo">Ulman Zittof</span></div></div><span id="45388"></span><div id="comment-45388" class="comment"><div id="post-45388-score" class="comment-score"></div><div class="comment-text"><p>Probably, see the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">WLAN capture setup</a>.</p></div><div id="comment-45388-info" class="comment-info"><span class="comment-age">(27 Aug '15, 01:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-45370" class="comment-tools"></div><div class="clear"></div><div id="comment-45370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

