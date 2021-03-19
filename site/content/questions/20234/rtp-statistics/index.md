+++
type = "question"
title = "RTP Statistics"
description = '''After capturing some RTP traffic i see the following Now i&#x27;m having troubles intepreting the Mean Jitter value. (looked on the forum but not alot info about it)  So three questions    1. Sot he max delta is the time difference between the packets correct?  2. The mean jitter is a calculation between...'''
date = "2013-04-09T05:03:00Z"
lastmod = "2013-04-11T07:45:00Z"
weight = 20234
keywords = [ "rtp" ]
aliases = [ "/questions/20234" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Statistics](/questions/20234/rtp-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20234-score" class="post-score" title="current number of votes">0</div><span id="post-20234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After capturing some RTP traffic i see the following</p><pre><code>Now i&#39;m having troubles intepreting the Mean Jitter value. (looked on the forum but not alot info about it)

So three questions 

 1. Sot he max delta is the time difference between the packets correct?
 2. The mean jitter is a calculation between the max delta and max jitter?
 3. What is max skew?

Thanks in advance!

Sica</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '13, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/113198545f0dd0c8f4b8be85e769aee8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sicabre&#39;s gravatar image" /><p><span>Sicabre</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sicabre has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '13, 10:41</strong> </span></p></div></div><div id="comments-container-20234" class="comments-container"></div><div id="comment-tools-20234" class="comment-tools"></div><div class="clear"></div><div id="comment-20234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20288"></span>

<div id="answer-container-20288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20288-score" class="post-score" title="current number of votes">0</div><span id="post-20288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So three questions</p></blockquote><p>Three answers ;-)</p><ol><li><p>The delta is the time difference between the current packet and the previous packet in the stream. <strong>max delta</strong> is the largest delta value.</p></li><li><p>Please take a look how Wireshark caluclates the jitter value: <a href="http://wiki.wireshark.org/RTP_statistics">http://wiki.wireshark.org/RTP_statistics</a> (search for: How jitter is calculated). The <strong>mean jitter</strong> value is the <a href="http://en.wikipedia.org/wiki/Arithmetic_mean">arithmetic mean value</a> of all jitter values.</p></li><li><p>Skew calculation is defined as follows (from: tap-rtp-common.c). <strong>max skew</strong> is the largest value of all skew values.</p></li></ol><pre><code>        /* Calculate skew, i.e. absolute jitter that also catches clock drift
         * Skew is positive if TS (nominal) is too fast
         */
        statinfo-&gt;skew    = nominaltime - arrivaltime;
        absskew = fabs(statinfo-&gt;skew);
        if(absskew &gt; fabs(statinfo-&gt;max_skew)){
            statinfo-&gt;max_skew = statinfo-&gt;skew;
        }</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '13, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20288" class="comments-container"><span id="20337"></span><div id="comment-20337" class="comment"><div id="post-20337-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt,</p><p>Thanks for your reply. So if mean(average) is 2 ms this imply's that the average jitter during the whole rtp call is 2ms with (somewhere during the call) was 5000ms?</p><p>Sica</p></div><div id="comment-20337-info" class="comment-info"><span class="comment-age">(11 Apr '13, 07:38)</span> <span class="comment-user userinfo">Sicabre</span></div></div><span id="20338"></span><div id="comment-20338" class="comment"><div id="post-20338-score" class="comment-score"></div><div class="comment-text"><p>Yes.</p><p>Kurt</p></div><div id="comment-20338-info" class="comment-info"><span class="comment-age">(11 Apr '13, 07:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20288" class="comment-tools"></div><div class="clear"></div><div id="comment-20288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

