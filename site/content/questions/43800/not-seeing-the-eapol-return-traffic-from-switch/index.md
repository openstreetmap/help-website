+++
type = "question"
title = "Not Seeing the EAPOL return traffic from switch"
description = '''I&#x27;m capturing the initial EAPOL traffic between the supplicant and the switch but the return EAP traffic are not reported by Wireshark. The workstation port is SPAN to send traffic to a laptop with Wireshark 1.12.6. The monitor session is set for both direction. I would expect to see the return traf...'''
date = "2015-07-01T13:14:00Z"
lastmod = "2015-07-02T04:37:00Z"
weight = 43800
keywords = [ "eapol" ]
aliases = [ "/questions/43800" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not Seeing the EAPOL return traffic from switch](/questions/43800/not-seeing-the-eapol-return-traffic-from-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43800-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing the initial EAPOL traffic between the supplicant and the switch but the return EAP traffic are not reported by Wireshark. The workstation port is SPAN to send traffic to a laptop with Wireshark 1.12.6. The monitor session is set for both direction. I would expect to see the return traffic for the request and Success but not seeing it Wireshark. The destination is shown as "Nearest: with MAC of 01:80:c2:00:00:03 which shown as static CPU. Any ideas?</p><p>Client----------------&gt;Nearest # Start Client----------------&gt;Nearest # Response,Idendity Client----------------&gt;Nearest # Client Hello Client----------------&gt;Nearest # Response, TLS EAP (EAP-TLS) Client----------------&gt;Nearest # Certificate, Client Key Exchange, Certificate Verify, Change Cipher, Encrypted Handshake Client----------------&gt;Switch # Response, TLS EAP (EAP-TLS)</p></div><div id="question-tags" class="tags-container tags">eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '15, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/a6cff05e03dd9ffe83d9675b114a0ab2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ub40&#39;s gravatar image" /><p>ub40<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ub40 has no accepted answers">0%</span></p></div></div><div id="comments-container-43800" class="comments-container"><span id="43819"></span><div id="comment-43819" class="comment"><div id="post-43819-score" class="comment-score"></div><div class="comment-text"><ol><li>Did you try to capture packets at the supplicant or server?</li><li>Are you seeing the complete security exchange at one endpoint (i.e., supplicant and/or server)?</li><li>Did you try using another port on the switch as a mirror port?</li></ol></div><div id="comment-43819-info" class="comment-info"><span class="comment-age">(02 Jul '15, 07:42)</span> Amato_C</div></div></div><div id="comment-tools-43800" class="comment-tools"></div><div class="clear"></div><div id="comment-43800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43813"></span>

<div id="answer-container-43813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43813-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My guess would be that the SPAN isn't providing the authenticator packets for the capture port. Try to setup the capture differently.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '15, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-43813" class="comments-container"></div><div id="comment-tools-43813" class="comment-tools"></div><div class="clear"></div><div id="comment-43813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

