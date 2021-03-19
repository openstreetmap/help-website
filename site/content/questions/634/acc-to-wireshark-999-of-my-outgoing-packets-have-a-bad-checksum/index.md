+++
type = "question"
title = "Acc. to Wireshark, 99.9% of my outgoing packets have a bad checksum..."
description = '''Pretty much stated above. When applying the filter ip.src == &amp;lt;my IP&amp;gt;, almost all of the packets are color-coded &quot;bad checksum&quot;. It claims all of the packets&#x27; checksums are 0x0000. ATM, I have ~2500 packets in the filter, and probably less than 10 of them aren&#x27;t highlighted as having a bad chec...'''
date = "2010-10-25T16:35:00Z"
lastmod = "2012-10-05T11:29:00Z"
weight = 634
keywords = [ "color-rules", "checksum", "bad", "wireshark" ]
aliases = [ "/questions/634" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Acc. to Wireshark, 99.9% of my outgoing packets have a bad checksum...](/questions/634/acc-to-wireshark-999-of-my-outgoing-packets-have-a-bad-checksum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-634-score" class="post-score" title="current number of votes">2</div><span id="post-634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Pretty much stated above. When applying the filter <code>ip.src == &lt;my IP&gt;</code>, almost all of the packets are color-coded "bad checksum". It claims all of the packets' checksums are 0x0000. ATM, I have ~2500 packets in the filter, and probably less than 10 of them aren't highlighted as having a bad checksum. Is this a bug in Wireshark, or is something seriously wrong with my internet connection?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-color-rules" rel="tag" title="see questions tagged &#39;color-rules&#39;">color-rules</span> <span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-bad" rel="tag" title="see questions tagged &#39;bad&#39;">bad</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '10, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/c04f2b4fb0d88dc25e89378b9b0542b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hmmwhatsthisdo&#39;s gravatar image" /><p><span>hmmwhatsthisdo</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hmmwhatsthisdo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Oct '10, 16:52</strong> </span></p></div></div><div id="comments-container-634" class="comments-container"></div><div id="comment-tools-634" class="comment-tools"></div><div class="clear"></div><div id="comment-634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="635"></span>

<div id="answer-container-635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-635-score" class="post-score" title="current number of votes">2</div><span id="post-635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Answer: neither....</p><p>Sounds like checksum offloading.</p><p>See:</p><p><a href="http://wiki.wireshark.org/CaptureSetup/Offloading">http://wiki.wireshark.org/CaptureSetup/Offloading</a></p><p><a href="http://wiki.wireshark.org/TCP_Checksum_Verification">http://wiki.wireshark.org/TCP_Checksum_Verification</a></p><p>In a nutshell: the NIC card does the checksum calculation just before sending the packet on the wire.<br />
So: when Wireshark gets the packet, the checksum is 0 because it hasn't been calculated yet.</p><p>There's no actual problem. See the referenced links for how to disable the verification of the checksum in Wireshark.</p><p>(Ps: Please use "comment" rather than "answer": See the FAQ as to how ask.wireshark works)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '10, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Oct '10, 17:23</strong> </span></p></div></div><div id="comments-container-635" class="comments-container"><span id="636"></span><div id="comment-636" class="comment"><div id="post-636-score" class="comment-score"></div><div class="comment-text"><p>And, this won't do any sort of damage to my network connection?</p><p>EDIT: It seems to have helped. Apparently there's 5 different options you need to (un)set in the network adapter - IPv4 Checksum Offload, TCP Checksum Offload (one for IPv4 and one for IPv6), and UDP Checksum Offload (same situation as TCP).</p></div><div id="comment-636-info" class="comment-info"><span class="comment-age">(25 Oct '10, 17:00)</span> <span class="comment-user userinfo">hmmwhatsthisdo</span></div></div><span id="638"></span><div id="comment-638" class="comment"><div id="post-638-score" class="comment-score">2</div><div class="comment-text"><p>You don't want to disable checksum offloading in the adapter - you can disable verification of checksums in Wireshark so this doesn't bother you.</p><p>Edit &gt; Preferences &gt; + Protocols .... disable Validate the x Checksum if possible in UDP, TCP and IP</p></div><div id="comment-638-info" class="comment-info"><span class="comment-age">(25 Oct '10, 18:12)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div><span id="639"></span><div id="comment-639" class="comment"><div id="post-639-score" class="comment-score"></div><div class="comment-text"><p>Why wouldn't I want to disable checksum offloading in the adapter? Is it some sort of security risk?</p></div><div id="comment-639-info" class="comment-info"><span class="comment-age">(25 Oct '10, 18:16)</span> <span class="comment-user userinfo">hmmwhatsthisdo</span></div></div><span id="640"></span><div id="comment-640" class="comment"><div id="post-640-score" class="comment-score">2</div><div class="comment-text"><p>It's some sort of potential <em>performance</em> risk - if disabled, the CPU has to fetch every byte of the packet data to compute the checksum in the CPU, but, if enabled, the adapter, which has to fetch every byte anyway to transmit it, can compute the checksum in <em>its</em> hardware.</p></div><div id="comment-640-info" class="comment-info"><span class="comment-age">(25 Oct '10, 19:00)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="641"></span><div id="comment-641" class="comment"><div id="post-641-score" class="comment-score"></div><div class="comment-text"><p>So, do you recommend I disable checksum offloading in Windows, disable checksum verification in WS, or both?</p></div><div id="comment-641-info" class="comment-info"><span class="comment-age">(25 Oct '10, 19:01)</span> <span class="comment-user userinfo">hmmwhatsthisdo</span></div></div><span id="14735"></span><div id="comment-14735" class="comment not_top_scorer"><div id="post-14735-score" class="comment-score"></div><div class="comment-text"><p>It's better to disable on the WS side. I'm having the same problem because some pcs can connect to the server and other can't. So I run the WS on the server side but it shows me a lot of Offloading IP checksum errors. Can the network adapter be damaged?</p></div><div id="comment-14735-info" class="comment-info"><span class="comment-age">(05 Oct '12, 11:16)</span> <span class="comment-user userinfo">Brennero Pardo</span></div></div><span id="14736"></span><div id="comment-14736" class="comment not_top_scorer"><div id="post-14736-score" class="comment-score"></div><div class="comment-text"><p><span>@Brennero Pardo</span>: If it shows them on <em>outgoing</em> packets, then it's the same problem. If you want to see the checksums of all packets on the wire/on the air, you'd need to run a sniffer on a separate machine and passively tap the network, or run it on both client and server and look at the checksums only on packets <em>received</em> by each of the machines.</p></div><div id="comment-14736-info" class="comment-info"><span class="comment-age">(05 Oct '12, 11:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-635" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="676"></span>

<div id="answer-container-676" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-676-score" class="post-score" title="current number of votes">1</div><span id="post-676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For right now, I'd disable checksum verification in Wireshark if the false alarms bother you.</p><p>One point of interest...if the machine in question is running Windows Server 2003 SP2 or Windows Small Business Server, there are specific client/server performance issues related to those features. See <a href="http://support.microsoft.com/kb/948496">http://support.microsoft.com/kb/948496</a> if you are running either of those operating systems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-676" class="comments-container"></div><div id="comment-tools-676" class="comment-tools"></div><div class="clear"></div><div id="comment-676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

