+++
type = "question"
title = "Writing a tshark filter through tcl"
description = '''Hi, I&#x27;m facing an issue while writing a tshark filter expression through tcl -- where we write the expression using &#x27;contains&#x27; For Eg. &quot;tshark -r $captureFile -qz io,stat,0, eth.src==$sourceMac&amp;amp;&amp;amp;isis.lsp.lspid contains &#x27;ff&#x27; &quot; I am able to write expressions which do not contain any spaces and...'''
date = "2012-08-17T13:07:00Z"
lastmod = "2012-08-20T07:01:00Z"
weight = 13710
keywords = [ "tcl", "capture-filter", "tshark" ]
aliases = [ "/questions/13710" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Writing a tshark filter through tcl](/questions/13710/writing-a-tshark-filter-through-tcl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13710-score" class="post-score" title="current number of votes">0</div><span id="post-13710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm facing an issue while writing a tshark filter expression through tcl -- where we write the expression using 'contains'</p><p>For Eg. "tshark -r $captureFile -qz io,stat,0, eth.src==$sourceMac&amp;&amp;<strong>isis.lsp.lspid contains 'ff'</strong> "</p><p>I am able to write expressions which do not contain any spaces and use the == operator but I'm getting an error when trying to get the above expression working ....essentially : isis.lsp.lspid contains "ff"</p><p>Somehow, either the spaces in the expression or the "" around ff are causing it. Also tried escaping the "" (\"ff\")</p><p>One of the errors: Protocol ("ff") cannot appear on right-hand side of comparison.</p><p>But I'm not able to get it working even after trying a number of different combinations.</p><p>Any suggestions on how to get it working ?</p><p>Thanks, Niliss</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcl" rel="tag" title="see questions tagged &#39;tcl&#39;">tcl</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '12, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/4d37e88d5596b824b7e09cad7d5097d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Niliss&#39;s gravatar image" /><p><span>Niliss</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Niliss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Aug '12, 13:12</strong> </span></p></div></div><div id="comments-container-13710" class="comments-container"></div><div id="comment-tools-13710" class="comment-tools"></div><div class="clear"></div><div id="comment-13710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13717"></span>

<div id="answer-container-13717" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13717-score" class="post-score" title="current number of votes">1</div><span id="post-13717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Niliss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that <code>ff</code> is a filter on its own, for <em>"FOUNDATION Fieldbus"</em> traffic. You should be able to work around it by adding a trailing colon, i.e., use <code>"ff:"</code>.</p><p>And in case you ever want to test for <code>fc</code>, you will run into the same problem as this is the filter used for <em>"Fibre Channel"</em> traffic.</p><p>See also <a href="http://ask.wireshark.org/questions/7724/problem-while-filtering-framex-ff-or-fc">question 2274</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '12, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-13717" class="comments-container"><span id="13753"></span><div id="comment-13753" class="comment"><div id="post-13753-score" class="comment-score"></div><div class="comment-text"><p>That works ! Thanks a lot !</p></div><div id="comment-13753-info" class="comment-info"><span class="comment-age">(20 Aug '12, 07:01)</span> <span class="comment-user userinfo">Niliss</span></div></div></div><div id="comment-tools-13717" class="comment-tools"></div><div class="clear"></div><div id="comment-13717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

