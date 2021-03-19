+++
type = "question"
title = "How to capture udp data in a ip range from Capture Filter?"
description = '''I tried to use  dst ...25/100  and dst ...25 ..***.26 ... It does not work Is this option available from Ethereal Option window? Thanks'''
date = "2011-04-26T06:56:00Z"
lastmod = "2011-04-26T11:02:00Z"
weight = 3720
keywords = [ "ip", "range", "multicast" ]
aliases = [ "/questions/3720" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture udp data in a ip range from Capture Filter?](/questions/3720/how-to-capture-udp-data-in-a-ip-range-from-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3720-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to use dst <strong><em>.</em></strong>.<strong><em>.25/100 and dst</em></strong> .<strong><em>.</em></strong>.25 <strong><em>.</em></strong>.***.26 ...</p><p>It does not work</p><p>Is this option available from Ethereal Option window?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ip range multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '11, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/08ecc2612a00e33839095852abd357aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="likeshark&#39;s gravatar image" /><p>likeshark<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="likeshark has no accepted answers">0%</span></p></div></div><div id="comments-container-3720" class="comments-container"></div><div id="comment-tools-3720" class="comment-tools"></div><div class="clear"></div><div id="comment-3720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3721"></span>

<div id="answer-container-3721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3721-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to use capture filters you need to use the tcpdump syntax, not display filter syntax. You could filter like this:</p><pre><code>net 192.168.0.0/24</code></pre><p>See also <a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '11, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3721" class="comments-container"></div><div id="comment-tools-3721" class="comment-tools"></div><div class="clear"></div><div id="comment-3721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3724"></span>

<div id="answer-container-3724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3724-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>And if you want to use Wireshark display filters, then you need to use the correct Wireshark display filter syntax. See: <a href="http://wiki.wireshark.org/DisplayFilters">http://wiki.wireshark.org/DisplayFilters</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '11, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3724" class="comments-container"></div><div id="comment-tools-3724" class="comment-tools"></div><div class="clear"></div><div id="comment-3724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

