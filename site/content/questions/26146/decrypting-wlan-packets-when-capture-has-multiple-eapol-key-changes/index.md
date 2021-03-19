+++
type = "question"
title = "Decrypting WLAN packets when capture has multiple EAPOL Key changes"
description = '''Issue: During a WLAN capture, the EAP keys between the Station and AP change due to an attack. After the keys are modified, decryption no longer occurs on subsequent packets. The WLAN packets are encrypted using WPA/WPA2-PSK Is it possible for Wireshark to determine that the EAP keys have changed an...'''
date = "2013-10-17T13:17:00Z"
lastmod = "2013-10-21T08:10:00Z"
weight = 26146
keywords = [ "decryption", "wlan" ]
aliases = [ "/questions/26146" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypting WLAN packets when capture has multiple EAPOL Key changes](/questions/26146/decrypting-wlan-packets-when-capture-has-multiple-eapol-key-changes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26146-score" class="post-score" title="current number of votes">0</div><span id="post-26146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Issue: During a WLAN capture, the EAP keys between the Station and AP change due to an attack. After the keys are modified, decryption no longer occurs on subsequent packets. The WLAN packets are encrypted using WPA/WPA2-PSK</p><p>Is it possible for Wireshark to determine that the EAP keys have changed and decrypt the subsequent packets using the new keys?</p><p>The work-around: 1) Save the portion of the capture before the keys are changed 2) Decrypt this portion 3) Save the next portion of the capture that includes the first key change, but before the next key change. 4) Decrypt this portion Follow this for all key changes. This works but is cumbersome.</p><p>Wireshark does show the new EAPOL exchange between the AP and Station in which the new keys are exchanged.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '13, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-26146" class="comments-container"></div><div id="comment-tools-26146" class="comment-tools"></div><div class="clear"></div><div id="comment-26146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26153"></span>

<div id="answer-container-26153" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26153-score" class="post-score" title="current number of votes">2</div><span id="post-26153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Amato_C has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible for Wireshark to determine that the EAP keys have changed and decrypt the subsequent packets using the new keys?</p></blockquote><p>It would probably be possible to modify Wireshark's code to do so. Without code changes, it'd be impossible - i.e., there's no configuration option you can set with <em>existing</em> versions of Wireshark to get it to do so.</p><p>Please file an enhancement request on <a href="http://bugs.wireshark.org">the Wireshark bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '13, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26153" class="comments-container"><span id="26255"></span><div id="comment-26255" class="comment"><div id="post-26255-score" class="comment-score"></div><div class="comment-text"><p>Bug 9313 created</p></div><div id="comment-26255-info" class="comment-info"><span class="comment-age">(21 Oct '13, 08:10)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-26153" class="comment-tools"></div><div class="clear"></div><div id="comment-26153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

