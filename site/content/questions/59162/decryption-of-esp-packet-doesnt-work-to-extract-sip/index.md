+++
type = "question"
title = "Decryption of ESP packet doesn&#x27;t work (to extract SIP)"
description = '''I have a pcap with SIP register, 401 messages and ESP.  I am trying to decrypt it but probably enter the wrong keys. What should I insert under &quot;Encryption Key&quot; and &quot;Authentication Key&quot;? I have the IK and CK? are those good enough? Thanks, Diana'''
date = "2017-01-30T12:32:00Z"
lastmod = "2017-01-31T00:15:00Z"
weight = 59162
keywords = [ "esp_sa", "sip", "decryption" ]
aliases = [ "/questions/59162" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decryption of ESP packet doesn't work (to extract SIP)](/questions/59162/decryption-of-esp-packet-doesnt-work-to-extract-sip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59162-score" class="post-score" title="current number of votes">0</div><span id="post-59162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap with SIP register, 401 messages and ESP. I am trying to decrypt it but probably enter the wrong keys. What should I insert under "Encryption Key" and "Authentication Key"? I have the IK and CK? are those good enough?</p><p>Thanks, Diana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-esp_sa" rel="tag" title="see questions tagged &#39;esp_sa&#39;">esp_sa</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '17, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-59162" class="comments-container"><span id="59168"></span><div id="comment-59168" class="comment"><div id="post-59168-score" class="comment-score"></div><div class="comment-text"><p>how did you get the IK and CK? Also which cipher is being used by the esp protocol for encryption and HMAC?</p></div><div id="comment-59168-info" class="comment-info"><span class="comment-age">(30 Jan '17, 22:33)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="59169"></span><div id="comment-59169" class="comment"><div id="post-59169-score" class="comment-score"></div><div class="comment-text"><p>Also you might want to read through this question on this forum.</p><p><a href="https://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets">https://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets</a></p></div><div id="comment-59169-info" class="comment-info"><span class="comment-age">(30 Jan '17, 22:37)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="59173"></span><div id="comment-59173" class="comment"><div id="post-59173-score" class="comment-score"></div><div class="comment-text"><p>I got the IK &amp; CK from SIP register</p></div><div id="comment-59173-info" class="comment-info"><span class="comment-age">(30 Jan '17, 23:52)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="59174"></span><div id="comment-59174" class="comment"><div id="post-59174-score" class="comment-score"></div><div class="comment-text"><p>I don't understand, Can you give more details about your setup. I am assuming you are using a IPSEC tunnel with ESP which is encapsulating sip messages is that correct? then how can you get the encryption and authentication key from the SIP register message?</p></div><div id="comment-59174-info" class="comment-info"><span class="comment-age">(31 Jan '17, 00:15)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-59162" class="comment-tools"></div><div class="clear"></div><div id="comment-59162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

