+++
type = "question"
title = "tshark meassuring bandwidth per IP"
description = '''I found this --&amp;gt; link text and I would like to use tshark for spitting bandwidth/IP on the command line. Is this possible?'''
date = "2016-03-02T03:13:00Z"
lastmod = "2016-03-02T04:36:00Z"
weight = 50649
keywords = [ "bandwidth", "bandwidthutilization", "tshark" ]
aliases = [ "/questions/50649" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark meassuring bandwidth per IP](/questions/50649/tshark-meassuring-bandwidth-per-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50649-score" class="post-score" title="current number of votes">0</div><span id="post-50649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I found this --&gt; <a href="https://ask.wireshark.org/questions/25575/sort-by-bandwidth-used-and-show-ip-addressnetwork-name">link text</a></p><p>and I would like to use tshark for spitting bandwidth/IP on the command line. Is this possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-bandwidthutilization" rel="tag" title="see questions tagged &#39;bandwidthutilization&#39;">bandwidthutilization</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/93eb17372bd105d80fc159bb1c97d6fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altdrugzgene&#39;s gravatar image" /><p><span>altdrugzgene</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altdrugzgene has no accepted answers">0%</span></p></div></div><div id="comments-container-50649" class="comments-container"></div><div id="comment-tools-50649" class="comment-tools"></div><div class="clear"></div><div id="comment-50649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50655"></span>

<div id="answer-container-50655" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50655-score" class="post-score" title="current number of votes">0</div><span id="post-50655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you should also look at the answer to <a href="https://ask.wireshark.org/questions/50445/tshark-stats-ip-conversations-sorted-to-most-bytes">this question</a>. It says that it is currently not possible to <em>sort</em> the output list of e.g. <code>tshark -q -z "conv,tcp"</code> by number of bytes per conversation directly with tshark, but otherwise these command line parameters of tshark provide you with the list of conversations of the indicated type, stating the common duration and both packet counts and byte counts per direction, so a simple post-process of that table can give you the bandwidths per direction calculated as <code>bytes/duration</code>. Just check whether the number of bytes represents whole frames or only the tcp part of them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '16, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50655" class="comments-container"><span id="50662"></span><div id="comment-50662" class="comment"><div id="post-50662-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy. I am doing 2 separate analyses at the moment one using the output from the TCP flows and one counting the bandwidth per intervals. However I cant find a way to correlate these two which is sad :P Anyways thanks</p></div><div id="comment-50662-info" class="comment-info"><span class="comment-age">(02 Mar '16, 04:23)</span> <span class="comment-user userinfo">altdrugzgene</span></div></div><span id="50664"></span><div id="comment-50664" class="comment"><div id="post-50664-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I've understood what you mean by "counting the bandwidth per intervals", but you can use a so-called "read" filter like <code>-2 -R frame.time_relative &gt;= t1 and frame.time_relative &lt; t2</code> to get the statistics only for a time slice t1..t2 of the capture file. You can <em>not</em> use <code>-Y</code> for the purpose as it does not affect the statistics calculation. Currently, <code>-R</code> can only be used together with <code>-2</code>, so the <code>-2</code> is there only as a "<code>-R</code> enabler", you do not need two-pass handling to calculate statistics.</p></div><div id="comment-50664-info" class="comment-info"><span class="comment-age">(02 Mar '16, 04:36)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50655" class="comment-tools"></div><div class="clear"></div><div id="comment-50655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

