+++
type = "question"
title = "tshark  Segmentation fault"
description = '''system info:Linux Linux 2.6.32.59-0.7-default #1 SMP 2012-07-13 15:50:56 +0200 x86_64 x86_64 x86_64 GNU/Linux tshark version:1.10.6,Compiled (64-bit) with GLib 2.14.0, with libpcap, with libz 1.2.8 i want to discard the sctp protocol packets in a pcap file, this pcap file size is 2.0G. command like ...'''
date = "2014-05-08T20:56:00Z"
lastmod = "2014-05-08T21:15:00Z"
weight = 32654
keywords = [ "fault", "segmentation", "tshark" ]
aliases = [ "/questions/32654" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark Segmentation fault](/questions/32654/tshark-segmentation-fault)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32654-score" class="post-score" title="current number of votes">0</div><span id="post-32654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><h1 id="system-infolinux-linux-2.6.32.59-0.7-default-1-smp-2012-07-13-155056-0200-x86_64-x86_64-x86_64-gnulinux">system info:Linux Linux 2.6.32.59-0.7-default #1 SMP 2012-07-13 15:50:56 +0200 x86_64 x86_64 x86_64 GNU/Linux</h1><h1 id="tshark-version1.10.6compiled-64-bit-with-glib-2.14.0-with-libpcap-with-libz-1.2.8">tshark version:1.10.6,Compiled (64-bit) with GLib 2.14.0, with libpcap, with libz 1.2.8</h1><p>i want to discard the sctp protocol packets in a pcap file, this pcap file size is 2.0G. command like this: tshark -r iub_20140326190105.pcap -R "not sctp" -F pcap -w result.pcap</p><p>i got a Segmentation fault. =.=!!!</p><p><strong>(process:7624): WARNING</strong> : Dissector bug, protocol MAC, in packet 80997: tvbuff.c:556: failed assertion "datalen&gt;0" <strong>(process:7624): WARNING</strong> : Dissector bug, protocol MAC, in packet 81274: tvbuff.c:556: failed assertion "datalen&gt;0" <strong>(process:7624): WARNING</strong> : Dissector bug, protocol MAC, in packet 81795: tvbuff.c:556: failed assertion "datalen&gt;0" Segmentation fault</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fault" rel="tag" title="see questions tagged &#39;fault&#39;">fault</span> <span class="post-tag tag-link-segmentation" rel="tag" title="see questions tagged &#39;segmentation&#39;">segmentation</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '14, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/8e17416f6dbcd81a14bd2bc8f483a6fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zty&#39;s gravatar image" /><p><span>zty</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zty has no accepted answers">0%</span></p></div></div><div id="comments-container-32654" class="comments-container"></div><div id="comment-tools-32654" class="comment-tools"></div><div class="clear"></div><div id="comment-32654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32655"></span>

<div id="answer-container-32655" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32655-score" class="post-score" title="current number of votes">0</div><span id="post-32655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>File a bug on <a href="http://bugs.wireshark.org/">the Wireshark bug database</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '14, 21:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-32655" class="comments-container"></div><div id="comment-tools-32655" class="comment-tools"></div><div class="clear"></div><div id="comment-32655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

