+++
type = "question"
title = "Adwin protocol"
description = '''Hi, anyone who can help with this ADwin frame ? (Especially the Gateway IP) ADwin configuration protocol ADwin Debug information  Unused  Unused Pattern: Unknown (0x6e4c9d8c) Version: 1087455434 Status: 0x3d2d682c, Status Configurable, Status Bootloader boots, Status Bootloader receive  .... .... .....'''
date = "2017-01-22T05:40:00Z"
lastmod = "2017-01-22T08:49:00Z"
weight = 58946
keywords = [ "adwin" ]
aliases = [ "/questions/58946" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adwin protocol](/questions/58946/adwin-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58946-score" class="post-score" title="current number of votes">0</div><span id="post-58946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>anyone who can help with this ADwin frame ? (Especially the Gateway IP)</p><pre><code>ADwin configuration protocol
ADwin Debug information
    Unused
    Unused
Pattern: Unknown (0x6e4c9d8c)
Version: 1087455434
Status: 0x3d2d682c, Status Configurable, Status Bootloader boots, Status Bootloader receive
   .... .... .... .... .... .... .... ...0 = Status Bootloader: False
   .... .... .... .... .... .... .... ..0. = Status Reprogrammable: False
   .... .... .... .... .... .... .... .1.. = Status Configurable: True
   .... .... .... .... .... .... .... 1... = Status Bootloader boots: True
   .... .... .... .... .... .... ...0 .... = Status Bootloader reprogrammable: False
   .... .... .... .... .... .... ..1. .... = Status Bootloader receive: True
   .... .... .... .... .... .... .0.. .... = Status Bootloader reprogramming done: False
   .... .... .... .... .... .... 0... .... = Status EEPROM Support: False</code></pre><p>server version (beta part): 230 Server version: 51930 XILINX Version: 0x8adac926 MAC address: 05:a4:25:f8:6e:3e (05:a4:25:f8:6e:3e) Port (16bit): 41662 DHCP enabled: True Netmask count: 237 Gateway IP: 110.46.141.140 Reply with broadcast: True Scan ID: 0x68437261</p></pre><p>Many thanks</p><p>Erwin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-adwin" rel="tag" title="see questions tagged &#39;adwin&#39;">adwin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '17, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/39740104b2ca3a57dc7545d15abb58d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erwin%20R&#39;s gravatar image" /><p><span>Erwin R</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erwin R has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '17, 09:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-58946" class="comments-container"><span id="58947"></span><div id="comment-58947" class="comment"><div id="post-58947-score" class="comment-score">1</div><div class="comment-text"><p>"help me with this frame" is not really a question... what do you want to ask precisely?</p></div><div id="comment-58947-info" class="comment-info"><span class="comment-age">(22 Jan '17, 06:26)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="58950"></span><div id="comment-58950" class="comment"><div id="post-58950-score" class="comment-score"></div><div class="comment-text"><p>Jasper,</p><p>thank you for your interest in my request for help. As asked precisely , let us start with the meaning of the "Gateway IP: 110.46.141.140" . Locating that IP learned me that this a host based in Hong Kong. To continue : what is the purpose of sending this frame in general. I assume this frame has some sense . Next, I would like to know the meaning of "MAC address: 05:a4:25:f8:6e:3e (05:a4:25:f8:6e:3e)" . What could possibly be the host ?</p><p>I want to know why my Android device is putting this frame on the wire(less).</p><p>I know 0 about "Adwin Config". Googling for more human readable information did not help me any further.</p><p>I am looking for some general explanation, probably to fire my next questions for help.</p><p>Kind regards</p><p>Erwin</p></div><div id="comment-58950-info" class="comment-info"><span class="comment-age">(22 Jan '17, 08:09)</span> <span class="comment-user userinfo">Erwin R</span></div></div><span id="58951"></span><div id="comment-58951" class="comment"><div id="post-58951-score" class="comment-score"></div><div class="comment-text"><p>Are you sure, that this is really an Adwind Frame?</p><p>Each TCP or UDP packet has a source and a destination port. If a UDP packet has a source port of 123 and a destination port of 53 Wireshark would not know, if it is NTP or DNS. The Decode-As Context menu helps.</p><p>And, thank you for asking, the afford-mentioned port combination should not be seen on the wire, but is send by a bunch of cable modems anyway.</p><p>Can you upload the tracefile for us?</p></div><div id="comment-58951-info" class="comment-info"><span class="comment-age">(22 Jan '17, 08:49)</span> <span class="comment-user userinfo">packethunter</span></div></div></div><div id="comment-tools-58946" class="comment-tools"></div><div class="clear"></div><div id="comment-58946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

