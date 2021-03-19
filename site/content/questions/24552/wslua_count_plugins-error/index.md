+++
type = "question"
title = "wslua_count_plugins error"
description = '''Hi, I am trying to compile from the SVN and everything has completed perfectly but when I try to run WireShark I get the following error: wireshark: symbol lookup error: wireshark: undefined symbol: wslua_count_plugin Has anyone encountered this at all?'''
date = "2013-09-11T02:49:00Z"
lastmod = "2013-09-11T06:16:00Z"
weight = 24552
keywords = [ "compile", "source", "errors" ]
aliases = [ "/questions/24552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wslua\_count\_plugins error](/questions/24552/wslua_count_plugins-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24552-score" class="post-score" title="current number of votes">0</div><span id="post-24552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to compile from the SVN and everything has completed perfectly but when I try to run WireShark I get the following error:</p><p>wireshark: symbol lookup error: wireshark: undefined symbol: wslua_count_plugin</p><p>Has anyone encountered this at all?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '13, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/bcc5516d6c36124de139f112f8657dd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmacuk&#39;s gravatar image" /><p><span>tmacuk</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmacuk has no accepted answers">0%</span></p></div></div><div id="comments-container-24552" class="comments-container"><span id="24556"></span><div id="comment-24556" class="comment"><div id="post-24556-score" class="comment-score"></div><div class="comment-text"><p>How are you running Wireshark, from the wireshark-gtk directory created during the build, or from an installed version using an installer that you've also built?</p></div><div id="comment-24556-info" class="comment-info"><span class="comment-age">(11 Sep '13, 03:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="24557"></span><div id="comment-24557" class="comment"><div id="post-24557-score" class="comment-score"></div><div class="comment-text"><p>I just typed Wireshark after doing a make install - I have no other build of Wireshark on my box</p></div><div id="comment-24557-info" class="comment-info"><span class="comment-age">(11 Sep '13, 04:02)</span> <span class="comment-user userinfo">tmacuk</span></div></div><span id="24564"></span><div id="comment-24564" class="comment"><div id="post-24564-score" class="comment-score"></div><div class="comment-text"><p>Ok, so you are running on some OS other than Windows then? What OS are you using?</p></div><div id="comment-24564-info" class="comment-info"><span class="comment-age">(11 Sep '13, 04:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="24565"></span><div id="comment-24565" class="comment"><div id="post-24565-score" class="comment-score"></div><div class="comment-text"><p>Ubuntu Linux 13.04</p></div><div id="comment-24565-info" class="comment-info"><span class="comment-age">(11 Sep '13, 05:09)</span> <span class="comment-user userinfo">tmacuk</span></div></div><span id="24566"></span><div id="comment-24566" class="comment"><div id="post-24566-score" class="comment-score">1</div><div class="comment-text"><p>And are you able to run from the build directory as described in the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcRunFirstTime.html#ChSrcRunFirstTimeUnix">Developers Guide Sect 3.6.1</a>?</p></div><div id="comment-24566-info" class="comment-info"><span class="comment-age">(11 Sep '13, 05:27)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-24552" class="comment-tools"></div><div class="clear"></div><div id="comment-24552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24570"></span>

<div id="answer-container-24570" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24570-score" class="post-score" title="current number of votes">0</div><span id="post-24570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That was the issue.</p><p>Run Wireshark with WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark and not just wireshark</p><p>Thanks for your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '13, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/bcc5516d6c36124de139f112f8657dd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmacuk&#39;s gravatar image" /><p><span>tmacuk</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmacuk has no accepted answers">0%</span></p></div></div><div id="comments-container-24570" class="comments-container"></div><div id="comment-tools-24570" class="comment-tools"></div><div class="clear"></div><div id="comment-24570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

