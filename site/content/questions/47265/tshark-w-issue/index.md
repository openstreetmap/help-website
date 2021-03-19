+++
type = "question"
title = "tshark -w issue"
description = '''Hello, I&#x27;m trying to capture traffic on a port that&#x27;s pushing about 600Mbps and figured the command line with a duration and file limit would be easiest. When I use tshark -i 1 -a files:10 -b duration:2 -w test I get tshark: The file to which the capture would be saved (&quot;test&quot;) could not be opened: ...'''
date = "2015-11-04T14:41:00Z"
lastmod = "2015-11-04T18:41:00Z"
weight = 47265
keywords = [ "windows10", "tshark" ]
aliases = [ "/questions/47265" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -w issue](/questions/47265/tshark-w-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47265-score" class="post-score" title="current number of votes">0</div><span id="post-47265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to capture traffic on a port that's pushing about 600Mbps and figured the command line with a duration and file limit would be easiest. When I use</p><p>tshark -i 1 -a files:10 -b duration:2 -w test</p><p>I get</p><p>tshark: The file to which the capture would be saved ("test") could not be opened: No such file or directory.</p><p>Any suggestions? I'm pretty new to this so any help is appreciated.</p><p>Thanks, X</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows10" rel="tag" title="see questions tagged &#39;windows10&#39;">windows10</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '15, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/9fc5bdc2cee35f96c694e71d564ae9b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xero&#39;s gravatar image" /><p><span>Xero</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xero has no accepted answers">0%</span></p></div></div><div id="comments-container-47265" class="comments-container"></div><div id="comment-tools-47265" class="comment-tools"></div><div class="clear"></div><div id="comment-47265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47269"></span>

<div id="answer-container-47269" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47269-score" class="post-score" title="current number of votes">0</div><span id="post-47269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which directory are you running the command from? You must have write permission to that directory if you're to save files to it. If you don't, you could specify a fully-qualified path for the output filename to a directory that you do have write access to, and I'd also recommend appending a <code>.pcapng</code> extension to the test filename so that the file will be associated with Wireshark. I'd further recommend adding the Wireshark installation directory to your <code>PATH</code> environment variable and then simply running the command from a directory you do have permission to write to without having to specify long paths for either the <code>tshark</code> command or the output filename.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '15, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-47269" class="comments-container"><span id="47271"></span><div id="comment-47271" class="comment"><div id="post-47271-score" class="comment-score"></div><div class="comment-text"><p>I'd expect to get "Permission denied" rather than "No such file or directory" - <code>open({path}, O_CREAT|..., {mode})</code> shouldn't fail with ENOENT unless some directory leading up to the final component was missing, and, in this case, the path passed to <code>open()</code> should just be "test".</p><p>Something odd is going on here. (Perhaps all that's going on is "this is Windows", but there might be more to it.)</p></div><div id="comment-47271-info" class="comment-info"><span class="comment-age">(04 Nov '15, 18:41)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-47269" class="comment-tools"></div><div class="clear"></div><div id="comment-47269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

