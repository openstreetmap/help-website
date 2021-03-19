+++
type = "question"
title = "wrong vlan outer tag shown?"
description = '''I am doing dot1q tunnel and I use double tagging. I tag the frame with outer vlan 220, but in Wireshark, it shows vlan 1195. Is it any conversion from 220 to 1195? or what i am seeing is not the outer vlan?  Thanks! the photo is attached: https://docs.google.com/file/d/0B6xwIiuptf5NZl90V0dlWWIzUUU/e...'''
date = "2012-11-08T00:22:00Z"
lastmod = "2012-11-08T19:45:00Z"
weight = 15682
keywords = [ "vlan", "id" ]
aliases = [ "/questions/15682" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [wrong vlan outer tag shown?](/questions/15682/wrong-vlan-outer-tag-shown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15682-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am doing dot1q tunnel and I use double tagging. I tag the frame with outer vlan 220, but in Wireshark, it shows vlan 1195.</p><p>Is it any conversion from 220 to 1195? or what i am seeing is not the outer vlan? Thanks!</p><p>the photo is attached: <a href="https://docs.google.com/file/d/0B6xwIiuptf5NZl90V0dlWWIzUUU/edit">https://docs.google.com/file/d/0B6xwIiuptf5NZl90V0dlWWIzUUU/edit</a></p></div><div id="question-tags" class="tags-container tags">vlan id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/8ab2bc114b3fb950f50b5c340c4e580e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bennettfan&#39;s gravatar image" /><p>bennettfan<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bennettfan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '12, 07:16</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-15682" class="comments-container"><span id="15690"></span><div id="comment-15690" class="comment"><div id="post-15690-score" class="comment-score"></div><div class="comment-text"><p>can you please post that single packet in pcap format on <a href="http://cloudshark.org">cloudshark.org</a>?</p></div><div id="comment-15690-info" class="comment-info"><span class="comment-age">(08 Nov '12, 01:01)</span> Kurt Knochner ♦</div></div><span id="15694"></span><div id="comment-15694" class="comment"><div id="post-15694-score" class="comment-score"></div><div class="comment-text"><p>i don't know why i can not upload there. I just upload to google. <a href="https://docs.google.com/open?id=0B6xwIiuptf5NZk83cEZrNG5lMzQ">https://docs.google.com/open?id=0B6xwIiuptf5NZk83cEZrNG5lMzQ</a></p><p>can you see it?</p></div><div id="comment-15694-info" class="comment-info"><span class="comment-age">(08 Nov '12, 01:26)</span> bennettfan</div></div><span id="15695"></span><div id="comment-15695" class="comment"><div id="post-15695-score" class="comment-score"></div><div class="comment-text"><p>unfortunately that's not in pcap format (it's some hex dump). How did you capture the packet and how did you generate the hex dump? I need the packet in pcap format to analyze it with Wireshark.</p></div><div id="comment-15695-info" class="comment-info"><span class="comment-age">(08 Nov '12, 01:31)</span> Kurt Knochner ♦</div></div><span id="15696"></span><div id="comment-15696" class="comment"><div id="post-15696-score" class="comment-score"></div><div class="comment-text"><p>how about this file? I use wireshark to print out the packet and save it.</p><p><a href="https://docs.google.com/open?id=0B6xwIiuptf5NVE5QVGk2ODZ6Q0E">https://docs.google.com/open?id=0B6xwIiuptf5NVE5QVGk2ODZ6Q0E</a></p></div><div id="comment-15696-info" class="comment-info"><span class="comment-age">(08 Nov '12, 01:39)</span> bennettfan</div></div><span id="15697"></span><div id="comment-15697" class="comment"><div id="post-15697-score" class="comment-score"></div><div class="comment-text"><p>Same format :-). Please Export the packet like this:</p><ul><li>Mark the packet. Click on it then press CTRL-M</li><li>Wireshark 1.6: File -&gt; Save as -&gt; Marked Packets</li><li>Wireshark 1.8: File -&gt; Export Specified Packets -&gt; Marked Packets</li></ul></div><div id="comment-15697-info" class="comment-info"><span class="comment-age">(08 Nov '12, 01:56)</span> Kurt Knochner ♦</div></div><span id="15700"></span><div id="comment-15700" class="comment not_top_scorer"><div id="post-15700-score" class="comment-score"></div><div class="comment-text"><p><a href="http://cloudshark.org/captures/8607aff92c7b">http://cloudshark.org/captures/8607aff92c7b</a></p><p>^^THX</p></div><div id="comment-15700-info" class="comment-info"><span class="comment-age">(08 Nov '12, 02:15)</span> bennettfan</div></div></div><div id="comment-tools-15682" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-15682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15751"></span>

<div id="answer-container-15751" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15751-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark only shows what is in the packet. In your first/real sample there are two 32 Bit 802.1q VLAN tag fields added:</p><blockquote><p><code>Outer Tag: 24ac8100</code><br />
<code>Inner Tag: 20c6ffff</code><br />
</p></blockquote><p>According to the 802.1q standard, those values contain this:</p><blockquote><p><code>http://en.wikipedia.org/wiki/IEEE_802.1Q</code><br />
<code>http://www.cisco.com/en/US/tech/tk389/tk689/technologies_tech_note09186a0080094665.shtml</code><br />
</p></blockquote><p>16 Bit Tag Protocol Identifier (TPID)<br />
16 Bit Tag Control Identifier (TCI), where the last 12 Bits are the VLAN tag</p><p><strong>Outer Tag</strong></p><blockquote><p>TPID = 0x8100 (Tagged frame)<br />
TCI = 0x24ac. Last 12 Bits: 010010101100 == 4AC == <strong>1196</strong></p></blockquote><p><strong>Inner Tag</strong></p><blockquote><p>TPID = 0xffff <strong>HINT:</strong> This should be 0x800 if the remainder is an ethernet frame. 0xfff is kind of strange/wrong<br />
TCI = 0x20c6. Last 12 Bits: 000011000110 == C6 == <strong>198</strong></p></blockquote><p>So, as you can see Wireshark just shows what is in the packet. If that is not what you expected, there is either a problem with the part that generated that packet or the tool that captured the packet (and wrote it to a pcap file).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 19:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '12, 19:47</p></div></div><div id="comments-container-15751" class="comments-container"><span id="15752"></span><div id="comment-15752" class="comment"><div id="post-15752-score" class="comment-score"></div><div class="comment-text"><p>Noted. Thanks so much^^</p></div><div id="comment-15752-info" class="comment-info"><span class="comment-age">(08 Nov '12, 20:36)</span> bennettfan</div></div><span id="15762"></span><div id="comment-15762" class="comment"><div id="post-15762-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-15762-info" class="comment-info"><span class="comment-age">(09 Nov '12, 01:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15751" class="comment-tools"></div><div class="clear"></div><div id="comment-15751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15723"></span>

<div id="answer-container-15723" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15723-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark shows a straight interpretation of the packet data it sees. Like shown on the screenshot and the packet shown through cloudshark, it is double tagged, but it seems you define the inner tag or something, not the outer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-15723" class="comments-container"><span id="15750"></span><div id="comment-15750" class="comment"><div id="post-15750-score" class="comment-score"></div><div class="comment-text"><p>Below is the double tagging layer 2 frame generated by JDSU and I just post it. The outer vlan 4000 and inner vlan 50 is clearly shown. <a href="http://cloudshark.org/captures/2e701df8b958">http://cloudshark.org/captures/2e701df8b958</a></p><p>Can anyone tell more about is it any problem with the below frame? is it the outer vlan wrong ? what is it? <a href="http://cloudshark.org/captures/8607aff92c7b">http://cloudshark.org/captures/8607aff92c7b</a></p></div><div id="comment-15750-info" class="comment-info"><span class="comment-age">(08 Nov '12, 19:27)</span> bennettfan</div></div></div><div id="comment-tools-15723" class="comment-tools"></div><div class="clear"></div><div id="comment-15723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

