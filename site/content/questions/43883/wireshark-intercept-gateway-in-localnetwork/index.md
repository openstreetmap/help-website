+++
type = "question"
title = "Wireshark intercept gateway in localnetwork."
description = '''In localnetwork 20 computers, my ip 192.168.0.77. Gateway address 192.168.0.1. I need to know who visits the site &quot;http://abcdef.ua/ and intercept all data. Please help me set up Wireshark and filter interception.'''
date = "2015-07-06T04:09:00Z"
lastmod = "2015-07-06T05:55:00Z"
weight = 43883
keywords = [ "localnetwork", "gateway" ]
aliases = [ "/questions/43883" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark intercept gateway in localnetwork.](/questions/43883/wireshark-intercept-gateway-in-localnetwork)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43883-score" class="post-score" title="current number of votes">0</div><span id="post-43883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In localnetwork 20 computers, my ip 192.168.0.77. Gateway address 192.168.0.1. I need to know who visits the site "http://abcdef.ua/ and intercept all data. Please help me set up Wireshark and filter interception.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-localnetwork" rel="tag" title="see questions tagged &#39;localnetwork&#39;">localnetwork</span> <span class="post-tag tag-link-gateway" rel="tag" title="see questions tagged &#39;gateway&#39;">gateway</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '15, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/c2c6bfd733c637bca41395437da09d63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbrshark&#39;s gravatar image" /><p><span>cbrshark</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbrshark has no accepted answers">0%</span></p></div></div><div id="comments-container-43883" class="comments-container"></div><div id="comment-tools-43883" class="comment-tools"></div><div class="clear"></div><div id="comment-43883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43885"></span>

<div id="answer-container-43885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43885-score" class="post-score" title="current number of votes">0</div><span id="post-43885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The best way to capture the traffic:</p><ol><li>Configure the switch for port mirroring (aka SPAN) on the gateway's Ethernet interface to the switch. In case you do not have a managed switch, then refer to the link below on the Wireshark wiki regarding Ethernet capturing: <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></li><li>In Wireshark, setup a capture option (Capture / Options) and create a capture filter: host www.abcdef.ua</li></ol><p>This filter will capture traffic to and from the IP address associated with the website.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-43885" class="comments-container"></div><div id="comment-tools-43885" class="comment-tools"></div><div class="clear"></div><div id="comment-43885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

