+++
type = "question"
title = "unable to build trunk Qt version without GTK+"
description = '''I&#x27;ve downloaded the latest package (wireshark-1.11.0-SVN-50460.tar.bz2) and after running ./configure I get the following output as last lines: checking for GTK+ - version &amp;gt;= 2.12.0 and &amp;lt; 3.0... no ** Could not run GTK+ test program, checking why... ** The test program failed to compile or lin...'''
date = "2013-07-09T07:03:00Z"
lastmod = "2013-07-09T09:58:00Z"
weight = 22762
keywords = [ "gtk", "build", "qt" ]
aliases = [ "/questions/22762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unable to build trunk Qt version without GTK+](/questions/22762/unable-to-build-trunk-qt-version-without-gtk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22762-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've downloaded the latest package (wireshark-1.11.0-SVN-50460.tar.bz2) and after running ./configure I get the following output as last lines:</p><pre><code>checking for GTK+ - version &gt;= 2.12.0 and &lt; 3.0... no
** Could not run GTK+ test program, checking why...
** The test program failed to compile or link. See the file config.log for the
** exact error that occured.
This usually means GTK+ is incorrectly installed.
configure: error: Neither Qt nor GTK+ 2.12.0 or later are available, so Wireshark can&#39;t be compiled</code></pre><p>I've installed Qt 5 through package ubuntu-sdk, I don't know which version of GTK+ I have or how to upgrade it (didn't found anything on the web)</p><p>Is GTK+ mandatory or is it possible to use Qt as suggested by the output?</p></div><div id="question-tags" class="tags-container tags">gtk build qt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/258b6e228a70fe84b9cb7df3b89c809b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ojay&#39;s gravatar image" /><p>ojay<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ojay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '13, 10:00</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22762" class="comments-container"></div><div id="comment-tools-22762" class="comment-tools"></div><div class="clear"></div><div id="comment-22762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22764"></span>

<div id="answer-container-22764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22764-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is possible but you have to specify <code>--without-gtk2</code> in addition to <code>--with-qt</code>. (This changed somewhat recently in the trunk.)</p><p>Do note that the Qt version is under development--you probably should only be using it if you are planning on developing it (adding code to Wireshark to expand this port).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '13, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-22764" class="comments-container"><span id="22766"></span><div id="comment-22766" class="comment"><div id="post-22766-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I got this output:</p><pre><code>checking for Qt - version &gt;= 4.6.0... Package QtCore was not found in the pkg-config search path.
Perhaps you should add the directory containing `QtCore.pc&#39;
to the PKG_CONFIG_PATH environment variable
No package &#39;QtCore&#39; found
Package QtGui was not found in the pkg-config search path.
Perhaps you should add the directory containing `QtGui.pc&#39;
to the PKG_CONFIG_PATH environment variable
No package &#39;QtGui&#39; found
Package QtCore was not found in the pkg-config search path.
Perhaps you should add the directory containing `QtCore.pc&#39;
to the PKG_CONFIG_PATH environment variable
No package &#39;QtCore&#39; found
Package QtGui was not found in the pkg-config search path.
Perhaps you should add the directory containing `QtGui.pc&#39;
to the PKG_CONFIG_PATH environment variable
No package &#39;QtGui&#39; found
Package QtCore was not found in the pkg-config search path.
Perhaps you should add the directory containing `QtCore.pc&#39;
to the PKG_CONFIG_PATH environment variable
No package &#39;QtCore&#39; found
Package QtGui was not found in the pkg-config search path.
Perhaps you should add the directory containing `QtGui.pc&#39;
to the PKG_CONFIG_PATH environment variable
No package &#39;QtGui&#39; found
no
configure: error: Qt is not available</code></pre><p>Do I also need to install package "qt-sdk"? I just checked and that didn't get installed with "ubuntu-sdk".<br />
Anyway, how can I use GTK? I have other applications installed that run on GTK without problems (Sublime Text, ghex). How can I solve this?</p></div><div id="comment-22766-info" class="comment-info"><span class="comment-age">(09 Jul '13, 13:43)</span> ojay</div></div><span id="22767"></span><div id="comment-22767" class="comment"><div id="post-22767-score" class="comment-score"></div><div class="comment-text"><p>How can you use GTK+? By installing the GTK+ development package (I don't know what it's called off hand, but look in the package manager for a package whose name contains "gtk" and "devel"), and configuring with <code>--with-gtk2</code> or <code>--with-gtk3</code>, depending on whether it's a package for GTK+ 2 or GTK+ 3.</p><p>How can you use Qt? By installing the Qt development package (see previous comment, but substitute "qt" for "gtk"), making sure that the directory containing Qt's .pc files is in your <code>PKG_CONFIG_PATH</code>, and configuring with <code>--with-qt</code>.</p></div><div id="comment-22767-info" class="comment-info"><span class="comment-age">(09 Jul '13, 13:48)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-22764" class="comment-tools"></div><div class="clear"></div><div id="comment-22764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

