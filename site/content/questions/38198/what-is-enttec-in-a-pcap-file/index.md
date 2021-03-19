+++
type = "question"
title = "what is ENTTEC IN A PCAP FILE"
description = '''i am seeing ENTTEC HEAD unknown so what basically ENTTEC IS :---- BELOW I S THE IMAGE'''
date = "2014-11-26T23:39:00Z"
lastmod = "2014-11-27T11:51:00Z"
weight = 38198
keywords = [ "ethernet", "tcpip" ]
aliases = [ "/questions/38198" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what is ENTTEC IN A PCAP FILE](/questions/38198/what-is-enttec-in-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38198-score" class="post-score" title="current number of votes">0</div><span id="post-38198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am seeing ENTTEC HEAD unknown so what basically ENTTEC IS :----<img src="https://osqa-ask.wireshark.org/upfiles/Capture_uF2vHKF.PNG" alt="alt text" /></p><p>BELOW I S THE IMAGE</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-tcpip" rel="tag" title="see questions tagged &#39;tcpip&#39;">tcpip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '14, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/eb6cd3260fd5969d287b352fffcb7059?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manish%20Rajput&#39;s gravatar image" /><p><span>Manish Rajput</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manish Rajput has no accepted answers">0%</span></p></img></div></div><div id="comments-container-38198" class="comments-container"></div><div id="comment-tools-38198" class="comment-tools"></div><div class="clear"></div><div id="comment-38198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38216"></span>

<div id="answer-container-38216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38216-score" class="post-score" title="current number of votes">1</div><span id="post-38216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's an indication that the dissector for <a href="http://www.enttec.com/docs/enttec_protocol.pdf">ENTTEC's DMX on Ethernet protocol</a> needs to be fixed so that TCP packets that <em>happen</em> to use the same port number as that protocol, but that don't appear to be DMX-on-Ethernet packets, don't get dissected as DMX-on-Ethernet packets.</p><p>Unlike, for example, Ethernet type values, TCP and UDP ports are not guaranteed to be reliable indications of the protocol being used, so there's always the chance that Wireshark will misidentify protocols running on top of TCP or UDP. There are ways in which "false positives", such as identifying traffic to or from port 3333 as DMX-on-Ethernet packets, can be reduced.</p><p>Please file a bug on this at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, so we can keep track of it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-38216" class="comments-container"></div><div id="comment-tools-38216" class="comment-tools"></div><div class="clear"></div><div id="comment-38216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

