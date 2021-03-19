+++
type = "question"
title = "SNA dissector not called when DSAP 0xc8"
description = '''Hello, wireshark doesn&#x27;t interpret the SNA payload contained in udp1200x packets when the LLC DSAP value is not 4 or 8. Some implementations use other values (always multiple of 4). In the testcase appended to http://www.cloudshark.org/captures/c1e5e07508f4 the DSAP value in Logical-Link Control is ...'''
date = "2013-07-30T07:18:00Z"
lastmod = "2014-06-01T00:26:00Z"
weight = 23446
keywords = [ "hprip", "dsap", "ee", "llc", "sna" ]
aliases = [ "/questions/23446" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SNA dissector not called when DSAP 0xc8](/questions/23446/sna-dissector-not-called-when-dsap-0xc8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23446-score" class="post-score" title="current number of votes">0</div><span id="post-23446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, wireshark doesn't interpret the SNA payload contained in udp1200x packets when the LLC DSAP value is not 4 or 8. Some implementations use other values (always multiple of 4). In the testcase appended to <a href="http://www.cloudshark.org/captures/c1e5e07508f4">http://www.cloudshark.org/captures/c1e5e07508f4</a> the DSAP value in Logical-Link Control is C8. Is there an easy way to 'decode as' SNA ? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hprip" rel="tag" title="see questions tagged &#39;hprip&#39;">hprip</span> <span class="post-tag tag-link-dsap" rel="tag" title="see questions tagged &#39;dsap&#39;">dsap</span> <span class="post-tag tag-link-ee" rel="tag" title="see questions tagged &#39;ee&#39;">ee</span> <span class="post-tag tag-link-llc" rel="tag" title="see questions tagged &#39;llc&#39;">llc</span> <span class="post-tag tag-link-sna" rel="tag" title="see questions tagged &#39;sna&#39;">sna</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '13, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-23446" class="comments-container"></div><div id="comment-tools-23446" class="comment-tools"></div><div class="clear"></div><div id="comment-23446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33235"></span>

<div id="answer-container-33235" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33235-score" class="post-score" title="current number of votes">1</div><span id="post-33235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde2 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The 0xC8 DSAP is only used for HPR NLP packets flowing towards outdated CS/Win platforms. So filing a bug to wireshark is not worth the effort as this software is no longer supported. The alternative for SNA applications on Windows platforms is to use SNA API clients as outlined in <a href="http://www.redbooks.ibm.com/abstracts/redp4998.html?Open">http://www.redbooks.ibm.com/abstracts/redp4998.html?Open</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '14, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-33235" class="comments-container"></div><div id="comment-tools-33235" class="comment-tools"></div><div class="clear"></div><div id="comment-33235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

