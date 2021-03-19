+++
type = "question"
title = "New file in Wireshark dissectors folder"
description = '''I want to add a new file that will enhance existing protocol - BACnet. The file will contain proprietary services analysis. When i add code, it does not get compiled. Which files do i need to modify to compile this file?'''
date = "2011-04-19T10:47:00Z"
lastmod = "2011-04-19T11:23:00Z"
weight = 3616
keywords = [ "new", "file" ]
aliases = [ "/questions/3616" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [New file in Wireshark dissectors folder](/questions/3616/new-file-in-wireshark-dissectors-folder)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3616-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to add a new file that will enhance existing protocol - BACnet. The file will contain proprietary services analysis. When i add code, it does not get compiled. Which files do i need to modify to compile this file?</p></div><div id="question-tags" class="tags-container tags">new file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p>dsprabhu4<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span></p></div></div><div id="comments-container-3616" class="comments-container"></div><div id="comment-tools-3616" class="comment-tools"></div><div class="clear"></div><div id="comment-3616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3618"></span>

<div id="answer-container-3618" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3618-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to add your files to lists in several locations under the source tree. You will need to make changes in all of the following files if you are compiling a plugin dissector, but you will not need all of them if you are building your dissector into Wireshark directly (obviously YMMV, but I successfully build plugins after changing these lists; paths are relative to the top of the source tree):</p><blockquote><ul><li>CMakeLists.txt (around line 360) [<strong>Built-in</strong>, <strong>Plugin</strong>]</li><li>configure.in (around line 1770) [<strong>Built-in</strong>, <strong>Plugin</strong>]</li><li>Makefile.am (around line 267 [<strong>Built-in</strong>, <strong>Plugin</strong>]</li><li>epan/Makefile.am (around line 190) [<strong>Built-in</strong>, <strong>Plugin</strong>]</li><li>plugins/Makefile.nmake (around line 15) [<strong>Plugin</strong>]</li><li>plugins/Makefile.am (around line 30) [<strong>Plugin</strong>]</li><li>packaging/nsis/Makefile.nmake (around line 48) [<strong>NSIS</strong>]</li><li>packaging/nsis/wireshark.nsi (around line 875) [<strong>NSIS</strong>]</li></ul></blockquote><p>Line numbers approximate; most of these are related to building a plugin or creating the Windows installer package, but you should be able to find where you need to make changes from this. Remember to check the <code>README.*</code> files under doc/ for your version specific needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '11, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '11, 12:58</p></div></div><div id="comments-container-3618" class="comments-container"><span id="3620"></span><div id="comment-3620" class="comment"><div id="post-3620-score" class="comment-score"></div><div class="comment-text"><p>I am not adding any new PlugIn. so i have modified only CMakeLists.txt. but still it does not compile the newly added file. as it does not create obj file. I saw other files mentioned here, but i do not think that i need to change. Am I missing something?</p></div><div id="comment-3620-info" class="comment-info"><span class="comment-age">(19 Apr '11, 12:51)</span> dsprabhu4</div></div><span id="3621"></span><div id="comment-3621" class="comment"><div id="post-3621-score" class="comment-score"></div><div class="comment-text"><p>@dsprabhu4 I've updated the list with what the edits are for. You will need to edit the files in the list marked <strong>Built-in</strong> to compile your dissectors.</p></div><div id="comment-3621-info" class="comment-info"><span class="comment-age">(19 Apr '11, 12:59)</span> multipleinte...</div></div><span id="3622"></span><div id="comment-3622" class="comment"><div id="post-3622-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I am able to compile.</p></div><div id="comment-3622-info" class="comment-info"><span class="comment-age">(19 Apr '11, 14:02)</span> dsprabhu4</div></div></div><div id="comment-tools-3618" class="comment-tools"></div><div class="clear"></div><div id="comment-3618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

