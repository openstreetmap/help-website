+++
type = "question"
title = "Is WIRESHARK capable for non network devices for WINDOWS"
description = '''Hi,  This is Karun from india(Hyderabad).I want to use wireshark for non network device(some raw device) to reach my requirement that to redirect the packets coming to raw device to the wireshark application in WINDOWS Platform.If so can you guys help me to find out where packet parsing happening ,w...'''
date = "2015-05-25T05:50:00Z"
lastmod = "2015-05-25T06:10:00Z"
weight = 42648
keywords = [ "capabilities" ]
aliases = [ "/questions/42648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is WIRESHARK capable for non network devices for WINDOWS](/questions/42648/is-wireshark-capable-for-non-network-devices-for-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42648-score" class="post-score" title="current number of votes">0</div><span id="post-42648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, This is Karun from india(Hyderabad).I want to use wireshark for non network device(some raw device) to reach my requirement that to redirect the packets coming to raw device to the wireshark application in WINDOWS Platform.If so can you guys help me to find out where packet parsing happening ,what format its expecting to transmit and receive(Location) in your source code.I had taken latest wireshark source code for windows.</p><p>Thanks, Karun.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capabilities" rel="tag" title="see questions tagged &#39;capabilities&#39;">capabilities</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '15, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/50c4b78862c6ca806916c3a71498cdf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karun256&#39;s gravatar image" /><p><span>karun256</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karun256 has no accepted answers">0%</span></p></div></div><div id="comments-container-42648" class="comments-container"></div><div id="comment-tools-42648" class="comment-tools"></div><div class="clear"></div><div id="comment-42648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42649"></span>

<div id="answer-container-42649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42649-score" class="post-score" title="current number of votes">0</div><span id="post-42649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you need the development release of Wireshark and extcap.</p><p>Extcap allows external "capturing" programs to present a configuration UI in wireshark and then pass captured data back to Wireshark using a pipe and is aimed to work on all the platforms Wireshark runs on.</p><p>Unfortunately there isn't much documentation on extcap at this time, there is an example extcap program in the sources under <code>docs\extcap_example.py</code> and a <a href="https://sharkfest.wireshark.org/sharkfest.13/presentations/NAP-11_Expanding-Wireshark-Beyond-Ethernet-and-Network-Interfaces_Kershaw-Ryan.pdf">SharkFest 2013 presentation</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '15, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42649" class="comments-container"></div><div id="comment-tools-42649" class="comment-tools"></div><div class="clear"></div><div id="comment-42649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

