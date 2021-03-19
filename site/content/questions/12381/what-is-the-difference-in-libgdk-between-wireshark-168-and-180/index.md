+++
type = "question"
title = "What is the difference in LIBGDK between Wireshark 1.6.8 and 1.8.0?"
description = '''What is the difference in libgdk-win32-2.0-0.dll between Wireshark 1.6.8 and 1.8.0? Both libraries have the same version 2.24.10.0, but they have different sizes from each other.  Wireshark 1.8.0: 680,068 bytes Wireshark 1.6.8: 932,373 bytes  In my environment, 1.8.0 has a little problem, but It wor...'''
date = "2012-07-02T19:31:00Z"
lastmod = "2012-07-06T10:47:00Z"
weight = 12381
keywords = [ "windows", "libgdk" ]
aliases = [ "/questions/12381" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the difference in LIBGDK between Wireshark 1.6.8 and 1.8.0?](/questions/12381/what-is-the-difference-in-libgdk-between-wireshark-168-and-180)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12381-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the difference in libgdk-win32-2.0-0.dll between Wireshark 1.6.8 and 1.8.0? Both libraries have the same version 2.24.10.0, but they have different sizes from each other.</p><ul><li><strong>Wireshark 1.8.0:</strong> 680,068 bytes</li><li><strong>Wireshark 1.6.8:</strong> 932,373 bytes</li></ul><p>In my environment, 1.8.0 has a little problem, but It works fine when I replace the dll which is included in Wireshark 1.6.8.</p><p>I'll try to compile GTK+ myself to see if I can determine the difference.</p></div><div id="question-tags" class="tags-container tags">windows libgdk</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '12, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/d236e633e60ac995b4a8f28d0575ba7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BlackWingCat&#39;s gravatar image" /><p>BlackWingCat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BlackWingCat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jul '12, 22:31</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-12381" class="comments-container"><span id="12383"></span><div id="comment-12383" class="comment"><div id="post-12383-score" class="comment-score"></div><div class="comment-text"><p>I don't know what the difference is, but ISTR that the actual build being used has changed. (I do note that the sizes of many (all ?) of the GLib/GTk stuff are different).</p><p>Please file a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a> with specific details about the "little problem" which shows up in 1.8.0 with the 1.8.0 libgdk DLL and doesn't show up using the libgdk DLL from 1.6.8</p></div><div id="comment-12383-info" class="comment-info"><span class="comment-age">(02 Jul '12, 21:17)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-12381" class="comment-tools"></div><div class="clear"></div><div id="comment-12381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12488"></span>

<div id="answer-container-12488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12488-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is this for 32-bit or 64-bit Windows? I'm assuming 32-bit since the file sizes you provided match that platform. The GLib and GTK+ DLLs in the 1.6.8 32-bit Windows installer come from <a href="http://ftp.gnome.org/pub/GNOME/binaries/win32/gtk+/2.24/">ftp.gnome.org</a>. Unfortunately the GNOME project stopped releasing updated bundles for 64-bit Windows in 2010 and haven't resumed. In order to ensure that the 32- and 64-bit installers match each other as closely as possible we now create bundles from packages built by the <a href="https://build.opensuse.org/project/show?project=windows%3Amingw%3Awin32">openSUSE Build Service</a>. The 1.8.0 32-bit installer ships with OBS-built DLLs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '12, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-12488" class="comments-container"></div><div id="comment-tools-12488" class="comment-tools"></div><div class="clear"></div><div id="comment-12488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

