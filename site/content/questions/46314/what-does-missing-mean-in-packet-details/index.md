+++
type = "question"
title = "What does MISSING mean in Packet Details"
description = '''I&#x27;m seeing &amp;lt;MISSING&amp;gt; in the Packet Details when looking at SNMP data: 1.3.6.1.3.118.1.2.2.1.2.4.109.109.114.99: &amp;lt;MISSING&amp;gt;  Object Name: 1.3.6.1.3.118.1.2.2.1.2.4.109.109.114.99 (iso.3.6.1.3.118.1.2.2.1.2.4.109.109.114.99)  Value (OctetString): &amp;lt;MISSING&amp;gt; The Packet Bytes shows that ...'''
date = "2015-10-01T10:11:00Z"
lastmod = "2015-10-02T08:54:00Z"
weight = 46314
keywords = [ "snmp", "missing" ]
aliases = [ "/questions/46314" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does MISSING mean in Packet Details](/questions/46314/what-does-missing-mean-in-packet-details)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46314-score" class="post-score" title="current number of votes">0</div><span id="post-46314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm seeing &lt;MISSING&gt; in the Packet Details when looking at SNMP data:</p><pre><code>1.3.6.1.3.118.1.2.2.1.2.4.109.109.114.99: &lt;MISSING&gt;
  Object Name: 1.3.6.1.3.118.1.2.2.1.2.4.109.109.114.99 (iso.3.6.1.3.118.1.2.2.1.2.4.109.109.114.99)
  Value (OctetString): &lt;MISSING&gt;
The Packet Bytes shows that data exists:
0110  01 01 30 13 06 0f 2b 06  01 03 76 01 02 02 01 02   ..0...+. ..v.....
0120  04 6d 6d 72 63 04 00 30  15 06 10 2b 06 01 03 76   .mmrc..0 ...+...v</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '15, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/cd9df3ebd7270653cba6bde5df2b7e75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="green73mgb&#39;s gravatar image" /><p><span>green73mgb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="green73mgb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Oct '15, 08:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-46314" class="comments-container"></div><div id="comment-tools-46314" class="comment-tools"></div><div class="clear"></div><div id="comment-46314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46341"></span>

<div id="answer-container-46341" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46341-score" class="post-score" title="current number of votes">0</div><span id="post-46341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="green73mgb has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It says that the tags are there, just no values.</p><p>If you could put a sample capture onto CloudShark we could have an even better look.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '15, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46341" class="comments-container"><span id="46344"></span><div id="comment-46344" class="comment"><div id="post-46344-score" class="comment-score"></div><div class="comment-text"><p>Ok, Thanks. That agrees with the snmpwalk output: 1.3.6.1.3.118.1.2.2.1.2.4.109.109.114.99, OctetString , although I was expecting "mmrc" to be the String value, but neither tool saw "mmrc" as the String value.</p></div><div id="comment-46344-info" class="comment-info"><span class="comment-age">(02 Oct '15, 08:54)</span> <span class="comment-user userinfo">green73mgb</span></div></div></div><div id="comment-tools-46341" class="comment-tools"></div><div class="clear"></div><div id="comment-46341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

