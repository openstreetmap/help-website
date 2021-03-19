+++
type = "question"
title = "undefined symbol: xmlParseFile"
description = '''I&#x27;m working in linux and I would need to use libxml2 functions for the development of a plugin for wireshark but when I start wireshark I get an error message: undefined symbol: xmlParseFile. I thought that the error would be resolved by including the header &quot;xmlexports.h&quot; but it was not so.  I am w...'''
date = "2014-05-12T03:01:00Z"
lastmod = "2014-05-12T07:21:00Z"
weight = 32722
keywords = [ "development", "libxml2", "symbol", "plugin", "error" ]
aliases = [ "/questions/32722" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [undefined symbol: xmlParseFile](/questions/32722/undefined-symbol-xmlparsefile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32722-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working in linux and I would need to use libxml2 functions for the development of a plugin for wireshark but when I start wireshark I get an error message: undefined symbol: xmlParseFile. I thought that the error would be resolved by including the header "xmlexports.h" but it was not so. I am writing a piece of code to facilitate the understanding:</p><pre><code>#include &lt;libxml/xmlmemory.h&gt;
#include &lt;libxml/parser.h&gt;
xmlDocPtr docS=NULL;
char *fileNameXML=&quot;test.xml&quot;
docS = xmlParseFile(fileNameXML);</code></pre><p>Thank you in advance!</p></div><div id="question-tags" class="tags-container tags">development libxml2 symbol plugin error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '14, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/beba516396947952b1ec047a91607492?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Junzo&#39;s gravatar image" /><p>Junzo<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Junzo has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 May '14, 09:00</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32722" class="comments-container"><span id="32725"></span><div id="comment-32725" class="comment"><div id="post-32725-score" class="comment-score"></div><div class="comment-text"><p>I guess you need to change the makefile(s) to link against libxml2.</p></div><div id="comment-32725-info" class="comment-info"><span class="comment-age">(12 May '14, 05:42)</span> Anders ♦</div></div><span id="32726"></span><div id="comment-32726" class="comment"><div id="post-32726-score" class="comment-score"></div><div class="comment-text"><p>I think the issue might be a runtime load problem, the OP says the problem occurs when starting Wireshark, not building.</p></div><div id="comment-32726-info" class="comment-info"><span class="comment-age">(12 May '14, 05:53)</span> grahamb ♦</div></div><span id="32729"></span><div id="comment-32729" class="comment"><div id="post-32729-score" class="comment-score"></div><div class="comment-text"><p>Or maybe not.</p></div><div id="comment-32729-info" class="comment-info"><span class="comment-age">(12 May '14, 07:27)</span> grahamb ♦</div></div></div><div id="comment-tools-32722" class="comment-tools"></div><div class="clear"></div><div id="comment-32722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32728"></span>

<div id="answer-container-32728" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had forgotten to include the library lxml2 in phase of linking. I'm sorry</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '14, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/beba516396947952b1ec047a91607492?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Junzo&#39;s gravatar image" /><p>Junzo<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Junzo has one accepted answer">100%</span></p></div></div><div id="comments-container-32728" class="comments-container"><span id="32731"></span><div id="comment-32731" class="comment"><div id="post-32731-score" class="comment-score"></div><div class="comment-text"><p>@Junzo,</p><p>No need to modify the question title to mark it as answered/solved, instead click the checkmark icon next to your answer. Please read the FAQ for more info.</p></div><div id="comment-32731-info" class="comment-info"><span class="comment-age">(12 May '14, 09:01)</span> grahamb ♦</div></div></div><div id="comment-tools-32728" class="comment-tools"></div><div class="clear"></div><div id="comment-32728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

