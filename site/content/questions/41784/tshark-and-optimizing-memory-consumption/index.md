+++
type = "question"
title = "tshark and optimizing memory consumption"
description = '''From other Q&amp;amp;A&#x27;s I&#x27;ve gathered that tshark may intrinsically grow without limit, and in auditing a home WLAN using low power devices (500-1000 MB RAM), I&#x27;ve found it runs out of memory in in 6-8 hours. The total volume of packets does not seem to be a predictor, although the volume within a shor...'''
date = "2015-04-24T08:36:00Z"
lastmod = "2015-04-27T07:34:00Z"
weight = 41784
keywords = [ "filter", "out-of-memory", "tshark" ]
aliases = [ "/questions/41784" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [tshark and optimizing memory consumption](/questions/41784/tshark-and-optimizing-memory-consumption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41784-score" class="post-score" title="current number of votes">0</div><span id="post-41784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From <a href="https://ask.wireshark.org/questions/34035/tshark-memory-usage-explanation-needed">other Q&amp;A's</a> I've gathered that tshark may intrinsically grow without limit, and in auditing a home WLAN using low power devices (500-1000 MB RAM), I've found it runs out of memory in in 6-8 hours. The total volume of packets does not seem to be a predictor, although the volume within a short time frame (0.5 GB/hour +) may be.<br />
</p><p>I'm only looking for specific information that it seems to me should not require this accumulation of memory, and hoping there's a smarter way to get it that can prevent this:</p><pre><code>-T fields -e frame.time -e wlan.ra -e ip.src -e ip.len \
    -e tcp.srcport -e tcp.dstport -e frame.protocols \</code></pre><p>Auditing a WLAN introduces a complication: I cannot arbitrarily restart tshark, because a constraint of monitor mode is that it must witness each device connecting to the network in order to track that device's packets. If I restart tshark, I must also restart the WLAN to force all devices to reconnect. There are only a handful of devices involved.</p><p>Currently the filter I am using is</p><p><strong>-Y "ip &amp;&amp; !ip.src == 192.168.0.0/24"</strong></p><p>Is there a way to do this which would extend tshark's potential lifespan?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-out-of-memory" rel="tag" title="see questions tagged &#39;out-of-memory&#39;">out-of-memory</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/abf01b6006996f947014ff671ba4151b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mk27&#39;s gravatar image" /><p><span>mk27</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mk27 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '15, 08:42</strong> </span></p></div></div><div id="comments-container-41784" class="comments-container"></div><div id="comment-tools-41784" class="comment-tools"></div><div class="clear"></div><div id="comment-41784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41788"></span>

<div id="answer-container-41788" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41788-score" class="post-score" title="current number of votes">1</div><span id="post-41788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mk27 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a limitation of tshark (and Wireshark) as they are packet analysers <strong>not</strong> network monitors and retain state information such as conversations and eventually will run out of memory as you have found. The rate of memory use is more down to the relationship between the packets rather than packet size.</p><p>I think you'll have to look for another tool to meet your requirements, which seem to involve WLAN decryption along with tcp port info and possibly other protocols in the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '15, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41788" class="comments-container"><span id="41887"></span><div id="comment-41887" class="comment"><div id="post-41887-score" class="comment-score"></div><div class="comment-text"><p>I'd forgotten about Evan's changes. Does WLAN decryption still work after a buffer changeover?</p></div><div id="comment-41887-info" class="comment-info"><span class="comment-age">(27 Apr '15, 07:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41788" class="comment-tools"></div><div class="clear"></div><div id="comment-41788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41796"></span>

<div id="answer-container-41796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41796-score" class="post-score" title="current number of votes">0</div><span id="post-41796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could give a try to tshark from 1.99.X branch combined with the -b flag. See this <a href="https://blog.wireshark.org/2014/07/to-infinity-and-beyond-capturing-forever-with-tshark/">blog post</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '15, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-41796" class="comments-container"><span id="41825"></span><div id="comment-41825" class="comment"><div id="post-41825-score" class="comment-score"></div><div class="comment-text"><p>The problem is not the output. It is the memory footprint of the tshark process; it continuously grows until the system runs out of RAM, then the OS kernel kills it.</p></div><div id="comment-41825-info" class="comment-info"><span class="comment-age">(25 Apr '15, 05:43)</span> <span class="comment-user userinfo">mk27</span></div></div><span id="41827"></span><div id="comment-41827" class="comment"><div id="post-41827-score" class="comment-score"></div><div class="comment-text"><p>With the flag I indicated, the memory will be released each time you start a new buffer, thus solving the memory growth.</p></div><div id="comment-41827-info" class="comment-info"><span class="comment-age">(25 Apr '15, 06:19)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-41796" class="comment-tools"></div><div class="clear"></div><div id="comment-41796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

