+++
type = "question"
title = "Wireshark not dissecting MPLS over UDP"
description = '''Here is the pcap file where I see the issue. https://onedrive.live.com/redir?resid=DCB291F7224C3741!182&amp;amp;authkey=!AAa_6r-uzbzrWn0&amp;amp;ithint=file%2cpcap'''
date = "2016-02-03T21:26:00Z"
lastmod = "2016-02-04T13:39:00Z"
weight = 49803
keywords = [ "udp", "mols" ]
aliases = [ "/questions/49803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not dissecting MPLS over UDP](/questions/49803/wireshark-not-dissecting-mpls-over-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is the pcap file where I see the issue.</p><p><a href="https://onedrive.live.com/redir?resid=DCB291F7224C3741!182&amp;authkey=!AAa_6r-uzbzrWn0&amp;ithint=file%2cpcap">https://onedrive.live.com/redir?resid=DCB291F7224C3741!182&amp;authkey=!AAa_6r-uzbzrWn0&amp;ithint=file%2cpcap</a></p></div><div id="question-tags" class="tags-container tags">udp mols</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '16, 21:26</strong></p><img src="https://secure.gravatar.com/avatar/b7590de43adb375f2d9c6ba1f98b72cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yacare&#39;s gravatar image" /><p>yacare<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yacare has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 04 Feb '16, 12:09</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-49803" class="comments-container"></div><div id="comment-tools-49803" class="comment-tools"></div><div class="clear"></div><div id="comment-49803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49868"></span>

<div id="answer-container-49868" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49868-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MPLS dissector currently only decodes MPLS over UDP when the UDP port is the <a href="https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=6635">IANA-assigned</a> one: 6635.</p><p>To decode MPLS over the non-standard ports used in this capture you'll need to use the Decode-As functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '16, 13:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-49868" class="comments-container"></div><div id="comment-tools-49868" class="comment-tools"></div><div class="clear"></div><div id="comment-49868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

