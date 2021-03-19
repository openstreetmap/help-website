+++
type = "question"
title = "how to close and save wireshark through cmd for task scheduler"
description = '''Hi, I would like to create a task that closes wireshark portable and saves the data automatically without any interaction from the user. What would my script look like ?  I appreciate everybody&#x27;s input. Thank You, Jake '''
date = "2017-02-28T12:57:00Z"
lastmod = "2017-03-01T13:40:00Z"
weight = 59743
keywords = [ "automation", "cmd-line" ]
aliases = [ "/questions/59743" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to close and save wireshark through cmd for task scheduler](/questions/59743/how-to-close-and-save-wireshark-through-cmd-for-task-scheduler)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59743-score" class="post-score" title="current number of votes">0</div><span id="post-59743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to create a task that closes wireshark portable and saves the data automatically without any interaction from the user.</p><p>What would my script look like ?</p><p>I appreciate everybody's input.</p><p>Thank You,</p><p>Jake</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-automation" rel="tag" title="see questions tagged &#39;automation&#39;">automation</span> <span class="post-tag tag-link-cmd-line" rel="tag" title="see questions tagged &#39;cmd-line&#39;">cmd-line</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/b75153854e7c7ef396a5f0405a7ce2f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DrunkenChinchila&#39;s gravatar image" /><p><span>DrunkenChinc...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DrunkenChinchila has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '17, 12:58</strong> </span></p></div></div><div id="comments-container-59743" class="comments-container"></div><div id="comment-tools-59743" class="comment-tools"></div><div class="clear"></div><div id="comment-59743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59785"></span>

<div id="answer-container-59785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59785-score" class="post-score" title="current number of votes">0</div><span id="post-59785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your question is very general. Your capture command is going to highly depend upon what you're trying to capture and for how long. Under what conditions should it stop?</p><p>In any case, you should probably be looking into using a command-line tool such as <code>dumpcap</code> instead of Wireshark. To help figure out your <code>dumpcap</code> command, I would suggest that you start by reading the <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap man page</a> or <a href="https://www.wireshark.org/docs/wsug_html_chunked/AppToolsdumpcap.html">dumpcap section of the Wireshark User Guide</a> for usage information and then determine which options best fit your capturing needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59785" class="comments-container"></div><div id="comment-tools-59785" class="comment-tools"></div><div class="clear"></div><div id="comment-59785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

