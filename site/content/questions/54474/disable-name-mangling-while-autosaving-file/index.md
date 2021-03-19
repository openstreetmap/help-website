+++
type = "question"
title = "disable name mangling while autosaving file"
description = '''I am using -b (ring buffer option) in tshark for saving in two files alternately. However it changes the name of the file everytime it writes and appends date and time to it. How can i disable it as i don&#x27;t want names to change? '''
date = "2016-08-01T01:55:00Z"
lastmod = "2016-08-01T02:38:00Z"
weight = 54474
keywords = [ "tshark" ]
aliases = [ "/questions/54474" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [disable name mangling while autosaving file](/questions/54474/disable-name-mangling-while-autosaving-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54474-score" class="post-score" title="current number of votes">0</div><span id="post-54474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using -b (ring buffer option) in tshark for saving in two files alternately. However it changes the name of the file everytime it writes and appends date and time to it. How can i disable it as i don't want names to change?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '16, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/557d426153aa6950b4ae3541a97ab03d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tatsugot&#39;s gravatar image" /><p><span>tatsugot</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tatsugot has no accepted answers">0%</span></p></div></div><div id="comments-container-54474" class="comments-container"></div><div id="comment-tools-54474" class="comment-tools"></div><div class="clear"></div><div id="comment-54474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54476"></span>

<div id="answer-container-54476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54476-score" class="post-score" title="current number of votes">0</div><span id="post-54476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">TShark manual page</a> you'll see that <code>-b</code> option is the multiple files mode. One of the possibilities is to make it into a ring buffer, by dropping old capture files. A ring of multiple files that is. And multiple files need to have unique names, which are generated from the base name you define and a suffix. So no mangling is going on, there is a suffix appended to the name of the file.</p><p>What you are probably imagining is a single file in which new bytes (frames in reality) are added at the back and 'old' bytes (frames)removed from the front. That is not really possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '16, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54476" class="comments-container"><span id="54477"></span><div id="comment-54477" class="comment"><div id="post-54477-score" class="comment-score"></div><div class="comment-text"><p>I want to save stream after 30s and extract fields from this pcap file and store in a file. If i use -a option it will shut off stream for saving ,i don't want to shut off and on capturing stream again and again. So i thought of using ring buffer so that I can replace old files with new ones,but since I want to extract fields I need to have names same so that I can hardcode it.</p></div><div id="comment-54477-info" class="comment-info"><span class="comment-age">(01 Aug '16, 02:38)</span> <span class="comment-user userinfo">tatsugot</span></div></div></div><div id="comment-tools-54476" class="comment-tools"></div><div class="clear"></div><div id="comment-54476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

