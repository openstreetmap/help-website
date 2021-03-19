+++
type = "question"
title = "How to open large pcap files faster?"
description = '''I&#x27;m trying to open fairly large pcap files (about 500MB) and they&#x27;re loading extremely slow. I imagine the reason for this is due to the sheer number of packets. While loading, I noticed that only a single core on my processor is being used (maxed out to 99% utilization). I believe this is my bottle...'''
date = "2012-09-28T07:44:00Z"
lastmod = "2012-09-28T08:42:00Z"
weight = 14592
keywords = [ "slow", "threads", "multicore", "pcap", "faster" ]
aliases = [ "/questions/14592" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to open large pcap files faster?](/questions/14592/how-to-open-large-pcap-files-faster)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14592-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to open fairly large pcap files (about 500MB) and they're loading extremely slow. I imagine the reason for this is due to the sheer number of packets. While loading, I noticed that only a single core on my processor is being used (maxed out to 99% utilization). I believe this is my bottleneck since I have plenty of memory.</p><p>Is there a way to utilize multiple cores when opening pcap files? Can anyone recommend other methods of speeding up the process?</p><p>Thanks, Keith</p></div><div id="question-tags" class="tags-container tags">slow threads multicore pcap faster</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/9d141f99918df47932149d44ef1d36bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kfryklund&#39;s gravatar image" /><p>kfryklund<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kfryklund has no accepted answers">0%</span></p></div></div><div id="comments-container-14592" class="comments-container"></div><div id="comment-tools-14592" class="comment-tools"></div><div class="clear"></div><div id="comment-14592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14601"></span>

<div id="answer-container-14601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14601-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is the 1M$ question :-) In trunk there is some speedup of loading files, something we are constantly trying to look at. Multi treading of packet dissection is not easy as the dissection of a packets may depend on dissection of a previous packet like reassembly or state or... It has been discussed but no one has come up with a solution yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '12, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-14601" class="comments-container"></div><div id="comment-tools-14601" class="comment-tools"></div><div class="clear"></div><div id="comment-14601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

