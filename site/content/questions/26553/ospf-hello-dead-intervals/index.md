+++
type = "question"
title = "OSPF Hello &amp; Dead Intervals"
description = '''Hello I have a pcap file and am parsing it using tshark and wish dump the OSPF hello and dead intervals but there are no display filter names for these two attribtues (or many other OSPF attribtues). Dumping the hex value would be fine but I can&#x27;t seem to find a filter that will give me these result...'''
date = "2013-10-30T14:43:00Z"
lastmod = "2013-10-30T15:11:00Z"
weight = 26553
keywords = [ "ospf" ]
aliases = [ "/questions/26553" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSPF Hello & Dead Intervals](/questions/26553/ospf-hello-dead-intervals)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26553-score" class="post-score" title="current number of votes">0</div><span id="post-26553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I have a pcap file and am parsing it using tshark and wish dump the OSPF hello and dead intervals but there are no display filter names for these two attribtues (or many other OSPF attribtues). Dumping the hex value would be fine but I can't seem to find a filter that will give me these results. I was fiddling around with "ospf[x:y]" but that doesn't work. Does anyone have any ideas as to how I can dump these values?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ospf" rel="tag" title="see questions tagged &#39;ospf&#39;">ospf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '13, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/9eb965afd55518b5cbcd092fdad4b941?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnAInDallas&#39;s gravatar image" /><p><span>JohnAInDallas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnAInDallas has no accepted answers">0%</span></p></div></div><div id="comments-container-26553" class="comments-container"></div><div id="comment-tools-26553" class="comment-tools"></div><div class="clear"></div><div id="comment-26553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26554"></span>

<div id="answer-container-26554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26554-score" class="post-score" title="current number of votes">1</div><span id="post-26554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently there are no fields for those two timers. They are shown as <code>text</code> in Wireshark. So, if you need/want these two fields (or more), please file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Meanwhile, here is what you can do:</p><p>Run tshark with option -V. Then <strong>parse the output</strong> of tshark to extract the two values.</p><blockquote><p>tshark -nr ospf.pcap -V</p></blockquote><p>Strings to look for:</p><blockquote><p><strong>Hello Interval:</strong> 10 seconds<br />
<strong>Router Dead Interval:</strong> 40 seconds</p></blockquote><p>An alternative to -V is <strong>-T pdml</strong> (XML like output).</p><blockquote><p>tshark -nr ospf.pcap -T pdml</p></blockquote><p>Finally you can print the text fields and then <strong>parse that output</strong> to extract the intervals</p><blockquote><p>tshark -nr ospf.pcap -Y "ospf.msg == 1" -T fields -e frame.number -e ip.src -e ip.dst -e text</p></blockquote><p>Output:</p><pre><code>1       192.168.170.8   224.0.0.5       Source GeoIP: Unknown,Destination GeoIP: Unknown,OSPF Header,OSPF Version: 2,Packet Length: 44,Area
ID: 0.0.0.1,Packet Checksum: 0x273b [correct],Auth Type: Null,Auth Data (none),OSPF Hello Packet,Network Mask: 255.255.255.0,Hello Interval:
 10 seconds,Router Priority: 1,Router Dead Interval: 40 seconds,Designated Router: 192.168.170.8,Backup Designated Router: 0.0.0.0</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '13, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Oct '13, 15:49</strong> </span></p></div></div><div id="comments-container-26554" class="comments-container"></div><div id="comment-tools-26554" class="comment-tools"></div><div class="clear"></div><div id="comment-26554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

