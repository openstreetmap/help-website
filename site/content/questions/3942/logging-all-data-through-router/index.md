+++
type = "question"
title = "Logging all data through router"
description = '''I have a legal requirement to log all data passing through a wireless router. Is this something Wireshark can do, assuming the router has a promiscuous mode available? Does Wireshark have any features to facilitate this (automated mode, starting a new file at 00:00 each day, etc.)?'''
date = "2011-05-05T08:00:00Z"
lastmod = "2011-05-05T09:14:00Z"
weight = 3942
keywords = [ "logging", "dumpcap", "automated" ]
aliases = [ "/questions/3942" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Logging all data through router](/questions/3942/logging-all-data-through-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3942-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a legal requirement to log all data passing through a wireless router. Is this something Wireshark can do, assuming the router has a promiscuous mode available? Does Wireshark have any features to facilitate this (automated mode, starting a new file at 00:00 each day, etc.)?</p></div><div id="question-tags" class="tags-container tags">logging dumpcap automated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '11, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/79d93d2a9e2c0ce6e01711343f9d2666?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brian%20Lewis&#39;s gravatar image" /><p>Brian Lewis<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brian Lewis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '11, 09:16</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3942" class="comments-container"><span id="3960"></span><div id="comment-3960" class="comment"><div id="post-3960-score" class="comment-score"></div><div class="comment-text"><p>IANAL (I am not a lawyer).</p><p>That being said, it seems to be that in my wanderings on the web I recently saw something about legal/technical requirements for a capture to be admissible in a court of law.</p><p>I got the impression that capturing from a span/monitoring router port might not be acceptable due to issues re guaranteeing that all packets are actually captured. (I'm guessing using a span/monitoring port is what you mean by "promiscuous mode").</p><p>So: I suggest you may want to get legal advice from someone qualified in this type of matter.</p></div><div id="comment-3960-info" class="comment-info"><span class="comment-age">(05 May '11, 12:29)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-3942" class="comment-tools"></div><div class="clear"></div><div id="comment-3942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3945"></span>

<div id="answer-container-3945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3945-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, [I believe] Wireshark can capture all user data through the wireless router. See <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">CaptureSetup/WLAN</a>. Also see <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">CaptureSetup/Ethernet</a> on how you could setup the physical connections of your Wireshark host and router (e.g., router --&gt; Wireshark host --&gt; modem).</p><p>Wireshark can start a new capture file every day. See <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html">Capture Options</a>. In the <strong>Capture Files(s)</strong> group box:</p><ol><li>Check the box for <strong>Use multiple files</strong></li><li>Check the second box for <strong>Next file every</strong> and leave the value as 1</li><li>From the dropdown menu, select <strong>day(s)</strong></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '11, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '11, 08:33</p></div></div><div id="comments-container-3945" class="comments-container"></div><div id="comment-tools-3945" class="comment-tools"></div><div class="clear"></div><div id="comment-3945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3952"></span>

<div id="answer-container-3952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3952-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will likely run out of memory if you try to run Wireshark continuously for an entire day. And if you don't roll to the next file more frequently than once a day, you will probably end up with gigantic capture files that will be unmanageable.</p><p>Instead, you should consider using <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> and rolling files more frequently than once a day, as well as limiting the maximum size of each capture file to something more manageable. Rather than retype everything here, you might want to refer to my first comment in <a href="http://ask.wireshark.org/questions/1346/limit-number-of-packets-i-can-see-in-wireshark">this</a> question for more information or search the site for references to dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '11, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3952" class="comments-container"></div><div id="comment-tools-3952" class="comment-tools"></div><div class="clear"></div><div id="comment-3952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

