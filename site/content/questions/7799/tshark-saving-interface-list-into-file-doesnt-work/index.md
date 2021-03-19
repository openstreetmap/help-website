+++
type = "question"
title = "TShark saving interface list into file doesn&#x27;t work"
description = '''Hi, I have problem with tshark when I&#x27;m trying to save interface list into a file. I used comand: tshark.exe -D &amp;gt; file.txt and file was created but it is empty. In console I can see list of my interfaces. I&#x27;m using wireshark 1.6.4 and have this problem. On wireshark 1.4.2 all works fine. '''
date = "2011-12-06T05:02:00Z"
lastmod = "2011-12-06T06:54:00Z"
weight = 7799
keywords = [ "interface", "list", "tshark" ]
aliases = [ "/questions/7799" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TShark saving interface list into file doesn't work](/questions/7799/tshark-saving-interface-list-into-file-doesnt-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7799-score" class="post-score" title="current number of votes">0</div><span id="post-7799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have problem with tshark when I'm trying to save interface list into a file. I used comand: tshark.exe -D &gt; file.txt and file was created but it is empty. In console I can see list of my interfaces. I'm using wireshark 1.6.4 and have this problem. On wireshark 1.4.2 all works fine.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '11, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/0f471ce56209c86791725fd26a4f658e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maniek&#39;s gravatar image" /><p><span>Maniek</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maniek has no accepted answers">0%</span></p></div></div><div id="comments-container-7799" class="comments-container"></div><div id="comment-tools-7799" class="comment-tools"></div><div class="clear"></div><div id="comment-7799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7801"></span>

<div id="answer-container-7801" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7801-score" class="post-score" title="current number of votes">4</div><span id="post-7801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Maniek has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark outputs the interface info on the standard error stream (stderr). To redirect this to a file use the redirection operator "2&gt;", e.g. <code>tshark.exe -D 2&gt; file.txt</code>.</p><p>I have no idea if this changed after 1.4.2, but is the current situation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '11, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7801" class="comments-container"></div><div id="comment-tools-7801" class="comment-tools"></div><div class="clear"></div><div id="comment-7801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

