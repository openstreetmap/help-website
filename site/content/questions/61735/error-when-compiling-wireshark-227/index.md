+++
type = "question"
title = "Error when compiling Wireshark 2.2.7"
description = '''Have not had this issue with any previous versions and now when compiling from source on CentOS 7.3 I receive this error: simple_dialog.cpp: In constructor ‘SimpleDialog::SimpleDialog(QWidget, ESD_TYPE_E, int, const char, __va_list_tag*)’: simple_dialog.cpp:93:54: error: ‘setTextInteractionFlags’ wa...'''
date = "2017-06-01T17:00:00Z"
lastmod = "2017-06-02T04:25:00Z"
weight = 61735
keywords = [ "compile" ]
aliases = [ "/questions/61735" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Error when compiling Wireshark 2.2.7](/questions/61735/error-when-compiling-wireshark-227)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61735-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have not had this issue with any previous versions and now when compiling from source on CentOS 7.3 I receive this error:</p><p>simple_dialog.cpp: In constructor ‘SimpleDialog::SimpleDialog(QWidget<em>, ESD_TYPE_E, int, const char</em>, __va_list_tag*)’: simple_dialog.cpp:93:54: error: ‘setTextInteractionFlags’ was not declared in this scope setTextInteractionFlags(Qt::TextSelectableByMouse); ^ make[2]: <strong><em>[simple_dialog.o] Error 1 make[2]: Leaving directory <code>/tmp/wireshark-2.2.7/ui/qt' make[1]: *** [all-recursive] Error 1 make[1]: Leaving directory</code>/tmp/wireshark-2.2.7' make:</em></strong> [all] Error 2</p><p>Any idea what the problem may be?</p></div><div id="question-tags" class="tags-container tags">compile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '17, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/aee16a16bd124554cc92fe6b60c103a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Danny%20Michael&#39;s gravatar image" /><p>Danny Michael<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Danny Michael has no accepted answers">0%</span></p></div></div><div id="comments-container-61735" class="comments-container"><span id="61737"></span><div id="comment-61737" class="comment"><div id="post-61737-score" class="comment-score"></div><div class="comment-text"><p>It's a QT thing. I compiled using --without-qt and it works fine.</p></div><div id="comment-61737-info" class="comment-info"><span class="comment-age">(01 Jun '17, 17:23)</span> Danny Michael</div></div><span id="61741"></span><div id="comment-61741" class="comment"><div id="post-61741-score" class="comment-score">1</div><div class="comment-text"><p>What version of Qt comes with CentOS 7.3? Perhaps Wireshark assumes a later version.</p><p>Was this built using autotools (running the configure script and doing make) or with CMake (running the cmake command and doing make)?</p></div><div id="comment-61741-info" class="comment-info"><span class="comment-age">(01 Jun '17, 21:47)</span> Guy Harris ♦♦</div></div><span id="61750"></span><div id="comment-61750" class="comment"><div id="post-61750-score" class="comment-score"></div><div class="comment-text"><p>It was run with autotools. It seems Pascal has found the solution. Thank you both for your input.</p></div><div id="comment-61750-info" class="comment-info"><span class="comment-age">(02 Jun '17, 06:11)</span> Danny Michael</div></div></div><div id="comment-tools-61735" class="comment-tools"></div><div class="clear"></div><div id="comment-61735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61747"></span>

<div id="answer-container-61747" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61747-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See also <a href="https://www.wireshark.org/lists/wireshark-dev/201706/msg00015.html">https://www.wireshark.org/lists/wireshark-dev/201706/msg00015.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '17, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-61747" class="comments-container"></div><div id="comment-tools-61747" class="comment-tools"></div><div class="clear"></div><div id="comment-61747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

