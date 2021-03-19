+++
type = "question"
title = "How to further decode Airpeek encapsulated packet"
description = '''Hi there, I captured some wireless traffic through the Cisco Wireless controller. It encapsulates the traffic in the Airpeek format. I decoded the packets with Airpeek however it only decoded up to the layer 2 header which is the &quot;IEEE 802.11 Data&quot;. The rest (IP header, TCP/UDP header, ...etc) is no...'''
date = "2013-01-02T13:37:00Z"
lastmod = "2013-01-04T15:10:00Z"
weight = 17398
keywords = [ "airopeek" ]
aliases = [ "/questions/17398" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to further decode Airpeek encapsulated packet](/questions/17398/how-to-further-decode-airpeek-encapsulated-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17398-score" class="post-score" title="current number of votes">0</div><span id="post-17398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I captured some wireless traffic through the Cisco Wireless controller. It encapsulates the traffic in the Airpeek format. I decoded the packets with Airpeek however it only decoded up to the layer 2 header which is the "IEEE 802.11 Data". The rest (IP header, TCP/UDP header, ...etc) is not decoded and it is just listed as "Data"... Is there way to even decode this part?</p><p>Please see my attached screenshot. The "Data" should be the ICMP ping packet. <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_Screenshot.gif" alt="alt text" /> Thanks and happy new year!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airopeek" rel="tag" title="see questions tagged &#39;airopeek&#39;">airopeek</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '13, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/08a7db94810c538eed59c44ad2601ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="difan&#39;s gravatar image" /><p><span>difan</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="difan has no accepted answers">0%</span></p></img></div></div><div id="comments-container-17398" class="comments-container"></div><div id="comment-tools-17398" class="comment-tools"></div><div class="clear"></div><div id="comment-17398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17399"></span>

<div id="answer-container-17399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17399-score" class="post-score" title="current number of votes">1</div><span id="post-17399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like it is a capture from an encrypted wireless network. Do you have the key? If you do, you can configure it in Wireshark so that wireshark can decrypt the traffic.</p><p>Please beware, If it is WPA(2) encrypted, you need to start the capture before the client (for which you want to decrypt the traffic) connects to the AP, as you need the 4 authentication packets at the start of the wireless session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17399" class="comments-container"><span id="17400"></span><div id="comment-17400" class="comment"><div id="post-17400-score" class="comment-score"></div><div class="comment-text"><p>Hey Thanks! I have the key. I have put it in however it is still shown as "Data...". I actually compared a packet before and after the decryption but the "data" part remained the same (Hex value)... Does it only decrypt the packet if it is not encapsulated in Airopeek? Thanks!</p></div><div id="comment-17400-info" class="comment-info"><span class="comment-age">(02 Jan '13, 14:19)</span> <span class="comment-user userinfo">difan</span></div></div><span id="17402"></span><div id="comment-17402" class="comment"><div id="post-17402-score" class="comment-score"></div><div class="comment-text"><p>I expect Wireshark to decrypt as the 802.11 dissector is unaware of the encapsulation (AFAIK). Can you disable decryption or create another SSID without encryption to verify that Wireshark does show the IP layer for unencrypted 802.11 in Airopeek encapsulation?</p></div><div id="comment-17402-info" class="comment-info"><span class="comment-age">(02 Jan '13, 15:53)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="17450"></span><div id="comment-17450" class="comment"><div id="post-17450-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYN-bit! I am currently in a change freeze period so I can't do any changes on the controller. However your reply prompted me to upgrade my wireshark. However after the upgrade from 1.4.x to current 1.8.4 I lost option to decode the packets by Airopeek protocol or dissector... Is it renamed or removed? Thanks!</p></div><div id="comment-17450-info" class="comment-info"><span class="comment-age">(04 Jan '13, 11:07)</span> <span class="comment-user userinfo">difan</span></div></div><span id="17469"></span><div id="comment-17469" class="comment"><div id="post-17469-score" class="comment-score">1</div><div class="comment-text"><p>See <a href="http://ask.wireshark.org/questions/16617">http://ask.wireshark.org/questions/16617</a></p></div><div id="comment-17469-info" class="comment-info"><span class="comment-age">(04 Jan '13, 15:10)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-17399" class="comment-tools"></div><div class="clear"></div><div id="comment-17399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

