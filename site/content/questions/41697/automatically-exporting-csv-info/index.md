+++
type = "question"
title = "Automatically exporting csv info"
description = '''Hello everyone,  I&#x27;m running a windows version of wireshark (if this matters) and I would like to set up something so that I can export csv packet info automatically to a directory (every 30-60s for a few minutes) so that a program I have can run some code on it afterwards.  I figure I need to write...'''
date = "2015-04-22T09:25:00Z"
lastmod = "2015-04-28T07:57:00Z"
weight = 41697
keywords = [ "lua", "csv", "export", "wireshark", "script" ]
aliases = [ "/questions/41697" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Automatically exporting csv info](/questions/41697/automatically-exporting-csv-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41697-score" class="post-score" title="current number of votes">0</div><span id="post-41697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I'm running a windows version of wireshark (if this matters) and I would like to set up something so that I can export csv packet info automatically to a directory (every 30-60s for a few minutes) so that a program I have can run some code on it afterwards.</p><p>I figure I need to write some kind of script to do this and was wondering if this was possible to insert something into the program, but the caveat being that I haven't done anything with scripting until this point. If someone could point me in the right direction of where to apply a script in the program and such, it would be greatly appreciated!</p><p>Thanks, Nathan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '15, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/d688a4d81e76cc304c82162eb707d2b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NathanR&#39;s gravatar image" /><p><span>NathanR</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NathanR has no accepted answers">0%</span></p></div></div><div id="comments-container-41697" class="comments-container"><span id="41831"></span><div id="comment-41831" class="comment"><div id="post-41831-score" class="comment-score"></div><div class="comment-text"><p>Are you planing to generate CSV file at which time? a) at the time of live capturing b) or in generated PCAP file?</p></div><div id="comment-41831-info" class="comment-info"><span class="comment-age">(25 Apr '15, 10:14)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="41888"></span><div id="comment-41888" class="comment"><div id="post-41888-score" class="comment-score"></div><div class="comment-text"><p>I suppose ideally it would generate at live capturing until a few minutes had passed and then everything would stop. I only am concerned about the interactions of one specific address and my home pc address, so I don't need to worry about all the interactions being captured.</p></div><div id="comment-41888-info" class="comment-info"><span class="comment-age">(27 Apr '15, 07:49)</span> <span class="comment-user userinfo">NathanR</span></div></div></div><div id="comment-tools-41697" class="comment-tools"></div><div class="clear"></div><div id="comment-41697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41918"></span>

<div id="answer-container-41918" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41918-score" class="post-score" title="current number of votes">1</div><span id="post-41918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could look into using tshark with option -T and either fields or PDML, depending on your application/script you intend to write.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41918" class="comments-container"></div><div id="comment-tools-41918" class="comment-tools"></div><div class="clear"></div><div id="comment-41918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

