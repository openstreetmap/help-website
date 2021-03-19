+++
type = "question"
title = "How to change the main UI font?"
description = '''The default font looks bad on my system. It&#x27;s also showing Japanese yen symbols in place of slashes. I have no idea why - my locale has always been set to English (US). I tried changing the Font setting under Preferences, but that doesn&#x27;t affect the main window. Help please? Edit: I didn&#x27;t realize t...'''
date = "2014-04-28T13:48:00Z"
lastmod = "2014-04-30T02:46:00Z"
weight = 32269
keywords = [ "font" ]
aliases = [ "/questions/32269" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to change the main UI font?](/questions/32269/how-to-change-the-main-ui-font)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32269-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The default font looks bad on my system. It's also showing Japanese yen symbols in place of slashes. I have no idea why - my locale has always been set to English (US). I tried changing the Font setting under Preferences, but that doesn't affect the main window. Help please?</p><p>Edit: I didn't realize the picture wouldn't zoom in. Here's a cropped version: <img src="http://u.cubeupload.com/Mogster/Wireshark1.png" alt="Bad font is bad." /></p></div><div id="question-tags" class="tags-container tags">font</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/db018af2a6c85bb76956e0dcc96f17f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mogster&#39;s gravatar image" /><p>Mogster<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mogster has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 29 Apr '14, 14:43</p></div></div><div id="comments-container-32269" class="comments-container"></div><div id="comment-tools-32269" class="comment-tools"></div><div class="clear"></div><div id="comment-32269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32308"></span>

<div id="answer-container-32308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32308-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not the issue here. The recent capture list is sourced from the recent_common file located in your personal configuration folder.</p><p>What OS are you using? What happens when you create a new text document and type a backslash?</p><p>Double check all region and language settings of your OS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-32308" class="comments-container"><span id="32380"></span><div id="comment-32380" class="comment"><div id="post-32380-score" class="comment-score"></div><div class="comment-text"><p>I'm using Windows 7 Pro 64-bit. Both text documents and the recent_common file itself show backslashes, not yen symbols.</p></div><div id="comment-32380-info" class="comment-info"><span class="comment-age">(02 May '14, 00:20)</span> Mogster</div></div><span id="32800"></span><div id="comment-32800" class="comment"><div id="post-32800-score" class="comment-score"></div><div class="comment-text"><p>If you log in with another user do you have the same problem? Have you tried reinstalling Wireshark?</p></div><div id="comment-32800-info" class="comment-info"><span class="comment-age">(14 May '14, 09:46)</span> Roland</div></div><span id="32806"></span><div id="comment-32806" class="comment"><div id="post-32806-score" class="comment-score"></div><div class="comment-text"><p>Could you please file a bug for the "Yen symbols instead of backslashes" problem on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>? Wireshark internally should be using UTF-8 for pathnames on Windows (and on UN*Xes that are set up to use UTF-8), and GTK+ should be displaying them correctly; there might either be an issue with the font <em>or</em> with the Wireshark code, the GTK+ code, or the GLib code that does file name character encoding translations.</p></div><div id="comment-32806-info" class="comment-info"><span class="comment-age">(14 May '14, 15:16)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-32308" class="comment-tools"></div><div class="clear"></div><div id="comment-32308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

