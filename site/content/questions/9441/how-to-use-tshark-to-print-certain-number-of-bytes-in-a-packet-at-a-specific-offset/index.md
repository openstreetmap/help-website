+++
type = "question"
title = "How to use tshark to print certain number of bytes in a packet at a specific offset"
description = '''I have a pcap file and want to print x number of bytes starting at offset i in the packet. I can specify a filter which will match the frames based on the content of those bytes, for instance, frame[i:x] == b2f5... , but I cannot figure out how to actually print those bytes. I tried &quot;-T fields -e fr...'''
date = "2012-03-08T12:13:00Z"
lastmod = "2012-03-08T12:13:00Z"
weight = 9441
keywords = [ "tshark" ]
aliases = [ "/questions/9441" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use tshark to print certain number of bytes in a packet at a specific offset](/questions/9441/how-to-use-tshark-to-print-certain-number-of-bytes-in-a-packet-at-a-specific-offset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file and want to print x number of bytes starting at offset i in the packet. I can specify a filter which will match the frames based on the content of those bytes, for instance, frame[i:x] == b2f5... , but I cannot figure out how to actually print those bytes. I tried "-T fields -e frame[i:x]" but that does not print anything.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '12, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/a55a96771782871921ea1d5a9b8d8407?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nixbox&#39;s gravatar image" /><p>nixbox<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nixbox has no accepted answers">0%</span></p></div></div><div id="comments-container-9441" class="comments-container"></div><div id="comment-tools-9441" class="comment-tools"></div><div class="clear"></div><div id="comment-9441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

