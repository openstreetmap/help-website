+++
type = "question"
title = "802.15.4 CCM star decryption?"
description = '''Hi. I&#x27;m trying to implement the 802.15.4-2006 security CCM* mode. So far I have implemented the security logic as in the 802.15.4-2006 standard. And now I&#x27;m trying to see if the encryption logic is correct. I have captured the communication packets and tried to view them with Wireshark, but I am get...'''
date = "2016-11-24T21:21:00Z"
lastmod = "2016-11-24T21:21:00Z"
weight = 57624
keywords = [ "ccm", "star" ]
aliases = [ "/questions/57624" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.15.4 CCM star decryption?](/questions/57624/802154-ccm-star-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57624-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I'm trying to implement the 802.15.4-2006 security CCM* mode.</p><p>So far I have implemented the security logic as in the 802.15.4-2006 standard.</p><p>And now I'm trying to see if the encryption logic is correct.</p><p>I have captured the communication packets and tried to view them with Wireshark, but I am getting a 'MIC check failed' message in the frame.</p><p>I noticed that the Wireshark IEEE 802.15.4 Low-Rate Wireless PAN protocol only supports Security Suite 802.15.4-2003 version.</p><p>Security in 802.15.4-2003 and 802.15.4-2006 are different so I'm not sure if the MIC check failed because the encryption logic is incorrect or because of the standard version mismatch.</p><p>I also noticed that in wireshark, zigbee network security supports 802.15.4-2006 CCM* mode.</p><p>But since I'm only using 802.15.4, I cannot find the right options to apply 802.15.4-2006 security in Wireshark.</p><p>Is there a way to decrypt 802.15.4-2006 CCM* encryption without the zigbee network layer?</p></div><div id="question-tags" class="tags-container tags">ccm star</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '16, 21:21</strong></p><img src="https://secure.gravatar.com/avatar/5831a2b2f90e0f800ba41e912bd85e7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zine314&#39;s gravatar image" /><p>zine314<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zine314 has no accepted answers">0%</span></p></div></div><div id="comments-container-57624" class="comments-container"></div><div id="comment-tools-57624" class="comment-tools"></div><div class="clear"></div><div id="comment-57624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

