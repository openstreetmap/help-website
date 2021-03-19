+++
type = "question"
title = "Ranap ErrorIndication"
description = '''I am new to telecom domain I am trying to encode and decode the ranap errorIndication message. but the specification specifies that Procedure Code is to be used if Criticality Diagnostics is part of Error Indication procedure, and not within the response message of the same procedure that caused the...'''
date = "2014-03-17T22:10:00Z"
lastmod = "2014-03-19T14:30:00Z"
weight = 30913
keywords = [ "3g", "wireshark" ]
aliases = [ "/questions/30913" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ranap ErrorIndication](/questions/30913/ranap-errorindication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30913-score" class="post-score" title="current number of votes">0</div><span id="post-30913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to telecom domain</p><p>I am trying to encode and decode the ranap errorIndication message.</p><p>but the specification specifies that</p><p>Procedure Code is to be used if Criticality Diagnostics is part of Error Indication procedure, and not within the response message of the same procedure that caused the error.</p><p>So if I include the procedure code of the failing message in the errorIndication message.Then the wireshark shows the errorIndication as the SACK of the failed message.</p><p>So I want to know how we can include the procedure code of the failing message in the errorIndication so that Wireshark should treat the message correctly.</p><p>Thanks in Advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-3g" rel="tag" title="see questions tagged &#39;3g&#39;">3g</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/98a57cd8f4c2bf70526fe58d4391856b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdk&#39;s gravatar image" /><p><span>sdk</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdk has no accepted answers">0%</span></p></div></div><div id="comments-container-30913" class="comments-container"><span id="30975"></span><div id="comment-30975" class="comment"><div id="post-30975-score" class="comment-score"></div><div class="comment-text"><p>Can you upload an example packet capture file for the scenario you're describing and post the link to it here (<a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> )?</p><p>I think you might be misinterpreting the capture. If it's RANAP over SCTP, you may see a "SACK", but that's an acknowledgement at the SCTP layer, not the RANAP layer. For RANAP exchanges, transactions are mapped based on the SCCP 'local reference' numbers, where a different transaction between the two system should have different reference numbers. The same procedureCode value shouldn't be mapped to the same transaction at a RANAP level if the reference numbers are different.</p></div><div id="comment-30975-info" class="comment-info"><span class="comment-age">(19 Mar '14, 14:30)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-30913" class="comment-tools"></div><div class="clear"></div><div id="comment-30913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

