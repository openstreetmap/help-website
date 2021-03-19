+++
type = "question"
title = "segment capture into smaller files of 1/2 hour increments on windows 2008 server"
description = '''how can this be done? when i attempt to editcap -i, an error is returned stating &#x27;editcap&#x27; is not recognized as an internal or external command,operable program or batch file'''
date = "2012-10-10T08:47:00Z"
lastmod = "2012-10-10T08:58:00Z"
weight = 14898
keywords = [ "editcap" ]
aliases = [ "/questions/14898" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [segment capture into smaller files of 1/2 hour increments on windows 2008 server](/questions/14898/segment-capture-into-smaller-files-of-12-hour-increments-on-windows-2008-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14898-score" class="post-score" title="current number of votes">0</div><span id="post-14898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can this be done? when i attempt to editcap -i, an error is returned stating 'editcap' is not recognized as an internal or external command,operable program or batch file</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '12, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/f18a877cab20e318afe949737b9e2cc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allstreamtech&#39;s gravatar image" /><p><span>allstreamtech</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allstreamtech has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Oct '12, 08:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-14898" class="comments-container"></div><div id="comment-tools-14898" class="comment-tools"></div><div class="clear"></div><div id="comment-14898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14899"></span>

<div id="answer-container-14899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14899-score" class="post-score" title="current number of votes">0</div><span id="post-14899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is Windows command line 101. You may:</p><ul><li>Supply the full path to editcap.exe when invoking it, e.g. <code>C:\Program Files\Wireshark\editcap.exe</code> for 32 bit systems.</li><li>Run the command from the directory containing editcap.exe</li><li>Amend your path environment variable to include the directory including editcap.exe</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14899" class="comments-container"></div><div id="comment-tools-14899" class="comment-tools"></div><div class="clear"></div><div id="comment-14899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

