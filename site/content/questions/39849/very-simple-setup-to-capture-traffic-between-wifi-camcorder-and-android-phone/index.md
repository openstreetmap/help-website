+++
type = "question"
title = "very simple setup to capture traffic between wifi camcorder and android phone"
description = '''Hi, I need a very simple setup to capture the traffic between a wifi enabled camcorder and an Android smartphone. I got an AirPcap (capture only) and the Wireshark 1.2.5 running in Windows, I know the SSID of the camcorder and its password but I don&#x27;t have the same information of the Android device....'''
date = "2015-02-13T06:40:00Z"
lastmod = "2015-02-13T07:34:00Z"
weight = 39849
keywords = [ "wificamcorder" ]
aliases = [ "/questions/39849" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [very simple setup to capture traffic between wifi camcorder and android phone](/questions/39849/very-simple-setup-to-capture-traffic-between-wifi-camcorder-and-android-phone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need a very simple setup to capture the traffic between a wifi enabled camcorder and an Android smartphone.</p><p>I got an AirPcap (capture only) and the Wireshark 1.2.5 running in Windows, I know the SSID of the camcorder and its password but I don't have the same information of the Android device.</p><p>How can I do to filter all the rest of the traffic and see only these two devices?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">wificamcorder</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '15, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/19e514b95015f799a47ec0ea065a8542?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrew500w&#39;s gravatar image" /><p>andrew500w<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrew500w has no accepted answers">0%</span></p></div></div><div id="comments-container-39849" class="comments-container"><span id="39852"></span><div id="comment-39852" class="comment"><div id="post-39852-score" class="comment-score"></div><div class="comment-text"><p>That's a very old version of Wireshark, you really should upgrade to the latest 1.12.x</p></div><div id="comment-39852-info" class="comment-info"><span class="comment-age">(13 Feb '15, 07:53)</span> grahamb ♦</div></div></div><div id="comment-tools-39849" class="comment-tools"></div><div class="clear"></div><div id="comment-39849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39850"></span>

<div id="answer-container-39850" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39850-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Perform a capture and find the Beacon frames from the camcorder. If you know the SSID, you can apply the display filter wlan_mgt.ssid =="SSID-name" where you place the name of the SSID instead of the SSID-name. Open a Beacon frame from the camcorder and write down the Transmitter/Source MAC address.</li><li>In the Android phone, go to the WiFi settings and select Advanced from the menu. You will see the MAC address of the device.</li></ol><p>Now you know the MAC addresses of the AP and the STA. Apply the following capture filter: ether host &lt;mac-1&gt; and ether host &lt;mac-2&gt;</p><p>For example: ether host 00:00:00:00:00:00 and ether host 00:00:00:00:00:01</p><p>To add a capture filter in Wireshark, go to Capture in the top menu and select Options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '15, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-39850" class="comments-container"><span id="39851"></span><div id="comment-39851" class="comment"><div id="post-39851-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!!!</p></div><div id="comment-39851-info" class="comment-info"><span class="comment-age">(13 Feb '15, 07:46)</span> andrew500w</div></div></div><div id="comment-tools-39850" class="comment-tools"></div><div class="clear"></div><div id="comment-39850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

