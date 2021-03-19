+++
type = "question"
title = "Command line option for &quot;save as&quot;"
description = '''Wireshark -w command line option defaults to pcap format. Need to save a Wireshark capture to a specific file with a specific format. Possible example: -w &quot;filename&quot; -F &quot;format&quot; where &quot;format&quot; defines the save as type. Is this possible? Thanks'''
date = "2013-11-11T15:03:00Z"
lastmod = "2013-11-11T21:11:00Z"
weight = 26857
keywords = [ "command-line" ]
aliases = [ "/questions/26857" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Command line option for "save as"](/questions/26857/command-line-option-for-save-as)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26857-score" class="post-score" title="current number of votes">0</div><span id="post-26857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark -w command line option defaults to pcap format. Need to save a Wireshark capture to a specific file with a specific format. Possible example: -w "filename" -F "format" where "format" defines the save as type. Is this possible? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '13, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/1f41035de4c07eb099ab3fdce375d637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JerryCape&#39;s gravatar image" /><p><span>JerryCape</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JerryCape has no accepted answers">0%</span></p></div></div><div id="comments-container-26857" class="comments-container"></div><div id="comment-tools-26857" class="comment-tools"></div><div class="clear"></div><div id="comment-26857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26862"></span>

<div id="answer-container-26862" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26862-score" class="post-score" title="current number of votes">1</div><span id="post-26862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're doing a live capture, either with Wireshark or with TShark, it can only be saved in pcap or pcap-ng format.</p><p>If you're using TShark or editcap to read a saved file in one format and write to a file in another format, you can use <code>-F</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '13, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26862" class="comments-container"></div><div id="comment-tools-26862" class="comment-tools"></div><div class="clear"></div><div id="comment-26862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

