+++
type = "question"
title = "ip of machine where wireshark is running"
description = '''Hi Friends, Can we find out ip add./mac-add of capture device by looking at capture file.Sometimes vendor provides us capture file and by looking into it , is there a way we can find out on which ip/mac that capture was taken.'''
date = "2013-05-20T03:59:00Z"
lastmod = "2013-05-20T09:34:00Z"
weight = 21297
keywords = [ "wireshark" ]
aliases = [ "/questions/21297" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [ip of machine where wireshark is running](/questions/21297/ip-of-machine-where-wireshark-is-running)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21297-score" class="post-score" title="current number of votes">0</div><span id="post-21297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Friends, Can we find out ip add./mac-add of capture device by looking at capture file.Sometimes vendor provides us capture file and by looking into it , is there a way we can find out on which ip/mac that capture was taken.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '13, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21297" class="comments-container"></div><div id="comment-tools-21297" class="comment-tools"></div><div class="clear"></div><div id="comment-21297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21304"></span>

<div id="answer-container-21304" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21304-score" class="post-score" title="current number of votes">2</div><span id="post-21304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kishan pandey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can we find out ip add./mac-add of capture device by looking at capture file.</p></blockquote><p>usually no, if the capture was done in the right way. Reason: Network capturing should be a passive process and the capture machine will not leave any information about itself in the capture file, with these exemptions.</p><ul><li>your capturing device sends some traffic into the network (DNS looks, broadcasts, etc.) on the same interface you captured the traffic. However, there is no <strong>reliable way</strong> to distinct this traffic from traffic on the network. It could be a relation between the IP addresses in the capture file and the DNS reequests. It could be something with the checksums (IP, TCP), or anything else. But none of that is really <strong>reliable</strong>.</li><li>your capturing device added some information about it's capturing interface into a pcapng option block. See <code>Statistics -&gt; Comments Summary</code> for a first idea.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21304" class="comments-container"><span id="21314"></span><div id="comment-21314" class="comment"><div id="post-21314-score" class="comment-score"></div><div class="comment-text"><p>Agree with you,Thanks for replying.</p></div><div id="comment-21314-info" class="comment-info"><span class="comment-age">(20 May '13, 08:35)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-21304" class="comment-tools"></div><div class="clear"></div><div id="comment-21304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21316"></span>

<div id="answer-container-21316" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21316-score" class="post-score" title="current number of votes">4</div><span id="post-21316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Kurt said, there is no guaranteed way to determine this, but here are a couple of things you can try:</p><ol><li>Look for frames smaller than 60 bytes. The minimum Ethernet frame size is 64 bytes. If a frame is smaller than this, then padding bytes will be added to bring it up to 64 bytes. When Wireshark sees an outgoing frame, the four-byte frame check sequence hasn't been added yet, and when Wireshark sees an incoming frame, the frame check sequence has already been stripped off, (at least on the Windows systems that I'm familiar with; some systems may pass the frame check sequence to Wireshark). So the smallest Ethernet frame that Wireshark should see is 60 bytes. If you see a frame smaller than 60 bytes, then it was below the minimum Ethernet frame size and the padding had not yet been added when Wireshark saw the frame, so the system that transmitted that frame is where the packets were captured.</li><li>Turn on IP, TCP, and UDP checksum validation and look for packets with bad checksums. Most modern NICs do checksum offloading, which means that the checksum is calculated and applied by the NIC after Wireshark sees an outgoing frame. If you see bad checksums only on packets transmitted by one host, then that is probably the host where the data was captured. The checksums are good when the frames are transmitted on the wire. If the checksums were actually bad, then the packets with bad checksums would have been retransmitted or the communication would fail.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 May '13, 10:04</strong> </span></p></div></div><div id="comments-container-21316" class="comments-container"><span id="21318"></span><div id="comment-21318" class="comment"><div id="post-21318-score" class="comment-score"></div><div class="comment-text"><p>Brilliant,it worked sir!grand salute sir.</p></div><div id="comment-21318-info" class="comment-info"><span class="comment-age">(20 May '13, 09:34)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-21316" class="comment-tools"></div><div class="clear"></div><div id="comment-21316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

