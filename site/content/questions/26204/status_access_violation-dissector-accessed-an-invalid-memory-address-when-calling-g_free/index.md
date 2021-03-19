+++
type = "question"
title = "STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address when calling g_free"
description = '''I have the following lines in a plugin dissector. The call to g_free below results in a &quot;STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address.&quot; Looking at the memory address of pchar1 it looks valid and holds a a short string string.  Looking deeper into get_CDR_octet_seq I can see ...'''
date = "2013-10-18T16:38:00Z"
lastmod = "2013-10-19T09:14:00Z"
weight = 26204
keywords = [ "dissector", "wmem", "plugin" ]
aliases = [ "/questions/26204" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [STATUS\_ACCESS\_VIOLATION: dissector accessed an invalid memory address when calling g\_free](/questions/26204/status_access_violation-dissector-accessed-an-invalid-memory-address-when-calling-g_free)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26204-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following lines in a plugin dissector. The call to g_free below results in a "STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address." Looking at the memory address of pchar1 it looks valid and holds a a short string string.<br />
</p><p>Looking deeper into get_CDR_octet_seq I can see that it allocates memory using ep_alloc_array0. However, the documentation of this function states "Caller of this function must remember to free the array pointed to by seq."</p><p>It looks like the code changed from 1.8 to 1.10. Should I file a bug report on the need for the code comments to change?</p><pre><code>gchar *pchar1=NULL;
gchar *pchar2=NULL;

get_CDR_octet_seq(tvb,&amp;pchar1,&amp;offset,4);
pchar2=make_printable_string(pchar1,4);
g_free(pchar1);</code></pre></div><div id="question-tags" class="tags-container tags">dissector wmem plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p>tlann<br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></p></div></div><div id="comments-container-26204" class="comments-container"></div><div id="comment-tools-26204" class="comment-tools"></div><div class="clear"></div><div id="comment-26204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26214"></span>

<div id="answer-container-26214" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26214-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are right the function was changed in revision <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=44498">4498</a> for bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3725">3725</a> but the comment was not updated accordingly.</p><p>I checked in updated comments in revision <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52690">52690</a> and in your code you just need to remove the g_free call (ephemeral memory will be automatically freed once the packet dissection is done).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '13, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-26214" class="comments-container"><span id="26219"></span><div id="comment-26219" class="comment"><div id="post-26219-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I kinda figured out I needed to remove g_free. ;-)</p></div><div id="comment-26219-info" class="comment-info"><span class="comment-age">(19 Oct '13, 15:22)</span> tlann</div></div></div><div id="comment-tools-26214" class="comment-tools"></div><div class="clear"></div><div id="comment-26214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

