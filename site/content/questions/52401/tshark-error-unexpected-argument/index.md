+++
type = "question"
title = "tshark error - unexpected argument"
description = '''hello  &amp;gt; C:&#92;Program Files&#92;Wireshark&amp;gt;tshark -r normal.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, quote=d -E occurrence=f  tshark: &quot;=&quot; was unexpected in this context.  what&#x27;s wrong o_O'''
date = "2016-05-10T11:30:00Z"
lastmod = "2016-05-10T14:10:00Z"
weight = 52401
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/52401" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark error - unexpected argument](/questions/52401/tshark-error-unexpected-argument)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52401-score" class="post-score" title="current number of votes">0</div><span id="post-52401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello</p><pre><code>&gt; C:\Program Files\Wireshark&gt;tshark -r normal.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, quote=d -E occurrence=f

tshark: &quot;=&quot; was unexpected in this context.</code></pre><p>what's wrong o_O</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '16, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/279908d3c8338ae7ec02baa9f51a3c1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khadidja%20Khadidja&#39;s gravatar image" /><p><span>Khadidja Kha...</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khadidja Khadidja has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 May '16, 13:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-52401" class="comments-container"></div><div id="comment-tools-52401" class="comment-tools"></div><div class="clear"></div><div id="comment-52401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52402"></span>

<div id="answer-container-52402" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52402-score" class="post-score" title="current number of votes">0</div><span id="post-52402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Khadidja Khadidja has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should try this:<br />
C:\Program Files\Wireshark&gt;tshark -r normal.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, <strong>-E</strong> quote=d -E occurrence=f</p><p><br />
I think you missed the <strong><code>-E</code></strong> in front of <strong><code>quote=d</code></strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '16, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div></div><div id="comments-container-52402" class="comments-container"><span id="52403"></span><div id="comment-52403" class="comment"><div id="post-52403-score" class="comment-score"></div><div class="comment-text"><p>thanks for your response it works now :) I have another question ^^, SORRY I am a beginner I want to convert normal.pcap file to csv file but I get</p><blockquote><p>C:\Program Files\Wireshark&gt;tshark -r normal.pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator=, -E quote=d -E occurrence=f &gt; test.csv Accès refusé.</p></blockquote><p>what is the pb here.</p><p>thanks in advance</p></div><div id="comment-52403-info" class="comment-info"><span class="comment-age">(10 May '16, 13:14)</span> <span class="comment-user userinfo">Khadidja Kha...</span></div></div><span id="52411"></span><div id="comment-52411" class="comment"><div id="post-52411-score" class="comment-score"></div><div class="comment-text"><p>As a normal user you are not allowed to write to C:\Program Files...</p><p>You should do like: &gt; C:\YOUR DOCUMENTS\test.csv</p></div><div id="comment-52411-info" class="comment-info"><span class="comment-age">(10 May '16, 13:44)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="52417"></span><div id="comment-52417" class="comment"><div id="post-52417-score" class="comment-score"></div><div class="comment-text"><p>thanks ^^ the problem is solved</p></div><div id="comment-52417-info" class="comment-info"><span class="comment-age">(10 May '16, 14:10)</span> <span class="comment-user userinfo">Khadidja Kha...</span></div></div></div><div id="comment-tools-52402" class="comment-tools"></div><div class="clear"></div><div id="comment-52402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

