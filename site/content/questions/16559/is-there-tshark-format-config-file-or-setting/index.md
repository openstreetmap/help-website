+++
type = "question"
title = "is there tshark format config file? or setting?"
description = '''I&#x27;m use tshark to read .pcap in linux i want result text to insert &#92;t(tab delimiter of coumn) as same command &quot;tshark -tad - n -r xxxx.pcap&quot; now  result text{ 2012-12-05 09:39:20.770766 xxxxxx -&amp;gt; xxxxx LLMNR 86 Standard query A isatap } want result text{ 1 2012-12-05 09:39:20.770766 xxxxxx -&amp;gt; ...'''
date = "2012-12-04T17:17:00Z"
lastmod = "2012-12-05T11:13:00Z"
weight = 16559
keywords = [ "tshark" ]
aliases = [ "/questions/16559" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [is there tshark format config file? or setting?](/questions/16559/is-there-tshark-format-config-file-or-setting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16559-score" class="post-score" title="current number of votes">0</div><span id="post-16559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm use tshark to read .pcap in linux</p><p>i want result text to insert \t(tab delimiter of coumn) as same command</p><p>"tshark -tad - n -r xxxx.pcap"</p><p>now</p><p>result text{</p><p><strong>2012-12-05 09:39:20.770766 xxxxxx -&gt; xxxxx LLMNR 86 Standard query A isatap</strong></p><p>}</p><p>want result text{</p><p><strong>1 2012-12-05 09:39:20.770766 xxxxxx -&gt; xxxxx LLMNR 86 Standard query A isatap</strong></p><p>}</p><p>Is there any way without change command ?</p><p>plz help me</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/7b0cfd1a07300acd66a1dd20d4d2e1ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doomgreen&#39;s gravatar image" /><p><span>doomgreen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doomgreen has no accepted answers">0%</span></p></div></div><div id="comments-container-16559" class="comments-container"></div><div id="comment-tools-16559" class="comment-tools"></div><div class="clear"></div><div id="comment-16559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16605"></span>

<div id="answer-container-16605" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16605-score" class="post-score" title="current number of votes">0</div><span id="post-16605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you just want the tabs instead of the spaces, pipe the output of tshark to sed/tr/awk (whatever you prefer) and replace the spaces with a tab.</p><p>Example for tr:</p><blockquote><p><code>tshark -tad -n -r input.cap | tr ' ' \\t &gt; output.txt</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '12, 12:45</strong> </span></p></div></div><div id="comments-container-16605" class="comments-container"></div><div id="comment-tools-16605" class="comment-tools"></div><div class="clear"></div><div id="comment-16605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

