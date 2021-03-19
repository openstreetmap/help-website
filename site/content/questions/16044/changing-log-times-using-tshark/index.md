+++
type = "question"
title = "Changing log times using tshark"
description = '''Hi all, I have been running tshark on a clean ubuntu server for a few weeks, but i&#x27;ve noticed something odd in the timestamps of each logfile, while i setup the duration to be each hour.. for example: Nov 19 04:05 example1.cap Nov 19 05:05 example2.cap Nov 19 06:05 example3.cap Nov 19 08:59 example4...'''
date = "2012-11-19T02:20:00Z"
lastmod = "2012-11-19T03:05:00Z"
weight = 16044
keywords = [ "duration", "timestamp", "tshark", "timestamps" ]
aliases = [ "/questions/16044" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Changing log times using tshark](/questions/16044/changing-log-times-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16044-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have been running tshark on a clean ubuntu server for a few weeks, but i've noticed something odd in the timestamps of each logfile, while i setup the duration to be each hour..</p><p>for example:</p><p>Nov 19 04:05 example1.cap</p><p>Nov 19 05:05 example2.cap</p><p>Nov 19 06:05 example3.cap</p><p>Nov 19 08:59 example4.cap</p><p>Nov 19 09:59 example5.cap</p><p>As can be seen there´s a time gap between example3.cap and example4.cap</p><p>This is the command i've been using: nohup tshark -i eth0 -t ad -w /var/log/filename.cap -b duration:3600 &amp;</p><p>I´m worrying about this since there are specific random network problems appearing, because they might happen in these gaps..</p><p>Does anyone have an explanation for this, and what i should be doing=</p></div><div id="question-tags" class="tags-container tags">duration timestamp tshark timestamps</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '12, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/b237517e936ee688b4129ab32992fc71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrsL&#39;s gravatar image" /><p>ChrsL<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrsL has no accepted answers">0%</span></p></div></div><div id="comments-container-16044" class="comments-container"></div><div id="comment-tools-16044" class="comment-tools"></div><div class="clear"></div><div id="comment-16044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16049"></span>

<div id="answer-container-16049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16049-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's where editcap can help.</p><blockquote><p><code>editcap -t 300 input.cap output.cap</code><br />
</p></blockquote><p>This will adjust the timestamp for +300 seconds. See the man page for editcap.</p><blockquote><p><code>http://www.wireshark.org/docs/man-pages/editcap.html</code><br />
</p></blockquote><p>You can do the same in Wireshark itself (please use the latest version).</p><p>Open the capture file and then:</p><blockquote><p><code>Edit -&gt; Time Shift</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16049" class="comments-container"><span id="16680"></span><div id="comment-16680" class="comment"><div id="post-16680-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer!</p></div><div id="comment-16680-info" class="comment-info"><span class="comment-age">(07 Dec '12, 07:27)</span> ChrsL</div></div><span id="16683"></span><div id="comment-16683" class="comment"><div id="post-16683-score" class="comment-score"></div><div class="comment-text"><p>you're welcome.</p><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-16683-info" class="comment-info"><span class="comment-age">(07 Dec '12, 07:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16049" class="comment-tools"></div><div class="clear"></div><div id="comment-16049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

