+++
type = "question"
title = "QT Language settings in Dev version"
description = '''Hi all When I compile a new version of Wireshark 2.0 from the github repo, the cancel and help buttons are displayed with the text below - as abort and help in German.  My settings are Windows 7 x64, with regional settings set to New Zealand. Same thing seems to occur with region set to australia - ...'''
date = "2016-02-02T16:33:00Z"
lastmod = "2016-02-02T16:44:00Z"
weight = 49750
keywords = [ "development", "wireshark-2.0", "qt" ]
aliases = [ "/questions/49750" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [QT Language settings in Dev version](/questions/49750/qt-language-settings-in-dev-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49750-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all When I compile a new version of Wireshark 2.0 from the github repo, the cancel and help buttons are displayed with the text below - as abort and help in German. My settings are Windows 7 x64, with regional settings set to New Zealand. Same thing seems to occur with region set to australia - but nothing I do to try and override this seems to work.</p><p>I've checked the translation files, and what I understand from the QT manual, it does suggest that the button text should be displayed, but for whatever reason it's just choosing the wrong string all the time. Any ideas? <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_XDA_story_TEST.pcapng_2016-02-03_11-20-55.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">development wireshark-2.0 qt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></img></div></div><div id="comments-container-49750" class="comments-container"></div><div id="comment-tools-49750" class="comment-tools"></div><div class="clear"></div><div id="comment-49750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49751"></span>

<div id="answer-container-49751" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49751-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you compiling with Qt 5.5.1? If so it looks like you've run into <a href="https://bugreports.qt.io/browse/QTBUG-48946">QTBUG-48946</a> / <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11619">Wireshark bug 11619</a>. The problem should be fixed in 5.5.2. The official Windows installers are built with 5.3.2, but we will likely upgrade to 5.5.2 when it's released.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '16, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-49751" class="comments-container"><span id="49752"></span><div id="comment-49752" class="comment"><div id="post-49752-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gerald - no idea why my prior search didn't come up with the existing bug!</p></div><div id="comment-49752-info" class="comment-info"><span class="comment-age">(02 Feb '16, 18:43)</span> Scott Harman</div></div></div><div id="comment-tools-49751" class="comment-tools"></div><div class="clear"></div><div id="comment-49751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

