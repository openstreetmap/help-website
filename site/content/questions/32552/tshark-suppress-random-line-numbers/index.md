+++
type = "question"
title = "Tshark: suppress random line numbers"
description = '''Hi all, I&#x27;m using tshark (in Linux) to return only packet source MAC addresses and signal strength. Here&#x27;s what I use:  tshark -i wlan0 -T fields -e wlan.sa -e radiotap.dbm_antsignal  The problem is that every few packets is prefixed by an annoying ID number. I assume that these are the same as the ...'''
date = "2014-05-06T09:15:00Z"
lastmod = "2014-05-06T09:43:00Z"
weight = 32552
keywords = [ "output", "numbering", "tshark" ]
aliases = [ "/questions/32552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark: suppress random line numbers](/questions/32552/tshark-suppress-random-line-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32552-score" class="post-score" title="current number of votes">0</div><span id="post-32552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm using tshark (in Linux) to return only packet source MAC addresses and signal strength. Here's what I use:</p><blockquote><p>tshark -i wlan0 -T fields -e wlan.sa -e radiotap.dbm_antsignal</p></blockquote><p>The problem is that every few packets is prefixed by an annoying ID number. I assume that these are the same as the numbers that show up unpredictably when I run "tshark -i wlan0 -n" and get this output (I've x'd out actual addresses...):</p><blockquote><p>Capturing on 'wlan0'</p><p>1 0.000000 00:02:6f:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>2 0.131605 00:18:d1:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>3 0.204522 00:02:6f:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>4 0.228617 -&gt; 00:18:d1:xx:xx:xx (RA)</p><p>4 5 0.336334 00:18:d1:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>6 0.409324 00:02:6f:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>7 0.447556 -&gt; 20:16:d8:xx:xx:xx (RA)</p><p>8 0.541174 00:18:d1:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>9 0.649089 -&gt; 20:16:d8:xx:xx:xx (RA)</p><p>10 0.665628 06:02:6f:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>11 0.746025 00:18:d1:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p><p>11 12 0.768025 06:02:6f:xx:xx:xx -&gt; ff:ff:ff:ff:ff:ff</p></blockquote><p>Notice the extra "4" and "11" Does anyone have any idea what these extra numbers are and, more importantly, how I can suppress them in my output? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span> <span class="post-tag tag-link-numbering" rel="tag" title="see questions tagged &#39;numbering&#39;">numbering</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/7ea7975b6f784ef65102e1d25adffdfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dlanced&#39;s gravatar image" /><p><span>dlanced</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dlanced has no accepted answers">0%</span></p></div></div><div id="comments-container-32552" class="comments-container"></div><div id="comment-tools-32552" class="comment-tools"></div><div class="clear"></div><div id="comment-32552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32553"></span>

<div id="answer-container-32553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32553-score" class="post-score" title="current number of votes">1</div><span id="post-32553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to <a href="http://ask.wireshark.org/questions/31564/tshark-output-refining">this</a> question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-32553" class="comments-container"><span id="32554"></span><div id="comment-32554" class="comment"><div id="post-32554-score" class="comment-score"></div><div class="comment-text"><p>Darn. I'm using 1.10.6-1 from the Ubuntu 14.04 repository and I'd like to stay within their upgrade cycle, so I'd rather not build my own. Is there an existing bug report asking for a backport? Thanks!</p></div><div id="comment-32554-info" class="comment-info"><span class="comment-age">(06 May '14, 09:29)</span> <span class="comment-user userinfo">dlanced</span></div></div><span id="32556"></span><div id="comment-32556" class="comment"><div id="post-32556-score" class="comment-score"></div><div class="comment-text"><p><em>Is there an existing bug report asking for a backport?</em></p><p>Not that I'm aware of, but you can browse/search the <a href="https://bugs.wireshark.org/bugzilla/buglist.cgi?resolution=---&amp;limit=0&amp;order=bug_id%20DESC&amp;list_id=14500">open bugs</a> and open one if there's not already one open.</p></div><div id="comment-32556-info" class="comment-info"><span class="comment-age">(06 May '14, 09:43)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-32553" class="comment-tools"></div><div class="clear"></div><div id="comment-32553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

