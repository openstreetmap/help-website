+++
type = "question"
title = "[closed] Why gtk/gtk.h cannot be included into any header file?"
description = '''Hello, I have tried to include gtk/gtk.h into main_filter_toolbar.h but this is resulting in an error saying Cannot include file gtk/gtk.h. No such file or directory. How can i solve this problem? '''
date = "2011-10-27T01:02:00Z"
lastmod = "2011-10-28T02:21:00Z"
weight = 7089
keywords = [ "gtk" ]
aliases = [ "/questions/7089" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Why gtk/gtk.h cannot be included into any header file?](/questions/7089/why-gtkgtkh-cannot-be-included-into-any-header-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7089-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have tried to include gtk/gtk.h into main_filter_toolbar.h but this is resulting in an error saying <code>Cannot include file gtk/gtk.h. No such file or directory.</code> How can i solve this problem?</p></div><div id="question-tags" class="tags-container tags">gtk</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '11, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 30 Oct '11, 23:22</p></div></div><div id="comments-container-7089" class="comments-container"><span id="7122"></span><div id="comment-7122" class="comment"><div id="post-7122-score" class="comment-score"></div><div class="comment-text"><p>Could you compile Wireshark source before you made any changes to it?</p><p>On what operating system are you trying to compile Wireshark?</p><p>If it's a Linux distribution, what packages are installed for GTK+, and have you installed a GTK+ <em>developer</em> package?</p></div><div id="comment-7122-info" class="comment-info"><span class="comment-age">(27 Oct '11, 18:51)</span> Guy Harris ♦♦</div></div><span id="7123"></span><div id="comment-7123" class="comment"><div id="post-7123-score" class="comment-score"></div><div class="comment-text"><p>Yes i can compile it well. Mine is Windows xp. I use CYGWIN. Actually, in our wireshark sources, there is no gtk/gtk.h file at all. But all the gtk's .c extension files can include them well. When it comes to header files, it's resulting as the above given error.</p></div><div id="comment-7123-info" class="comment-info"><span class="comment-age">(27 Oct '11, 21:40)</span> Terrestrial ...</div></div></div><div id="comment-tools-7089" class="comment-tools"></div><div class="clear"></div><div id="comment-7089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Terrestrial shark 30 Oct '11, 23:22

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7133"></span>

<div id="answer-container-7133" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7133-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is correct, there is no <code>gtk/gtk.h</code> file in Wireshark, just as there isn't a <code>stdio.h</code> file in Wireshark, even though both of them are included by files in Wireshark. <code>stdio.h</code> is part of the C support library (comes with the OS on UN*X, comes with, I think, the MSVC compiler on Windows). <code>gtk/gtk.h</code> is part of the GTK+ library, and is included by several other header files in the<code>gtk</code> directory; I suggest that if you need to include <code>gtk/gtk.h</code> in <code>main_filter_toolbar.h</code>, you do so the same way it's done in the header files in the <code>gtk</code> directory that already include it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '11, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7133" class="comments-container"></div><div id="comment-tools-7133" class="comment-tools"></div><div class="clear"></div><div id="comment-7133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

