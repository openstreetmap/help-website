+++
type = "question"
title = "WPA2-PSK with &quot;£&quot;"
description = '''I have been trying to capture and decrypt from a WPA2-PSK wireless network, but the preshared key has a &quot;£&quot; (UK pound sign). It seams that wireshark (1.12.1 Win7 with AirPCAP) is corrupting the Preshared key. If I enter the PSK in the &quot;Decryption key management&quot; dialog, exit the dialog and reopen it...'''
date = "2014-11-06T09:31:00Z"
lastmod = "2014-11-06T12:18:00Z"
weight = 37624
keywords = [ "wpa-psk" ]
aliases = [ "/questions/37624" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WPA2-PSK with "£"](/questions/37624/wpa2-psk-with)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37624-score" class="post-score" title="current number of votes">0</div><span id="post-37624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been trying to capture and decrypt from a WPA2-PSK wireless network, but the preshared key has a "£" (UK pound sign).</p><p>It seams that wireshark (1.12.1 Win7 with AirPCAP) is corrupting the Preshared key. If I enter the PSK in the "Decryption key management" dialog, exit the dialog and reopen it the key is corrupted.</p><p>Has anyone else come across this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa-psk" rel="tag" title="see questions tagged &#39;wpa-psk&#39;">wpa-psk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '14, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/c9951eba219b12c3382c51b5ed58c37a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C_P&#39;s gravatar image" /><p><span>C_P</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C_P has one accepted answer">100%</span></p></div></div><div id="comments-container-37624" class="comments-container"></div><div id="comment-tools-37624" class="comment-tools"></div><div class="clear"></div><div id="comment-37624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37626"></span>

<div id="answer-container-37626" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37626-score" class="post-score" title="current number of votes">0</div><span id="post-37626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="C_P has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After some research I have been able to resolve my issue.</p><p>From the "<a href="http://wiki.wireshark.org/HowToDecrypt802.11">How to Decrypt 802.11</a>" wiki page?</p><p><em>"The WPA passphrase and SSID preferences let you encode non-printable or otherwise troublesome characters using URI-style percent escapes, e.g. %20 for a space. As a result you have to escape the percent characters themselves using %25."</em></p><p>By replacing the "£" with "%a3" I am able to decrypt the capture.</p><p>Interestingly the last two characters of the corrupted part of the PSK was "a3".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '14, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/c9951eba219b12c3382c51b5ed58c37a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C_P&#39;s gravatar image" /><p><span>C_P</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C_P has one accepted answer">100%</span></p></div></div><div id="comments-container-37626" class="comments-container"></div><div id="comment-tools-37626" class="comment-tools"></div><div class="clear"></div><div id="comment-37626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

