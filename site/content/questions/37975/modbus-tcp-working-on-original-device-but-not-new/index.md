+++
type = "question"
title = "Modbus TCP working on original device but not new"
description = '''We have a datalogic barcode scanner communicating with a momentum PLC which transmits data correctly. It is failing and we need to replace it with a new scanner which is the same model but has 10 years worth of device upgrades.  The new device is showing a lot of TCP [Ethernet frame check sequence i...'''
date = "2014-11-19T11:18:00Z"
lastmod = "2014-11-20T02:50:00Z"
weight = 37975
keywords = [ "modbus", "tcp" ]
aliases = [ "/questions/37975" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Modbus TCP working on original device but not new](/questions/37975/modbus-tcp-working-on-original-device-but-not-new)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37975-score" class="post-score" title="current number of votes">0</div><span id="post-37975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a datalogic barcode scanner communicating with a momentum PLC which transmits data correctly. It is failing and we need to replace it with a new scanner which is the same model but has 10 years worth of device upgrades. The new device is showing a lot of TCP [Ethernet frame check sequence incorrect] errors and the packet size is different (110 original and 107 new). The only difference that I can see is that in the original scanner the Ethernet II frame in the "Modbus TCP" packet at the bottom below the "Type: IP(0X0800)" shows "Trailer: 200000". The new scanner Ethernet II frame does not have this. From what I've read on the internet "Trailer" increases the packet size to the minimum allowable without the need of padding. This makes sense as on the original scanner padding is 0 whereas the new scanner is always &gt;0. Am I correct in assuming this and it is a hardware/firmware issue that needs to be addressed by the device supplier?<br />
</p><p><strong>Updated link for public viewing.</strong> I've attached a link to the 2 file captures. <a href="https://drive.google.com/folderview?id=0B_wXYpDae4NcZi03QUJFYmZFUDA&amp;usp=sharing">https://drive.google.com/folderview?id=0B_wXYpDae4NcZi03QUJFYmZFUDA&amp;usp=sharing</a></p><p>Brief description of events to make sense of file below.</p><pre><code>FILE: ORIGINAL SCANNER.
1-6     Hand Held     1183648 (part of barcode that can be seen in packet)
7-12     No Read     Main scanner failed to read (sends NO READ to 10.240.119.201 to halt line)
13-20     Hand Held     1184494
21-24     Main Scanner Unit     1184676

FILE: NEW SCANNER.
1-6     Hand Held     Failed read (Appears to be writing 0000... to the PLC registers on each failed read)
7-13     Hand Held     Failed read
14-21     Hand Held     Failed read
22-30     Hand Held     Failed read
31-40     Hand Held     Successful read
41-47     Main Scanner     Failed read
48-56    Hand Held     Failed read
57-63     Hand Held     Failed read
64-70     Hand Held     Failed read
71-75     Hand Held     Failed read
75-79     Hand Held     Successful read</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/55a1164db71809747f872b07af68319d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Getrick&#39;s gravatar image" /><p><span>Getrick</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Getrick has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '14, 08:29</strong> </span></p></div></div><div id="comments-container-37975" class="comments-container"><span id="37978"></span><div id="comment-37978" class="comment"><div id="post-37978-score" class="comment-score"></div><div class="comment-text"><p>Could you post the capture file somewhere so folks could actually look at it rather than relying on your interpretation? Try <a href="http://cloudshark.org">Cloudshark</a>, Drop Box or Google Drive etc. As it's only modbus traffic it won't be sensitive.</p></div><div id="comment-37978-info" class="comment-info"><span class="comment-age">(19 Nov '14, 13:31)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38009"></span><div id="comment-38009" class="comment"><div id="post-38009-score" class="comment-score"></div><div class="comment-text"><p>Google Drive says the files aren't shared publicly and I need permission.</p></div><div id="comment-38009-info" class="comment-info"><span class="comment-age">(20 Nov '14, 02:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37975" class="comment-tools"></div><div class="clear"></div><div id="comment-37975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

