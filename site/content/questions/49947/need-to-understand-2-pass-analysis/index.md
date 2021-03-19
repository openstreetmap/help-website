+++
type = "question"
title = "Need to understand 2 pass analysis ?"
description = '''Hello, I am looking to the 2 pass analysis (-2 -R) for a while, but I could not see difference between &quot; -2 -R xxx &quot;instead of using 2 parameter &quot; -Y xxx -Y xxx &quot; . Can soneone explain me that with some examples how to use it or the difference. Thanks, Best Regards'''
date = "2016-02-07T05:53:00Z"
lastmod = "2016-02-07T08:40:00Z"
weight = 49947
keywords = [ "display-filter" ]
aliases = [ "/questions/49947" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need to understand 2 pass analysis ?](/questions/49947/need-to-understand-2-pass-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49947-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am looking to the 2 pass analysis (-2 -R) for a while, but I could not see difference between " -2 -R xxx "instead of using 2 parameter " -Y xxx -Y xxx " . Can soneone explain me that with some examples how to use it or the difference.</p><p>Thanks, Best Regards</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '16, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/9d86fdf69e0c61a61eb4f0b2e0b625b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EY-security&#39;s gravatar image" /><p>EY-security<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EY-security has no accepted answers">0%</span></p></div></div><div id="comments-container-49947" class="comments-container"></div><div id="comment-tools-49947" class="comment-tools"></div><div class="clear"></div><div id="comment-49947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49949"></span>

<div id="answer-container-49949" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49949-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Among other things 2 pass mode allows the dissection engine to update forward references, e.g. an http request can have the link to the response updated as the response was dissected on the first pass after the request had initially been dissected.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '16, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49949" class="comments-container"><span id="49952"></span><div id="comment-49952" class="comment"><div id="post-49952-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb,</p><p>Yeah I read all the things on the internet that explain 2 pass analysis, but, when I try with some examples that I only see the difference is the sequence numbers are starting at the begiging again (1,2,..) instead of real sequence number (100, 4800,...) . Can you give me the 2 whole filter that can I see the difference between -Y and -2 -R.</p><p>I only see the bugs on the given examples in internet.</p><p>Thanks, Best Regards</p></div><div id="comment-49952-info" class="comment-info"><span class="comment-age">(07 Feb '16, 13:36)</span> EY-security</div></div><span id="50341"></span><div id="comment-50341" class="comment"><div id="post-50341-score" class="comment-score"></div><div class="comment-text"><p>Could <a href="https://ask.wireshark.org/questions/50323/i-lose-data-when-filtering-in-a-reassembled-pdu/50339">this answer to another question</a> be an answer to your question too?</p></div><div id="comment-50341-info" class="comment-info"><span class="comment-age">(19 Feb '16, 06:41)</span> sindy</div></div></div><div id="comment-tools-49949" class="comment-tools"></div><div class="clear"></div><div id="comment-49949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

