+++
type = "question"
title = "Is there an equivalent to tshark -z follow... for use with -w?"
description = '''I would like to output the raw packets for just one thread. E.g. something like: tshark -r in.cap -z&quot;follow,tcp,hex,1.2.3.4:2000,1.2.3.9:2001&quot; -F pcap -w out.cap The -z follow... switch does the job in principle but only seems to do text output. Adding -w gives no output. Is there an equivalent filt...'''
date = "2013-10-31T06:13:00Z"
lastmod = "2013-11-04T05:15:00Z"
weight = 26587
keywords = [ "follow", "tshark" ]
aliases = [ "/questions/26587" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there an equivalent to tshark -z follow... for use with -w?](/questions/26587/is-there-an-equivalent-to-tshark-z-follow-for-use-with-w)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26587-score" class="post-score" title="current number of votes">0</div><span id="post-26587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to output the raw packets for just one thread. E.g. something like:</p><p><code>tshark -r in.cap -z"follow,tcp,hex,1.2.3.4:2000,1.2.3.9:2001" -F pcap -w out.cap</code></p><p>The -z follow... switch does the job in principle but only seems to do text output. Adding -w gives no output. Is there an equivalent filter for -R or -Y?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '13, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/310c7b54264c9e10ad43acb3bb1d042a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiggers&#39;s gravatar image" /><p><span>wiggers</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiggers has no accepted answers">0%</span></p></div></div><div id="comments-container-26587" class="comments-container"></div><div id="comment-tools-26587" class="comment-tools"></div><div class="clear"></div><div id="comment-26587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26626"></span>

<div id="answer-container-26626" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26626-score" class="post-score" title="current number of votes">1</div><span id="post-26626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiggers has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you want to save one conversation in a new capture file.</p><p>If so, please run tshark with the appropriate display filter</p><blockquote><p>tshark -nr input.pcap -Y "ip.addr eq 1.2.3.4 and ip.addr eq 1.2.3.9 and tcp.port eq 2000 and tcp.port eq 2001" -F pcap -w out.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '13, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26626" class="comments-container"><span id="26653"></span><div id="comment-26653" class="comment"><div id="post-26653-score" class="comment-score"></div><div class="comment-text"><p>Using .addr and .port is the key, I thought you needed src or dst as well.</p></div><div id="comment-26653-info" class="comment-info"><span class="comment-age">(04 Nov '13, 02:25)</span> <span class="comment-user userinfo">wiggers</span></div></div><span id="26656"></span><div id="comment-26656" class="comment"><div id="post-26656-score" class="comment-score"></div><div class="comment-text"><p>.addr is <strong>both</strong> directions, so it matches for .src and .dst.</p></div><div id="comment-26656-info" class="comment-info"><span class="comment-age">(04 Nov '13, 05:15)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26626" class="comment-tools"></div><div class="clear"></div><div id="comment-26626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

