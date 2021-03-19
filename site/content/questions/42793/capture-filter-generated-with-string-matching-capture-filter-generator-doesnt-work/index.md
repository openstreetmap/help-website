+++
type = "question"
title = "Capture filter generated with String-Matching Capture Filter Generator doesn&#x27;t work"
description = '''Hi all, I am trying to collect a specific audio codec call on both sides of a SBC. Only a few calls are establishe with AMR (payload 96) while all others are established with G.729. I used String-Matching Capture Filter Generator:    Enter the string you want to match sip || rtp.p_type == 96    Ente...'''
date = "2015-06-01T06:24:00Z"
lastmod = "2015-06-01T06:31:00Z"
weight = 42793
keywords = [ "filter", "capture", "string-matching" ]
aliases = [ "/questions/42793" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter generated with String-Matching Capture Filter Generator doesn't work](/questions/42793/capture-filter-generated-with-string-matching-capture-filter-generator-doesnt-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42793-score" class="post-score" title="current number of votes">0</div><span id="post-42793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am trying to collect a specific audio codec call on both sides of a SBC. Only a few calls are establishe with AMR (payload 96) while all others are established with G.729. I used <a href="https://www.wireshark.org/tools/string-cf.html">String-Matching Capture Filter Generator</a>:</p><ol><li><p>Enter the string you want to match sip || rtp.p_type == 96</p></li><li><p>Enter the offset from the start of the TCP data 0</p></li><li><p>Copy the filter below</p></li></ol><p>tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x73697020 &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 4:4] = 0x7c7c2072 &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 8:4] = 0x74702e70 &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 12:4] = 0x5f747970 &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 16:4] = 0x65203d3d &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 20:2] = 0x2039 &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 22:1] = 0x36</p><p>but filter doesn't work as expected. Could you please advice ?</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-string-matching" rel="tag" title="see questions tagged &#39;string-matching&#39;">string-matching</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '15, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/7a2b831f6b8b64c5a65b3b5dfa451393?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michele&#39;s gravatar image" /><p><span>michele</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michele has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '15, 17:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-42793" class="comments-container"></div><div id="comment-tools-42793" class="comment-tools"></div><div class="clear"></div><div id="comment-42793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42794"></span>

<div id="answer-container-42794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42794-score" class="post-score" title="current number of votes">2</div><span id="post-42794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the problem is, that the generator is a <strong>String-Matching</strong> generator, meaning: it builds capture filters that look for <strong>strings</strong>, not display filter expressions. Or, in other words: it does <strong>not</strong> turn display filters into capture filters. So what you're doing is looking for the string "sip || rtp.ptype == 96" inside the packets, not for rtp-p_type being 95 and the protocol being sip.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '15, 06:32</strong> </span></p></div></div><div id="comments-container-42794" class="comments-container"></div><div id="comment-tools-42794" class="comment-tools"></div><div class="clear"></div><div id="comment-42794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

