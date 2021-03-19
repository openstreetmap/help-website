+++
type = "question"
title = "Need to find which IP address is taking  most bandwith usage in my network"
description = '''Using Wireshark, is there any possibility to check which IP address is using more bandwidth in my network?'''
date = "2012-04-02T08:13:00Z"
lastmod = "2012-04-02T14:07:00Z"
weight = 9900
keywords = [ "bandwidth" ]
aliases = [ "/questions/9900" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Need to find which IP address is taking most bandwith usage in my network](/questions/9900/need-to-find-which-ip-address-is-taking-most-bandwith-usage-in-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9900-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark, is there any possibility to check which IP address is using more bandwidth in my network?</p></div><div id="question-tags" class="tags-container tags">bandwidth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '12, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/c10742b15beca2fd871828ccdee554bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arasu&#39;s gravatar image" /><p>arasu<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arasu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Apr '12, 11:00</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9900" class="comments-container"></div><div id="comment-tools-9900" class="comment-tools"></div><div class="clear"></div><div id="comment-9900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9902"></span>

<div id="answer-container-9902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9902-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try looking at Statistics -&gt; Endpoints, then choose the IPv4 (or IPv6) tab. You can sort by any of the columns. In your case, sorting by the Bytes column might help you find the top "talkers" more easily. You can also copy the data and paste it into a .csv file for further analysis if you need to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '12, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-9902" class="comments-container"></div><div id="comment-tools-9902" class="comment-tools"></div><div class="clear"></div><div id="comment-9902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9904"></span>

<div id="answer-container-9904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9904-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @cmaynard has mentioned Wiresharks Endpoints display can help, as long as you are capturing everything in your network. If you're not capturing on your egress router and you have a switched network you probably won't be seeing all the traffic. Read the <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> page on the wiki for more help on this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '12, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9904" class="comments-container"></div><div id="comment-tools-9904" class="comment-tools"></div><div class="clear"></div><div id="comment-9904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

