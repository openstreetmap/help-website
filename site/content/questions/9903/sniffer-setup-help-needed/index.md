+++
type = "question"
title = "sniffer setup help needed"
description = '''I&#x27;m trying to put together a sniff environment where wireless client hit a WAP, the waps wired ethernet port brings the traffic back to a port mirror switch for me to look at. Does anyone know how to get a WAP to stop &quot;local switching&quot; (the wap seems to switch the local traffic and only allows traff...'''
date = "2012-04-02T12:51:00Z"
lastmod = "2012-04-05T01:20:00Z"
weight = 9903
keywords = [ "environment", "sniffer", "setup" ]
aliases = [ "/questions/9903" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [sniffer setup help needed](/questions/9903/sniffer-setup-help-needed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9903-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to put together a sniff environment where wireless client hit a WAP, the waps wired ethernet port brings the traffic back to a port mirror switch for me to look at. Does anyone know how to get a WAP to stop "local switching" (the wap seems to switch the local traffic and only allows traffic destined to a different network to come over the wired port. I want to see everything). Once I'm at the wired switch, wireshark can do its thing.</p><p>thnx</p></div><div id="question-tags" class="tags-container tags">environment sniffer setup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '12, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/2b12f1f0687101a1dd8f75db884aed8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakelt&#39;s gravatar image" /><p>wakelt<br />
<span class="score" title="13 reputation points">13</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakelt has no accepted answers">0%</span></p></div></div><div id="comments-container-9903" class="comments-container"><span id="9908"></span><div id="comment-9908" class="comment"><div id="post-9908-score" class="comment-score"></div><div class="comment-text"><p>That's not so much a Wireshark question but a WAP configuration question, like how to setup a monitor port on a switch. Without make and model this is rather fruitless.</p></div><div id="comment-9908-info" class="comment-info"><span class="comment-age">(02 Apr '12, 23:49)</span> Jaap ♦</div></div><span id="9911"></span><div id="comment-9911" class="comment"><div id="post-9911-score" class="comment-score"></div><div class="comment-text"><p>The WAP is a Cisco/Linksys WAP610N, and yes this is more of a packet capture environment question. I figured Wireshark folks would be the experts in setting up an environment.</p><p>I guess the crux of my question is, can a WAP (any WAP device) be configured to not "switch" local wireless traffic and simply act as a mux and forward the traffic on to another device that would actually perform the switching ??? If not a WAP device, what device could I use as a wireless mux/demux ? Specific device recommendations welcome.</p><p>thanks,wk</p></div><div id="comment-9911-info" class="comment-info"><span class="comment-age">(03 Apr '12, 05:31)</span> wakelt</div></div></div><div id="comment-tools-9903" class="comment-tools"></div><div class="clear"></div><div id="comment-9903-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9951"></span>

<div id="answer-container-9951" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9951-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you could use a Wireless LAN Controller and a dumb Access Point and port mirror the WLC, it might just pose a whole new array of questions though.. A WLC should handle most of the traffic of an AP , what exactly are you hoping to find?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '12, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-9951" class="comments-container"><span id="9962"></span><div id="comment-9962" class="comment"><div id="post-9962-score" class="comment-score"></div><div class="comment-text"><p>Not sure what you mean by a "dumb access point" ?? If there is an access point that doesn't do any "local wireless switching", and simply forwards ALL wireless traffic on the wired side of the wap so a wired switch could perform the forwarding (and mirroring to a sniffer port, then I'd be most interested in a pointer to such a wap.</p><p>I want to capture ALL wireless and wired traffic in a network in a single sniff. We can't guarantee that all traffic will be wireless, so we to be prepared to capture wireless and wired traffic hitting a single switch. I am hoping to find a "really dumb wap" that forwards ALL rx'd wireless traffic upstreamed in wired fashion so I can have a single sniff point.</p></div><div id="comment-9962-info" class="comment-info"><span class="comment-age">(05 Apr '12, 08:18)</span> wakelt</div></div><span id="9983"></span><div id="comment-9983" class="comment"><div id="post-9983-score" class="comment-score"></div><div class="comment-text"><p>I think by dumb he means an access point that is no smarter than a hub. All it could do is the physical later stuff thus requiring a switch to control it. I've worked with some rather dumb access points in a past job and honestly it has never occurred to me if the AP handles the local traffic or not on it's own. I'm pretty sure all the modern Cisco stuff will switch locally and I doubt you will be able to do much of any configuration on anything Linksys. Only suggestion I have, if this is just for testing purposes, is to setup a wireless network using a computer and perform the capture there.</p></div><div id="comment-9983-info" class="comment-info"><span class="comment-age">(06 Apr '12, 08:33)</span> networkguy09</div></div></div><div id="comment-tools-9951" class="comment-tools"></div><div class="clear"></div><div id="comment-9951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

