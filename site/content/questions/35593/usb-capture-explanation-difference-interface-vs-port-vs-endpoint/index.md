+++
type = "question"
title = "USB Capture Explanation: Difference Interface vs. Port vs. Endpoint"
description = '''Hi there, I am currently trying to sniff some USB traffic from a USB flash drive to a virtual (Ubuntu) machine. But I am confronted with a few understanding problems. Given the following packet (contains every field I am unsure about):  1 0.000000000 host 1.0 USBHUB 64 GET_STATUS Request [Port 1] Fr...'''
date = "2014-08-19T12:13:00Z"
lastmod = "2014-08-19T12:13:00Z"
weight = 35593
keywords = [ "sniffing", "usbmon", "usb", "virtualbox" ]
aliases = [ "/questions/35593" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [USB Capture Explanation: Difference Interface vs. Port vs. Endpoint](/questions/35593/usb-capture-explanation-difference-interface-vs-port-vs-endpoint)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35593-score" class="post-score" title="current number of votes">0</div><span id="post-35593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I am currently trying to sniff some USB traffic from a USB flash drive to a virtual (Ubuntu) machine. But I am confronted with a few understanding problems. Given the following packet (contains every field I am unsure about):</p><pre><code>1   0.000000000 host    1.0 USBHUB  64  GET_STATUS Request     [Port 1]
Frame 1: 64 bytes on wire (512 bits), 64 bytes captured (512 bits) on interface 0
Endpoint: 0x80, Direction: IN</code></pre><p>So my questions are:</p><ol><li><p>Is the port (indicated with "[Port 1]") the physical port on my machine? And if so: Are they numbered beginning with 0? (So if I have 4 ports, the first one would be 0 and the last one would be 3)</p></li><li><p>What is the interface then...?</p></li><li><p>The endpoints are just the indication of the (in case of the mass storage I connected) direction of the access (in this case "IN" -&gt; from host to USB device)</p></li></ol><p>Thanks a lot for your help!</p><p>Regards, Rolf</p><p><strong>UPDATE</strong></p><p>I think I got the thing with the endpoints and interfaces now (please correct me, if I am wrong):</p><p>An interface is the logical grouping of several endpoints with the same features.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-usbmon" rel="tag" title="see questions tagged &#39;usbmon&#39;">usbmon</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span> <span class="post-tag tag-link-virtualbox" rel="tag" title="see questions tagged &#39;virtualbox&#39;">virtualbox</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/ed42d94d476f543682fea8aab051d515?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rolf&#39;s gravatar image" /><p><span>Rolf</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rolf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '14, 13:44</strong> </span></p></div></div><div id="comments-container-35593" class="comments-container"></div><div id="comment-tools-35593" class="comment-tools"></div><div class="clear"></div><div id="comment-35593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

