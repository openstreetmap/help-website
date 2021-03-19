+++
type = "question"
title = "MAP user abort"
description = '''hi... i need your expertise... below is an SS7 trace captured where the MSC is sending an abort message... what is causing this abort? Transaction Capabilities Application Part abort Destination Transaction ID Transaction Id: 0817184d reason: u-abortCause (11) oid: 0.0.17.773.1.1.1 (id-as-dialogue) ...'''
date = "2012-10-01T05:40:00Z"
lastmod = "2013-06-24T23:53:00Z"
weight = 14625
keywords = [ "map", "ss7", "gsm" ]
aliases = [ "/questions/14625" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAP user abort](/questions/14625/map-user-abort)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14625-score" class="post-score" title="current number of votes">0</div><span id="post-14625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi... i need your expertise...</p><p>below is an SS7 trace captured where the MSC is sending an abort message... what is causing this abort?</p><pre><code>Transaction Capabilities Application Part
abort
Destination Transaction ID
Transaction Id: 0817184d
reason: u-abortCause (11)
oid: 0.0.17.773.1.1.1 (id-as-dialogue)
dialogueAbort
abort-source: dialogue-service-user (0)
user-information: 1 item
user-information item
direct-reference: 0.4.0.0.1.1.1.1 (map-DialogueAS)
encoding: single-ASN1-type (0)
MAP-DialoguePDU: map-userAbort (4)
map-userAbort
map-UserAbortChoice: userSpecificReason (0)
userSpecificReason
.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '12, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/b448732553ca07bfdcb9a3d765f1ece8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sau2k122&#39;s gravatar image" /><p><span>sau2k122</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sau2k122 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Oct '12, 08:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-14625" class="comments-container"><span id="22303"></span><div id="comment-22303" class="comment"><div id="post-22303-score" class="comment-score"></div><div class="comment-text"><p>Dear Sir,</p><p>i also have the same issue kindly please help me.</p><p>i am testing a USSD conversation, while i am in the responding to the USSD from Mobile handset my transaction abourt.</p><p>Example:</p><p>handset: *303# USSD: please enter your facebook ID handset: during typing the facebook ID after 45 secound the transaction disconnecting.</p><p>our USSD team has set this priod to 2 minutes. i want to know which platform abourt the trasaction.</p><p>Trace:</p><p>MSC send message as your snapshoot above and as i took GSM trace on MSC it showing Radio Interface Failur.</p><p>in this piont i couldn't prove that problem is where while BSS is doing nating with timer.</p><p>i am looking for your comment.</p><p>regards,</p><p>Hafizullah Afghanistan (AWCC) company</p></div><div id="comment-22303-info" class="comment-info"><span class="comment-age">(24 Jun '13, 23:53)</span> <span class="comment-user userinfo">Hafiz</span></div></div></div><div id="comment-tools-14625" class="comment-tools"></div><div class="clear"></div><div id="comment-14625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14788"></span>

<div id="answer-container-14788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14788-score" class="post-score" title="current number of votes">0</div><span id="post-14788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what is causing this abort?</p></blockquote><p>Well.... how are we supposed to tell with only the abort message?</p><p>Can you post the whole conversation in pcap format (<a href="http://cloudshark.org">cloudshark.org</a>)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14788" class="comments-container"><span id="14790"></span><div id="comment-14790" class="comment"><div id="post-14790-score" class="comment-score"></div><div class="comment-text"><p><a href="http://cloudshark.org/captures/bb9205c0e633">http://cloudshark.org/captures/bb9205c0e633</a></p><p>pls find the trace</p></div><div id="comment-14790-info" class="comment-info"><span class="comment-age">(08 Oct '12, 12:36)</span> <span class="comment-user userinfo">sau2k122</span></div></div><span id="14793"></span><div id="comment-14793" class="comment"><div id="post-14793-score" class="comment-score"></div><div class="comment-text"><p>There is no information about the abort reason in the posted capture file. Do you see any frame with "MAP-NOTICE" in the <strong>full</strong> capture file?</p></div><div id="comment-14793-info" class="comment-info"><span class="comment-age">(08 Oct '12, 12:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-14788" class="comment-tools"></div><div class="clear"></div><div id="comment-14788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

