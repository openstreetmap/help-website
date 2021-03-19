+++
type = "question"
title = "SNMP request/response  not appearing on wireshark"
description = '''Hello, In my application, I am sending SNMP GET requests to multiple SNMP devices. Randomly for some of the devices, I am not getting the SNMP GET response. I looked at the wireshark capture and it contained SNMP request/response for those devices for which the SNMP response was received successfull...'''
date = "2012-11-19T02:41:00Z"
lastmod = "2013-05-07T06:00:00Z"
weight = 16047
keywords = [ "snmpwireshark" ]
aliases = [ "/questions/16047" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SNMP request/response not appearing on wireshark](/questions/16047/snmp-requestresponse-not-appearing-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16047-score" class="post-score" title="current number of votes">0</div><span id="post-16047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>In my application, I am sending SNMP GET requests to multiple SNMP devices. Randomly for some of the devices, I am not getting the SNMP GET response. I looked at the wireshark capture and it contained SNMP request/response for those devices for which the SNMP response was received successfully. For the devices for which SNMP response was not received, wireshark capture does not even show any SNMP GET request.</p><p>Does anyone have any idea about why the SNMP GET request not appearing on the interface for some of the devices?</p><p>The behavior is random and the devices that failed SNMP query in first attempt may respond in another attempt.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmpwireshark" rel="tag" title="see questions tagged &#39;snmpwireshark&#39;">snmpwireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '12, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/0c3da44cf7f76905a24c76006fc27587?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="supercruise&#39;s gravatar image" /><p><span>supercruise</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="supercruise has no accepted answers">0%</span></p></div></div><div id="comments-container-16047" class="comments-container"><span id="21002"></span><div id="comment-21002" class="comment"><div id="post-21002-score" class="comment-score"></div><div class="comment-text"><p>I am seeing similar behavior with Wireshark 1.8.6 on Windows 7. I do not see the SNMP get-request but I do see the SNMP get-response. That is how I know the request was sent. I'm not using any capture filters or display filters. Any help would be appreciated.</p></div><div id="comment-21002-info" class="comment-info"><span class="comment-age">(07 May '13, 06:00)</span> <span class="comment-user userinfo">webfxmasta</span></div></div></div><div id="comment-tools-16047" class="comment-tools"></div><div class="clear"></div><div id="comment-16047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16048"></span>

<div id="answer-container-16048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16048-score" class="post-score" title="current number of votes">0</div><span id="post-16048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does anyone have any idea about why the SNMP GET request not appearing on the interface for some of the devices?</p></blockquote><p>If you don't see the GET request it was possible not sent. How do you know the request was sent?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16048" class="comments-container"></div><div id="comment-tools-16048" class="comment-tools"></div><div class="clear"></div><div id="comment-16048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

