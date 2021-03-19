+++
type = "question"
title = "RTP stream analysis on large files (greater than 10GB)"
description = '''Hi, I am trying to do RTP stream analysis on files greater than 10GB in size. The files only contain packet headers (packets were truncated to first 64 Bytes during capture). RTP analysis on one 10GB file is taking a few hours on a very fast server machine with multiple CPUs and 6GB RAM. Is there an...'''
date = "2014-05-07T03:52:00Z"
lastmod = "2014-05-07T04:53:00Z"
weight = 32582
keywords = [ "large", "files", "rtp", "analysis" ]
aliases = [ "/questions/32582" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP stream analysis on large files (greater than 10GB)](/questions/32582/rtp-stream-analysis-on-large-files-greater-than-10gb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32582-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to do RTP stream analysis on files greater than 10GB in size. The files only contain packet headers (packets were truncated to first 64 Bytes during capture).</p><p>RTP analysis on one 10GB file is taking a few hours on a very fast server machine with multiple CPUs and 6GB RAM.</p><p>Is there any way to do optimize this and make the RTP stream analysis run faster?</p><p>Any advice/pointers will be much appreciated.</p><p>Many thanks.</p></div><div id="question-tags" class="tags-container tags">large files rtp analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/14c9aa91a292327e1e0c0fe18a5fe4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hasanm&#39;s gravatar image" /><p>hasanm<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hasanm has no accepted answers">0%</span></p></div></div><div id="comments-container-32582" class="comments-container"></div><div id="comment-tools-32582" class="comment-tools"></div><div class="clear"></div><div id="comment-32582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32588"></span>

<div id="answer-container-32588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32588-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Other than checking if it's possible to optimize the code of epan/rtp_analysis.c and epan/rtp_stream.c or try splitting the file in smaller chunk and analyse them on by one - I think not. Are you using the latest version 1.10.7 or he development version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32588" class="comments-container"><span id="32590"></span><div id="comment-32590" class="comment"><div id="post-32590-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thanks Anders. I'm using 1.10.5.</p><p>Regards</p></div><div id="comment-32590-info" class="comment-info"><span class="comment-age">(07 May '14, 04:56)</span> hasanm</div></div><span id="32591"></span><div id="comment-32591" class="comment"><div id="post-32591-score" class="comment-score"></div><div class="comment-text"><p>Well I don't think there has been any improvment in the development version but you could try it. If you are going to try to optimize I would recommend using the development version and give us the patches.</p></div><div id="comment-32591-info" class="comment-info"><span class="comment-age">(07 May '14, 04:59)</span> Anders ♦</div></div><span id="32638"></span><div id="comment-32638" class="comment"><div id="post-32638-score" class="comment-score"></div><div class="comment-text"><p>Thanks Anders.</p></div><div id="comment-32638-info" class="comment-info"><span class="comment-age">(08 May '14, 04:54)</span> hasanm</div></div><span id="32660"></span><div id="comment-32660" class="comment"><div id="post-32660-score" class="comment-score"></div><div class="comment-text"><p>Hi again,</p><p>Using tshark for rtp stream analysis is faster. However, i can't find an option to generate a csv file that i can get through the gui (with the 'save as csv' option on RTP stream analysis window).</p><p>Any ideas?</p><p>Thanks.</p></div><div id="comment-32660-info" class="comment-info"><span class="comment-age">(09 May '14, 03:14)</span> hasanm</div></div></div><div id="comment-tools-32588" class="comment-tools"></div><div class="clear"></div><div id="comment-32588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

