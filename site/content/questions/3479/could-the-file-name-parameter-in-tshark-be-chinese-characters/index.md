+++
type = "question"
title = "could the file name parameter in tshark be chinese characters?"
description = '''when I use   tshark -r chinese-characters.cap such as &quot;tshark -r 中文.cap&quot; It says that the file name is invalid.  How could I resolve this problem? thanks'''
date = "2011-04-13T07:47:00Z"
lastmod = "2011-04-13T07:59:00Z"
weight = 3479
keywords = [ "characters", "tshark", "chinese" ]
aliases = [ "/questions/3479" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [could the file name parameter in tshark be chinese characters?](/questions/3479/could-the-file-name-parameter-in-tshark-be-chinese-characters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3479-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when I use tshark -r chinese-characters.cap such as "tshark -r 中文.cap" It says that the file name is invalid. How could I resolve this problem?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">characters tshark chinese</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '11, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/420ef21d0f86668efe372f918583e39d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="janequeen&#39;s gravatar image" /><p>janequeen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="janequeen has no accepted answers">0%</span></p></div></div><div id="comments-container-3479" class="comments-container"></div><div id="comment-tools-3479" class="comment-tools"></div><div class="clear"></div><div id="comment-3479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3480"></span>

<div id="answer-container-3480" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3480-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The obvious workaround is to either rename the file before opening it with tshark (or create a link or shortcut to the original file).</p><p>Which version of tshark are you running? I believe there has been some work done recently on handling non-ascii filenames. Could you try version 1.5.1?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '11, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3480" class="comments-container"><span id="3496"></span><div id="comment-3496" class="comment"><div id="post-3496-score" class="comment-score"></div><div class="comment-text"><p>Thanks. version 1.5.1 supports non-ascii filenames.</p></div><div id="comment-3496-info" class="comment-info"><span class="comment-age">(14 Apr '11, 05:47)</span> janequeen</div></div><span id="3503"></span><div id="comment-3503" class="comment"><div id="post-3503-score" class="comment-score"></div><div class="comment-text"><p>Good to hear you were able to solve your issue with version 1.5.1!</p><p>(I changed your "answer" to a "comment", as that's the way this site works best, please see the FAQ. Also, to get this question of the "unanswered questions" list, you can accept an answer by clicking on the checkmark on the left of the answer)</p></div><div id="comment-3503-info" class="comment-info"><span class="comment-age">(14 Apr '11, 11:12)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3480" class="comment-tools"></div><div class="clear"></div><div id="comment-3480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

