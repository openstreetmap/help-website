+++
type = "question"
title = "Why does file sets require an already saved arbitrary file for it to work ?"
description = '''Under capture options, I have to browse for a valid saved arbitrary Wireshark file under &quot;browse&quot; for file sets to work. If I manually enter the file title for instance, setTest01 , file sets wouldn&#x27;t work even after setting the proper conditions like &quot; Next file every 1 min &quot; etc. Confused. Guidanc...'''
date = "2013-03-25T21:08:00Z"
lastmod = "2013-03-25T22:44:00Z"
weight = 19825
keywords = [ "fileset" ]
aliases = [ "/questions/19825" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does file sets require an already saved arbitrary file for it to work ?](/questions/19825/why-does-file-sets-require-an-already-saved-arbitrary-file-for-it-to-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19825-score" class="post-score" title="current number of votes">0</div><span id="post-19825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Under capture options, I have to browse for a valid saved arbitrary Wireshark file under "browse" for file sets to work.</p><p>If I manually enter the file title for instance, setTest01 , file sets wouldn't work even after setting the proper conditions like " Next file every 1 min " etc.</p><p>Confused. Guidance is appreciated :) .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fileset" rel="tag" title="see questions tagged &#39;fileset&#39;">fileset</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '13, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/9b52984d9786885d47fe81e43d8591ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinged&#39;s gravatar image" /><p><span>Dinged</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinged has no accepted answers">0%</span></p></div></div><div id="comments-container-19825" class="comments-container"></div><div id="comment-tools-19825" class="comment-tools"></div><div class="clear"></div><div id="comment-19825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19826"></span>

<div id="answer-container-19826" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19826-score" class="post-score" title="current number of votes">3</div><span id="post-19826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dinged has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you simply enter a file name in the "File" field of the Capture Options dialog, your file set will be saved in the Wireshark program directory (C:\Program Files\Wireshark on a Windows PC), which is probably not what you want.</p><p>The Browse button is there so that you can select the <em>location</em> where you want your file set stored, not for you to browse to a file. After you click Browse, navigate to the directory where you want to save your file set using the left pane, then at the top, type the base file name that you want in the "Name" field, then click OK. You'll see your file name, including the path, in the "File" field of the Capture Options dialog.</p><p>So, if I click Browse, select Desktop on the left, type "capture.pcapng" in the Name field at the top, and click OK, I'll see "C:\Users\Owner\Desktop\capture.pcapng" in the File field of the Capture Options dialog and my file set will be saved on my Windows desktop.</p><p>Even though you will see files listed in the right pane as you're browsing, just specify the desired file name by manually typing it into the "Name" field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 22:04</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19826" class="comments-container"><span id="19828"></span><div id="comment-19828" class="comment"><div id="post-19828-score" class="comment-score"></div><div class="comment-text"><p>Thanks a great deal. Your explanation is very concise and clear :)</p></div><div id="comment-19828-info" class="comment-info"><span class="comment-age">(25 Mar '13, 22:44)</span> <span class="comment-user userinfo">Dinged</span></div></div></div><div id="comment-tools-19826" class="comment-tools"></div><div class="clear"></div><div id="comment-19826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

