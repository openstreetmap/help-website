+++
type = "question"
title = "Recent trace - Expert info warning reporting 20% Out-Of-Order"
description = '''We have a manufacturing warehouse facility that is complaining of wireless network slowness and disconnects thru-out the facility. I have been tasked to do a packet analysis of the problem using wireshark. I installed wireshark on a dell desktop that is inside a stainless steel manufacturing cart.  ...'''
date = "2014-01-06T08:00:00Z"
lastmod = "2014-01-08T09:22:00Z"
weight = 28601
keywords = [ "out-of-order" ]
aliases = [ "/questions/28601" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Recent trace - Expert info warning reporting 20% Out-Of-Order](/questions/28601/recent-trace-expert-info-warning-reporting-20-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28601-score" class="post-score" title="current number of votes">0</div><span id="post-28601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a manufacturing warehouse facility that is complaining of wireless network slowness and disconnects thru-out the facility.</p><p>I have been tasked to do a packet analysis of the problem using wireshark. I installed wireshark on a dell desktop that is inside a stainless steel manufacturing cart.</p><p>In any case, the dry mix operators use a Intermec SR61B Cordless Scanner that uses Bluetooth radio for RF communications to scan ingredients before mixing. In addition, there is a Cisco AIR-PI21AG-AK9 network interface card with an integrated dual-band 2.4/5-ghz, 1-dbi, effective-gain antenna on a two meter cable. So, the operators use the Intermec scanner to scan barcodes of packages that is connected to this dell desktop via usb using a Windows XP operating system. The clients 'scans' the barcode which sends the information over the Cisco NIC to the application server via wireless connectivity.</p><p>I am wondering if the blue tooth radio (both in the scanner gun and in the charging base) is interfering with the Cisco antenna causing interference and cause the tcp out-of-orders in my packet trace. I have read somewhere that it is recommended that the bluetooth devices should be at least 5 feet apart from other wireless devices to minimize interference. In this particular case, the Cisco antenna is about 12 inches from the Intermec base.</p><p>So, I installed wireshark on this dell pc; and I believe I am only capturing packets leaving the windows operating systems on/off the nic card. So, perhaps a real wirelss trace would be better. Nonetheless.</p><p>I will more than likely have to make another trip back to my manufacturing facility to do an spectrum analysis of interference or whatever.</p><p>Is it possible that the Bluetooth is causing interference and the Cisco antenna cannot transmit/receive packets? Thus, resulting in the expert info report of 20% out of order packets?</p><p>So my Cisco SE says: Retransmissions are common in wireless. And a certain percentage of retransmissions is acceptable. They result from several things. Multipath, interference, low SNR, hidden node, near/far, mismatched power settings, adjacent cell interference, …</p><p>Thanks so much</p><p>I will try to send a small snipet of the Wireshark Export information and a small snippet of packets. I am not sure if I am allowed to upload packet trace, but, I am open to suggestions.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '14, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/cabfb8bd35ccc8f904bb4e646a3add5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kargentus&#39;s gravatar image" /><p><span>kargentus</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kargentus has no accepted answers">0%</span></p></div></div><div id="comments-container-28601" class="comments-container"></div><div id="comment-tools-28601" class="comment-tools"></div><div class="clear"></div><div id="comment-28601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28677"></span>

<div id="answer-container-28677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28677-score" class="post-score" title="current number of votes">0</div><span id="post-28677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible that the Bluetooth is causing interference and the Cisco antenna cannot transmit/receive packets?</p></blockquote><p>for sure. Just <a href="https://www.google.com/?q=bluetooth%20interference%20with%20wlan">search google</a> and you'll find several documents about that. Just some examples:</p><blockquote><p><a href="http://support.apple.com/kb/ht1365">http://support.apple.com/kb/ht1365</a><br />
</p><p><a href="http://www.cisco.com/en/US/prod/collateral/wireless/ps9391/ps9393/ps9394/prod_white_paper0900aecd807395a9_ns736_Networking_Solutions_White_Paper.html">http://www.cisco.com/en/US/prod/collateral/wireless/ps9391/ps9393/ps9394/prod_white_paper0900aecd807395a9_ns736_Networking_Solutions_White_Paper.html</a><br />
</p><p><a href="http://www.ecnmag.com/articles/2012/03/wi-fi-and-bluetooth-coexistence">http://www.ecnmag.com/articles/2012/03/wi-fi-and-bluetooth-coexistence</a><br />
<a href="http://www.hp.com/rnd/library/pdf/WiFi_Bluetooth_coexistance.pdf">http://www.hp.com/rnd/library/pdf/WiFi_Bluetooth_coexistance.pdf</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-28677" class="comments-container"></div><div id="comment-tools-28677" class="comment-tools"></div><div class="clear"></div><div id="comment-28677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

