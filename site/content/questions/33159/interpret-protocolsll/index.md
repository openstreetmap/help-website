+++
type = "question"
title = "interpret protocol=sll"
description = '''Hello, I&#x27;ve captured some traffic where wireshark can&#x27;t interpret packet as there are destination MAC address (capture was done on all interfaces). I know that this is SCTP packet. How can i force wireshark to interprat it?'''
date = "2014-05-29T03:18:00Z"
lastmod = "2014-06-02T13:18:00Z"
weight = 33159
keywords = [ "sll" ]
aliases = [ "/questions/33159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [interpret protocol=sll](/questions/33159/interpret-protocolsll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33159-score" class="post-score" title="current number of votes">1</div><span id="post-33159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I've captured some traffic where wireshark can't interpret packet as there are destination MAC address (capture was done on all interfaces). I know that this is SCTP packet. How can i force wireshark to interprat it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sll" rel="tag" title="see questions tagged &#39;sll&#39;">sll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '14, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p><span>BMWE</span><br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div></div><div id="comments-container-33159" class="comments-container"><span id="33160"></span><div id="comment-33160" class="comment"><div id="post-33160-score" class="comment-score"></div><div class="comment-text"><p>Your question is not really clear - Wireshark should be able to read cooked captures. Can you post the capture at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> so we can take a look?</p></div><div id="comment-33160-info" class="comment-info"><span class="comment-age">(29 May '14, 03:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="33239"></span><div id="comment-33239" class="comment"><div id="post-33239-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>File can be found here: <a href="https://www.cloudshark.org/captures/d6cb15b41593">https://www.cloudshark.org/captures/d6cb15b41593</a></p><p>i refer to packets like 3,4, 7,8,9...</p></div><div id="comment-33239-info" class="comment-info"><span class="comment-age">(01 Jun '14, 07:12)</span> <span class="comment-user userinfo">BMWE</span></div></div><span id="33247"></span><div id="comment-33247" class="comment"><div id="post-33247-score" class="comment-score"></div><div class="comment-text"><p>Was that packet sent over a VLAN? Linux does things with VLAN headers that are not particularly helpful for code that's trying to capture packets, and there are some issues with libpcap in "cooked mode" and VLAN headers.</p><p>Unfortunately, the only way to get Wireshark to dissect those packets would be to undo whatever damage was done to them in the capture process, by removing the 4 bytes starting at an offset of 14 into the packet data. I don't know of any tools that would make that easy.</p></div><div id="comment-33247-info" class="comment-info"><span class="comment-age">(01 Jun '14, 15:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-33159" class="comment-tools"></div><div class="clear"></div><div id="comment-33159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33249"></span>

<div id="answer-container-33249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33249-score" class="post-score" title="current number of votes">1</div><span id="post-33249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the packet bytes of those frames (3,4,7, etc.) you can see the bytes:</p><blockquote><p>81 00 00 0a</p></blockquote><p>That is a VLAN tag (VLAN 10). Only after that VLAN tag, the IP ethertype (0x0800) and the IP header starts (45 9f 00).</p><p>Either there is a problem with libpcap on that system (adding the VLAN tag in cooked mode in the wrong way - there has been a problem in earlier libpcap versions) or Wireshark is unable to handle VLAN tagged frames in Linux cooked mode.</p><p>So, please do the following:</p><ul><li>try to use the latest libpcap on your capturing system.</li><li>If that does not help: File a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></li></ul><p>In the meantime, you can simply remove the extra bytes with editcap.</p><p>First export only those frames with 0x81 at position 12 in the frame (start of VLAN tag marker):</p><blockquote><p>tshark -nr sample.pcap -Y "frame[12] eq 0x81" -w export.pcap</p></blockquote><p>Now remove the 4 additional bytes (VLAN tag)</p><blockquote><p>editcap -C 12:4 export.pcap fixed.pcap</p></blockquote><p>If you open <strong>fixed.pcap</strong> you'll see that there are UDP, TCP and ARP frames, but <strong>no</strong> SCTP frames!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '14, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '14, 15:49</strong> </span></p></div></div><div id="comments-container-33249" class="comments-container"><span id="33253"></span><div id="comment-33253" class="comment"><div id="post-33253-score" class="comment-score"></div><div class="comment-text"><p>Yes, there are definitely problems with libpcap and VLAN, and I don't think they're fixed in the latest libpcap; the right place to file a bug on libpcap about this is <a href="https://github.com/the-tcpdump-group/libpcap/issues/new">the libpcap GitHub issues list</a>.</p></div><div id="comment-33253-info" class="comment-info"><span class="comment-age">(01 Jun '14, 21:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="33315"></span><div id="comment-33315" class="comment"><div id="post-33315-score" class="comment-score"></div><div class="comment-text"><p>I modified the original capture file with a hex editor (only frame 3).</p><blockquote><p><a href="https://www.cloudshark.org/captures/24b4754bb602">https://www.cloudshark.org/captures/24b4754bb602</a></p></blockquote><p>Wireshark is now able to read frame #3 as a VLAN tagged frame in cooked mode.</p><p>So, yes it looks like a problem with libpcap and VLAN tagging in cooked mode. The byte order is somehow mixed up and thus Wireshark is unable to dissect those VLAN tagged frames in cooked mode.</p></div><div id="comment-33315-info" class="comment-info"><span class="comment-age">(02 Jun '14, 13:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33249" class="comment-tools"></div><div class="clear"></div><div id="comment-33249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

