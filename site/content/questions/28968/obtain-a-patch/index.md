+++
type = "question"
title = "Obtain a patch"
description = '''Hello I want to obtain this patch: https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4814 But I have no idea how to do this :/ Thanks in advance for your reply !'''
date = "2014-01-16T11:31:00Z"
lastmod = "2014-01-16T12:14:00Z"
weight = 28968
keywords = [ "patch" ]
aliases = [ "/questions/28968" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Obtain a patch](/questions/28968/obtain-a-patch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28968-score" class="post-score" title="current number of votes">0</div><span id="post-28968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I want to obtain this patch: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4814">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4814</a> But I have no idea how to do this :/</p><p>Thanks in advance for your reply !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-patch" rel="tag" title="see questions tagged &#39;patch&#39;">patch</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '14, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/77b726e03e08d01222297257457db129?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rofghl&#39;s gravatar image" /><p><span>Rofghl</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rofghl has no accepted answers">0%</span></p></div></div><div id="comments-container-28968" class="comments-container"></div><div id="comment-tools-28968" class="comment-tools"></div><div class="clear"></div><div id="comment-28968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28969"></span>

<div id="answer-container-28969" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28969-score" class="post-score" title="current number of votes">2</div><span id="post-28969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rofghl has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can download automated builds from <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a> . We're in the process of migrating from Subversion, which uses monotonically increasing revision numbers such as "43214", to Git, which uses commit hashes such as "62aef67". Automated version numbers currently use SVN notation but will use Git notation in the future.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-28969" class="comments-container"><span id="28970"></span><div id="comment-28970" class="comment"><div id="post-28970-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the sources but is the patch in automated builds ? I don't understand</p></div><div id="comment-28970-info" class="comment-info"><span class="comment-age">(16 Jan '14, 11:58)</span> <span class="comment-user userinfo">Rofghl</span></div></div><span id="28971"></span><div id="comment-28971" class="comment"><div id="post-28971-score" class="comment-score"></div><div class="comment-text"><p>In the context of bug 4814 (and in Wireshark development in general) "patch" means a change to the source code. Tyson and Chris attached several patches to the bug while working on the feature, such as this one: <a href="https://bugs.wireshark.org/bugzilla/attachment.cgi?id=6304">https://bugs.wireshark.org/bugzilla/attachment.cgi?id=6304</a></p><p>Chris then checked that change into the code repository in revision 37039. The automated build system then attempted to create packages stamped "SVN-37039".</p><p>We don't do binary patching. If you want to modify a Wireshark executable you either download a new installer package or recompile the whole thing.</p><p>In any case this particular bug is over 2.5 years old. This feature should be present in the official 1.10 and 1.8 releases.</p></div><div id="comment-28971-info" class="comment-info"><span class="comment-age">(16 Jan '14, 12:09)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div><span id="28973"></span><div id="comment-28973" class="comment"><div id="post-28973-score" class="comment-score"></div><div class="comment-text"><p>Ok I understand now Thank you :) I'm not sure that this feature is present in official release I'm going to check this</p></div><div id="comment-28973-info" class="comment-info"><span class="comment-age">(16 Jan '14, 12:14)</span> <span class="comment-user userinfo">Rofghl</span></div></div></div><div id="comment-tools-28969" class="comment-tools"></div><div class="clear"></div><div id="comment-28969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

