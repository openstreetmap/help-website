+++
type = "question"
title = "Unable to install / uninstall WireShark silently"
description = '''According to the documentation, running the installer with a &quot;/s&quot; will enable WireShark to be installed silently with the default settings. I&#x27;ve downloaded wireshark-win32-1.4.3.exe and have been unable to get the /s switch to work. After a manual install, I have tried a silent uninstall running &quot;un...'''
date = "2011-01-23T21:14:00Z"
lastmod = "2011-01-26T15:33:00Z"
weight = 1902
keywords = [ "wireshark", "unattended", "silent", "install", "uninstall" ]
aliases = [ "/questions/1902" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to install / uninstall WireShark silently](/questions/1902/unable-to-install-uninstall-wireshark-silently)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1902-score" class="post-score" title="current number of votes">0</div><span id="post-1902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to the documentation, running the installer with a "/s" will enable WireShark to be installed silently with the default settings.</p><p>I've downloaded wireshark-win32-1.4.3.exe and have been unable to get the /s switch to work.</p><p>After a manual install, I have tried a silent uninstall running "uninstall.exe /s". This does not work either.</p><p>Any help with the above?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-unattended" rel="tag" title="see questions tagged &#39;unattended&#39;">unattended</span> <span class="post-tag tag-link-silent" rel="tag" title="see questions tagged &#39;silent&#39;">silent</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '11, 21:14</strong></p><img src="https://secure.gravatar.com/avatar/b5f62b3bbd85e8c518056e13f2dbf9f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrish&#39;s gravatar image" /><p><span>chrish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrish has no accepted answers">0%</span></p></div></div><div id="comments-container-1902" class="comments-container"></div><div id="comment-tools-1902" class="comment-tools"></div><div class="clear"></div><div id="comment-1902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1932"></span>

<div id="answer-container-1932" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1932-score" class="post-score" title="current number of votes">1</div><span id="post-1932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chrish has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using <code>/s</code> or <code>/S</code>? NSIS (the system we use to create installation packages) makes a distinction between upper and lower case options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '11, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jan '11, 12:23</strong> </span></p></div></div><div id="comments-container-1932" class="comments-container"><span id="1960"></span><div id="comment-1960" class="comment"><div id="post-1960-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I didn't realise the switch was case sensitive. I have tried "/S" and it worked.</p></div><div id="comment-1960-info" class="comment-info"><span class="comment-age">(26 Jan '11, 15:33)</span> <span class="comment-user userinfo">chrish</span></div></div></div><div id="comment-tools-1932" class="comment-tools"></div><div class="clear"></div><div id="comment-1932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

