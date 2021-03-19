+++
type = "question"
title = "Need Help Understanding Capture"
description = '''I am working on a pair of Windows 7 x64 machines. When I open a DOC file across the network it takes a long time to open and save. If I rename the file DOCX it opens and saves quickly. I have used Wireshark to capture traffic for both operations but don&#x27;t know enough about TCP to analyze what I have...'''
date = "2010-11-14T21:54:00Z"
lastmod = "2010-11-15T14:04:00Z"
weight = 951
keywords = [ "open", "file" ]
aliases = [ "/questions/951" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Need Help Understanding Capture](/questions/951/need-help-understanding-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-951-score" class="post-score" title="current number of votes">0</div><span id="post-951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on a pair of Windows 7 x64 machines. When I open a DOC file across the network it takes a long time to open and save. If I rename the file DOCX it opens and saves quickly. I have used Wireshark to capture traffic for both operations but don't know enough about TCP to analyze what I have.</p><p>Are there any examples around that might help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-open" rel="tag" title="see questions tagged &#39;open&#39;">open</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '10, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/9a5c60015cedf43171ca8eede3484f77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="broosth&#39;s gravatar image" /><p><span>broosth</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="broosth has no accepted answers">0%</span></p></div></div><div id="comments-container-951" class="comments-container"><span id="961"></span><div id="comment-961" class="comment"><div id="post-961-score" class="comment-score"></div><div class="comment-text"><p>I don't see how file extension can cause a network slowdown. Why don't you take word out of the picture and simply copy your doc and docx files using windows explorer. I bet it would take same time to copy, if it doesn't you may have an antivirus application that's scanning doc, but does not scan docx files. Anyway this sounds like a problem in the Application Layer, which wireshark would not make obvious. (Please correct me on the last sentence if i am mistaken)</p></div><div id="comment-961-info" class="comment-info"><span class="comment-age">(15 Nov '10, 12:13)</span> <span class="comment-user userinfo">net_tech</span></div></div></div><div id="comment-tools-951" class="comment-tools"></div><div class="clear"></div><div id="comment-951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="952"></span>

<div id="answer-container-952" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-952-score" class="post-score" title="current number of votes">0</div><span id="post-952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are tons of example files at www.wiresharkbook.com in the downloads section. You can also see several videos on that site as well.</p><p>When you rename the file are you saving it local or on the network? Are you opening in Word 2003 or 2007?</p><p>Can you look through both trace files and examine the Analyze &gt; Expert Info Composite to see TCP errors listed?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '10, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-952" class="comments-container"></div><div id="comment-tools-952" class="comment-tools"></div><div class="clear"></div><div id="comment-952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="965"></span>

<div id="answer-container-965" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-965-score" class="post-score" title="current number of votes">0</div><span id="post-965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>broosth, CIFS protocol can take a <strong>HUGE</strong> performance hit when copying, opening across WAN (with high latency). DOCX happens to produce a much smaller file so it can be as simple as that. It can also have to do with file locking, but the most likely suspect is simple file size issue.</p><p>In CIFS, the rule of thumb can be, READ operations will consume data at 16KB or 32KB per round-trip. WRITE operation will consume 8KB or 16KB per round trip.</p><p>So regardless of available bandwidth, speed of the circuit, or TCP window sizes, READ and WRITE operations are limited by CIFS upper bound. CIFS is the weakest link.</p><p>Windows 7 (and Vista, I suppose) can improve on the READ/WRITE performance, but as a general rule of thumb, what I wrote is "good enough."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '10, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-965" class="comments-container"></div><div id="comment-tools-965" class="comment-tools"></div><div class="clear"></div><div id="comment-965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

