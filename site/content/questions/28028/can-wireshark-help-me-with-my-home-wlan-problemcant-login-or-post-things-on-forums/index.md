+++
type = "question"
title = "Can wireshark help me with my home wlan problem?(Cant login or post things on forums)"
description = '''I made the following quesiton on superuser, please give it a look: http://superuser.com/questions/686738/home-wlan-wont-let-me-do-very-specific-thingslog-in-facebook-post-on-some-for And put a similar on ubuntuforuns.org . But got no answer yet. Its strange because I don&#x27;t get a &#x27;page not found&#x27; or ...'''
date = "2013-12-11T16:37:00Z"
lastmod = "2013-12-12T04:01:00Z"
weight = 28028
keywords = [ "test", "router", "modem", "wlan" ]
aliases = [ "/questions/28028" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can wireshark help me with my home wlan problem?(Cant login or post things on forums)](/questions/28028/can-wireshark-help-me-with-my-home-wlan-problemcant-login-or-post-things-on-forums)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28028-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I made the following quesiton on superuser, please give it a look:</p><p><a href="http://superuser.com/questions/686738/home-wlan-wont-let-me-do-very-specific-thingslog-in-facebook-post-on-some-for">http://superuser.com/questions/686738/home-wlan-wont-let-me-do-very-specific-thingslog-in-facebook-post-on-some-for</a></p><p>And put a similar on ubuntuforuns.org . But got no answer yet.</p><p>Its strange because I don't get a 'page not found' or 'timeout' the page simply does not load.</p><p>I installed wireshark to see if I can get a clue on whats happening, but I don't know even what to look for.</p><p>Here are two screenshots of the logs when:</p><p>A) Logging on facebook while connected directly to the modem: <a href="http://s12.postimg.org/cph9ybpb1/facebook_wo_wlan.png">http://s12.postimg.org/cph9ybpb1/facebook_wo_wlan.png</a></p><p>B) <strong>Trying</strong>(didn't work) to log on facebook while connected to the router: <a href="http://s30.postimg.org/8makj4is1/facebook_w_wlan.png">http://s30.postimg.org/8makj4is1/facebook_w_wlan.png</a></p><p>I see a difference (apparently a lot of bad checksum packages) but I don't know if that's the problem or how to fix it</p><p>I'd like some directions on what tests to do or what to look for.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">test router modem wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '13, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/5b735127f5ae91bcc2e95cda09e1256d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="galmeida&#39;s gravatar image" /><p>galmeida<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="galmeida has no accepted answers">0%</span></p></div></div><div id="comments-container-28028" class="comments-container"></div><div id="comment-tools-28028" class="comment-tools"></div><div class="clear"></div><div id="comment-28028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28046"></span>

<div id="answer-container-28046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28046-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Retransmission s seem to be the problem in your bad trace. Looks like you lose IP connectivity with the server for that time when you use the router, though it allows the TCP session to be set up. That trace is really just what you would see from the clients perspective if IP connectivity was lost after session setup.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '13, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-28046" class="comments-container"></div><div id="comment-tools-28046" class="comment-tools"></div><div class="clear"></div><div id="comment-28046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

