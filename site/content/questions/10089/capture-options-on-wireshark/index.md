+++
type = "question"
title = "Capture Options on wireshark"
description = '''Based on what i read from a forum : http://ask.wireshark.org/questions/1709/automatically-start-capturing-packets-when-bandwidth-is-high Ninjadude101 wants to capture log events that contains DoS attack from WireShark. hansangb told him to open the capture options (CTRL-K) I don&#x27;t understand and how...'''
date = "2012-04-12T02:48:00Z"
lastmod = "2012-04-13T02:17:00Z"
weight = 10089
keywords = [ "capture" ]
aliases = [ "/questions/10089" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Options on wireshark](/questions/10089/capture-options-on-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10089-score" class="post-score" title="current number of votes">0</div><span id="post-10089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Based on what i read from a forum : <a href="http://ask.wireshark.org/questions/1709/automatically-start-capturing-packets-when-bandwidth-is-high">http://ask.wireshark.org/questions/1709/automatically-start-capturing-packets-when-bandwidth-is-high</a></p><p>Ninjadude101 wants to capture log events that contains DoS attack from WireShark.</p><p>hansangb told him to open the capture options (CTRL-K)</p><p>I don't understand and how to go to the capture options on wireshark??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '12, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p><span>misteryuku</span><br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div></div><div id="comments-container-10089" class="comments-container"></div><div id="comment-tools-10089" class="comment-tools"></div><div class="clear"></div><div id="comment-10089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10090"></span>

<div id="answer-container-10090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10090-score" class="post-score" title="current number of votes">0</div><span id="post-10090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to start reading the very fine manual, as seen <a href="http://www.wireshark.org/docs/wsug_html_chunked/">here</a>. In particular, you should look at the Capture menu info <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseCaptureMenuSection.html">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '12, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10090" class="comments-container"><span id="10104"></span><div id="comment-10104" class="comment"><div id="post-10104-score" class="comment-score"></div><div class="comment-text"><p>I went to the caputure options and created file name, check use multiple files, determine the rotation of files, check ring buffer with x files, how many files to create...? The files are generated and when i opened up the files, i saw many unreadable characters on the windows 7 notepad file. Why is this so? I want to get the events in the windows 7 notepad file as readable logs.</p></div><div id="comment-10104-info" class="comment-info"><span class="comment-age">(13 Apr '12, 00:55)</span> <span class="comment-user userinfo">misteryuku</span></div></div><span id="10115"></span><div id="comment-10115" class="comment"><div id="post-10115-score" class="comment-score"></div><div class="comment-text"><p>See the answers to your question @ <a href="http://ask.wireshark.org/questions/10105/capturing-packets-to-a-file-using-wiresharks-capture-options">http://ask.wireshark.org/questions/10105/capturing-packets-to-a-file-using-wiresharks-capture-options</a></p></div><div id="comment-10115-info" class="comment-info"><span class="comment-age">(13 Apr '12, 02:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-10090" class="comment-tools"></div><div class="clear"></div><div id="comment-10090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

