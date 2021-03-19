+++
type = "question"
title = "Cannot decrypt WPA2 despite EAPOL capture"
description = '''Hello everyone, I have spent several hours trying to get this to work without any success, so I would really appreciate your help. So here is the scenario, I have a Macbook pro running Mac OS X Lion connected to my home wireless network secured with WPA2. I have Wireshark running on this computer an...'''
date = "2012-07-08T01:50:00Z"
lastmod = "2014-10-10T07:49:00Z"
weight = 12504
keywords = [ "eapol", "wpa2" ]
aliases = [ "/questions/12504" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot decrypt WPA2 despite EAPOL capture](/questions/12504/cannot-decrypt-wpa2-despite-eapol-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12504-score" class="post-score" title="current number of votes">0</div><span id="post-12504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I have spent several hours trying to get this to work without any success, so I would really appreciate your help. So here is the scenario, I have a Macbook pro running Mac OS X Lion connected to my home wireless network secured with WPA2. I have Wireshark running on this computer and want to capture and decrypt the traffic. I have specified the passphrase and the network SSID in IEEE 802.11 from the protocols list under Edit-&gt; Preferences. I have also done it in the Wireless toolbar.</p><p>Now when I start the capture, I can decrypt the traffic to and from Macook pro running Wireshark but not from another computer connected to the same wireless network even if I disconnect and re-associate that computer with the wireless network. I can see the 4-way EAPOL handshake from that computer in my trace but the traffic following that is not decrypted.</p><p>Any ideas what I might be doing wrong here please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '12, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/bb0cccfee703da42899385a47603ce95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nawaz&#39;s gravatar image" /><p><span>Nawaz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nawaz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '12, 05:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-12504" class="comments-container"></div><div id="comment-tools-12504" class="comment-tools"></div><div class="clear"></div><div id="comment-12504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36959"></span>

<div id="answer-container-36959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36959-score" class="post-score" title="current number of votes">0</div><span id="post-36959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have found that I have to toggle between None, Wireshark, or Driver then back to Wireshark for decryption to actually work sometimes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '14, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/bda58696b063972a940d088c92843330?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Murray&#39;s gravatar image" /><p><span>Murray</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Murray has no accepted answers">0%</span></p></div></div><div id="comments-container-36959" class="comments-container"></div><div id="comment-tools-36959" class="comment-tools"></div><div class="clear"></div><div id="comment-36959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

