+++
type = "question"
title = "On windows xp, error of temporary file"
description = '''I have windows xp; I have this error;  The temporary file to which the capture would be saved (&quot;&quot;) could not be opened: No such file or directory. how to solve?'''
date = "2012-09-14T12:52:00Z"
lastmod = "2012-09-17T12:53:00Z"
weight = 14271
keywords = [ "windows", "temp", "error" ]
aliases = [ "/questions/14271" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [On windows xp, error of temporary file](/questions/14271/on-windows-xp-error-of-temporary-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14271-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have windows xp;</p><p>I have this error;</p><p>The temporary file to which the capture would be saved ("") could not be opened: No such file or directory.</p><p>how to solve?</p></div><div id="question-tags" class="tags-container tags">windows temp error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/a31c9569c633df80e1aa0282060798a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="albs&#39;s gravatar image" /><p>albs<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="albs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Sep '12, 12:53</p></div></div><div id="comments-container-14271" class="comments-container"></div><div id="comment-tools-14271" class="comment-tools"></div><div class="clear"></div><div id="comment-14271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14331"></span>

<div id="answer-container-14331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14331-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark writes a temp file while capturing (to be able to recover from crashes). The path for the TEMP directory is retrieved by reading some environment variables via the glib function g_get_tmp_dir().</p><blockquote><p><code>Cite: Gets the directory to use for temporary files. This is found from inspecting the environment variables TMPDIR, TMP, and TEMP. If none of those are defined "/tmp" is returned on UNIX and "C:\" on Windows.</code><br />
</p></blockquote><p>So, if you defined one of these variables with an empty string, you will get that error message.</p><p>Please check those variables:</p><blockquote><p><code>open a DOS box</code><br />
<code>Type 'set' and look for those three variables</code><br />
</p></blockquote><p>If you see something like the output below, you will get the error message (verified on WinXP).</p><blockquote><p><code>c:\&gt;set | find "TMP"</code><br />
<code>TMP=""</code><br />
<code>TMPDIR=""</code><br />
<code>c:\&gt;set | find "TEMP"</code><br />
<code>TEMP=""</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '12, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14331" class="comments-container"></div><div id="comment-tools-14331" class="comment-tools"></div><div class="clear"></div><div id="comment-14331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

