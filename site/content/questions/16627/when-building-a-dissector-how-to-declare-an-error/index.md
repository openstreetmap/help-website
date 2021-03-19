+++
type = "question"
title = "When building a dissector: How to declare an error?"
description = '''Hey, I&#x27;m building a dissector and I would like to know if it is possible to explicitly declare about errors. for example: If something&#x27;s length should be 0, but it doesn&#x27;t, then I want to say &quot;error, something is wrong&quot; Thanks ahead.'''
date = "2012-12-06T02:15:00Z"
lastmod = "2012-12-06T02:58:00Z"
weight = 16627
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/16627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [When building a dissector: How to declare an error?](/questions/16627/when-building-a-dissector-how-to-declare-an-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16627-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I'm building a dissector and I would like to know if it is possible to explicitly declare about errors. for example: If something's length should be 0, but it doesn't, then I want to say "error, something is wrong"</p><p>Thanks ahead.</p></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '12, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div></div><div id="comments-container-16627" class="comments-container"></div><div id="comment-tools-16627" class="comment-tools"></div><div class="clear"></div><div id="comment-16627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16628"></span>

<div id="answer-container-16628" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16628-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks to "SidR", You should take the following line, and do variations on him. (remember to include epan/expert.h )</p><p>expert_add_info_format(pinfo, acp_data_tree, PI_MALFORMED, PI_WARN, "Length &gt; 0");</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '12, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div></div><div id="comments-container-16628" class="comments-container"><span id="16629"></span><div id="comment-16629" class="comment"><div id="post-16629-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. :)</p></div><div id="comment-16629-info" class="comment-info"><span class="comment-age">(06 Dec '12, 03:06)</span> SidR</div></div></div><div id="comment-tools-16628" class="comment-tools"></div><div class="clear"></div><div id="comment-16628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

