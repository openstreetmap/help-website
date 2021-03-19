+++
type = "question"
title = "Uploading config via TFTP, wireshark show some errors"
description = '''I used Wireshark to control communication between PC and ATA when uploading configuration file via local network. PC with Ubuntu and ATA connected to small hub (blue WAN port &amp;lt;-&amp;gt; to hub). Ubuntu run ISC-DHCP Server with subnet configured for ATA, and config file is in TFTP root directory. As I...'''
date = "2017-01-21T15:27:00Z"
lastmod = "2017-01-22T04:33:00Z"
weight = 58936
keywords = [ "dhcp", "tftp", "cisco", "packet" ]
aliases = [ "/questions/58936" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Uploading config via TFTP, wireshark show some errors](/questions/58936/uploading-config-via-tftp-wireshark-show-some-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58936-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I used Wireshark to control communication between PC and ATA when uploading configuration file via local network. PC with Ubuntu and ATA connected to small hub (blue WAN port &lt;-&gt; to hub). Ubuntu run ISC-DHCP Server with subnet configured for ATA, and config file is in TFTP root directory. As I can see, Wireshark does show that the device downloads it's profile successfully, but it never reboot to apply the new profile to the device. I tried few times, what can be the problem? There is also ETHERNET FRAME CHECK SEQUENCE INCORRECT entries, but not sure this can be an issue. <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_2hNMmGW.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">dhcp tftp cisco packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '17, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/e1ebbc0c6bc592bc2b6629ca872ccec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kosmicity&#39;s gravatar image" /><p>kosmicity<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kosmicity has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '17, 15:42</p></div></div><div id="comments-container-58936" class="comments-container"></div><div id="comment-tools-58936" class="comment-tools"></div><div class="clear"></div><div id="comment-58936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58945"></span>

<div id="answer-container-58945" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58945-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Ethernet Frame Check Sequence is handled by the network adapter - it's unusual to see the actual FCS in a wired capture without certain equipment. Since it is handled by your adapter, you see all 0's for the value, while Wireshark is calculating the actual value, and of course it is failing the check. The preferences pain has the requisite entries to disable the validation:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2017-01-22_07_16_12-Wireshark__Preferences.png" alt="alt text" /></p><p>Also google has a lot of information on this topic, much from previous questions related to FCS:</p><p><a href="https://www.google.com/search?q=wireshark+ethernet+fcs+error&amp;oq=wireshark+ethernet+fcs+error&amp;aqs=chrome..69i57j69i64.7413j0j7&amp;sourceid=chrome&amp;ie=UTF-8">https://www.google.com/search?q=wireshark+ethernet+fcs+error&amp;oq=wireshark+ethernet+fcs+error&amp;aqs=chrome..69i57j69i64.7413j0j7&amp;sourceid=chrome&amp;ie=UTF-8</a></p><p>Most likely, you can ignore this error or turn off the check in Wireshark. An actual bad frame with a bad FCS would usually never make it up to Wireshark, so you wouldn't see it - you would need specific hardware configured to pass up bad frames, or see it in the various interface counters as dropped. If you have a managed switch, you likely have counters for this sort of thing. A basic unmanaged switch likely does not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '17, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></img></div></div><div id="comments-container-58945" class="comments-container"><span id="58949"></span><div id="comment-58949" class="comment"><div id="post-58949-score" class="comment-score"></div><div class="comment-text"><p>So config file was definitely uploaded into ATA, but ATA not resyncing and not reboots?</p></div><div id="comment-58949-info" class="comment-info"><span class="comment-age">(22 Jan '17, 08:08)</span> kosmicity</div></div><span id="58952"></span><div id="comment-58952" class="comment"><div id="post-58952-score" class="comment-score"></div><div class="comment-text"><p>It certainly looks that way from the trace. You have the packets inverted, but you can see the request, the response (indicates last frame), then the acknowledgment.<br />
</p><p>I don't know what an ATA is, or if it should do the things that you expect. One thing to check that was left out of the trace: if the ACK was not accepted, you would expect the data frame to retry for some amount of time / number of retries. I can't see if that occurred or not from the picture you provided. If this is the whole signature, you can rule out network issues as the file is being delivered.<br />
</p><p>Is the config file valid? Does the device have to be in a certain state to accept a config?</p><p>I don't think this is your issue, but it's along the same lines:</p><p><a href="https://quickview.cloudapps.cisco.com/quickview/bug/CSCsd44357">https://quickview.cloudapps.cisco.com/quickview/bug/CSCsd44357</a></p><p>Cisco Bug: CSCsd44357 - ATA186 Auto-Registration Fails if XMLDefault file exceeds 4k in Size</p></div><div id="comment-58952-info" class="comment-info"><span class="comment-age">(22 Jan '17, 09:37)</span> Bob Jones</div></div><span id="58958"></span><div id="comment-58958" class="comment"><div id="post-58958-score" class="comment-score"></div><div class="comment-text"><p>I didn't found the retries, so it looks like it's the whole signature. I recorded 108 packets, maybe I should wait more time. If assume that file has been delivered, then I can rule out network issues. The config is valid, file size is only 366 bytes, so its not file size issue.</p><p>The device (Cisco SPA Voice adapter with router) should accept default config profile on boot, when powered up it resyncs to this file on the local TFTP server specified by DHCP option 66.</p><p>I wasn't sure about my LAN and DHCP server setup, as I used WAN IP addresses for subnet, not common private ip address range, as ATA was not reachable via its default IP address.</p></div><div id="comment-58958-info" class="comment-info"><span class="comment-age">(22 Jan '17, 16:32)</span> kosmicity</div></div></div><div id="comment-tools-58945" class="comment-tools"></div><div class="clear"></div><div id="comment-58945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

