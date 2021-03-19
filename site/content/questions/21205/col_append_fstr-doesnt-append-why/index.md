+++
type = "question"
title = "col_append_fstr doesn&#x27;t append. Why?"
description = '''Hi all; After the reassembling developments we&#x27;ve made in our dissector plugin, col__ append__ fstr doesn&#x27;t work correctly anymore. It does not append, it works like col__ add__fstr and displays the last item only. col append fstr(pinfo-&amp;gt;cinfo, COL __ INFO, &quot;%s(%d) &quot;, message_name, messageId); Wh...'''
date = "2013-05-17T00:01:00Z"
lastmod = "2013-05-17T00:17:00Z"
weight = 21205
keywords = [ "add", "col_append_str", "append" ]
aliases = [ "/questions/21205" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [col\_append\_fstr doesn't append. Why?](/questions/21205/col_append_fstr-doesnt-append-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21205-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all;</p><p>After the reassembling developments we've made in our dissector plugin, <strong>col__ append__ fstr</strong> doesn't work correctly anymore. It does not append, it works like <strong>col__ add__fstr</strong> and displays the last item only.</p><p>col <strong>append</strong> fstr(pinfo-&gt;cinfo, COL __ INFO, "%s(%d) ", message_name, messageId);</p><p>Why would it be?</p></div><div id="question-tags" class="tags-container tags">add col_append_str append</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/6a00de8bbb0f734aa577de7dd00b3e52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barisalis&#39;s gravatar image" /><p>barisalis<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barisalis has one accepted answer">100%</span></p></div></div><div id="comments-container-21205" class="comments-container"></div><div id="comment-tools-21205" class="comment-tools"></div><div class="clear"></div><div id="comment-21205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21207"></span>

<div id="answer-container-21207" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21207-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>After reassambling, pinfo does not contain the whole packet but contains the specific message only. That's the reason of the problem.</p><p>It's solved after calling the col _ clear function before tcp _ dissect _ pdus.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '13, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/6a00de8bbb0f734aa577de7dd00b3e52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barisalis&#39;s gravatar image" /><p>barisalis<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barisalis has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '13, 00:18</p></div></div><div id="comments-container-21207" class="comments-container"></div><div id="comment-tools-21207" class="comment-tools"></div><div class="clear"></div><div id="comment-21207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

