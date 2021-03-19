+++
type = "question"
title = "Request-to-send flood from access point"
description = '''I&#x27;m experiencing constant intermittent lag spikes from my wireless network and decided the investigate using wireshark. I found out that during one of the spikes, the transmitting address (Station A), which happens to be my wireless router (Engenius ESR9850), is sending out 25 of these RTS packets. ...'''
date = "2012-06-06T08:15:00Z"
lastmod = "2012-06-07T17:31:00Z"
weight = 11717
keywords = [ "flood", "rts" ]
aliases = [ "/questions/11717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Request-to-send flood from access point](/questions/11717/request-to-send-flood-from-access-point)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm experiencing constant intermittent lag spikes from my wireless network and decided the investigate using wireshark.</p><p>I found out that during one of the spikes, the transmitting address (Station A), which happens to be my wireless router (Engenius ESR9850), is sending out 25 of these RTS packets.</p><p>540 0.201225 <strong>Station A (TA)</strong> <strong>Station B (RA)</strong> 802.11 52 Request-to-send, Flags=........C</p><p>I've exhausted all my options trying to eliminate the lag spike. These are the following things I've tried.</p><ul><li>Changing the wireless channel (It is using channel 11 now)</li><li>Changing the preamble</li><li>Changing the transmission bandwidth (20/40mhz)</li><li>Changing the RTS and fragmentation threshold</li></ul><p>Is the router going rogue?? It is also linked to an ESR6670 via WDS. Station B is probably connected to the ESR6670 when this happened.</p><p>Please help :/</p></div><div id="question-tags" class="tags-container tags">flood rts</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '12, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/5d8ce84e47b45ffe35eae4575482edce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cloudsix&#39;s gravatar image" /><p>cloudsix<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cloudsix has no accepted answers">0%</span></p></div></div><div id="comments-container-11717" class="comments-container"></div><div id="comment-tools-11717" class="comment-tools"></div><div class="clear"></div><div id="comment-11717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11743"></span>

<div id="answer-container-11743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11743-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the transmitting station is seeing interference or real traffic on the channel, it will not find long enough clear (silent) intervals to be able to send the size packet it wants to send. As a result, it decides that it will have to take the more expensive protocol step (in terms of overhead and channel usage) of sending out an RTS (Request To Send).</p><p>It then expects somebody, presumably the Access Point in an infrastructure network or one of the other nodes in the case of an ad hoc network, to send back a CTS (Clear To Send). When all of the other stations participating in that network see the CTS, they are obligated to hold off transmission for the interval specified in the CTS message.</p><p>So my guess is that there is either reverse direction traffic, traffic involving another station, or radio interference present that causes A to send RTS. It will do that at frequent intervals, trying to break through, until it gets a CTS back. During the time that it waits for a CTS it will be blocking and not sending outbound traffic.</p><p>Look at the RF side, look for other networks' beacons on the channnel, and look for other traffic on that network.</p><p>And of course it could just be Station A going rogue. :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '12, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-11743" class="comments-container"></div><div id="comment-tools-11743" class="comment-tools"></div><div class="clear"></div><div id="comment-11743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

