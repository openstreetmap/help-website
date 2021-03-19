+++
type = "question"
title = "How to capture outgoing packets?"
description = '''Is there any way wireshark can be used to capture outgoing packets. Actually I want to get a list of all the requested URL&#x27;s from my PC. '''
date = "2014-09-21T10:43:00Z"
lastmod = "2014-09-21T12:25:00Z"
weight = 36493
keywords = [ "outgoing", "packets" ]
aliases = [ "/questions/36493" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture outgoing packets?](/questions/36493/how-to-capture-outgoing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36493-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way wireshark can be used to capture outgoing packets. Actually I want to get a list of all the requested URL's from my PC.</p></div><div id="question-tags" class="tags-container tags">outgoing packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '14, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/efaae5979001e7c6c41dfa1ad893c218?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vasil&#39;s gravatar image" /><p>Vasil<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vasil has no accepted answers">0%</span></p></div></div><div id="comments-container-36493" class="comments-container"></div><div id="comment-tools-36493" class="comment-tools"></div><div class="clear"></div><div id="comment-36493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36494"></span>

<div id="answer-container-36494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36494-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, start Wireshark, select your network card, and run the capture. If you want to exclude all packets that do not originate from your PC you can use a capture filter to only allow packets coming from your MAC or IP address, e.g. by using "ether src host aa:bb:cc:dd:ee:ff" (where aa:bb:... is your MAC address) or "src host w.x.y.z" where w.x.y.z is your IP address.</p><p>Then, to find all your requests, you can use a display filter like "http.request_method" to find all packets that contain a HTTP request, which will also show you the URL.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '14, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '14, 12:26</p></div></div><div id="comments-container-36494" class="comments-container"></div><div id="comment-tools-36494" class="comment-tools"></div><div class="clear"></div><div id="comment-36494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

