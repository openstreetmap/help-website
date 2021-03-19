+++
type = "question"
title = "audit a log file"
description = '''Sir&#x27;s is there someone or somewhere that I can get an audit on my logfile? I don&#x27;t really know how to read this, but I believe that a computer in my office is attacking my computer and would like to verify it.'''
date = "2013-06-11T09:47:00Z"
lastmod = "2013-06-12T14:41:00Z"
weight = 21927
keywords = [ "audit" ]
aliases = [ "/questions/21927" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [audit a log file](/questions/21927/audit-a-log-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21927-score" class="post-score" title="current number of votes">0</div><span id="post-21927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sir's is there someone or somewhere that I can get an audit on my logfile? I don't really know how to read this, but I believe that a computer in my office is attacking my computer and would like to verify it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-audit" rel="tag" title="see questions tagged &#39;audit&#39;">audit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '13, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/122ae1098e10ce2f1e1fb5bb5803af11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sol%20Weinstein&#39;s gravatar image" /><p><span>Sol Weinstein</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sol Weinstein has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '13, 09:47</strong> </span></p></div></div><div id="comments-container-21927" class="comments-container"></div><div id="comment-tools-21927" class="comment-tools"></div><div class="clear"></div><div id="comment-21927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21943"></span>

<div id="answer-container-21943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21943-score" class="post-score" title="current number of votes">0</div><span id="post-21943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're talking about a file on your computer, logging some form of attack, that's not something Wireshark can help you with but if you mean you want to capture traffic that your computer is receiving from a suspected attacker then yes, Wireshark can do that. Just download Wireshark and start capturing data on your network card to see traffic coming to or from it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 20:37</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21943" class="comments-container"><span id="21966"></span><div id="comment-21966" class="comment"><div id="post-21966-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I should be able to see how much data is going to where in the "statistics conversations" section for each separate log, correct?</p><p>I'm just confused because of all of the different protocols and sooo much information, which is great.</p></div><div id="comment-21966-info" class="comment-info"><span class="comment-age">(12 Jun '13, 10:59)</span> <span class="comment-user userinfo">Sol Weinstein</span></div></div><span id="21981"></span><div id="comment-21981" class="comment"><div id="post-21981-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "log" here? The Statistics &gt; Conversations section will list every session that exists in the trace, per protocol, but your use of the term "log" is not clear to me.</p><p>For example, if you have a TCP session between your computer and theirs, it would appear in the TCP section of that window, listing the source/destination IP address and port numbers. You can also right-click on that conversation and apply it as a filter, so that Wireshark itself will display only the packets that relate to that 'conversation' between the two systems.</p></div><div id="comment-21981-info" class="comment-info"><span class="comment-age">(12 Jun '13, 14:41)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-21943" class="comment-tools"></div><div class="clear"></div><div id="comment-21943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

