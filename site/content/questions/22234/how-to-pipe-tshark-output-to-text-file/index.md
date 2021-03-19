+++
type = "question"
title = "How to pipe tshark output to text file"
description = '''I want to pipe the output of following command to a text file for further processing.Please let me know how to do the same.. tshark -r &amp;lt;mypcap&amp;gt; -Tfields -e ip.src -e ip.dst  10.10.10.10 1.1.1.1 2.2.2.2 3.3.3.3 16.1.1.1 11.11.11.1 I want to pipe this output to a text file what field to add to t...'''
date = "2013-06-21T18:33:00Z"
lastmod = "2013-06-21T18:47:00Z"
weight = 22234
keywords = [ "tshark" ]
aliases = [ "/questions/22234" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to pipe tshark output to text file](/questions/22234/how-to-pipe-tshark-output-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22234-score" class="post-score" title="current number of votes">0</div><span id="post-22234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to pipe the output of following command to a text file for further processing.Please let me know how to do the same..</p><p>tshark -r &lt;mypcap&gt; -Tfields -e ip.src -e ip.dst</p><p>10.10.10.10 1.1.1.1</p><p>2.2.2.2 3.3.3.3</p><p>16.1.1.1 11.11.11.1</p><p>I want to pipe this output to a text file what field to add to the command</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '13, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-22234" class="comments-container"></div><div id="comment-tools-22234" class="comment-tools"></div><div class="clear"></div><div id="comment-22234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22235"></span>

<div id="answer-container-22235" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22235-score" class="post-score" title="current number of votes">2</div><span id="post-22235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For either Linux or Windows, just add "&gt;" to the end of the command and name a file to save it to: 'tshark -r {file.pcap} -Tfields -e ip.src -e ip.dst <strong>&gt; file.txt</strong>'</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 18:47</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '13, 18:49</strong> </span></p></div></div><div id="comments-container-22235" class="comments-container"></div><div id="comment-tools-22235" class="comment-tools"></div><div class="clear"></div><div id="comment-22235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

