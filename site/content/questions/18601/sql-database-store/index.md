+++
type = "question"
title = "SQL Database Store"
description = '''A similar question was asked in 10/2011 so I&#x27;ll test the waters again to see if anything has changed since then. Has an extension or plugin been developed that supports taking filtered packets and storing them directly into a database (yes, the schema would need to be compatible with the export)? I ...'''
date = "2013-02-13T10:49:00Z"
lastmod = "2013-02-13T13:07:00Z"
weight = 18601
keywords = [ "storage", "archive", "database" ]
aliases = [ "/questions/18601" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SQL Database Store](/questions/18601/sql-database-store)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18601-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A similar question was asked in 10/2011 so I'll test the waters again to see if anything has changed since then.<br />
Has an extension or plugin been developed that supports taking filtered packets and storing them directly into a database (yes, the schema would need to be compatible with the export)? I have tested the C5 Sigma code and while it works well, the latency incurred in creating a PCAPNG file, closing the file while opening another PCAPNG file, then launching the C5 Sigma to store the data plus the complexity of writing O/S script code to orchestrate this process on a continuing basis doesn't fit well with the intended application. If not, is there an API that supports exporting the capture (preferably a pre/post-cap filtered) that can be programatically (preferably late binding) access to perform this store?</p></div><div id="question-tags" class="tags-container tags">storage archive database</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '13, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/1c1238ea8ea1b0fee5f28b1315de9232?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r772&#39;s gravatar image" /><p>r772<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r772 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '13, 10:50</p></div></div><div id="comments-container-18601" class="comments-container"><span id="18604"></span><div id="comment-18604" class="comment"><div id="post-18604-score" class="comment-score"></div><div class="comment-text"><blockquote><p>A similar question was asked in 10/2011</p></blockquote><p>can you please post the link to that question?</p></div><div id="comment-18604-info" class="comment-info"><span class="comment-age">(13 Feb '13, 11:11)</span> Kurt Knochner ♦</div></div><span id="18609"></span><div id="comment-18609" class="comment"><div id="post-18609-score" class="comment-score"></div><div class="comment-text"><p>Is this asking for a tap somehow?</p></div><div id="comment-18609-info" class="comment-info"><span class="comment-age">(13 Feb '13, 12:20)</span> Jaap ♦</div></div></div><div id="comment-tools-18601" class="comment-tools"></div><div class="clear"></div><div id="comment-18601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18611"></span>

<div id="answer-container-18611" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18611-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I recommend to look at some of these projects.</p><blockquote><p><code>https://labs.ripe.net/Members/wnagele/large-scale-pcap-data-analysis-using-apache-hadoop</code><br />
<code>http://code.google.com/p/pcap2sql/</code><br />
<code>http://www.commandfive.com/downloads/c5sigma.html  (you mentioned it already)</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '13, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18611" class="comments-container"></div><div id="comment-tools-18611" class="comment-tools"></div><div class="clear"></div><div id="comment-18611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

