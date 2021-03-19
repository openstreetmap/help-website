+++
type = "question"
title = "Local Network sluggish/slow between clients and server"
description = '''Local Network (12 Users) lag and general poor performance on SBS2011 SP1 running on a HP ML350 G8 12GB RAM (soon to become 32GB) 4 x 600GB SAS in Raid 5. Users experience the green bar when trying to open or save documents (small and large) also read only errors when opening documents. Its intermitt...'''
date = "2013-10-18T03:28:00Z"
lastmod = "2013-10-18T03:28:00Z"
weight = 26161
keywords = [ "performance", "slow", "network" ]
aliases = [ "/questions/26161" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Local Network sluggish/slow between clients and server](/questions/26161/local-network-sluggishslow-between-clients-and-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26161-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Local Network (12 Users) lag and general poor performance on SBS2011 SP1 running on a HP ML350 G8 12GB RAM (soon to become 32GB) 4 x 600GB SAS in Raid 5. Users experience the green bar when trying to open or save documents (small and large) also read only errors when opening documents. Its intermittent but reproduceable by creating a word doc on the server from a client machine I can make minor changes and save...do this a number of times and the issue will appear. sometimes it can take up to 90 seconds to save a 50kb file.</p><p>Have thrown the kitchen sink at it and thought I would try Wireshark but I am no expert, except to say that when installed on the client and reproduce the error, wireshark shows that something is amiss, hoping someone can assist with interpreting the results.<br />
</p><p>I would upload an image but for some reason can't get it to upload from local machine.here is the file via sendspace hopefully this will help</p><p><a href="http://www.sendspace.com/file/w8td34">http://www.sendspace.com/file/w8td34</a></p></div><div id="question-tags" class="tags-container tags">performance slow network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/609c294495ba25b7a16a12d1f51c31f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pulseone&#39;s gravatar image" /><p>pulseone<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pulseone has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '13, 03:40</p></div></div><div id="comments-container-26161" class="comments-container"><span id="26200"></span><div id="comment-26200" class="comment"><div id="post-26200-score" class="comment-score"></div><div class="comment-text"><p>Pictures won't help too much here. Can you post it on Cloudshark (not sure what sensitivity there is in the CIFS so think about that)</p><p>What jumps out (first guess) is oplock issues. Towards the bottom of this link: <a href="http://wiki.wireshark.org/SMB2">http://wiki.wireshark.org/SMB2</a> it will tell you how to look for oplocks (code). W/o the actual trace file, it may be difficult to help.</p></div><div id="comment-26200-info" class="comment-info"><span class="comment-age">(18 Oct '13, 14:48)</span> hansangb</div></div><span id="26235"></span><div id="comment-26235" class="comment"><div id="post-26235-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but with only that screenshot it is impossible to make any educated guess. Please post a capture file somewhere (google docs, dropbox, skydrive, cloudshark) for a case where you observed a slow file transfer. Please consider this:</p><ul><li>take the capture file when there are no other users generating traffic, as it may be complicated to find the one conversation that causes trouble</li><li>capture some seconds (20-30) before and after you do your file download</li><li>post the filename you were using in the test</li></ul></div><div id="comment-26235-info" class="comment-info"><span class="comment-age">(21 Oct '13, 03:49)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26161" class="comment-tools"></div><div class="clear"></div><div id="comment-26161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

