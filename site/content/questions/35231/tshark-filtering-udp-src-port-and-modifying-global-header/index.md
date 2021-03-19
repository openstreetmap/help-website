+++
type = "question"
title = "tshark - Filtering UDP SRC port and modifying global header"
description = '''I am using tshark and mergecap to filter and merge a lot of PCAP files into one file for analysis. I have two problems that I can&#x27;t solve. 1: With tshark, I cannot apply a filter to just the UDP source port. The data has a port that is the same on the source and destination side, so some criteria ju...'''
date = "2014-08-05T11:24:00Z"
lastmod = "2014-08-05T12:25:00Z"
weight = 35231
keywords = [ "tshark" ]
aliases = [ "/questions/35231" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark - Filtering UDP SRC port and modifying global header](/questions/35231/tshark-filtering-udp-src-port-and-modifying-global-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35231-score" class="post-score" title="current number of votes">0</div><span id="post-35231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using tshark and mergecap to filter and merge a lot of PCAP files into one file for analysis. I have two problems that I can't solve.</p><p>1: With tshark, I cannot apply a filter to just the UDP source port. The data has a port that is the same on the source and destination side, so some criteria just pass all data by. Is there a workaround?</p><p>2: It seems that after I run tshark, my global header gets modified. I am most concerned about the link type being changed from my application specific type to a maxed out hex field. Is there an option to fix this?</p><p>My batch script calls tshark as follows:</p><pre><code>tshark -r input.pcap -w output.pcap -Y ip.addr=1.2.3.4 -Y udp.port==12345</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/326b835a00e2581434d60880c06dfcd8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="okayh&#39;s gravatar image" /><p><span>okayh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="okayh has no accepted answers">0%</span></p></div></div><div id="comments-container-35231" class="comments-container"></div><div id="comment-tools-35231" class="comment-tools"></div><div class="clear"></div><div id="comment-35231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35232"></span>

<div id="answer-container-35232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35232-score" class="post-score" title="current number of votes">0</div><span id="post-35232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Replace udp.port by udp.srcport. Not sure to understand what you mean regarding the header content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '14, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-35232" class="comments-container"></div><div id="comment-tools-35232" class="comment-tools"></div><div class="clear"></div><div id="comment-35232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

