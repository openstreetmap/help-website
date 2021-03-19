+++
type = "question"
title = "Networking Issue or Wireshark"
description = '''All,  I recently inherited a large airport network and I&#x27;m performing Wireshark analysis to get a feel of what is being transmitted. I&#x27;m seeing a lot of Dup Acks, TCP Retransmits and Reassembling. The trace that I will post was between two computers performing a simple file transfer. The two compute...'''
date = "2012-08-02T09:30:00Z"
lastmod = "2012-08-02T11:27:00Z"
weight = 13321
keywords = [ "duplicates", "reassembly", "retransmissions", "wireshark" ]
aliases = [ "/questions/13321" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Networking Issue or Wireshark](/questions/13321/networking-issue-or-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13321-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All,</p><p>I recently inherited a large airport network and I'm performing Wireshark analysis to get a feel of what is being transmitted. I'm seeing a lot of Dup Acks, TCP Retransmits and Reassembling. The trace that I will post was between two computers performing a simple file transfer. The two computers are attached to the same Cisco switch, member of the same VLAN and in the same building. I'm seeing no errors or drop packets when I look at the switchport. Do I have a network issue or is it the configuration of Wireshark. Thanks</p><p><a href="https://docs.google.com/open?id=0B8IhRTPihfVvLXdDSUNLdHVmVUk">https://docs.google.com/open?id=0B8IhRTPihfVvLXdDSUNLdHVmVUk</a></p></div><div id="question-tags" class="tags-container tags">duplicates reassembly retransmissions wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '12, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/70d989eae374237595a75f67552c53b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyarger&#39;s gravatar image" /><p>tyarger<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyarger has no accepted answers">0%</span></p></div></div><div id="comments-container-13321" class="comments-container"><span id="13324"></span><div id="comment-13324" class="comment"><div id="post-13324-score" class="comment-score"></div><div class="comment-text"><p>I apologize for the large file. I was in a hurry and didn't apply the proper filters. I appreciate your help. I'll perform another capture and post with the three way handshake.</p></div><div id="comment-13324-info" class="comment-info"><span class="comment-age">(02 Aug '12, 11:55)</span> tyarger</div></div></div><div id="comment-tools-13321" class="comment-tools"></div><div class="clear"></div><div id="comment-13321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13322"></span>

<div id="answer-container-13322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13322-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all... almost 400MB of trace file are not exactly a good thing to post, because you can't expect anyone to take a look at that much data in detail. You should reduce trace files to a size that is showing your problem in as few packets as possible, so people will be more willing to spend their time to help you.</p><p>And yes, it looks like you have a problem with lost frames that trigger fast retransmissions. The lost frames are not the real problem, because they tend to happen in any network. Unfortunately you did not capture the three way handshake, but I guess your PCs are using window scaling and quite large receive windows. Because of it when a frame gets lost it takes a while to retransmit since the sender is pushing out tons of packets due to the large window, and so the retransmission comes in late after a ton of duplicate acks. This is a quite common thing to see these days, especially since Windows Vista/7/2008/2008R2.</p><p>See @landi's Sharkfest talk "A-18: Effects of Receiver-Side Window Scaling on Enterprise Networks" at <a href="http://sharkfest.wireshark.org/sharkfest.12/index.html">http://sharkfest.wireshark.org/sharkfest.12/index.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '12, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Aug '12, 11:29</p></div></div><div id="comments-container-13322" class="comments-container"><span id="13326"></span><div id="comment-13326" class="comment"><div id="post-13326-score" class="comment-score"></div><div class="comment-text"><p>I performed another trace with the three way handshake visible and a much smaller file transfer. Thanks again</p><p><a href="http://www.cloudshark.org/captures/8606deee840f">http://www.cloudshark.org/captures/8606deee840f</a></p></div><div id="comment-13326-info" class="comment-info"><span class="comment-age">(02 Aug '12, 13:07)</span> tyarger</div></div><span id="13329"></span><div id="comment-13329" class="comment"><div id="post-13329-score" class="comment-score"></div><div class="comment-text"><p>Okay, looks like your window scaling factor is 8, which means that the window size is multiplied by 256. In your case it means that your receiver advertised a buffer of almost half a megabyte. When the packet gets lost the sender has already pushed out a lot of data, which leads to the fast retransmission trailing in after tons of dupe acks. I think your network isn't performing bad, you just loose a packet here and there, and because of the large window the retransmission takes a while to come in.</p></div><div id="comment-13329-info" class="comment-info"><span class="comment-age">(02 Aug '12, 15:15)</span> Jasper ♦♦</div></div></div><div id="comment-tools-13322" class="comment-tools"></div><div class="clear"></div><div id="comment-13322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

