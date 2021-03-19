+++
type = "question"
title = "How to correctly configure SAs for decryption when using AES-GCM"
description = '''I am trying to decrypt ESP payloads with AES-GCM as the encryption algorithm. I am able to identify the correct settings for all of the fields, but I am not clear on what to use for the encryption key and authentication algorithm, key settings. I have tried various configurations and while I can get...'''
date = "2014-04-02T06:49:00Z"
lastmod = "2016-03-01T10:01:00Z"
weight = 31387
keywords = [ "encryption", "aes-gcm", "esp" ]
aliases = [ "/questions/31387" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to correctly configure SAs for decryption when using AES-GCM](/questions/31387/how-to-correctly-configure-sas-for-decryption-when-using-aes-gcm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31387-score" class="post-score" title="current number of votes">0</div><span id="post-31387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt ESP payloads with AES-GCM as the encryption algorithm. I am able to identify the correct settings for all of the fields, but I am not clear on what to use for the encryption key and authentication algorithm, key settings. I have tried various configurations and while I can get decrypted data, it is not dissected and I am guessing that the decryption is not correct.</p><p>I used the command ip xfrm state to obtain the SA information. It shows that AES-GCM is used with 256 bit key. Do I use the entire 72 octet keymat supplied in xfrm output for the authentication key?</p><p>For the authentication in am using the ANY 128 bit authentication [no checking} - setting. Is this correct?</p><p>I am using wireshark 1.10.6</p><p>Thx, Rich</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-aes-gcm" rel="tag" title="see questions tagged &#39;aes-gcm&#39;">aes-gcm</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/c9276be73f6bef191ad5df102c6ff321?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rich&#39;s gravatar image" /><p><span>Rich</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rich has no accepted answers">0%</span></p></div></div><div id="comments-container-31387" class="comments-container"></div><div id="comment-tools-31387" class="comment-tools"></div><div class="clear"></div><div id="comment-31387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31423"></span>

<div id="answer-container-31423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31423-score" class="post-score" title="current number of votes">1</div><span id="post-31423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you follow the steps outlined in my answer to the following question?</p><blockquote><p><a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets">http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets</a></p></blockquote><p>see <strong>ESP decryption</strong> in that answer.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31423" class="comments-container"><span id="31483"></span><div id="comment-31483" class="comment"><div id="post-31483-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>I appreciate the feedback. I have read through and followed the approach outlined in your reference. I have been looking for a successful example that is specific to the particular algorithm aes-gcm and have yet to see one.</p><p>This ESP transform does not have an explicit authentication algorithm. I am not sure how to correctly map the keymat generated by the xfrm command into the key field for the SA ui form. We are using 256 bit key so the keymat provides 32 octets (64 hex digits) and 4 octets used a slat value for the nonce. I can only get an indication of decryption when I plug-in the whole keymat field (key+ nonce).</p><p>We also have a 128 bit (16 octet ICV). I am not sure if there needs to be a setting configured for the authentication algorithm and key fields so have been using any 128 bit authentication [no checking] to at least the correct size for the ICV.</p><p>Rich</p></div><div id="comment-31483-info" class="comment-info"><span class="comment-age">(03 Apr '14, 07:23)</span> <span class="comment-user userinfo">Rich</span></div></div><span id="50613"></span><div id="comment-50613" class="comment"><div id="post-50613-score" class="comment-score"></div><div class="comment-text"><p>Likewise, I came here looking for a way to make Wireshark aware of rfc4106(gcm(aes)) and instead saw a reference to a page that assumes, as Wireshark seems to, that we want to use cbc(aes) (which is for IKEv2, rather than ESP) for ESP using aead.</p></div><div id="comment-50613-info" class="comment-info"><span class="comment-age">(01 Mar '16, 10:01)</span> <span class="comment-user userinfo">Jerry Miller</span></div></div></div><div id="comment-tools-31423" class="comment-tools"></div><div class="clear"></div><div id="comment-31423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

