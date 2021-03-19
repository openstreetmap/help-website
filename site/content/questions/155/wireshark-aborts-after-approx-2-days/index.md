+++
type = "question"
title = "Wireshark aborts after approx. 2 days"
description = '''I&#x27;m using Wireshark to try and capture some very rare events that occur very infrequently (months between) but Wireshakr shutsdown after a couple of days. It&#x27;s configured to use ring buffered, multiple trace files, but when I return to the machine after more than 2/3 days Wireshark is not running. T...'''
date = "2010-09-16T09:14:00Z"
lastmod = "2010-09-16T09:48:00Z"
weight = 155
keywords = [ "events", "shutdown" ]
aliases = [ "/questions/155" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark aborts after approx. 2 days](/questions/155/wireshark-aborts-after-approx-2-days)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-155-score" class="post-score" title="current number of votes">0</div><span id="post-155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark to try and capture some very rare events that occur very infrequently (months between) but Wireshakr shutsdown after a couple of days. It's configured to use ring buffered, multiple trace files, but when I return to the machine after more than 2/3 days Wireshark is not running. There is plenty of RAM and disc space. I've asked other people and get the answer"It just does that" which is not a lot of use to me. Any help would be greatly appeciated. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-events" rel="tag" title="see questions tagged &#39;events&#39;">events</span> <span class="post-tag tag-link-shutdown" rel="tag" title="see questions tagged &#39;shutdown&#39;">shutdown</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '10, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/fc307170cf853059dc34bc0b7478ee08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dorsetsteve&#39;s gravatar image" /><p><span>dorsetsteve</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dorsetsteve has no accepted answers">0%</span></p></div></div><div id="comments-container-155" class="comments-container"></div><div id="comment-tools-155" class="comment-tools"></div><div class="clear"></div><div id="comment-155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="158"></span>

<div id="answer-container-158" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-158-score" class="post-score" title="current number of votes">5</div><span id="post-158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark keeps state-information and reassembled data in memory. This means that even if you write to several files to disk, the memory use does increase over time. See: <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a></p><p>You can use 'dumpcap' to do the capturing instead, I have used dumpcap to capture a rare problem too and it has been running for months. The syntax you could use is:</p><p>dumpcap -i <em>interface</em> -w <em>file</em> -b filesize:16384 -b files:1024</p><p>which will create 1024 files of 16MB, giving you a 16GB ringbuffer. When the problem occurs, just stop dumpcap and use wireshark (or tshark) to analyse the files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '10, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-158" class="comments-container"></div><div id="comment-tools-158" class="comment-tools"></div><div class="clear"></div><div id="comment-158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

