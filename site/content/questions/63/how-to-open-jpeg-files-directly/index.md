+++
type = "question"
title = "How to open JPEG files directly?"
description = '''Hi All, I read in the relnotes from version 1.4.0 http://www.wireshark.org/docs/relnotes/wireshark-1.4.0.html .... You can open JPEG files directly in Wireshark I opened in a browser http://www.linuxmigration.com/quickref/admin/images/wireshark_capture.jpg and Wireshark runs. With image-jfif i could...'''
date = "2010-09-14T09:42:00Z"
lastmod = "2010-09-14T10:04:00Z"
weight = 63
keywords = [ "file-format", "jpeg", "wireshark" ]
aliases = [ "/questions/63" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to open JPEG files directly?](/questions/63/how-to-open-jpeg-files-directly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I read in the relnotes from version 1.4.0</p><p>http://www.wireshark.org/docs/relnotes/wireshark-1.4.0.html</p><p>.... You can open JPEG files directly in Wireshark</p><p>I opened in a browser http://www.linuxmigration.com/quickref/admin/images/wireshark_capture.jpg and Wireshark runs. With image-jfif i could filter it. But how can i open it directly? The only what i still coild do is follow tcp stream and then save it raw</p><p>Regards</p></div><div id="question-tags" class="tags-container tags">file-format jpeg wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '10, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/17772e652ae4538f6d6f9d1027673772?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark&#39;s gravatar image" /><p>wireshark<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Sep '10, 10:05</p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-63" class="comments-container"></div><div id="comment-tools-63" class="comment-tools"></div><div class="clear"></div><div id="comment-63-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64"></span>

<div id="answer-container-64" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Open JPEG files directly" means that you can open them via <em>File→Open</em>. Wireshark will display the JPEG file as a single "packet". You can open and analyze MP3 files in the same way.</p><p>If you want to export a JPEG you've captured in an HTTP session you can use <em>File→Export→Objects→HTTP</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '10, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-64" class="comments-container"><span id="129"></span><div id="comment-129" class="comment"><div id="post-129-score" class="comment-score">2</div><div class="comment-text"><p>Note that "Open JPEG files" means that Wireshark will dissect the JPEG file, not that it'll display it as an image. Wireshark currently includes no code to hand the contents of, for example, an HTTP GET reply to something that can display it in its native format, e.g. displaying a JPEG or GIF or PNG or... as an image. To do that, you'd need to export it, as per Gerald's instructions.</p></div><div id="comment-129-info" class="comment-info"><span class="comment-age">(15 Sep '10, 17:11)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-64" class="comment-tools"></div><div class="clear"></div><div id="comment-64-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

