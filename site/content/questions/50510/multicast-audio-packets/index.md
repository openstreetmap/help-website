+++
type = "question"
title = "Multicast Audio Packets"
description = '''I am trying to troubleshoot a &quot;choppy audio&quot; issue with a wifi voice communication device. I have taken a packet capture using wireshark, however, I cannot seem to filter out any of the multicast audio packets. I see the device receive/join the multicast session, but then it&#x27;s almost as if there are...'''
date = "2016-02-25T10:15:00Z"
lastmod = "2016-02-27T15:30:00Z"
weight = 50510
keywords = [ "vowlan", "wifi", "multicast" ]
aliases = [ "/questions/50510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multicast Audio Packets](/questions/50510/multicast-audio-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to troubleshoot a "choppy audio" issue with a wifi voice communication device. I have taken a packet capture using wireshark, however, I cannot seem to filter out any of the multicast audio packets. I see the device receive/join the multicast session, but then it's almost as if there are no audio packets getting to the badge. I have also done a completely open capture with no filters, and see the same thing.</p><p>Anyone know how to capture and view this info in wireshark?</p></div><div id="question-tags" class="tags-container tags">vowlan wifi multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '16, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/a0130e6fe82da2fbab65b99c89471953?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WiresRDumb&#39;s gravatar image" /><p>WiresRDumb<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WiresRDumb has no accepted answers">0%</span></p></div></div><div id="comments-container-50510" class="comments-container"><span id="50516"></span><div id="comment-50516" class="comment"><div id="post-50516-score" class="comment-score"></div><div class="comment-text"><p>How is your capture setup?</p></div><div id="comment-50516-info" class="comment-info"><span class="comment-age">(25 Feb '16, 13:53)</span> Jaap ♦</div></div><span id="50537"></span><div id="comment-50537" class="comment"><div id="post-50537-score" class="comment-score"></div><div class="comment-text"><p>I did an open capture, meaning that I had 6 AirPCAP NX adapters assigned to each of the surrounding 5Ghz channels (we're only doing 20Mhz wide). I used no capture filters, but when I use the display filter wlan.addr == ########## I see everything except the multicast audio packets.</p><p>I also took a second capture using the capture filter wlan host ########### and it did the same thing.</p></div><div id="comment-50537-info" class="comment-info"><span class="comment-age">(26 Feb '16, 05:18)</span> WiresRDumb</div></div><span id="50558"></span><div id="comment-50558" class="comment"><div id="post-50558-score" class="comment-score"></div><div class="comment-text"><p>Maybe I'm stupid, but why do you expect the destination <code>wlan.addr</code> to be the individual MAC address of the receiving device in case of multicast?</p></div><div id="comment-50558-info" class="comment-info"><span class="comment-age">(26 Feb '16, 14:50)</span> sindy</div></div><span id="50573"></span><div id="comment-50573" class="comment"><div id="post-50573-score" class="comment-score"></div><div class="comment-text"><p>Maybe I'M stupid (haha) but I would expect the multicast audio packets coming to the device to have a destination address, right?</p></div><div id="comment-50573-info" class="comment-info"><span class="comment-age">(29 Feb '16, 06:01)</span> WiresRDumb</div></div><span id="50575"></span><div id="comment-50575" class="comment"><div id="post-50575-score" class="comment-score"></div><div class="comment-text"><p>As Amato has answered in the meantime - the very idea of multicast is that the sender sends a single packet and all recipients interested in it receive it. To facilitate that, not only the IP destination address needs to be a multicast one, i.e. different from the individual addresses of the receiving devices, but the same is true also for the MAC addresses. So please apply the last version of display filter suggested by Amato and see whether you'll see any frames.</p></div><div id="comment-50575-info" class="comment-info"><span class="comment-age">(29 Feb '16, 06:06)</span> sindy</div></div></div><div id="comment-tools-50510" class="comment-tools"></div><div class="clear"></div><div id="comment-50510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50562"></span>

<div id="answer-container-50562" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50562-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the following display filter to show only the Multicast traffic:</p><p>wlan.addr[:1] &amp; 01</p><p>This display filter will only display packets with the Individual/Group (I/G) bit set (==1). For WLAN addresses, only the Destination and Receiver addresses may have the I/G bit set to 1. So to be more appropriate:</p><p>(wlan.da[:1] &amp; 01) || (wlan.ra[:1] &amp; 01)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '16, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-50562" class="comments-container"><span id="50567"></span><div id="comment-50567" class="comment"><div id="post-50567-score" class="comment-score"></div><div class="comment-text"><p>If you need to eliminate broadcast frames from the WiFi elements, then apply the following filter:</p><p>!(wlan.addr == ff:ff:ff:ff:ff:ff)</p><p>So the entire filter would be:</p><p>(wlan.addr[:1] &amp; 01) &amp;&amp; !(wlan.addr == ff:ff:ff:ff:ff:ff)</p></div><div id="comment-50567-info" class="comment-info"><span class="comment-age">(28 Feb '16, 15:00)</span> Amato_C</div></div><span id="50574"></span><div id="comment-50574" class="comment"><div id="post-50574-score" class="comment-score"></div><div class="comment-text"><p>Thank you Amato, I will try this today and let you know!</p></div><div id="comment-50574-info" class="comment-info"><span class="comment-age">(29 Feb '16, 06:01)</span> WiresRDumb</div></div><span id="50612"></span><div id="comment-50612" class="comment"><div id="post-50612-score" class="comment-score"></div><div class="comment-text"><p>I tried this display filter on a capture I performed today and it was successful. Procedure I used:</p><ol><li>Captured all traffic on channel. I did not use any capture filters.</li><li>Applied the following display filter after stopped capture:</li></ol><p>(wlan.addr[:1] &amp; 01) &amp;&amp; !(wlan.addr == ff:ff:ff:ff:ff:ff)</p><p>I was then able to see all the multicast traffic over the WiFi network without seeing the broadcast frames.</p></div><div id="comment-50612-info" class="comment-info"><span class="comment-age">(01 Mar '16, 09:24)</span> Amato_C</div></div></div><div id="comment-tools-50562" class="comment-tools"></div><div class="clear"></div><div id="comment-50562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

