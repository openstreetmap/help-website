+++
type = "question"
title = "Does Wireshark capture/support RSC packets"
description = '''Hi,  Windows 8 Server and certain network adapters will be supporting Receive Side Coalescing (or Receive Segment Coalescing if you&#x27;re Intel). Does Wireshark support the capturing of Coalesced packets? Will Wireshark have any restrictions on the packet size?  Thank you! '''
date = "2012-02-16T11:01:00Z"
lastmod = "2014-09-04T05:39:00Z"
weight = 9074
keywords = [ "windows8", "coalescing", "rsc" ]
aliases = [ "/questions/9074" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark capture/support RSC packets](/questions/9074/does-wireshark-capturesupport-rsc-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9074-score" class="post-score" title="current number of votes">0</div><span id="post-9074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Windows 8 Server and certain network adapters will be supporting Receive Side Coalescing (or Receive Segment Coalescing if you're Intel). Does Wireshark support the capturing of Coalesced packets? Will Wireshark have any restrictions on the packet size?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows8" rel="tag" title="see questions tagged &#39;windows8&#39;">windows8</span> <span class="post-tag tag-link-coalescing" rel="tag" title="see questions tagged &#39;coalescing&#39;">coalescing</span> <span class="post-tag tag-link-rsc" rel="tag" title="see questions tagged &#39;rsc&#39;">rsc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '12, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/d28d90e7ebf0160c8a0ee55e87f6a95f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eastilleros&#39;s gravatar image" /><p><span>eastilleros</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eastilleros has no accepted answers">0%</span></p></div></div><div id="comments-container-9074" class="comments-container"></div><div id="comment-tools-9074" class="comment-tools"></div><div class="clear"></div><div id="comment-9074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9081"></span>

<div id="answer-container-9081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9081-score" class="post-score" title="current number of votes">1</div><span id="post-9081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ul><li>Does Wireshark support the capturing of Coalesced packets?</li></ul><p>This seems to be done in the NIC, or low level driver. It's most likely WinPcap will see the packets after that, which should be indistinguishable from normal packets.</p><ul><li>Will Wireshark have any restrictions on the packet size?</li></ul><p>WinPcap captures into the pcap format which has a max record size of 64kB. That would pose a limit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '12, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-9081" class="comments-container"><span id="9083"></span><div id="comment-9083" class="comment"><div id="post-9083-score" class="comment-score">1</div><div class="comment-text"><p>"Indistinguishable" other than perhaps being much larger than the largest link-layer frame size on the network type on which you're capturing; for example, you might have Ethernet packet larger than 1514 bytes (without FCS)/1518 bytes (including FCS).</p><p>Actually, pcap itself doesn't have a maximum record size of 64KB, but Wireshark <em>currently</em> imposes that limit (so it doesn't try to do ridiculously-large memory allocation with a corrupted capture); that limit could be raised, although we'll probably never raise it to, say, 2^32-1.</p></div><div id="comment-9083-info" class="comment-info"><span class="comment-age">(17 Feb '12, 00:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-9081" class="comment-tools"></div><div class="clear"></div><div id="comment-9081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36000"></span>

<div id="answer-container-36000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36000-score" class="post-score" title="current number of votes">0</div><span id="post-36000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In windows the RSC getting disabled after i start wireshark</p><p>RSC table before starting wireshark</p><p><code>PS C:\Users\Administrator&gt; get-netadapterrsc</code></p><code></code><p><code>Name        IPv4Enabled  IPv6Enabled  IPv4Operational IPv6Operational IPv4FailureReason IPv6Failure                                       State           State                             Reason ----        -----------  -----------  --------------- --------------- ----------------- ------------ Ethernet 4  True         True         True            True            NoFailure         NoFailure Ethernet 3  True         True         True            True            NoFailure         NoFailure</code></p><p>RSC table after starting wireshark.</p><p><code>PS C:\Users\Administrator&gt; get-netadapterrsc|format-table -wrap -autosize</code></p><code></code><p><code>Name       IPv4Enabled IPv6Enabled IPv4OperationalState IPv6OperationalState IPv4FailureReason IPv6FailureReason ----       ----------- ----------- -------------------- -------------------- ----------------- ----------------- Ethernet 4 True        True        False                False                NDISCompatibility NDISCompatibility Ethernet 3 True        True        False                False                NDISCompatibility NDISCompatibility</code></p><p>The above output is complaining about the NDIS for compatibility.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '14, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/a76c80d3ab3b8e4115206df2f80176b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Naveen1115&#39;s gravatar image" /><p><span>Naveen1115</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Naveen1115 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Sep '14, 10:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36000" class="comments-container"></div><div id="comment-tools-36000" class="comment-tools"></div><div class="clear"></div><div id="comment-36000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

