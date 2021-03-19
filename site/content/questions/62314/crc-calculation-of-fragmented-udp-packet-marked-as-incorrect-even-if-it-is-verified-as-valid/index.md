+++
type = "question"
title = "CRC calculation of fragmented UDP packet marked as incorrect. Even if it is verified as valid."
description = '''I am using Wireshark (Version 2.2.7 (v2.2.7-0-g1861a96)) and was hoping someone explain why fragmented udp packets with a valid CRC are being marked with Checksum 0x7c21 [incorrect, should be 0xf934] (maybe caused by &quot;UDP checksum offload&quot;) even if the packet has the checksum of 0xf934. Any help wou...'''
date = "2017-06-26T18:27:00Z"
lastmod = "2017-06-28T06:33:00Z"
weight = 62314
keywords = [ "crc", "udp", "checksum" ]
aliases = [ "/questions/62314" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [CRC calculation of fragmented UDP packet marked as incorrect. Even if it is verified as valid.](/questions/62314/crc-calculation-of-fragmented-udp-packet-marked-as-incorrect-even-if-it-is-verified-as-valid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62314-score" class="post-score" title="current number of votes">0</div><span id="post-62314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark (Version 2.2.7 (v2.2.7-0-g1861a96)) and was hoping someone explain why fragmented udp packets with a valid CRC are being marked with Checksum 0x7c21 [incorrect, should be 0xf934] (maybe caused by "UDP checksum offload") even if the packet has the checksum of 0xf934. Any help would be appreciated. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crc" rel="tag" title="see questions tagged &#39;crc&#39;">crc</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '17, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/74e62b7b08522dfffcf3318af951ae3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slb3&#39;s gravatar image" /><p><span>slb3</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slb3 has no accepted answers">0%</span></p></div></div><div id="comments-container-62314" class="comments-container"><span id="62315"></span><div id="comment-62315" class="comment"><div id="post-62315-score" class="comment-score"></div><div class="comment-text"><p>Is that the <em>IP</em> checksum or the <em>UDP</em> checksum (neither of which are Cyclic Redundancy Checks)?</p></div><div id="comment-62315-info" class="comment-info"><span class="comment-age">(26 Jun '17, 18:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="62334"></span><div id="comment-62334" class="comment"><div id="post-62334-score" class="comment-score"></div><div class="comment-text"><p>When you say fragmented I assume you mean IP fragmentation?</p><p>Do you have IP reassembly enabled? If not it may be that we're trying to check the checksum when we're not supposed to be.</p><p>It might be simpler if you just posted the PCAP file.</p></div><div id="comment-62334-info" class="comment-info"><span class="comment-age">(27 Jun '17, 06:40)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="62340"></span><div id="comment-62340" class="comment"><div id="post-62340-score" class="comment-score"></div><div class="comment-text"><p>Yes. I meant checksum not crc. I found if I turn off the IPv4 reassembly the "problem" with not calculating the UDP checksum is not marked as an error (but is unverified).</p></div><div id="comment-62340-info" class="comment-info"><span class="comment-age">(27 Jun '17, 10:02)</span> <span class="comment-user userinfo">slb3</span></div></div></div><div id="comment-tools-62314" class="comment-tools"></div><div class="clear"></div><div id="comment-62314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62342"></span>

<div id="answer-container-62342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62342-score" class="post-score" title="current number of votes">0</div><span id="post-62342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds as if it's the UDP checksum.</p><p>If the UDP packet is fragmented, its checksum cannot be calculated unless it's reassembled, so Wireshark can't verify the checksum.</p><p>If the checksum is reported as incorrect, either it really <em>is</em> incorrect, or it's a packet sent by the machine on which the capture was done and the network adapter is doing checksum offloading (so that the copy of the packet handed to the capture program hasn't had the checksum set), or there's a bug in Wireshark.</p><p>To determine which of those is the case, we'd need a copy of the capture. Please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> and attach the capture file to it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62342" class="comments-container"><span id="62343"></span><div id="comment-62343" class="comment"><div id="post-62343-score" class="comment-score"></div><div class="comment-text"><p>Yes. It is a UDP checksum issue. I will post a copy of the pcap file in Wireshark's Bugzillia. Thanks.</p></div><div id="comment-62343-info" class="comment-info"><span class="comment-age">(27 Jun '17, 10:25)</span> <span class="comment-user userinfo">slb3</span></div></div><span id="62344"></span><div id="comment-62344" class="comment"><div id="post-62344-score" class="comment-score"></div><div class="comment-text"><p>Bug # <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13853">13853</a></p></div><div id="comment-62344-info" class="comment-info"><span class="comment-age">(27 Jun '17, 11:00)</span> <span class="comment-user userinfo">slb3</span></div></div><span id="62356"></span><div id="comment-62356" class="comment"><div id="post-62356-score" class="comment-score"></div><div class="comment-text"><p>If you could answer the questions posted in the bug, that would be helpful too.</p></div><div id="comment-62356-info" class="comment-info"><span class="comment-age">(28 Jun '17, 06:33)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-62342" class="comment-tools"></div><div class="clear"></div><div id="comment-62342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

