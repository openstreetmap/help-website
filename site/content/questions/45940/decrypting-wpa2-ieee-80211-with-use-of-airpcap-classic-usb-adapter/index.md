+++
type = "question"
title = "Decrypting WPA2/ IEEE 802.11 with use of AirPcap classic USB adapter"
description = '''Hello, I am using Ethereal/Wireshark for years. I wanted to enhance my mobility when it comes to the capturing WiFi with use of AirPcap classic USB adapter (http://www.airpcap.nl/airpcap-classic.htm):  I am using WPA2 encryption I am using NetGear WNDAP30 (http://www.netgear.com/business/products/wi...'''
date = "2015-09-17T22:57:00Z"
lastmod = "2015-09-19T14:52:00Z"
weight = 45940
keywords = [ "eapol", "airpcap", "ieee802_11_radio_avs" ]
aliases = [ "/questions/45940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting WPA2/ IEEE 802.11 with use of AirPcap classic USB adapter](/questions/45940/decrypting-wpa2-ieee-80211-with-use-of-airpcap-classic-usb-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45940-score" class="post-score" title="current number of votes">0</div><span id="post-45940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am using Ethereal/Wireshark for years. I wanted to enhance my mobility when it comes to the capturing WiFi with use of AirPcap classic USB adapter (<a href="http://www.airpcap.nl/airpcap-classic.htm):">http://www.airpcap.nl/airpcap-classic.htm):</a></p><ol><li>I am using WPA2 encryption</li><li>I am using NetGear WNDAP30 (<a href="http://www.netgear.com/business/products/wireless/business-wireless/wndap350.aspx)">http://www.netgear.com/business/products/wireless/business-wireless/wndap350.aspx)</a></li><li>I have set correct channel</li><li>I have seen EAPOL packets captured</li><li>I have entered WPA-PWD password and SSID correctly</li><li>Sample capture from Wireshark wiki works for me (<a href="https://wiki.wireshark.org/HowToDecrypt802.11)">https://wiki.wireshark.org/HowToDecrypt802.11)</a></li><li>I was experimenting with "Assume Packets have FCS" and "Ignore the protection bit"</li><li>I spend ~5 hours trying to decrypt the communication - none positive result..., but I am not expert on IEEE 802.11</li><li>My Wireshark version is: Version 1.10.0 (SVN Rev 49790 from /trunk-1.10)</li><li></li></ol><p>Any idea what I m doing wrong? Thanks a lot STeN</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-ieee802_11_radio_avs" rel="tag" title="see questions tagged &#39;ieee802_11_radio_avs&#39;">ieee802_11_radio_avs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '15, 22:57</strong></p><img src="https://secure.gravatar.com/avatar/66193d3518048067e8947736eedb44d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stenlik&#39;s gravatar image" /><p><span>stenlik</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stenlik has one accepted answer">100%</span></p></div></div><div id="comments-container-45940" class="comments-container"><span id="45946"></span><div id="comment-45946" class="comment"><div id="post-45946-score" class="comment-score"></div><div class="comment-text"><ol><li><p>Did you read the Wireshark Wiki at: <a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p></li><li><p>Were you able to capture all 4 EAPOL packets between the client and the AP?</p></li><li><p>Did you enter the correct SSID and passphrase using the procedure described in the following question: <a href="https://ask.wireshark.org/questions/45881/cant-decrypt-80211-traffic">https://ask.wireshark.org/questions/45881/cant-decrypt-80211-traffic</a></p></li><li><p>Are you able to post a sample capture on cloudshark or Google Drive?</p></li></ol></div><div id="comment-45946-info" class="comment-info"><span class="comment-age">(18 Sep '15, 06:14)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-45940" class="comment-tools"></div><div class="clear"></div><div id="comment-45940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45958"></span>

<div id="answer-container-45958" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45958-score" class="post-score" title="current number of votes">0</div><span id="post-45958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stenlik has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, I have double checked everything and I did not changed anything except I reset AP and notebook and now it starts working… I have no explanation for that :( However thanks for trying to help me! Regards, Petr</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '15, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/66193d3518048067e8947736eedb44d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stenlik&#39;s gravatar image" /><p><span>stenlik</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stenlik has one accepted answer">100%</span></p></div></div><div id="comments-container-45958" class="comments-container"><span id="45965"></span><div id="comment-45965" class="comment"><div id="post-45965-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I reset AP and notebook</p></blockquote><p>That may have forced an EAPOL handshake to be transmitted. On a WPA or WPA2 network, you need more than just the password, you need the EAPOL handshake.</p></div><div id="comment-45965-info" class="comment-info"><span class="comment-age">(19 Sep '15, 14:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-45958" class="comment-tools"></div><div class="clear"></div><div id="comment-45958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

