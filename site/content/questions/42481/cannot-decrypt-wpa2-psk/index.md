+++
type = "question"
title = "cannot decrypt WPA2-PSK"
description = '''Hi all, I&#x27;m running 1.12.2 and trying to decrypt 802.11 WPA2 Personal. Under IEEE 802.11 protocol of Edit -&amp;gt; Preferences, I chosen the Key type as wpa-psk, input the Key (generated here https://www.wireshark.org/tools/wpa-psk.html) and check marked the &quot;Enable decryption&quot; checkbox. After clicking...'''
date = "2015-05-17T22:13:00Z"
lastmod = "2015-05-19T00:51:00Z"
weight = 42481
keywords = [ "802.11" ]
aliases = [ "/questions/42481" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [cannot decrypt WPA2-PSK](/questions/42481/cannot-decrypt-wpa2-psk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42481-score" class="post-score" title="current number of votes">0</div><span id="post-42481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm running 1.12.2 and trying to decrypt 802.11 WPA2 Personal. Under IEEE 802.11 protocol of Edit -&gt; Preferences, I chosen the Key type as wpa-psk, input the Key (generated here <a href="https://www.wireshark.org/tools/wpa-psk.html)">https://www.wireshark.org/tools/wpa-psk.html)</a> and check marked the "Enable decryption" checkbox. After clicking Apply, I still see Data shown under IEEE 802.11 Data field of the Packet Details pane, cannot see any IP or upper later header. The data was not decrypted. Am I missing something?</p><p>thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '15, 22:13</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-42481" class="comments-container"></div><div id="comment-tools-42481" class="comment-tools"></div><div class="clear"></div><div id="comment-42481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42483"></span>

<div id="answer-container-42483" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42483-score" class="post-score" title="current number of votes">0</div><span id="post-42483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some ideas:</p><ul><li>Do you see the 4 EAPOL frames in the capture file? If no, then you can't decrypt the frames (see: <a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a> ).</li><li>Try to use "wpa-pwd" (Passphrase) instead "wpa-psk" and the online generated key</li></ul><p>Additionally, please read my answer to the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/29592/decrypting-a-80211-packets-on-wpa2-psk">https://ask.wireshark.org/questions/29592/decrypting-a-80211-packets-on-wpa2-psk</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 22:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42483" class="comments-container"><span id="42528"></span><div id="comment-42528" class="comment"><div id="post-42528-score" class="comment-score"></div><div class="comment-text"><p>I hit idea-1. Thanks a lot!</p></div><div id="comment-42528-info" class="comment-info"><span class="comment-age">(19 May '15, 00:51)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-42483" class="comment-tools"></div><div class="clear"></div><div id="comment-42483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

