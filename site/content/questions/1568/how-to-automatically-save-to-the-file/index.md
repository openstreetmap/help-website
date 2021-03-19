+++
type = "question"
title = "how to automatically save to the file?"
description = '''I want to save result to a file automatically when start a new capture, but I don&#x27;t want to set option each time, how i can do that?'''
date = "2011-01-01T02:50:00Z"
lastmod = "2011-01-25T04:53:00Z"
weight = 1568
keywords = [ "auto", "save" ]
aliases = [ "/questions/1568" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to automatically save to the file?](/questions/1568/how-to-automatically-save-to-the-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1568-score" class="post-score" title="current number of votes">0</div><span id="post-1568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to save result to a file automatically when start a new capture, but I don't want to set option each time, how i can do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-auto" rel="tag" title="see questions tagged &#39;auto&#39;">auto</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '11, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/b8b39dd5a7fa336493da43602f89b228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jackydi&#39;s gravatar image" /><p><span>jackydi</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jackydi has no accepted answers">0%</span></p></div></div><div id="comments-container-1568" class="comments-container"></div><div id="comment-tools-1568" class="comment-tools"></div><div class="clear"></div><div id="comment-1568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1571"></span>

<div id="answer-container-1571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1571-score" class="post-score" title="current number of votes">1</div><span id="post-1571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you drop out to a command line and do a "wireshark -h", it will give you all of the command line options.</p><p>For example:</p><p>wireshark -i 2 -k -b duration:20 -b filesize:100 -b files:10 -w paul.pcap</p><p>This sets the capture interface to interface 2 (-i 2), starts capturing immediatel (-k), sets a maximum file duration ring buffer option to 20 seconds (-b duration:20), a maximum ring buffer file size to 100KB (-b filesize:100), a maximum number of files saved to the last 10 (-b files:10), and an output basefile to paul.pcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1571" class="comments-container"><span id="1917"></span><div id="comment-1917" class="comment"><div id="post-1917-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer, I mean when I click the 'start' button, it automatically creates a new pcap file, the file name format is a fixed prefix + date and time,eg. log20110125081112.pcap. thank you.</p></div><div id="comment-1917-info" class="comment-info"><span class="comment-age">(25 Jan '11, 04:00)</span> <span class="comment-user userinfo">jackydi</span></div></div><span id="1920"></span><div id="comment-1920" class="comment"><div id="post-1920-score" class="comment-score"></div><div class="comment-text"><p>wireshark -i 2 -b duration:20 -b filesize:1000 -b files:10 -w log.pcap</p><p>You can try the above. I'm away from my computer.</p></div><div id="comment-1920-info" class="comment-info"><span class="comment-age">(25 Jan '11, 04:53)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div></div><div id="comment-tools-1571" class="comment-tools"></div><div class="clear"></div><div id="comment-1571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

