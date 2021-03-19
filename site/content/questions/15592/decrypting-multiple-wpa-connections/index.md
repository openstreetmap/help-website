+++
type = "question"
title = "Decrypting multiple WPA connections"
description = '''I&#x27;ve been fiddling around with wireshark capturing packets from my (WPA2 protected) wlan.  I got it to decrypt traffic when it see the four handshakes from a device, but it if another device authenticates, it wont decrypt traffic from that device.  So it goes like this:  I have set up the passphrase...'''
date = "2012-11-06T10:47:00Z"
lastmod = "2012-11-06T10:47:00Z"
weight = 15592
keywords = [ "decryption", "eapol", "wpa2", "multiple" ]
aliases = [ "/questions/15592" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting multiple WPA connections](/questions/15592/decrypting-multiple-wpa-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15592-score" class="post-score" title="current number of votes">0</div><span id="post-15592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been fiddling around with wireshark capturing packets from my (WPA2 protected) wlan.</p><p>I got it to decrypt traffic when it see the four handshakes from a device, but it if another device authenticates, it wont decrypt traffic from that device.</p><p>So it goes like this: I have set up the passphrase in preferences, nic is monitor mode.</p><ul><li>Start capturing.</li><li>Restart my iphone's wifi</li><li>EAPOL packets apear and subsequent traffic from my iphone is decrypted</li><li>Restart my (other) laptop's wifi</li><li>EAPOL packets appear but the traffic from this device doesn't get encrypted</li></ul><p>If i do this the other way around: stop capturing, restart capturing, restart my laptop's wifi and then my iphone's. It only sees decrypted traffic from my laptop.</p><p>How can i fix this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '12, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/b95b67ef4599381949952191048c81c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbosman&#39;s gravatar image" /><p><span>tbosman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbosman has no accepted answers">0%</span></p></div></div><div id="comments-container-15592" class="comments-container"></div><div id="comment-tools-15592" class="comment-tools"></div><div class="clear"></div><div id="comment-15592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

