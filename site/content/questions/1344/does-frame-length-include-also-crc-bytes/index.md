+++
type = "question"
title = "Does &quot;Frame Length&quot; include also CRC-Bytes?"
description = '''Does &quot;Frame Length&quot; include also CRC-Bytes? When a packet is shown 60 bytes on wire, 60 bytes captured Frame Length: 60 bytes Capture Length: 60 bytes and also the hex/data-view shows 60 bytes Does this mean that the 4-CRC-Bytes / FCS is included also (but my NIC normally does not provide the CRC to...'''
date = "2010-12-14T07:05:00Z"
lastmod = "2010-12-14T09:33:00Z"
weight = 1344
keywords = [ "crc", "fcs", "framelength" ]
aliases = [ "/questions/1344" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does "Frame Length" include also CRC-Bytes?](/questions/1344/does-frame-length-include-also-crc-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1344-score" class="post-score" title="current number of votes">0</div><span id="post-1344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does "Frame Length" include also CRC-Bytes?</p><p>When a packet is shown 60 bytes on wire, 60 bytes captured Frame Length: 60 bytes Capture Length: 60 bytes</p><p>and also the hex/data-view shows 60 bytes</p><p>Does this mean that the 4-CRC-Bytes / FCS is included also (but my NIC normally does not provide the CRC to the host)? But if this is not the case should'nt it be "64 bytes on wire" but "60 bytes captured"?</p><p>My Background is that i write a file-export to the pcap-Format and i have no CRC-Bytes in my data and so i would say that i have 64Bytes on wire (including the CRC-Bytes) but only 60Bytes captured. Wireshark says now that the packet is truncated (which is correct for my opinion), anyhow i wonder why the packets captured via winpcap are "not" also shown as truncated? Is here the "bytes on wire" rather more a "bytes on wire without CRC"???</p><p>Thanks for responses!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crc" rel="tag" title="see questions tagged &#39;crc&#39;">crc</span> <span class="post-tag tag-link-fcs" rel="tag" title="see questions tagged &#39;fcs&#39;">fcs</span> <span class="post-tag tag-link-framelength" rel="tag" title="see questions tagged &#39;framelength&#39;">framelength</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '10, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/f2b84aa885b46276b07c90377024c39e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fdxshark&#39;s gravatar image" /><p><span>fdxshark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fdxshark has no accepted answers">0%</span></p></div></div><div id="comments-container-1344" class="comments-container"></div><div id="comment-tools-1344" class="comment-tools"></div><div class="clear"></div><div id="comment-1344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1347"></span>

<div id="answer-container-1347" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1347-score" class="post-score" title="current number of votes">1</div><span id="post-1347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it is "bytes on wire without CRC", which is a very common thing for network analyzer file formats. The explanation I was told is that the 4 bytes FCS were not stored to spare the memory for it. Nowadays with that much memory we all have it may be hard to understand, but those 4 bytes were really valuable back in the days of "640k should be enough for everybody" :-)</p><p>On a side note: I have one high end gigabit capture device though that does write the FCS into the tracefile, but all others don't.</p><p>Edit: I forgot: the FCS also isn't that important, because if it is not correct the frame would be dropped at the first NIC/Switchport it is received. You wouldn't even be able to capture it with Wireshark even if it makes it to your NIC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '10, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '10, 09:34</strong> </span></p></div></div><div id="comments-container-1347" class="comments-container"></div><div id="comment-tools-1347" class="comment-tools"></div><div class="clear"></div><div id="comment-1347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

