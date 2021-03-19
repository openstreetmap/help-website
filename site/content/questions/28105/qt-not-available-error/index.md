+++
type = "question"
title = "Qt not available error?"
description = '''This might be a dumb question since no one asked before. I used git to clone the code base. And I am on Mac, so I run macosx-setup script to setup the environment. Everything went OK except there is a CURL error with libsmi. I found that it&#x27;s an optional package so I commented out this line and inst...'''
date = "2013-12-14T10:56:00Z"
lastmod = "2013-12-15T13:00:00Z"
weight = 28105
keywords = [ "compile", "qt" ]
aliases = [ "/questions/28105" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Qt not available error?](/questions/28105/qt-not-available-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28105-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This might be a dumb question since no one asked before.<br />
I used git to clone the code base. And I am on Mac, so I run macosx-setup script to setup the environment. Everything went OK except there is a CURL error with libsmi. I found that it's an optional package so I commented out this line and installed libsmi with 'port install libsmi'. Then I tried to configure, it gives me this message:<br />
<code>checking for Qt5Core - version &gt;= 4.6.0... no checking for QtCore - version &gt;= 4.6.0... no configure: error: Qt is not available</code><br />
I can see qt5.2 is in the macosx-support-libs directory after setting up the environment, is there any extra steps I missed?</p></div><div id="question-tags" class="tags-container tags">compile qt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '13, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/39442a32c6ceb159821eeb2123154ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jacul&#39;s gravatar image" /><p>Jacul<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jacul has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-28105" class="comments-container"></div><div id="comment-tools-28105" class="comment-tools"></div><div class="clear"></div><div id="comment-28105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28129"></span>

<div id="answer-container-28129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28129-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What does</p><pre><code>pkg-config --libs --cflags Qt5Core</code></pre><p>return? You might need to make sure <code>/path/to/Qt5.2/clang_64/lib/pkgconfig</code> is in <code>PKG_CONFIG_PATH</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span> </br></p></div></div><div id="comments-container-28129" class="comments-container"><span id="28132"></span><div id="comment-28132" class="comment"><div id="post-28132-score" class="comment-score"></div><div class="comment-text"><p>Thanks. It says QT5 is not included in the path. I exported the path of Qt5Core.pc to the PKG_CONFIG_PATH, now it passes. Now I have one other question, Qt5 should be already downloaded and ready to use, but it doesn't seem like that. Is there any other steps I am missing, say including some path in the environmental variable? Because I am now missing GTK+3 and I think potentially there are more.</p></div><div id="comment-28132-info" class="comment-info"><span class="comment-age">(15 Dec '13, 13:23)</span> Jacul</div></div></div><div id="comment-tools-28129" class="comment-tools"></div><div class="clear"></div><div id="comment-28129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

