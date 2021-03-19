+++
type = "question"
title = "Trigger a capture"
description = '''I&#x27;m looking for a feature to trigger a capture from either tcpdump or tshark I have a setup where a capture easily could take up giga bytes.  So what I need is some kind of trigger which would cause a capture to start when ex a SIP invite to a certain URI is detected, and then capture the next 100M ...'''
date = "2011-01-31T16:02:00Z"
lastmod = "2011-02-02T10:58:00Z"
weight = 2049
keywords = [ "capture" ]
aliases = [ "/questions/2049" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Trigger a capture](/questions/2049/trigger-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2049-score" class="post-score" title="current number of votes">0</div><span id="post-2049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for a feature to trigger a capture from either tcpdump or tshark I have a setup where a capture easily could take up giga bytes. So what I need is some kind of trigger which would cause a capture to start when ex a SIP invite to a certain URI is detected, and then capture the next 100M</p><p>Is this somehow possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '11, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/b0ac00407121781dba912c3cd3ede4c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kjeld%20Flarup&#39;s gravatar image" /><p><span>Kjeld Flarup</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kjeld Flarup has no accepted answers">0%</span></p></div></div><div id="comments-container-2049" class="comments-container"></div><div id="comment-tools-2049" class="comment-tools"></div><div class="clear"></div><div id="comment-2049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2052"></span>

<div id="answer-container-2052" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2052-score" class="post-score" title="current number of votes">2</div><span id="post-2052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kjeld Flarup has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know that is on the wish list of features for quite some time now, but doesn't exist in Wireshark yet. You could go for setting up a ring buffered capture that overwrites older trace files. If you set the buffer large enough you might be able to capture what you want and have enough time to find out about it without overloading your disk.</p><p>Finding the SIP invite in tons of trace data isn't that hard using tshark, using the <code>"-r &lt;infile&gt; -R "&lt;filter for the sip invite&gt;" -w &lt;outfile&gt;"</code> syntax in a batch on all captured files and checking if a call was found by looking into the outfile. Then track down the full trace by looking at absolute date and time and extract it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2052" class="comments-container"><span id="2084"></span><div id="comment-2084" class="comment"><div id="post-2084-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper</p><p>Although I cannot use the ring buffer either, you gave me an idea to emulate this. Currently I have put a packet limit on the tcpdump, and when that exceeds I restart it with a new file name.</p><p>I could of course run a filter when it restarts I could check if I got my data, and delete the old file if not use able.</p></div><div id="comment-2084-info" class="comment-info"><span class="comment-age">(01 Feb '11, 13:53)</span> <span class="comment-user userinfo">Kjeld Flarup</span></div></div><span id="2112"></span><div id="comment-2112" class="comment"><div id="post-2112-score" class="comment-score">1</div><div class="comment-text"><p>(I changed your answer to a comment to adhere to the Q&amp;A style of this website)</p><p>You can also use the "-C &lt;size&gt;" option of tcpdump, it will create a new file after each &lt;size&gt; million bytes. You can then run a cleaning script that deletes all files <em>but</em> the latest &lt;x&gt; ones. That will create a "ring-buffer" of X*size MB :-)</p><p>(lets call it a "poor-mans-dumpcap-ringbuffer" :-))</p></div><div id="comment-2112-info" class="comment-info"><span class="comment-age">(02 Feb '11, 10:58)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2052" class="comment-tools"></div><div class="clear"></div><div id="comment-2052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

