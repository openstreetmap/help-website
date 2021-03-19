+++
type = "question"
title = "Wireshark in Dos"
description = '''Hi guys Does anyone know if you can use wireshark from DOS, basically, i m trying to read the wireshark output in labview. I would aim on sending to the DOS prompt the wireshark command to report back the traffic on a network and then read this in to labview for analysis. Any ideas would be greatly ...'''
date = "2011-12-14T03:29:00Z"
lastmod = "2011-12-15T16:30:00Z"
weight = 7955
keywords = [ "dos", "help", "wireshark" ]
aliases = [ "/questions/7955" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark in Dos](/questions/7955/wireshark-in-dos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7955-score" class="post-score" title="current number of votes">0</div><span id="post-7955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys Does anyone know if you can use wireshark from DOS, basically, i m trying to read the wireshark output in labview. I would aim on sending to the DOS prompt the wireshark command to report back the traffic on a network and then read this in to labview for analysis. Any ideas would be greatly appreciated?? I am afraid i m a wireshark virgin really.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dos" rel="tag" title="see questions tagged &#39;dos&#39;">dos</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '11, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/7e0464de58aa849b80a167437ed73b4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smiles429&#39;s gravatar image" /><p><span>smiles429</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smiles429 has no accepted answers">0%</span></p></div></div><div id="comments-container-7955" class="comments-container"><span id="7957"></span><div id="comment-7957" class="comment"><div id="post-7957-score" class="comment-score">1</div><div class="comment-text"><p>do you mean using MS-DOS or using wireshark from a windows cli ?</p></div><div id="comment-7957-info" class="comment-info"><span class="comment-age">(14 Dec '11, 03:31)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-7955" class="comment-tools"></div><div class="clear"></div><div id="comment-7955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7959"></span>

<div id="answer-container-7959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7959-score" class="post-score" title="current number of votes">1</div><span id="post-7959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For command line output use tshark. See the documentation <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '11, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7959" class="comments-container"><span id="7969"></span><div id="comment-7969" class="comment"><div id="post-7969-score" class="comment-score"></div><div class="comment-text"><p>Or take a look at the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a> man-page.</p></div><div id="comment-7969-info" class="comment-info"><span class="comment-age">(14 Dec '11, 08:48)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-7959" class="comment-tools"></div><div class="clear"></div><div id="comment-7959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8003"></span>

<div id="answer-container-8003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8003-score" class="post-score" title="current number of votes">1</div><span id="post-8003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per Landi's question:</p><ul><li><p>If you mean "using MS-DOS", you can't - the only Microsoft operating systems on which Wireshark is supported are 32-bit and 64-bit versions of Windows.</p></li><li><p>If you mean "using Wireshark from a Windows CLI", see grahamb's response - use TShark or, if all you want to do is capture to a file and then read the file in LabView, use dumpcap (which comes with Wireshark, just as TShark does).</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '11, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8003" class="comments-container"></div><div id="comment-tools-8003" class="comment-tools"></div><div class="clear"></div><div id="comment-8003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

