+++
type = "question"
title = "Wireshark core dumped on capture start"
description = '''Hi everyone, I&#x27;ve been using wireshark for a long time and all went perfectly until a week ago I tried to sniff my network traffic and it crashed when I hit the start button. It does not matter what interface I pick, it always crashes when trying to capture packets. It seems like problems came along...'''
date = "2013-11-07T11:41:00Z"
lastmod = "2013-11-11T07:32:00Z"
weight = 26730
keywords = [ "core", "gtk", "error" ]
aliases = [ "/questions/26730" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark core dumped on capture start](/questions/26730/wireshark-core-dumped-on-capture-start)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26730-score" class="post-score" title="current number of votes">0</div><span id="post-26730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I've been using wireshark for a long time and all went perfectly until a week ago I tried to sniff my network traffic and it crashed when I hit the start button. It does not matter what interface I pick, it always crashes when trying to capture packets. It seems like problems came along with the new version (1.10). I do not remember what version I was using before (last time I used wireshark was one year ago or so). I tried falling back to 1.8 but it's even worse, it crashes on startup. Here it's the error reported in the command line:</p><p>Gtk:ERROR:/build/buildd/gtk+3.0-3.8.1+git20130422.0ce7854a/./gtk/gtkwidget.c:14133:gtk_widget_unregister_window: assertion failed: (user_data == widget)</p><p>[1]+ Aborted (`core' dumped) wireshark</p><p>OS: Ubuntu 12.10 x64<br />
Wireshark 1.10.3<br />
libpcap: 1.3.0</p><p>Edit: I tried to open a capture file in wireshark to try to isolate the problem. Wireshark also crashes when loading the "main packet analysis window"</p><p>Any help will be much appreciated. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-core" rel="tag" title="see questions tagged &#39;core&#39;">core</span> <span class="post-tag tag-link-gtk" rel="tag" title="see questions tagged &#39;gtk&#39;">gtk</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/7c27b60cc8d5b7df605576bd088502f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fernando98&#39;s gravatar image" /><p><span>fernando98</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fernando98 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '13, 10:59</strong> </span></p></div></div><div id="comments-container-26730" class="comments-container"><span id="26770"></span><div id="comment-26770" class="comment"><div id="post-26770-score" class="comment-score"></div><div class="comment-text"><p>OS, Wireshark and WinPCap versions please.</p></div><div id="comment-26770-info" class="comment-info"><span class="comment-age">(08 Nov '13, 04:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="26773"></span><div id="comment-26773" class="comment"><div id="post-26773-score" class="comment-score"></div><div class="comment-text"><blockquote><p>all went perfectly until a week ago</p></blockquote><p>what kind of software did you install during that week? Probably another tool/software that uses GTK+ ??</p></div><div id="comment-26773-info" class="comment-info"><span class="comment-age">(08 Nov '13, 04:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26775"></span><div id="comment-26775" class="comment"><div id="post-26775-score" class="comment-score"></div><div class="comment-text"><p>Also, as a first workaround measure you might want to delete all your Wireshark profile files to see if it starts up then. Best would be to backup them to a save location first, so if the profile is the problem it may be possible to determine from the backups what exactly the problem was.</p></div><div id="comment-26775-info" class="comment-info"><span class="comment-age">(08 Nov '13, 05:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="26782"></span><div id="comment-26782" class="comment"><div id="post-26782-score" class="comment-score"></div><div class="comment-text"><p>I am sorry if I did not explain myself correctly. I have been using wireshark for half a year or so, then I stopped using it for a year and when I went to use it again (last week) it crashed. The amount of software I have installed ever since is tremendous. I also tried removing ~/.wireshark but did not work.</p></div><div id="comment-26782-info" class="comment-info"><span class="comment-age">(08 Nov '13, 10:48)</span> <span class="comment-user userinfo">fernando98</span></div></div></div><div id="comment-tools-26730" class="comment-tools"></div><div class="clear"></div><div id="comment-26730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26842"></span>

<div id="answer-container-26842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26842-score" class="post-score" title="current number of votes">0</div><span id="post-26842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Gtk:ERROR:/build/buildd/gtk+3.0-3.8.1+git20130422.0ce7854a/./gtk/gtkwidget.c:14133:gtk_widget_unregister_window: assertion failed: (user_data == widget)</p></blockquote><p>There is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8604">a bug with that error message</a>, however it is marked as FIXED.</p><p>Can you please try to use a more recent (latest) version of Wireshark?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '13, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26842" class="comments-container"></div><div id="comment-tools-26842" class="comment-tools"></div><div class="clear"></div><div id="comment-26842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

