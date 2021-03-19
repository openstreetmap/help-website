+++
type = "question"
title = "WPA decoding problems"
description = '''Hi all, I&#x27;m having troubles with WiFi decoding, WPA2 decoding, to be precise.  I&#x27;ll explain situation that I have. I&#x27;m having WiFi chip on one side with AP set on it, protected with WPA2. And android App on the other side, ASCII is sent to chip, and is received as ASCII. I want to read those ASCII o...'''
date = "2016-07-05T14:15:00Z"
lastmod = "2016-07-05T14:15:00Z"
weight = 53845
keywords = [ "decode", "wap2", "wireshark" ]
aliases = [ "/questions/53845" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WPA decoding problems](/questions/53845/wpa-decoding-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53845-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm having troubles with WiFi decoding, WPA2 decoding, to be precise.</p><p>I'll explain situation that I have. I'm having WiFi chip on one side with AP set on it, protected with WPA2. And android App on the other side, ASCII is sent to chip, and is received as ASCII. I want to read those ASCII on my Ubuntu laptop. I'm seeing communication between those two, but I can't read ASCII. I have tried to follow decoding 802.11 article, but without success. Actually, I don't have the same GUI, so I tried with using WPA-pwd key with 123:MyWiFI, and 123 passwords, neither helped.</p><p>Can you please tell me what am I doing wrong?</p><p>When I'm using monitor mode, I see LLC protocol, and when not I'm seeing 802.11 or vice versa, I'm not sure right now.<br />
</p><p>Thank you,</p><p>Bojan</p></div><div id="question-tags" class="tags-container tags">decode wap2 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '16, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/fb599089263071976ceb148a345e0831?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bojan990&#39;s gravatar image" /><p>Bojan990<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bojan990 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-53845" class="comments-container"><span id="53847"></span><div id="comment-53847" class="comment"><div id="post-53847-score" class="comment-score"></div><div class="comment-text"><p>Do you see any protocols <em>on top of</em> LLC? I.e., is there anything <em>after</em> LLC?</p></div><div id="comment-53847-info" class="comment-info"><span class="comment-age">(05 Jul '16, 20:00)</span> Guy Harris ♦♦</div></div><span id="53851"></span><div id="comment-53851" class="comment"><div id="post-53851-score" class="comment-score"></div><div class="comment-text"><p>No, nothing...</p><p>I have checked, I see LLC if LLH is set to Ethernet, and 802.11 if it's set to 802.11 plus radio header. I have catch once TCP protocol (which is actual protocol), but I have no idea how, and anyhow it was also encrypted, so that didn't help...</p></div><div id="comment-53851-info" class="comment-info"><span class="comment-age">(06 Jul '16, 02:01)</span> Bojan990</div></div></div><div id="comment-tools-53845" class="comment-tools"></div><div class="clear"></div><div id="comment-53845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

