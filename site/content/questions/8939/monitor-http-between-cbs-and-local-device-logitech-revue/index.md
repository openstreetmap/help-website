+++
type = "question"
title = "monitor HTTP between CBS and local device Logitech Revue"
description = '''Hi, Trying to find out what gets sent to CBS.com from my Google TV device(Logitech Revue) that is different then when I use my PC to watch a TV show using Chrome browser.  I am pretty sure that the User Agent is different but I think that&#x27;s NOT everything.  Looking to find out what else is different...'''
date = "2012-02-09T10:47:00Z"
lastmod = "2012-02-10T02:37:00Z"
weight = 8939
keywords = [ "revue" ]
aliases = [ "/questions/8939" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [monitor HTTP between CBS and local device Logitech Revue](/questions/8939/monitor-http-between-cbs-and-local-device-logitech-revue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8939-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Trying to find out what gets sent to CBS.com from my Google TV device(Logitech Revue) that is different then when I use my PC to watch a TV show using Chrome browser.<br />
</p><p>I am pretty sure that the User Agent is different but I think that's NOT everything.<br />
</p><p>Looking to find out what else is different as ABC,CBS &amp; NBC tells the Revue that it not a supported device.</p><p>Can WireShark monitor HTTP traffic between my Revue plugged into a Wireless Access Point on my home network and CBS.com.<br />
</p><p>Is the filter below valid when trying to monitor info between a local device and an internet IP address?<br />
</p><pre><code>ip.addr==192.168.1.28  &amp;&amp; ip.addr==170.20.0.17</code></pre><p>192.168.1.28 - local static IP address of the Logitech Revue 170.20.0.17 - found by entering 'CBS.com' at http://www.dnswatch.info</p><p>I will be running WireShark from device 192.168.1.10 on my home network.</p><p>Thanks, Rich</p></div><div id="question-tags" class="tags-container tags">revue</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '12, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/6345935314cdaf1a01d95b90700d9e93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flowersrj&#39;s gravatar image" /><p>flowersrj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flowersrj has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-8939" class="comments-container"></div><div id="comment-tools-8939" class="comment-tools"></div><div class="clear"></div><div id="comment-8939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8943"></span>

<div id="answer-container-8943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8943-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all the capture needs to be done from a monitor port, on your access point for instance.</p><p>Second, your resolved address for cbs.com may not be the content provisioning address. I would leave it out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-8943" class="comments-container"><span id="8948"></span><div id="comment-8948" class="comment"><div id="post-8948-score" class="comment-score"></div><div class="comment-text"><p>Jaap,</p><p>By '... from a monitor point', are you saying I have to have WireShark installed on my Gateway or Wireless Access Point and run it from the Gateway or Wireless Access Point?<br />
</p><p>Thanks, Rich</p></div><div id="comment-8948-info" class="comment-info"><span class="comment-age">(10 Feb '12, 10:07)</span> flowersrj</div></div><span id="8955"></span><div id="comment-8955" class="comment"><div id="post-8955-score" class="comment-score"></div><div class="comment-text"><p>Read about <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">capture setup</a> here first.</p></div><div id="comment-8955-info" class="comment-info"><span class="comment-age">(10 Feb '12, 12:33)</span> Jaap ♦</div></div></div><div id="comment-tools-8943" class="comment-tools"></div><div class="clear"></div><div id="comment-8943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

