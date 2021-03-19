+++
type = "question"
title = "in http.cookie only my ip"
description = '''I am trying to sniff cookies from another computer. But in wireshark I see only cookies from my ip. How to fix that?'''
date = "2014-10-13T08:42:00Z"
lastmod = "2014-10-13T09:24:00Z"
weight = 37012
keywords = [ "cookie" ]
aliases = [ "/questions/37012" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [in http.cookie only my ip](/questions/37012/in-httpcookie-only-my-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37012-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to sniff cookies from another computer. But in wireshark I see only cookies from my ip. How to fix that?</p></div><div id="question-tags" class="tags-container tags">cookie</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '14, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/7af40962d0f312d4964cf6e24cd433f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testerrus&#39;s gravatar image" /><p>testerrus<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testerrus has no accepted answers">0%</span></p></div></div><div id="comments-container-37012" class="comments-container"></div><div id="comment-tools-37012" class="comment-tools"></div><div class="clear"></div><div id="comment-37012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37013"></span>

<div id="answer-container-37013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37013-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How are your computer and the other computer connected? Where is the web server? It's likely that you'll be running on either a switched Ethernet network (the switches don't normally forward the traffic from other computers) or a wireless one, which is very similar to a switched network, but also has it's own issues.</p><p>See the wiki page on <a href="http://wiki.wireshark.org/CaptureSetup">capture setup</a>, particularly the ones for your network media type as listed at the bottom of the page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '14, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37013" class="comments-container"><span id="37014"></span><div id="comment-37014" class="comment"><div id="post-37014-score" class="comment-score"></div><div class="comment-text"><p>sorry. i forget to say, that that is Wi-Fi network. And on another computer (Windows 7) everything working. So probably problem in my comp (Windows 8).</p></div><div id="comment-37014-info" class="comment-info"><span class="comment-age">(13 Oct '14, 09:28)</span> testerrus</div></div><span id="37015"></span><div id="comment-37015" class="comment"><div id="post-37015-score" class="comment-score"></div><div class="comment-text"><p>You'll need to have a look at the <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN capture page</a> then, note capturing the WLAN traffic of other devices is very difficult using windows.</p></div><div id="comment-37015-info" class="comment-info"><span class="comment-age">(13 Oct '14, 09:32)</span> grahamb ♦</div></div></div><div id="comment-tools-37013" class="comment-tools"></div><div class="clear"></div><div id="comment-37013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

