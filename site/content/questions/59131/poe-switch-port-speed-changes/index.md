+++
type = "question"
title = "poe switch port speed changes"
description = '''Hi, We have a situation that occasionally the poe port speed changes to 10Mhdpx. Upon connection 100Mfdpx is negotiated. As far as I can tell the device speed remains at 100Mfdpx, but the poe port speed changes to 10Mhdpx, which results in massive lossed frames. Can wireshark be used to monitor a po...'''
date = "2017-01-29T05:37:00Z"
lastmod = "2017-01-29T11:54:00Z"
weight = 59131
keywords = [ "speed", "port" ]
aliases = [ "/questions/59131" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [poe switch port speed changes](/questions/59131/poe-switch-port-speed-changes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59131-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have a situation that occasionally the poe port speed changes to 10Mhdpx. Upon connection 100Mfdpx is negotiated. As far as I can tell the device speed remains at 100Mfdpx, but the poe port speed changes to 10Mhdpx, which results in massive lossed frames. Can wireshark be used to monitor a port speed and flag when it changes?</p><p>regards peter</p></div><div id="question-tags" class="tags-container tags">speed port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '17, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/8b78a3aea62dd5c96464dabc5f4769e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pverkaikheemstede&#39;s gravatar image" /><p>pverkaikheem...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pverkaikheemstede has no accepted answers">0%</span></p></div></div><div id="comments-container-59131" class="comments-container"></div><div id="comment-tools-59131" class="comment-tools"></div><div class="clear"></div><div id="comment-59131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59132"></span>

<div id="answer-container-59132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59132-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, that's not possible, as Wireshark cannot capture/read the physical link characteristics. This is something you might be able to monitor on the switch console itself instead.</p><p>And it is very improbable that a device and the switch go to different link speeds, because no communication would be possible <strong>at all</strong>, so it would mean that <strong>all</strong> frames are lost, not just some. Do you mean 100MBit half duplex maybe?</p><p>10HDX is usually a speed a port has when nothing is connected. Duplex mismatch (meaning same speed, but half duplex on one side and full duplex on the other) is very often caused by a misconfiguration, e.g. when setting one side to "auto" and the other to "fixed". More details about that can be found here:</p><p><a href="https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-2-speed-duplex-and-drops/">https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-2-speed-duplex-and-drops/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '17, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-59132" class="comments-container"><span id="59134"></span><div id="comment-59134" class="comment"><div id="post-59134-score" class="comment-score"></div><div class="comment-text"><p>@Jasper I agree. haven´t seen a duplex changing like this. Maybe it is somekind of fracture on the physical wire.</p></div><div id="comment-59134-info" class="comment-info"><span class="comment-age">(29 Jan '17, 11:26)</span> Christian_R</div></div></div><div id="comment-tools-59132" class="comment-tools"></div><div class="clear"></div><div id="comment-59132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59135"></span>

<div id="answer-container-59135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59135-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The link speed is negotiated only, when the link goes down and up. This happens when the cable is unplugged and replugged OR the port is set to shutdown / no shutdown.</p><p>Your best friends are the switch console or the log file from the end device.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '17, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-59135" class="comments-container"></div><div id="comment-tools-59135" class="comment-tools"></div><div class="clear"></div><div id="comment-59135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

