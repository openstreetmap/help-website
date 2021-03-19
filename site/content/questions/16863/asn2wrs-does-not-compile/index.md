+++
type = "question"
title = "ASN2WRS does not compile"
description = '''Hello, I tried to compile my own dissector yesterday. I&#x27;m quite new to the matter, so I copied already available configuration files (Makefile, .cnf) from the inap dissector, changed the name there and removed asn files which I do not use. Then I put the name of my asn file in. After execution of ma...'''
date = "2012-12-14T02:08:00Z"
lastmod = "2012-12-14T08:49:00Z"
weight = 16863
keywords = [ "asn2wrs", "error", "asn", "output" ]
aliases = [ "/questions/16863" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ASN2WRS does not compile](/questions/16863/asn2wrs-does-not-compile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16863-score" class="post-score" title="current number of votes">0</div><span id="post-16863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I tried to compile my own dissector yesterday. I'm quite new to the matter, so I copied already available configuration files (Makefile, .cnf) from the inap dissector, changed the name there and removed asn files which I do not use. Then I put the name of my asn file in. After execution of make I got additional files in the directory: <a href="http://parsetab.py">parsetab.py</a>, -exp.cnf. Nothing else. According to <a href="http://wiki.wireshark.org/Asn2wrs" title="http://wiki.wireshark.org/Asn2wrs">http://wiki.wireshark.org/Asn2wrs</a> files</p><p>packet-proto-ett.c<br />
packet-proto-ettarr.c<br />
packet-proto-fn.c<br />
packet-proto-hf.c<br />
packet-proto-hfarr.c<br />
packet-proto-val.h<br />
packet-proto-exp.h<br />
packet-proto-table.c<br />
packet-proto-syn-reg.c<br />
</p><p>Should be created. So, I did something wrong. But what? There was no error output by asn2wrs...</p><p>BR Ewgenij</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn2wrs" rel="tag" title="see questions tagged &#39;asn2wrs&#39;">asn2wrs</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-asn" rel="tag" title="see questions tagged &#39;asn&#39;">asn</span> <span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '12, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p><span>Ewgenijkkg</span><br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span> </br></br></p></div></div><div id="comments-container-16863" class="comments-container"><span id="16864"></span><div id="comment-16864" class="comment"><div id="post-16864-score" class="comment-score">1</div><div class="comment-text"><p>Dis you run asn2wrs with the -k option? Does your template file have the needed #includes ? (Like #include "packet-acp133-ett.c" etc).</p></div><div id="comment-16864-info" class="comment-info"><span class="comment-age">(14 Dec '12, 04:20)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="16897"></span><div id="comment-16897" class="comment"><div id="post-16897-score" class="comment-score"></div><div class="comment-text"><p>Ah, OK, the -k option, thanks :)</p></div><div id="comment-16897-info" class="comment-info"><span class="comment-age">(14 Dec '12, 08:47)</span> <span class="comment-user userinfo">Ewgenijkkg</span></div></div></div><div id="comment-tools-16863" class="comment-tools"></div><div class="clear"></div><div id="comment-16863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16898"></span>

<div id="answer-container-16898" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16898-score" class="post-score" title="current number of votes">0</div><span id="post-16898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ewgenijkkg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, the issue is solved :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 08:49</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p><span>Ewgenijkkg</span><br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span> </br></br></p></div></div><div id="comments-container-16898" class="comments-container"></div><div id="comment-tools-16898" class="comment-tools"></div><div class="clear"></div><div id="comment-16898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

