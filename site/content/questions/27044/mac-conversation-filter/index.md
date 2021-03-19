+++
type = "question"
title = "MAC conversation filter"
description = '''I have been working with Wireshark, AirPcap and Cascade for a few years now. One thing I frequently spend time on when I analyze a log is setting up what I’ll call a “MAC level conversation” filter. This is similar to the TCP/IP conversation filter except of course it is at the lowest level. For exa...'''
date = "2013-11-15T15:37:00Z"
lastmod = "2013-11-19T00:12:00Z"
weight = 27044
keywords = [ "filter", "conversation", "retransmission" ]
aliases = [ "/questions/27044" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [MAC conversation filter](/questions/27044/mac-conversation-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27044-score" class="post-score" title="current number of votes">0</div><span id="post-27044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been working with Wireshark, AirPcap and Cascade for a few years now. One thing I frequently spend time on when I analyze a log is setting up what I’ll call a “MAC level conversation” filter. This is similar to the TCP/IP conversation filter except of course it is at the lowest level. For example, if I want to restrict the display to show only packets going to/from an AP and STA, my filter looks like this:</p><p>(wlan.addr == 00:03:7f:04:09:7c) || (wlan.addr == 00:03:7f:04:09:6b)</p><p>The problem with this filter is two-fold: 1) There are packets triggered from other STA that clutter the log e.g. Probe Responses 2) In the presence of retransmissions, it takes a significant amount of manual post-log analysis to determine which packet(s) were actually received properly (acknowledged.)</p><p>Ideally, I would like to define a filter that was truly restricted to the properly transmitted and received packets between two devices. With this filter, for example, you would only see a retransmitted packet if and only if it was acknowledged by the correct device. The filter would also have enough “smarts” to use sequence numbers to determine if a packet acknowledgment was recognized - in other words, you would never see more than one packet of each sequence number after applying the filter.</p><p>It seems to me that a certain amount of scripting is required; one problem is that ACK packets do not have source addresses.</p><p>Anyone ever solve this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '13, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/55fa12360adc0075a07b4312027d6fc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ReidW&#39;s gravatar image" /><p><span>ReidW</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ReidW has no accepted answers">0%</span></p></div></div><div id="comments-container-27044" class="comments-container"></div><div id="comment-tools-27044" class="comment-tools"></div><div class="clear"></div><div id="comment-27044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27077"></span>

<div id="answer-container-27077" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27077-score" class="post-score" title="current number of votes">2</div><span id="post-27077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The filter would also have enough “smarts” to use <strong>sequence numbers</strong> to determine if a packet acknowledgment was recognized<br />
</p></blockquote><p>There are no sequence numbers in 802.11 ACK frames, so you can't build a 'simple' filter to find frames without an ACK.</p><blockquote><p>In order to filter out un-acknowledged packets <strong>we would need some smarts</strong> to check for an ACK - any idea how to do this?</p></blockquote><p>The 'smarts' could a script you'll have to develop.</p><p>So, here is what you can do: Use tshark to print the DATA and ACK frames for a certain station. Then use a script to find several consecutive DATA frames. Those are (most certainly) the ones without ACK. Additionally you can look at the time delta between the data frames and the next ACK frame.</p><blockquote><p>tshark -nr wlan.pcap -Y "(wlan.sa == 00:0d:93:82:36:3a and wlan.da == 00:0c:41:82:b2:53 and wlan.fc.type_subtype == 0x20) or (wlan.ra == 00:0d:93:82:36:3a and wlan.fc.type_subtype == 0x1d)" -T fields -e frame.number -e frame.time_relative -e wlan.sa -e wlan.da -e wlan.ra -e wlan.fc.type_subtype -E header=y -E separator=;</p></blockquote><p>Explanation of the filter:</p><p>DATA frames: <code>wlan.sa == 00:0d:93:82:36:3a and wlan.da == 00:0c:41:82:b2:53 and wlan.fc.type_subtype == 0x20</code><br />
ACK frames: <code>wlan.ra == 00:0d:93:82:36:3a and wlan.fc.type_subtype == 0x1d</code></p><p>Sample output for the following capture file:</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=wpa-Induction.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=wpa-Induction.pcap</a><br />
</p></blockquote><pre><code>439;13.405660000;00:0d:93:82:36:3a;00:0c:41:82:b2:53;00:0c:41:82:b2:55;0x20
440;13.405677000;;;00:0d:93:82:36:3a;0x1d
451;13.517648000;00:0d:93:82:36:3a;00:0c:41:82:b2:53;00:0c:41:82:b2:55;0x20
457;13.656629000;00:0d:93:82:36:3a;00:0c:41:82:b2:53;00:0c:41:82:b2:55;0x20
458;13.656641000;;;00:0d:93:82:36:3a;0x1d
459;13.667624000;00:0d:93:82:36:3a;00:0c:41:82:b2:53;00:0c:41:82:b2:55;0x20
460;13.667637000;;;00:0d:93:82:36:3a;0x1d</code></pre><p>There no real retransmissons in that capture file, but if you look at frames 451 and 457 you'll get an idea how it will look like. Those frames are two data frames without an ACK inbetween.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '13, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Nov '13, 12:25</strong> </span></p></div></div><div id="comments-container-27077" class="comments-container"><span id="27079"></span><div id="comment-27079" class="comment"><div id="post-27079-score" class="comment-score"></div><div class="comment-text"><p>Thanks - this is getting closer. Is there a way to build this type of logic into Wireshark itself? Like a complex macro or function that works in conjunction with a filter?</p></div><div id="comment-27079-info" class="comment-info"><span class="comment-age">(18 Nov '13, 15:38)</span> <span class="comment-user userinfo">ReidW</span></div></div><span id="27087"></span><div id="comment-27087" class="comment"><div id="post-27087-score" class="comment-score">1</div><div class="comment-text"><p>Sure, you can grab the source code of Wireshark and add whatever functionality you may need.</p><p>There are two other options, but I'm not really sure if it is possible to solve your problem with these two.</p><ul><li><a href="http://wiki.wireshark.org/Mate">MATE</a></li><li>Lua post dissector</li></ul><blockquote><p><a href="http://wiki.wireshark.org/Lua">http://wiki.wireshark.org/Lua</a><br />
<a href="http://wiki.wireshark.org/Lua/Examples/PostDissector">http://wiki.wireshark.org/Lua/Examples/PostDissector</a><br />
<a href="http://ask.wireshark.org/questions/26247/dissect-data-using-lua-post-dissector">http://ask.wireshark.org/questions/26247/dissect-data-using-lua-post-dissector</a><br />
<a href="http://ask.wireshark.org/questions/24876/ethercat-sub-dissector-in-lua">http://ask.wireshark.org/questions/24876/ethercat-sub-dissector-in-lua</a><br />
</p></blockquote></div><div id="comment-27087-info" class="comment-info"><span class="comment-age">(19 Nov '13, 00:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27077" class="comment-tools"></div><div class="clear"></div><div id="comment-27077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27048"></span>

<div id="answer-container-27048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27048-score" class="post-score" title="current number of votes">1</div><span id="post-27048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you probably want to use <code>&amp;&amp;</code> instead of <code>||</code>, as in:</p><p><code>(wlan.addr == 00:03:7f:04:09:7c) &amp;&amp; (wlan.addr == 00:03:7f:04:09:6b)</code></p><p>That probably won't give you everything you want, but it should be closer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '13, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Nov '13, 06:29</strong> </span></p></div></div><div id="comments-container-27048" class="comments-container"><span id="27074"></span><div id="comment-27074" class="comment"><div id="post-27074-score" class="comment-score"></div><div class="comment-text"><p>Yes - this filters out the extra traffic - including the ACKs. In order to filter out un-acknowledged packets we would need some smarts to check for an ACK - any idea how to do this?</p></div><div id="comment-27074-info" class="comment-info"><span class="comment-age">(18 Nov '13, 10:45)</span> <span class="comment-user userinfo">ReidW</span></div></div></div><div id="comment-tools-27048" class="comment-tools"></div><div class="clear"></div><div id="comment-27048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

