+++
type = "question"
title = "error LNK2019"
description = '''hello guys, I just add a sub-menu in menu &#x27;statistics&#x27;, and I created a new file named &#x27;vss_dlg.c&#x27; and then copy some code from &#x27;summary_dlg.c&#x27; and filled into the &#x27;vss_dlg.c&#x27;, some related code also modified, but still some ERROR founded as below: libui.lib(vss_dlg.obj) : error LNK2019: unresolved ...'''
date = "2011-10-28T17:53:00Z"
lastmod = "2011-10-29T12:03:00Z"
weight = 7142
keywords = [ "lnk2019", "error" ]
aliases = [ "/questions/7142" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [error LNK2019](/questions/7142/error-lnk2019)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7142-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello guys,</p><p>I just add a sub-menu in menu 'statistics', and I created a new file named 'vss_dlg.c' and then copy some code from 'summary_dlg.c' and filled into the 'vss_dlg.c', some related code also modified, but still some ERROR founded as below:</p><p>libui.lib(vss_dlg.obj) : error LNK2019: unresolved external symbol _vss_fill_in_capture referenced in function _vss_open_cb</p><p>libui.lib(vss_dlg.obj) : error LNK2019: unresolved external symbol _vss_fill_in referenced in function _vss_open_cb</p><p>wireshark.exe : fatal error LNK1120: 2 unresolved externals</p><p>NMAKE : fatal error U1077: '"C:Program FilesMicrosoft Visual Studio 9.0VCBINlink.EXE"' : return code '0x460' Stop.</p><p>Who guys met this problem before?</p><p>Many thanks in advance!</p><p>Sam</p></div><div id="question-tags" class="tags-container tags">lnk2019 error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '11, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/e9d668dd28830dd8f79d4dbb56e5f2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam&#39;s gravatar image" /><p>Sam<br />
<span class="score" title="51 reputation points">51</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam has no accepted answers">0%</span></p></div></div><div id="comments-container-7142" class="comments-container"></div><div id="comment-tools-7142" class="comment-tools"></div><div class="clear"></div><div id="comment-7142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7148"></span>

<div id="answer-container-7148" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7148-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your changes have introduced the error but as you haven't really told us what your changes are we can't really help you.</p><p>However the explanation of the LNK2019 error is that a function is called, but there is no definition of the function in any object file fed to the linker.</p><p>In your case you are calling <code>vss_fill_in_capture</code> and <code>vss_open_cb</code> which are presumably new functions from your changes but there is no definition of these two functions in any of the object files fed to the linker when linking libui.lib.</p><p>See also the MSDN page for the error <a href="http://msdn.microsoft.com/en-us/library/799kze2z%28v=VS.90%29.aspx">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '11, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7148" class="comments-container"><span id="7164"></span><div id="comment-7164" class="comment"><div id="post-7164-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot, Grahamb.</p></div><div id="comment-7164-info" class="comment-info"><span class="comment-age">(30 Oct '11, 18:09)</span> Sam</div></div></div><div id="comment-tools-7148" class="comment-tools"></div><div class="clear"></div><div id="comment-7148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

