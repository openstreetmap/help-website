+++
type = "question"
title = "Does wireshark support capturing traffic at 10GB?"
description = '''I want to know that the wireshark support 10Gb interface data traffic .If not can i have any way to extend wireshark to support 10G.plesae respond as soon as possible. Thank you'''
date = "2016-02-19T03:32:00Z"
lastmod = "2016-08-14T10:37:00Z"
weight = 50330
keywords = [ "10gbe", "packet-capture", "tcpdump", "libpcap", "wireshark" ]
aliases = [ "/questions/50330" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Does wireshark support capturing traffic at 10GB?](/questions/50330/does-wireshark-support-capturing-traffic-at-10gb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50330-score" class="post-score" title="current number of votes">0</div><span id="post-50330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know that the wireshark support 10Gb interface data traffic .If not can i have any way to extend wireshark to support 10G.plesae respond as soon as possible.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-10gbe" rel="tag" title="see questions tagged &#39;10gbe&#39;">10gbe</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '16, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/8a669421eea30a71c4677fff8b0c5734?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rathnaTech&#39;s gravatar image" /><p><span>rathnaTech</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rathnaTech has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Aug '16, 10:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-50330" class="comments-container"></div><div id="comment-tools-50330" class="comment-tools"></div><div class="clear"></div><div id="comment-50330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50331"></span>

<div id="answer-container-50331" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50331-score" class="post-score" title="current number of votes">2</div><span id="post-50331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rathnaTech has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark run on a normal PC won't be able to support full rate 10GB traffic. In my local experiments it can't even support full rate 1GB traffic, lots of packet drops.</p><p>To capture at that rate you're probably looking at a specialized capture appliance, e.g. Steelhead Netshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '16, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50331" class="comments-container"><span id="50333"></span><div id="comment-50333" class="comment"><div id="post-50333-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response grahamb, i agree with u. Is there any other libraries(like wireshark) that support 10G traffic capture .</p></div><div id="comment-50333-info" class="comment-info"><span class="comment-age">(19 Feb '16, 04:18)</span> <span class="comment-user userinfo">rathnaTech</span></div></div><span id="50334"></span><div id="comment-50334" class="comment"><div id="post-50334-score" class="comment-score"></div><div class="comment-text"><p>Wireshark works with 10Gb ethernet cards, the thing is the traffic rate. Most probably you don't want to save saturated 10Gbit link traffic to file any way as it would produce a huge amount of data and if you do you probably will have to look for comersial solutions with custom HW and lots of disk strorage.</p></div><div id="comment-50334-info" class="comment-info"><span class="comment-age">(19 Feb '16, 04:23)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="50338"></span><div id="comment-50338" class="comment"><div id="post-50338-score" class="comment-score"></div><div class="comment-text"><p>You can use special capture NICs that support capture filters to reduce the amount of traffic being written to disk, e.g. from Napatech, Accolade Technology or Fiberblaze</p></div><div id="comment-50338-info" class="comment-info"><span class="comment-age">(19 Feb '16, 05:52)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="54801"></span><div id="comment-54801" class="comment"><div id="post-54801-score" class="comment-score"></div><div class="comment-text"><blockquote><p>In my local experiments it can't even support full rate 1GB traffic, lots of packet drops.</p></blockquote><p>Have you tried capturing with tcpdump instead? In at least some experiments on Linux a while ago (done by the person who did the TPACKET_V3 support for libpcap), tcpdump run with the <code>-w</code> flag dropped fewer packets than dumpcap.</p></div><div id="comment-54801-info" class="comment-info"><span class="comment-age">(14 Aug '16, 10:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-50331" class="comment-tools"></div><div class="clear"></div><div id="comment-50331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54788"></span>

<div id="answer-container-54788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54788-score" class="post-score" title="current number of votes">0</div><span id="post-54788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I used wireshark on a PC in 2013 to capture full 10Gb/s traffic (Windows 7 I think). The trick was to capture only to RAM -- increase the capture buffer, stop when it is full, use best capture filters, use best NIC driver.</p><p>Noam Cohen</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '16, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/52622940cc8b78d78a14efe3e9c6e5a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noam&#39;s gravatar image" /><p><span>noam</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noam has no accepted answers">0%</span></p></div></div><div id="comments-container-54788" class="comments-container"><span id="54795"></span><div id="comment-54795" class="comment"><div id="post-54795-score" class="comment-score"></div><div class="comment-text"><p>It's more a question of whether your hard disk can write as fast as 10Gbps. If it cannot, you will get a lot of dropped packets waiting to be written out to disk!</p><p>Semiconductor hard disks or RAM disks are usually required to capture at that speed.</p><p>FWIW</p></div><div id="comment-54795-info" class="comment-info"><span class="comment-age">(14 Aug '16, 06:21)</span> <span class="comment-user userinfo">wbenton</span></div></div></div><div id="comment-tools-54788" class="comment-tools"></div><div class="clear"></div><div id="comment-54788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

