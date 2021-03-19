+++
type = "question"
title = "Run DumpCap without displaying anything to user."
description = '''I&#x27;m running Dumpcap on a machine at user login, but I would like for it to be hidden. Right now I&#x27;m able to get it running and logging like I need it to, however it pops up a window that the user can see (Capturing on &#x27;Interface Name&#x27; | File: x:&#92;path&#92;name.pcapng), and if they close that window the c...'''
date = "2016-03-30T08:22:00Z"
lastmod = "2016-03-30T11:11:00Z"
weight = 51292
keywords = [ "dumpcap" ]
aliases = [ "/questions/51292" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Run DumpCap without displaying anything to user.](/questions/51292/run-dumpcap-without-displaying-anything-to-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51292-score" class="post-score" title="current number of votes">0</div><span id="post-51292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Dumpcap on a machine at user login, but I would like for it to be hidden. Right now I'm able to get it running and logging like I need it to, however it pops up a window that the user can see (Capturing on 'Interface Name' | File: x:\path\name.pcapng), and if they close that window the capture stops. I would like to hide the window so that they cannot close it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '16, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/1683a1f35897718f4b06696938ca1961?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZekeTheSquirrel&#39;s gravatar image" /><p><span>ZekeTheSquirrel</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZekeTheSquirrel has no accepted answers">0%</span></p></div></div><div id="comments-container-51292" class="comments-container"></div><div id="comment-tools-51292" class="comment-tools"></div><div class="clear"></div><div id="comment-51292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51297"></span>

<div id="answer-container-51297" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51297-score" class="post-score" title="current number of votes">0</div><span id="post-51297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ZekeTheSquirrel has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look over at <a href="http://superuser.com/questions/140047/how-to-run-a-batch-file-without-launching-a-command-window">http://superuser.com/questions/140047/how-to-run-a-batch-file-without-launching-a-command-window</a></p><p>Basically, create 2 files:</p><p>1) <code>hidecmd.vbs</code> whose contents are, e.g.:</p><pre><code>&#39;HideBat.vbs
CreateObject(&quot;Wscript.Shell&quot;).Run &quot;your_batch_file.bat&quot;, 0, True</code></pre><p>(The top answer also works but this one was shorter/simpler. I did not test every solution provided.)</p><p>2) The <code>your_batch_file.bat</code> with the <code>dumpcap.exe</code> command and options that you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '16, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-51297" class="comments-container"><span id="51298"></span><div id="comment-51298" class="comment"><div id="post-51298-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I'd seen this before but I could not get it to work. I realized my problem was that the bat file was using start "...\dumpcap.exe", which still opened a new window.</p></div><div id="comment-51298-info" class="comment-info"><span class="comment-age">(30 Mar '16, 11:11)</span> <span class="comment-user userinfo">ZekeTheSquirrel</span></div></div></div><div id="comment-tools-51297" class="comment-tools"></div><div class="clear"></div><div id="comment-51297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

