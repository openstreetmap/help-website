+++
type = "question"
title = "tshark wiresharkXXXX file even with text to stdout"
description = '''I&#x27;m using tshark (Windows version) in a script that I would like to run for an indefinite period of time. The tshark parameters are something like -i1 -s48 -x&amp;lt;filter&amp;gt;. This results in text to stdout that I process with gawk. However, a wiresharkXXXX temp file is also created. There doesn&#x27;t see...'''
date = "2011-09-23T09:37:00Z"
lastmod = "2011-09-23T13:03:00Z"
weight = 6517
keywords = [ "tshark", "script" ]
aliases = [ "/questions/6517" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [tshark wiresharkXXXX file even with text to stdout](/questions/6517/tshark-wiresharkxxxx-file-even-with-text-to-stdout)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6517-score" class="post-score" title="current number of votes">0</div><span id="post-6517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using <code>tshark</code> (Windows version) in a script that I would like to run for an indefinite period of time. The <code>tshark</code> parameters are something like <code>-i1 -s48 -x&lt;filter&gt;</code>. This results in text to stdout that I process with <code>gawk</code>. However, a <code>wiresharkXXXX</code> temp file is also created. There doesn't seem to be a need for a temp file when the start parameters do not specify any file creation. It looks like the temp file will grow as long as my script runs, so eventually my HD will fill up, and the script will fail. Is there a solution?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '11, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/bd3aa6113f3a9130c6db4bce2468d519?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="faceoff&#39;s gravatar image" /><p><span>faceoff</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="faceoff has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '11, 15:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6517" class="comments-container"></div><div id="comment-tools-6517" class="comment-tools"></div><div class="clear"></div><div id="comment-6517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="6525"></span>

<div id="answer-container-6525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6525-score" class="post-score" title="current number of votes">0</div><span id="post-6525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually: tshark runs dumpcap as a separate process to do the actual capture and the temp file is the method by which data to transferred to tshark.</p><p>I think using the tshark -b option to control the output file(s) will work.</p><p>Something like <code>-b duration:...</code> <code>-b files:...</code></p><p>See <code>tshark -h</code> or the <code>tshark</code> man apge.</p><p>It's possible you may also need to use <code>-w</code>. I haven't actually tried this so I can't guarantee that this approach will work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-6525" class="comments-container"></div><div id="comment-tools-6525" class="comment-tools"></div><div class="clear"></div><div id="comment-6525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6526"></span>

<div id="answer-container-6526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6526-score" class="post-score" title="current number of votes">0</div><span id="post-6526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Be aware of the following:</p><ul><li>dumpcap is the process that does the actual capture</li><li>the temporary capture file is used between dumpcap and tshark</li><li>tshark has the <code>-b</code> <a href="http://www.wireshark.org/docs/man-pages/tshark.html">command line option</a> to use a circular buffer</li><li>tshark builds up state, increasing memory footprint over time, leading to <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory problems</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6526" class="comments-container"></div><div id="comment-tools-6526" class="comment-tools"></div><div class="clear"></div><div id="comment-6526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6527"></span>

<div id="answer-container-6527" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6527-score" class="post-score" title="current number of votes">0</div><span id="post-6527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the resolution to this problem will come when someone takes the time to resolve <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2743">bug 2743</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6527" class="comments-container"></div><div id="comment-tools-6527" class="comment-tools"></div><div class="clear"></div><div id="comment-6527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

