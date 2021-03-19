+++
type = "question"
title = "tshark RTP/AMR payload/data export"
description = '''By running the command tshark -r file.pcap -T pdml, we can get a dump of the field names which tshark/wireshark can display. I do not see any way to extract the: field name=&quot;&quot; show=&quot;Frame Data (32 Bytes)&quot; value. I was hoping to use tshark to get the AMR payload similar to tshark -r file.pcap -T fiel...'''
date = "2015-04-28T08:10:00Z"
lastmod = "2015-04-29T02:04:00Z"
weight = 41919
keywords = [ "tshark", "rtp" ]
aliases = [ "/questions/41919" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark RTP/AMR payload/data export](/questions/41919/tshark-rtpamr-payloaddata-export)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41919-score" class="post-score" title="current number of votes">0</div><span id="post-41919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>By running the command tshark -r file.pcap -T pdml, we can get a dump of the field names which tshark/wireshark can display. I do not see any way to extract the: field name="" show="Frame Data (32 Bytes)" value. I was hoping to use tshark to get the AMR payload similar to tshark -r file.pcap -T fields -e data. This command works if tshark/wireshark is not able to decode the UDP payload.</p><p>example of tshark -r file.pcap -T pdml ...</p><pre><code>  &lt;proto name=&quot;rtp&quot; showname=&quot;Real-Time Transport Protocol&quot; size=&quot;45&quot; pos=&quot;48&quot;&gt;
    &lt;field name=&quot;rtp.setup&quot; showname=&quot;Stream setup by SDP (frame 6)&quot; size=&quot;0&quot; pos=&quot;48&quot; show=&quot;&quot;&gt;
      &lt;field name=&quot;rtp.setup-frame&quot; showname=&quot;Setup frame: 6&quot; size=&quot;0&quot; pos=&quot;48&quot; show=&quot;6&quot;/&gt;
      &lt;field name=&quot;rtp.setup-method&quot; showname=&quot;Setup Method: SDP&quot; size=&quot;0&quot; pos=&quot;48&quot; show=&quot;SDP&quot;/&gt;
    &lt;/field&gt;
    &lt;field name=&quot;rtp.version&quot; showname=&quot;10.. .... = Version: RFC 1889 Version (2)&quot; size=&quot;1&quot; pos=&quot;48&quot; show=&quot;2&quot; value=&quot;2&quot; unmaskedvalue=&quot;80&quot;/&gt;
    &lt;field name=&quot;rtp.padding&quot; showname=&quot;..0. .... = Padding: False&quot; size=&quot;1&quot; pos=&quot;48&quot; show=&quot;0&quot; value=&quot;0&quot; unmaskedvalue=&quot;80&quot;/&gt;
    &lt;field name=&quot;rtp.ext&quot; showname=&quot;...0 .... = Extension: False&quot; size=&quot;1&quot; pos=&quot;48&quot; show=&quot;0&quot; value=&quot;0&quot; unmaskedvalue=&quot;80&quot;/&gt;
    &lt;field name=&quot;rtp.cc&quot; showname=&quot;.... 0000 = Contributing source identifiers count: 0&quot; size=&quot;1&quot; pos=&quot;48&quot; show=&quot;0&quot; value=&quot;0&quot; unmaskedvalue=&quot;80&quot;/&gt;
    &lt;field name=&quot;rtp.marker&quot; showname=&quot;0... .... = Marker: False&quot; size=&quot;1&quot; pos=&quot;49&quot; show=&quot;0&quot; value=&quot;0&quot; unmaskedvalue=&quot;68&quot;/&gt;
    &lt;field name=&quot;rtp.p_type&quot; showname=&quot;Payload type: AMR-WB (104)&quot; size=&quot;1&quot; pos=&quot;49&quot; show=&quot;104&quot; value=&quot;68&quot; unmaskedvalue=&quot;68&quot;/&gt;
    &lt;field name=&quot;rtp.seq&quot; showname=&quot;Sequence number: 399&quot; size=&quot;2&quot; pos=&quot;50&quot; show=&quot;399&quot; value=&quot;018f&quot;/&gt;
    &lt;field name=&quot;rtp.extseq&quot; showname=&quot;Extended sequence number: 65935&quot; size=&quot;2&quot; pos=&quot;50&quot; show=&quot;65935&quot; value=&quot;018f&quot;/&gt;
    &lt;field name=&quot;rtp.timestamp&quot; showname=&quot;Timestamp: 95304&quot; size=&quot;4&quot; pos=&quot;52&quot; show=&quot;95304&quot; value=&quot;00017448&quot;/&gt;
    &lt;field name=&quot;rtp.ssrc&quot; showname=&quot;Synchronization Source identifier: 0x0000f800 (63488)&quot; size=&quot;4&quot; pos=&quot;56&quot; show=&quot;63488&quot; value=&quot;0000f800&quot;/&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;amr&quot; showname=&quot;Adaptive Multi-Rate&quot; size=&quot;33&quot; pos=&quot;60&quot;&gt;
    &lt;field name=&quot;&quot; show=&quot;Payload decoded as RFC 3267 bandwidth-efficient mode&quot; size=&quot;33&quot; pos=&quot;60&quot; value=&quot;f17017f03865b095e96be78073c3897080d2d0fe674de85bb00cc6d87b8cd436fc&quot;/&gt;
    &lt;field name=&quot;amr.wb.cmr&quot; showname=&quot;1111 .... = CMR: No mode request (15)&quot; size=&quot;1&quot; pos=&quot;60&quot; show=&quot;15&quot; value=&quot;f1&quot;/&gt;
    &lt;field name=&quot;amr.toc.f&quot; showname=&quot;.... 0... = F bit: Last frame in this payload&quot; size=&quot;1&quot; pos=&quot;60&quot; show=&quot;0&quot; value=&quot;f1&quot;/&gt;
    &lt;field name=&quot;amr.wb.toc.ft&quot; showname=&quot;.... .001  0... .... = FT bits: AMR-WB 12.65 kbit/s (2) / Frame OK&quot; size=&quot;2&quot; pos=&quot;60&quot; show=&quot;2&quot; value=&quot;f170&quot;/&gt;
    &lt;field name=&quot;amr.toc.q&quot; showname=&quot;.1.. .... = Q bit: Ok&quot; size=&quot;1&quot; pos=&quot;61&quot; show=&quot;1&quot; value=&quot;70&quot;/&gt;
    &lt;field name=&quot;&quot; show=&quot;Frame Data (32 Bytes)&quot; size=&quot;32&quot; pos=&quot;61&quot; value=&quot;7017f03865b095e96be78073c3897080d2d0fe674de85bb00cc6d87b8cd436fc&quot;/&gt;
  &lt;/proto&gt;</code></pre><p>desired output from tshark (&lt;field name="" show="Frame Data (32 Bytes)" size="32" pos="61" value=...):</p><p>6e512f224ee5b53453ba7b0f41da57e2dbd9d1d0f1226b2b3fb77f3f26a01818 7017f03865b095e96be78073c3897080d2d0fe674de85bb00cc6d87b8cd436fc</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '15, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/53b8847fa65a923a3053e9de044061ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ler224&#39;s gravatar image" /><p><span>ler224</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ler224 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '15, 08:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41919" class="comments-container"></div><div id="comment-tools-41919" class="comment-tools"></div><div class="clear"></div><div id="comment-41919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41936"></span>

<div id="answer-container-41936" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41936-score" class="post-score" title="current number of votes">1</div><span id="post-41936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ler224 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately the dissector author choose to use a deprecated function to show that data, a function that creates a non filterable field. Either a change to the dissector code should be implemented, or a different packet export chosen, which allows for easier (text-)filtering.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '15, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41936" class="comments-container"><span id="41938"></span><div id="comment-41938" class="comment"><div id="post-41938-score" class="comment-score"></div><div class="comment-text"><p>IF you're unable to chnage (and submit) the change to the dissector yourself, you can raise an issue on the <a href="https://bugs.wireshark.org/">Wireshark Bugzilla</a>. Attaching a capture that displays the issue helps enormously.</p></div><div id="comment-41938-info" class="comment-info"><span class="comment-age">(29 Apr '15, 02:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41936" class="comment-tools"></div><div class="clear"></div><div id="comment-41936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

