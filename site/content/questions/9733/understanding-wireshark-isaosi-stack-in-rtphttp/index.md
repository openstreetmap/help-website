+++
type = "question"
title = "Understanding wireshark ISA/OSI stack (in RTP/HTTP)"
description = '''Hello, I am trying to understand how wirehark generates the 7 levels of ISA/OSI stack in the trace. Because after stack level 4 (trasport), how could I know if the &quot;data&quot; shown is level 5,6 or 7? For example, theoretically HTTP works on level 7, but in trace are only displayed:  1.Frame -&amp;gt; 2. Eth...'''
date = "2012-03-24T05:50:00Z"
lastmod = "2012-03-25T12:42:00Z"
weight = 9733
keywords = [ "wireshark" ]
aliases = [ "/questions/9733" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding wireshark ISA/OSI stack (in RTP/HTTP)](/questions/9733/understanding-wireshark-isaosi-stack-in-rtphttp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9733-score" class="post-score" title="current number of votes">0</div><span id="post-9733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to understand how wirehark generates the 7 levels of ISA/OSI stack in the trace. Because after stack level 4 (trasport), how could I know if the "data" shown is level 5,6 or 7? For example, theoretically HTTP works on level 7, but in trace are only displayed: 1.Frame -&gt; 2. Eth II -&gt; 3.IPv4 -&gt; 4. TCP -&gt; 5.HTTP So, seems "session" and "presentation" are skipped? and in case trace of RTP, I can see: 1.Frame -&gt; 2. Eth II -&gt; 3.IPv4 -&gt; 4. UDP -&gt; 5.RTP According some info reported in internet, RTP works in level 5 while others report it works on level 7. Hence, would you please help me to understand how could I read the stack of ISA/OSI, by reading trace output of wirshark and the mechanism? Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '12, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/b679fef533217556c51820ed76eea798?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SchrodingerCat&#39;s gravatar image" /><p><span>SchrodingerCat</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SchrodingerCat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Mar '12, 07:08</strong> </span></p></div></div><div id="comments-container-9733" class="comments-container"></div><div id="comment-tools-9733" class="comment-tools"></div><div class="clear"></div><div id="comment-9733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9735"></span>

<div id="answer-container-9735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9735-score" class="post-score" title="current number of votes">1</div><span id="post-9735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not all protocol stacks strictly follow the OSI model, and different people might have different opinions about where protocols at layers above the transport layer belong in the OSI model.</p><p>The OSI model isn't the only model; the <a href="http://en.wikipedia.org/wiki/TCP/IP_model">TCP/IP model</a> also exists, and puts everything above the transport layer at the application layer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '12, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9735" class="comments-container"><span id="9741"></span><div id="comment-9741" class="comment"><div id="post-9741-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it's clear!</p></div><div id="comment-9741-info" class="comment-info"><span class="comment-age">(25 Mar '12, 02:44)</span> <span class="comment-user userinfo">SchrodingerCat</span></div></div><span id="9749"></span><div id="comment-9749" class="comment"><div id="post-9749-score" class="comment-score">1</div><div class="comment-text"><p>When someone successfully answers your question you're meant to accept the answer by clicking the "check". Thanks.</p></div><div id="comment-9749-info" class="comment-info"><span class="comment-age">(25 Mar '12, 12:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-9735" class="comment-tools"></div><div class="clear"></div><div id="comment-9735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

