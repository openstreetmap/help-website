+++
type = "question"
title = "[Wireshark-bugs] [Bug 8395] IPsec ESP: add AES-GCM decryption"
description = '''I noticed that for AES256, 36 bytes should be supplied as a key (instead of 32 bytes). What is the origin of the extra 4 bytes? And in general, what is the format that should be given for such decryption key?'''
date = "2013-09-15T06:31:00Z"
lastmod = "2013-09-15T22:17:00Z"
weight = 24715
keywords = [ "decryption", "aes", "gcm" ]
aliases = [ "/questions/24715" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[Wireshark-bugs\] \[Bug 8395\] IPsec ESP: add AES-GCM decryption](/questions/24715/wireshark-bugs-bug-8395-ipsec-esp-add-aes-gcm-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24715-score" class="post-score" title="current number of votes">0</div><span id="post-24715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I noticed that for AES256, 36 bytes should be supplied as a key (instead of 32 bytes). What is the origin of the extra 4 bytes? And in general, what is the format that should be given for such decryption key?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-aes" rel="tag" title="see questions tagged &#39;aes&#39;">aes</span> <span class="post-tag tag-link-gcm" rel="tag" title="see questions tagged &#39;gcm&#39;">gcm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '13, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/2c12d132c3c19b02e1b7d865c8beabc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YuvalAdler&#39;s gravatar image" /><p><span>YuvalAdler</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YuvalAdler has no accepted answers">0%</span></p></div></div><div id="comments-container-24715" class="comments-container"><span id="24721"></span><div id="comment-24721" class="comment"><div id="post-24721-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I noticed that for AES256, 36 bytes should be supplied as a key (instead of 32 bytes).</p></blockquote><p>I'm just curious. Where did you notice that?</p></div><div id="comment-24721-info" class="comment-info"><span class="comment-age">(15 Sep '13, 12:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24715" class="comment-tools"></div><div class="clear"></div><div id="comment-24715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24728"></span>

<div id="answer-container-24728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24728-score" class="post-score" title="current number of votes">3</div><span id="post-24728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://tools.ietf.org/html/rfc4106#section-8.1">RFC 4106 Section 8.1</a>:</p><p>AES-GCM-ESP with a 256 bit key The KEYMAT requested for each AES GCM key is 36 octets. The first 32 octets are the 256-bit AES key, and the remaining four octets are used as the salt value in the nonce.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '13, 17:11</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24728" class="comments-container"><span id="24733"></span><div id="comment-24733" class="comment"><div id="post-24733-score" class="comment-score"></div><div class="comment-text"><p>I see, Thanks! (Kurt - this is on Wireshark 1.10.1)</p></div><div id="comment-24733-info" class="comment-info"><span class="comment-age">(15 Sep '13, 22:17)</span> <span class="comment-user userinfo">YuvalAdler</span></div></div></div><div id="comment-tools-24728" class="comment-tools"></div><div class="clear"></div><div id="comment-24728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

