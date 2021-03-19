+++
type = "question"
title = "Capture filter for IP address in PPP-over-double-tagged-Ethernet traffic"
description = '''OK, I give up--been bangin&#x27; my head against this one for awhile now. I know how it SHOULD work, but something&#x27;s wrong. I am sniffing a trunk carrying double-tagged traffic on a distribution switch with massive amounts of data, so I don&#x27;t have the liberty of capturing all packets and then doing a dis...'''
date = "2014-02-18T15:42:00Z"
lastmod = "2014-02-18T16:00:00Z"
weight = 29988
keywords = [ "capture-filter" ]
aliases = [ "/questions/29988" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capture filter for IP address in PPP-over-double-tagged-Ethernet traffic](/questions/29988/capture-filter-for-ip-address-in-ppp-over-double-tagged-ethernet-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK, I give up--been bangin' my head against this one for awhile now. I know how it SHOULD work, but something's wrong. I am sniffing a trunk carrying double-tagged traffic on a distribution switch with massive amounts of data, so I don't have the liberty of capturing all packets and then doing a display filter. I need to capture a single IP address (using the WS GUI, not TShark), so I enter "host 1.2.3.4" without the quotes, for example. But this captures zero packets. If I capture all the traffic and then display filter it for 1.2.3.4, it appears in numerous packets, so I know the IP is correct.</p><p>If I enter the MAC address associated with the IP in the capture filter: "ether host ab:cd:ef:12:34:56" it works perfectly. I read where this could possibly be due to encapsulation, so I've tried "ip and host 1.2.3.4" I have also tried "ppp and host 1.2.3.4" I have also tried "pppoe and host 1.2.3.4" I have also tried "pppoes and host 1.2.3.4"</p><p>Nothing's working so far. Anyone have a suggestion? Thanks!</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '14, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/3d1f94fd059d26805abac57ed6299bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randyp&#39;s gravatar image" /><p>randyp<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randyp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '14, 15:18</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-29988" class="comments-container"><span id="30022"></span><div id="comment-30022" class="comment"><div id="post-30022-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to post a small sample capture file (just a few frames, taken without capture filter) <strong>with the double vlan tags</strong> on google drive, dropbox, cloudshark.org?</p></div><div id="comment-30022-info" class="comment-info"><span class="comment-age">(19 Feb '14, 10:18)</span> Kurt Knochner ♦</div></div><span id="30030"></span><div id="comment-30030" class="comment"><div id="post-30030-score" class="comment-score"></div><div class="comment-text"><p>Kurt, I did a raw capture with no filters, which captured all packets on the trunk (VLAN 873:1032 only on this pipe), then display-filtered it down to a single IP so it ended up with about 300 packets. Uploaded to CloudShark as VLAN873-1032-withSingleIP. Thanks for taking a look!</p></div><div id="comment-30030-info" class="comment-info"><span class="comment-age">(19 Feb '14, 12:29)</span> randyp</div></div><span id="30031"></span><div id="comment-30031" class="comment"><div id="post-30031-score" class="comment-score"></div><div class="comment-text"><p>The link is missing.</p></div><div id="comment-30031-info" class="comment-info"><span class="comment-age">(19 Feb '14, 13:14)</span> Kurt Knochner ♦</div></div><span id="30034"></span><div id="comment-30034" class="comment"><div id="post-30034-score" class="comment-score"></div><div class="comment-text"><p><a href="http://cloudshark.org/captures/54c2818338ed">http://cloudshark.org/captures/54c2818338ed</a></p><p>--Sorry. First timer.</p></div><div id="comment-30034-info" class="comment-info"><span class="comment-age">(19 Feb '14, 13:46)</span> randyp</div></div></div><div id="comment-tools-29988" class="comment-tools"></div><div class="clear"></div><div id="comment-29988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29990"></span>

<div id="answer-container-29990" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29990-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am sniffing a trunk carrying double-tagged traffic</p></blockquote><p>Then you need to be careful with capture filters.</p><p>If you want to capture traffic to 1.2.3.4 in traffic with <em>no</em> tags, the correct filter is <code>host 1.2.3.4</code>.</p><p>If you want to capture traffic to 1.2.3.4 in traffic with one level of VLAN tagging, the correct filter is <code>vlan and host 1.2.3.4</code> - and bear in mind that any IP-layer or above filter operations after <code>vlan and</code> will look only at packets with one layer of tagging.</p><p>If you want to capture traffic to 1.2.3.4 in traffic with two levels of VLAN tagging, the correct filter is <code>vlan and vlan and host 1.2.3.4</code> - and bear in mind that any IP-layer or above filter operations after <code>vlan and</code> will look only at packets with two layers of tagging.</p><p>(Bear in mind that <code>vlan</code> checks either for 0x8100 or 0x9100 as an Ethernet type, so <code>vlan</code> will match either of those and <code>vlan and vlan</code> will match 0x8100+0x8100, 0x8100+0x9100, 0x9100+0x8100, or 0x9100+0x9100.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '14, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29990" class="comments-container"><span id="30013"></span><div id="comment-30013" class="comment"><div id="post-30013-score" class="comment-score"></div><div class="comment-text"><p>What you suggested makes sense, but unfortunately, it didn't work either. I am going to try the same idea with a different NIC card that understands double-tags. I'll let you know how that works. And thanks for the response!</p></div><div id="comment-30013-info" class="comment-info"><span class="comment-age">(19 Feb '14, 07:06)</span> randyp</div></div><span id="30035"></span><div id="comment-30035" class="comment"><div id="post-30035-score" class="comment-score">1</div><div class="comment-text"><p>your frames are doubled tagged, <strong>but</strong> also 'encapsulated' in PPPoE. That's the reason why the capture filter does not work, because the IP header is at a different location, if you encapsulate the frames in PPPoE.</p><p>In this case the capture filter would be: <strong><code>vlan and vlan and pppoes and host x.x.x.x</code></strong></p></div><div id="comment-30035-info" class="comment-info"><span class="comment-age">(19 Feb '14, 13:57)</span> Kurt Knochner ♦</div></div><span id="30086"></span><div id="comment-30086" class="comment"><div id="post-30086-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help, guys, that worked! Here's what I found, though:</p><p>Using a NIC card that is not capable of tagging VLANs, I had to use "vlan and pppoes and host 1.2.3.4" This would only show the inner tag of the double-tagged frame in my VLAN column.</p><p>If I use a NIC card that is capable of tagging, I had to use "vlan and vlan and pppoes and host 1.2.3.4" This would show both the inner and outer tags in the two VLAN columns I have set up in WS.</p><p>Thanks again! I will click the "Credit" button for you!</p></div><div id="comment-30086-info" class="comment-info"><span class="comment-age">(21 Feb '14, 09:16)</span> randyp</div></div></div><div id="comment-tools-29990" class="comment-tools"></div><div class="clear"></div><div id="comment-29990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

