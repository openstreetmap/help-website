+++
type = "question"
title = "Linux: monitor my own internet usage page by page (url by url)."
description = '''Hi all, I have a monthly broadband subscription which rolls over on the 23rd of each month. I had arrived near the end of my usage so I was carefully checking that I didn&#x27;t go over my limit - they crucify you for excess usage! So, when my usage didn&#x27;t roll over on the 23rd, I rang them to check what...'''
date = "2015-02-24T16:08:00Z"
lastmod = "2015-02-25T01:38:00Z"
weight = 40056
keywords = [ "url", "monitoring", "bandwidthutilization", "linux" ]
aliases = [ "/questions/40056" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Linux: monitor my own internet usage page by page (url by url).](/questions/40056/linux-monitor-my-own-internet-usage-page-by-page-url-by-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40056-score" class="post-score" title="current number of votes">0</div><span id="post-40056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have a monthly broadband subscription which rolls over on the 23rd<br />
of each month.</p><p>I had arrived near the end of my usage so I was carefully checking<br />
that I didn't go over my limit - they <strong>crucify</strong> you for excess usage!</p><p>So, when my usage didn't roll over on the 23rd, I rang them<br />
to check what was up (turned out that it was due to their<br />
end-user web interface not being entirely not up to date<br />
- they're quick enough to bill though!).</p><p>Now to the question - the agent told me that I had used 2.5MB<br />
(or similar figures) PER PAGE just to check my usage (the only<br />
pages I had accessed on the two days in question). To say I<br />
was <strong>shocked</strong> is an understatement. These are not fancy pages -<br />
v. little graphics &amp;c.</p><p>So, now I want to check up my internet usage (per page).<br />
I don't want something that I have to monitor continually,<br />
rather keeps a record, preferably something I can put in<br />
a database or at least a spreadsheet.</p><p>Is it possible to do this with tshark/Wireshark?</p><p>What I'd like ideally is a daemon (I know that I can do it<br />
from a terminal as a background process).</p><p>If it is not possible, can anyone point me to useful Linux<br />
tools in this domain? I have Googled and the only thing close<br />
is <a href="http://sickbits.net/tcptrack-simple-tcp-connection-monitor/">tcptrack here</a>.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span> <span class="post-tag tag-link-bandwidthutilization" rel="tag" title="see questions tagged &#39;bandwidthutilization&#39;">bandwidthutilization</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '15, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/0abb7e25b0cba7a76d71ce793001a774?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dragam&#39;s gravatar image" /><p><span>dragam</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dragam has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-40056" class="comments-container"></div><div id="comment-tools-40056" class="comment-tools"></div><div class="clear"></div><div id="comment-40056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40062"></span>

<div id="answer-container-40062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40062-score" class="post-score" title="current number of votes">0</div><span id="post-40062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://en.wikipedia.org/wiki/Ntopng">ntop-ng</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '15, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-40062" class="comments-container"></div><div id="comment-tools-40062" class="comment-tools"></div><div class="clear"></div><div id="comment-40062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40064"></span>

<div id="answer-container-40064" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40064-score" class="post-score" title="current number of votes">0</div><span id="post-40064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on the browser you use, the developer tools provided by the browser can also show this. This <a href="http://rossb.biz/blog/2013/measuring-page-weight/">page</a> shows how to measure page "weight" using various browsers.</p><p>Note your browser will hopefully cache a lot of the data so it isn't retrieved subsequently. You can see this by running a normal reload (e.g. F5 in Chrome) and then a full reload (e.g. Ctrl + F5 in Chrome).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '15, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-40064" class="comments-container"></div><div id="comment-tools-40064" class="comment-tools"></div><div class="clear"></div><div id="comment-40064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

