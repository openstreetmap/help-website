+++
type = "question"
title = "Error attempting to capture to files using tshark"
description = '''First, the system: Ubuntu server 16.04, up to date as of today tshark 22.02 installed from repositories If I run tshark, I see the text capture messages scrolling on the screen, so I know I am seeing data coming into the capture PC. When I attempt to capture to a filename, I see the data being writt...'''
date = "2016-08-08T08:37:00Z"
lastmod = "2016-08-08T08:48:00Z"
weight = 54667
keywords = [ "tshark", "ringbuffer" ]
aliases = [ "/questions/54667" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error attempting to capture to files using tshark](/questions/54667/error-attempting-to-capture-to-files-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54667-score" class="post-score" title="current number of votes">0</div><span id="post-54667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First, the system: Ubuntu server 16.04, up to date as of today tshark 22.02 installed from repositories</p><p>If I run tshark, I see the text capture messages scrolling on the screen, so I know I am seeing data coming into the capture PC.</p><p>When I attempt to capture to a filename, I see the data being written to the file.</p><p>When I attempt to capture using a ring buffer of 5 files, each 1024k, I receive the following error:</p><p><em>tshark: Maximum capture file size specified, but capture isn't being saved to a file.</em></p><p>The command I am using is:</p><p><em>tshark -b filesize:1024 files:5 -w outfile.pcapng</em></p><p>I have also tried with no file extension and using pcap as the extension.</p><p>My overall goal is to have this machine installed in a remote location, headless, where I can access it via SSH to do the captures, then retrieve the files using SFTP and analyze them on my own machine. I am performing all of the above over SSH already, the only part not working is the ring buffer, which is critical for this application.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-ringbuffer" rel="tag" title="see questions tagged &#39;ringbuffer&#39;">ringbuffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '16, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/e68b935030441ccc0722f4d634057b9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rtstarliper&#39;s gravatar image" /><p><span>rtstarliper</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rtstarliper has no accepted answers">0%</span></p></div></div><div id="comments-container-54667" class="comments-container"></div><div id="comment-tools-54667" class="comment-tools"></div><div class="clear"></div><div id="comment-54667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54668"></span>

<div id="answer-container-54668" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54668-score" class="post-score" title="current number of votes">0</div><span id="post-54668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rtstarliper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you need to repeat the "-b" parameter for each ring buffer setting. In your case:</p><p>tshark -b filesize:1024 -b files:5 -w outfile.pcapng</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '16, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54668" class="comments-container"><span id="54669"></span><div id="comment-54669" class="comment"><div id="post-54669-score" class="comment-score"></div><div class="comment-text"><p>That appears to have done the trick. Running a test now to make sure I get multiple capture files before I ship this box out. Thanks.</p></div><div id="comment-54669-info" class="comment-info"><span class="comment-age">(08 Aug '16, 08:48)</span> <span class="comment-user userinfo">rtstarliper</span></div></div></div><div id="comment-tools-54668" class="comment-tools"></div><div class="clear"></div><div id="comment-54668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

