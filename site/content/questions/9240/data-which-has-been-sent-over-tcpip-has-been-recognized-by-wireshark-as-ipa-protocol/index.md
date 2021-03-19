+++
type = "question"
title = "Data which has been sent over TCP&#92;IP has been recognized by wireshark as &quot;IPA&quot; Protocol"
description = '''Hey I was trying to send some data in TCP&#92;IP protocol, and Wireshark has defined it as IPA protocol. The data was in there, but also some kind of unknown info at the start of the monitored data, data which I don&#x27;t know and didn&#x27;t try to send... did anybody heard about this phenomenon ? thx kobi'''
date = "2012-02-27T03:25:00Z"
lastmod = "2012-02-27T13:27:00Z"
weight = 9240
keywords = [ "ip", "ipa", "protocol", "tcp" ]
aliases = [ "/questions/9240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Data which has been sent over TCP\\IP has been recognized by wireshark as "IPA" Protocol](/questions/9240/data-which-has-been-sent-over-tcpip-has-been-recognized-by-wireshark-as-ipa-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey</p><p>I was trying to send some data in TCP\IP protocol, and Wireshark has defined it as IPA protocol. The data was in there, but also some kind of unknown info at the start of the monitored data, data which I don't know and didn't try to send...</p><p>did anybody heard about this phenomenon ?</p><p>thx</p><p>kobi</p></div><div id="question-tags" class="tags-container tags">ip ipa protocol tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '12, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/adde90509f0d5c99bca292a143a018d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kobi1209&#39;s gravatar image" /><p>kobi1209<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kobi1209 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Feb '12, 04:19</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-9240" class="comments-container"></div><div id="comment-tools-9240" class="comment-tools"></div><div class="clear"></div><div id="comment-9240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9256"></span>

<div id="answer-container-9256" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9256-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>"IPA" is the ip.access "GSM over IP" protocol. That protocol apparently uses ports 3002, 3003, 3006, 4249, 4250, and 5000 over TCP. The ip.access dissector doesn't check whether the packets handed to it look like ip.access packets, so traffic that's not ip.access traffic but that's to or from one of those ports might be incorrectly dissected as ip.access traffic.</p><p>This problem is difficult if not impossible to solve in general; neither TCP nor UDP have a "protocol identifier" field to definitively identify the protocol being transported over TCP or UDP, they just have port numbers that, along with the IP host addresses, uniquely specify the communications endpoints. A given port is not guaranteed to carry only traffic for a particular protocol.</p><p>In your case, you could try disabling the ip.access dissector, or changing its TCP port number preference to an empty string or a string that doesn't mention the TCP port you're using.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '12, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9256" class="comments-container"></div><div id="comment-tools-9256" class="comment-tools"></div><div class="clear"></div><div id="comment-9256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

