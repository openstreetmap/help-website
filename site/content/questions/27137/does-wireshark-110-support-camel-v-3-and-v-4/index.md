+++
type = "question"
title = "Does wireshark-1.10 support Camel v-3 and v-4?"
description = '''Hi all, I&#x27;m dissecting Camel packet by using wireshark. I see most of my packet are &quot;Camel-v1&quot; or &quot;Camel-v2&quot; or &quot;Camel&quot; and nothing else. So:  Does this mean my camel packets are version 1, version 2 ? How can I know the version of Camel packet if it is unknown (Protocol = &quot;Camel&quot; on GUI)? I check t...'''
date = "2013-11-20T00:48:00Z"
lastmod = "2013-11-20T00:48:00Z"
weight = 27137
keywords = [ "version", "camel" ]
aliases = [ "/questions/27137" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does wireshark-1.10 support Camel v-3 and v-4?](/questions/27137/does-wireshark-110-support-camel-v-3-and-v-4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27137-score" class="post-score" title="current number of votes">0</div><span id="post-27137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm dissecting Camel packet by using wireshark. I see most of my packet are "<strong>Camel-v1</strong>" or "<strong>Camel-v2</strong>" or "<strong>Camel</strong>" and nothing else. So:</p><ol><li>Does this mean my camel packets are <strong>version 1</strong>, <strong>version 2</strong> ?</li><li>How can I know the version of Camel packet if it is unknown (Protocol = "Camel" on GUI)?</li><li>I check the code (branch trunk-1.10) and don't see other versions (<strong>Camel-v3, Camel-v4</strong>...) in the code. Does this mean this code of Wireshark does not support Camel version 3 and version 4?</li><li>If the answer of question 3 is <strong>YES (IT DOESN'T SUPPORT)</strong>: I read a book "Intelligent Network for the GSM, GPRS and UMTS Network" and it says:</li></ol><blockquote><p>One of the enhancements to the O-BCSM and the T-BCSM, compared with CAMEL phase 3,is the introduction of the alerting detection points. The following DPs are used for the alerting event: O-BCSM: O Term Seized; and T-BCSM: T Call Accepted</p></blockquote><p>As I understand, if so, only camel-v4 has "<strong>O Term Seized</strong>" and "<strong>T Call Accepted</strong>" but I search in the wireshark code (which support only version 1 and version 2), there are values for "<strong>O Term Seized</strong>" and "<strong>T Call Accepted</strong>" as below:</p><pre><code>static const value_string camel_EventTypeBCSM_vals[] = {
  {   2, &quot;collectedInfo&quot; },
  {   3, &quot;analyzedInformation&quot; },
  {   4, &quot;routeSelectFailure&quot; },
  {   5, &quot;oCalledPartyBusy&quot; },
  {   6, &quot;oNoAnswer&quot; },
  {   7, &quot;oAnswer&quot; },
  {   8, &quot;oMidCall&quot; },
  {   9, &quot;oDisconnect&quot; },
  {  10, &quot;oAbandon&quot; },
  {  12, &quot;termAttemptAuthorized&quot; },
  {  13, &quot;tBusy&quot; },
  {  14, &quot;tNoAnswer&quot; },
  {  15, &quot;tAnswer&quot; },
  {  16, &quot;tMidCall&quot; },
  {  17, &quot;tDisconnect&quot; },
  {  18, &quot;tAbandon&quot; },
  {  19, &quot;oTermSeized&quot; },
  {  27, &quot;callAccepted&quot; },
  {  50, &quot;oChangeOfPosition&quot; },
  {  51, &quot;tChangeOfPosition&quot; },
  {  52, &quot;oServiceChange&quot; },
  {  53, &quot;tServiceChange&quot; },</code></pre><p>My question 4 is: If wireshark 1-10 does not support v3, v4, so why there are code string for values of v4 only? And if wireshark 1-10 support v3, v4, so why I cannot find out the indication of these versions in the code?</p><p>Thanks for your help :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-camel" rel="tag" title="see questions tagged &#39;camel&#39;">camel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '13, 02:25</strong> </span></p></div></div><div id="comments-container-27137" class="comments-container"></div><div id="comment-tools-27137" class="comment-tools"></div><div class="clear"></div><div id="comment-27137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

