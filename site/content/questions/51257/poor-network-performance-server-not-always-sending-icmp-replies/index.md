+++
type = "question"
title = "Poor network performance, server not always sending icmp replies"
description = '''I&#x27;ve been battling poor network performance with three new servers for the past month now. This performance is present even when doing a basic ping to the server. I can pretty much recreate this issue at will. If I start up a ping from my desk to one of these servers, it will time out. How long it w...'''
date = "2016-03-29T07:38:00Z"
lastmod = "2016-03-29T07:38:00Z"
weight = 51257
keywords = [ "icmp" ]
aliases = [ "/questions/51257" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Poor network performance, server not always sending icmp replies](/questions/51257/poor-network-performance-server-not-always-sending-icmp-replies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51257-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been battling poor network performance with three new servers for the past month now. This performance is present even when doing a basic ping to the server. I can pretty much recreate this issue at will. If I start up a ping from my desk to one of these servers, it will time out. How long it will time out varies. Just recently I ran wireshark on my workstation as well as one of the servers. I then started up a ping to the server. It timed out 18 times and then started responding. During the timeouts, the wireshark on my PC showed 18 ICMP requests being sent out from my PC. The wireshark on the server shows that the server received these ICMP requests. However, it never sent a reply for any of these 18. Then, everything starts working properly. Every one of my requests is matched with a reply.</p><p>What complicates this issue is that when my workstation is timing out to one of these servers, other workstations are having no problems communicating with it. It seems like leaving a continuous ping up maintains connectivity.</p><p>I realize I have spared you the details of the network environment, but I feel like since I can see my requests successfully making it to the server I can ignore everything in the middle for now.</p><p>I'm at a loss. Thoughts? I can provide the wiresharks if necessary, but they are pretty straight forward.</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '16, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/abe1354d9bf1de33757970a7b7a01403?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hamlen&#39;s gravatar image" /><p>hamlen<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hamlen has no accepted answers">0%</span></p></div></div><div id="comments-container-51257" class="comments-container"><span id="51258"></span><div id="comment-51258" class="comment"><div id="post-51258-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us an unfiltered capture taken as close as possible outside the system?</p></div><div id="comment-51258-info" class="comment-info"><span class="comment-age">(29 Mar '16, 09:03)</span> Christian_R</div></div></div><div id="comment-tools-51257" class="comment-tools"></div><div class="clear"></div><div id="comment-51257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

