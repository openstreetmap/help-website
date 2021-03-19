+++
type = "question"
title = "Can&#x27;t build wireshark from source - ui_about_dialog.h:13:25: fatal error: QtGui/QAction: No such file or directory"
description = '''I have installed latest versions of both GTK3+ as well as Qt (v5.4.0 installed /opt folder). I would like to build Wireshark 1.12.3 for my Linux Mint box with the newer Qt interface. Running into nothing but trouble. Does&#x27;t help that I&#x27;m a newbie when it comes to troubleshooting build issues. When I...'''
date = "2015-01-19T12:36:00Z"
lastmod = "2015-01-19T12:39:00Z"
weight = 39295
keywords = [ "ui_about_dialog.h", "qt5", "qaction", "qt", "qtgui" ]
aliases = [ "/questions/39295" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't build wireshark from source - ui\_about\_dialog.h:13:25: fatal error: QtGui/QAction: No such file or directory](/questions/39295/cant-build-wireshark-from-source-ui_about_dialogh1325-fatal-error-qtguiqaction-no-such-file-or-directory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39295-score" class="post-score" title="current number of votes">0</div><span id="post-39295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed latest versions of both GTK3+ as well as Qt (v5.4.0 installed /opt folder). I would like to build Wireshark 1.12.3 for my Linux Mint box with the newer Qt interface. Running into nothing but trouble. Does't help that I'm a newbie when it comes to troubleshooting build issues.</p><p>When I run ./configure --with-qt=yes --with-gtk3=yes, it completes just fine. When I follow up with a 'make' it fails with the following error:</p><p>make[2]: Entering directory <code>/home/marlon/Downloads/wireshark-1.12.3/ui/qt'   CXX      about_dialog.o In file included from about_dialog.cpp:25:0: ui_about_dialog.h:13:25: fatal error: QtGui/QAction: No such file or directory  #include &lt;QtGui/QAction&gt;                          ^ compilation terminated. make[2]: *** [about_dialog.o] Error 1 make[2]: Leaving directory</code>/home/User/Downloads/wireshark-1.12.3/ui/qt' make[1]: <strong><em>[all-recursive] Error 1 make[1]: Leaving directory `/home/User/Downloads/wireshark-1.12.3' make:</em></strong> [all] Error 2</p><p>Anyone know how to resolve this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ui_about_dialog.h" rel="tag" title="see questions tagged &#39;ui_about_dialog.h&#39;">ui_about_dialog.h</span> <span class="post-tag tag-link-qt5" rel="tag" title="see questions tagged &#39;qt5&#39;">qt5</span> <span class="post-tag tag-link-qaction" rel="tag" title="see questions tagged &#39;qaction&#39;">qaction</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span> <span class="post-tag tag-link-qtgui" rel="tag" title="see questions tagged &#39;qtgui&#39;">qtgui</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '15, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/e9b28f3a68d2709d5233cdcc740b2209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iThrive&#39;s gravatar image" /><p><span>iThrive</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iThrive has no accepted answers">0%</span></p></div></div><div id="comments-container-39295" class="comments-container"></div><div id="comment-tools-39295" class="comment-tools"></div><div class="clear"></div><div id="comment-39295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39296"></span>

<div id="answer-container-39296" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39296-score" class="post-score" title="current number of votes">0</div><span id="post-39296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Qt support in 1.12.X version is very partial (lacks many features, has many bugs, ...) and not maintained (all the Qt work happens in 1.99.X versions). If you really want so play with Qt GUI, I highly suggest you to checkout the latest code from Git (see <a href="https://www.wireshark.org/develop.html)">https://www.wireshark.org/develop.html)</a> and compile this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '15, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39296" class="comments-container"></div><div id="comment-tools-39296" class="comment-tools"></div><div class="clear"></div><div id="comment-39296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

