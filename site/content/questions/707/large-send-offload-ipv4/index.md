+++
type = "question"
title = "large send offload (ipv4)"
description = '''if large send offload (ipv4) setting is enabled on the server (default nic setting) and disabled on the client (default nic setting) what problems can arise from a mismatched LSO setting if any? is there any indication in WS trace that large send offload (ipv4) is enabled/disabled on the NIC? Thanks'''
date = "2010-10-27T10:25:00Z"
lastmod = "2010-10-28T08:49:00Z"
weight = 707
keywords = [ "large", "lso", "offload", "send" ]
aliases = [ "/questions/707" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [large send offload (ipv4)](/questions/707/large-send-offload-ipv4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-707-score" class="post-score" title="current number of votes">0</div><span id="post-707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>if large send offload (ipv4) setting is enabled on the server (default nic setting) and disabled on the client (default nic setting) what problems can arise from a mismatched LSO setting if any? is there any indication in WS trace that large send offload (ipv4) is enabled/disabled on the NIC?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-lso" rel="tag" title="see questions tagged &#39;lso&#39;">lso</span> <span class="post-tag tag-link-offload" rel="tag" title="see questions tagged &#39;offload&#39;">offload</span> <span class="post-tag tag-link-send" rel="tag" title="see questions tagged &#39;send&#39;">send</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '10, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p><span>net_tech</span><br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>07 Jan '11, 02:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span></p></div></div><div id="comments-container-707" class="comments-container"></div><div id="comment-tools-707" class="comment-tools"></div><div class="clear"></div><div id="comment-707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="709"></span>

<div id="answer-container-709" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-709-score" class="post-score" title="current number of votes">2</div><span id="post-709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="net_tech has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>LSO is an internal process - when the packets go out on the wire, they are not larger than a normal packet. Just like TCP Segmentation Offload and Large Receive Offload, this feature is designed to improve performance by using the brains of the adapter for certain tasks.</p><p>See http://www.chappellseminars.com/10blog0907.html (and the image of a LSO capture) for the effect of LSO on Wireshark. In essence, if Wireshark is running on the sending machine that supports LSO, Wireshark will see unusually high frame length values when LSO is in use.</p><p>I don't image mismatched LSO settings should cause a problem because again, on the wire the packets are normal size.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-709" class="comments-container"></div><div id="comment-tools-709" class="comment-tools"></div><div class="clear"></div><div id="comment-709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="711"></span>

<div id="answer-container-711" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-711-score" class="post-score" title="current number of votes">1</div><span id="post-711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am troubleshooting an RDP issue ("Because of an error in data encryption, this session will end. Please try connecting to the remote computer again) and came across a long thread on MS forum, where the problem seem to be related to LSO setting of the NIC. I thought miss-matched LSO setting (server – client) had something to do with it, but apparently not.</p><p><a href="http://social.technet.microsoft.com/Forums/en-US/winserverTS/thread/3e4e9d8a-cf6a-4e7a-9072-f9ecd3f17a72/#43a55f95-3e39-47a1-bd09-9b15cbd06f29">MS Forum Link</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p><span>net_tech</span><br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Oct '10, 12:41</strong> </span></p></div></div><div id="comments-container-711" class="comments-container"><span id="714"></span><div id="comment-714" class="comment"><div id="post-714-score" class="comment-score">1</div><div class="comment-text"><p>As Laura said, "LSO is an internal process - when the packets go out on the wire, they are not larger than a normal packet." LSO, like TSO and LRO, just hands some of the job of processing packets from the host's TCP/IP stack to the adapter's TCP/IP stack; it doesn't affect what's on the wire, unlike, for example, Ethernet full and half duplex, so there's no need for the settings on the machines to match.</p></div><div id="comment-714-info" class="comment-info"><span class="comment-age">(27 Oct '10, 16:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="728"></span><div id="comment-728" class="comment"><div id="post-728-score" class="comment-score"></div><div class="comment-text"><p>This is almost identical to my problem, the only difference is my Windows 2008 is on VMWare server.</p><p>http://www.petri.co.il/network-issues-with-windows-server-2008-rdp-on-dell-servers.htm</p><p>What I am getting out of this is that everything that makes logical sense and works on the physical network DOES NOT, when virtualization is involved.</p></div><div id="comment-728-info" class="comment-info"><span class="comment-age">(28 Oct '10, 08:49)</span> <span class="comment-user userinfo">net_tech</span></div></div></div><div id="comment-tools-711" class="comment-tools"></div><div class="clear"></div><div id="comment-711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

