+++
type = "question"
title = "Capture filter"
description = '''I am not that computer literate and have lost tons of data to &#x27;unknown&#x27; uploads and downloads. Service provider Afrihost encouraged me to download Wire Shark. I have managed to do this but on opening the program it asks for the &#x27;capture filter&#x27;. I have no clue what this means and how to move forward...'''
date = "2016-04-29T08:22:00Z"
lastmod = "2016-04-29T11:55:00Z"
weight = 52078
keywords = [ "capturefilter" ]
aliases = [ "/questions/52078" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter](/questions/52078/capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52078-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am not that computer literate and have lost tons of data to 'unknown' uploads and downloads. Service provider Afrihost encouraged me to download Wire Shark. I have managed to do this but on opening the program it asks for the 'capture filter'. I have no clue what this means and how to move forward from here. HELP!please</p></div><div id="question-tags" class="tags-container tags">capturefilter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '16, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/4072a572191d357a86b0dc06a13b0296?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allandavidharvey&#39;s gravatar image" /><p>allandavidha...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allandavidharvey has no accepted answers">0%</span></p></div></div><div id="comments-container-52078" class="comments-container"><span id="52088"></span><div id="comment-52088" class="comment"><div id="post-52088-score" class="comment-score"></div><div class="comment-text"><p>It depends on what you want to achieve, i.e. what is the ultimate goal of using Wireshark. The capture filter is not mandatory, so you can capture without specifying one; it becomes useful when you know exactly what you are doing, and you can afford to exclude some packets from the capture because you are sure you won't ever be interested in them.</p></div><div id="comment-52088-info" class="comment-info"><span class="comment-age">(29 Apr '16, 10:52)</span> sindy</div></div></div><div id="comment-tools-52078" class="comment-tools"></div><div class="clear"></div><div id="comment-52078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52089"></span>

<div id="answer-container-52089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52089-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, after second reading I've understood that your goal is to find out what has your PC spent the data volume for. In that case, don't use any capture filter, and after capturing the traffic for a couple of minutes (for training) and then rather for hours, go <code>Statistics-&gt;Conversations-&gt;IPv4</code> to get a list of all conversations between your PC and some other machines in the internet. Then, sort these conversations by <code>Bytes A-&gt;B</code> and then <code>Bytes B-&gt;A</code>, descending in both cases (by clicking at the column header twice), so that you could see the most heavy conversations at the top of the table. Then, you'll want to find out what these conversations actually were good for.</p><p>By experience, the candidates for data hogs are</p><ul><li><p>automatic software upgrades (of both the operating system and applications)</p></li><li><p>youtube or other videos</p></li><li><p>some malware sending tons of spam from your PC</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '16, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52089" class="comments-container"></div><div id="comment-tools-52089" class="comment-tools"></div><div class="clear"></div><div id="comment-52089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

