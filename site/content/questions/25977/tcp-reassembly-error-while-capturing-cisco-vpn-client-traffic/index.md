+++
type = "question"
title = "TCP Reassembly error while capturing Cisco VPN client traffic"
description = '''I am getting the same error. We have a few users who connect to the corporate network using Cisco VPN Client software. They open up two Explorer windows, each with a UNC path to two different shares on the same file server. When they try to copy a file from one share to another while VPN&#x27;d in from h...'''
date = "2013-10-14T12:34:00Z"
lastmod = "2013-10-14T13:39:00Z"
weight = 25977
keywords = [ "reassembly", "vpn", "cisco", "tcp", "error" ]
aliases = [ "/questions/25977" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Reassembly error while capturing Cisco VPN client traffic](/questions/25977/tcp-reassembly-error-while-capturing-cisco-vpn-client-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25977-score" class="post-score" title="current number of votes">0</div><span id="post-25977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting the same error. We have a few users who connect to the corporate network using Cisco VPN Client software. They open up two Explorer windows, each with a UNC path to two different shares on the same file server. When they try to copy a file from one share to another while VPN'd in from home, it just sits there saying "Calculating..." and eventually times out. A wireshark capture on the Cisco Systems VPN adapter shows multiple "Reassembly errors" saying "Reassembly error, protocol TCP: New fragment overlaps old data (retransmission?)]. Further into the packet says it's malformed. Same as the image in <a href="http://ask.wireshark.org/questions/25480/can-a-reassembly-error-be-sufficient-to-kick-a-client-off-the-system">another question</a>(in red). How would I even begin to diagnose this?</p><p>This packet's info has a TCP Retransmission errr, has a "Source" IP address of the VPN adapter (10.10.10.100) and the destination is the file server's internal IP address (192.168.200.100).</p><p>There are other packet errors where the source and destination IP address are reversed and those packet errors report TCP Dup ACK.</p><p>Any ideas anyone?</p><p>UPDATE: I would also like to mention, this issue is Cisco Client VPN specific. I installed the Shrew VPN Client software, imported the PCF file and it works perfectly.</p><p><strong>EDIT</strong>: I converted your comment to a new question, as your problem is (most certainly) not related to the one in the <a href="http://ask.wireshark.org/questions/25480/can-a-reassembly-error-be-sufficient-to-kick-a-client-off-the-system">original question</a>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '13, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/cad1ea6a3561c6f279b7d6226064a253?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="g0ldeneye&#39;s gravatar image" /><p><span>g0ldeneye</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="g0ldeneye has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Oct '13, 13:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-25977" class="comments-container"><span id="25980"></span><div id="comment-25980" class="comment"><div id="post-25980-score" class="comment-score"></div><div class="comment-text"><p>where did you capture? On the system with the VPN client software?</p></div><div id="comment-25980-info" class="comment-info"><span class="comment-age">(14 Oct '13, 13:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25977" class="comment-tools"></div><div class="clear"></div><div id="comment-25977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

