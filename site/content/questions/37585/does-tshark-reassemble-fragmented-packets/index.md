+++
type = "question"
title = "Does TShark reassemble fragmented packets"
description = '''This is my first project where I&#x27;m dealing with analyzing network traffic so bare with me. I&#x27;m trying to analyze some TCP data that is normally fragmented into several frames due to the size. I know WireShark has the ability to reassemble the frames for me, does TShark have this same ability? I don&#x27;...'''
date = "2014-11-05T05:52:00Z"
lastmod = "2014-11-05T06:05:00Z"
weight = 37585
keywords = [ "fragmentation", "data", "tshark", "tcp" ]
aliases = [ "/questions/37585" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does TShark reassemble fragmented packets](/questions/37585/does-tshark-reassemble-fragmented-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37585-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is my first project where I'm dealing with analyzing network traffic so bare with me.</p><p>I'm trying to analyze some TCP data that is normally fragmented into several frames due to the size. I know WireShark has the ability to reassemble the frames for me, does TShark have this same ability? I don't want to start down the path of using TShark if it can't do this.</p><p>Thanks Ed</p></div><div id="question-tags" class="tags-container tags">fragmentation data tshark tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '14, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/cd84182756c41ff09be94e2961752880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdDickens&#39;s gravatar image" /><p>EdDickens<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdDickens has no accepted answers">0%</span></p></div></div><div id="comments-container-37585" class="comments-container"></div><div id="comment-tools-37585" class="comment-tools"></div><div class="clear"></div><div id="comment-37585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37586"></span>

<div id="answer-container-37586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37586-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The dissection "engine" is shared between Wireshark (the GUI application) and tshark (the command line application). Both applications also read the same configuration file, e.g. for reassembly settings, so there should be no difference in behaviour.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '14, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37586" class="comments-container"><span id="37588"></span><div id="comment-37588" class="comment"><div id="post-37588-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham.</p><p>So as long as the option to reassemble is turned on in Wireshark, TShark will do the same.</p></div><div id="comment-37588-info" class="comment-info"><span class="comment-age">(05 Nov '14, 06:27)</span> EdDickens</div></div><span id="37589"></span><div id="comment-37589" class="comment"><div id="post-37589-score" class="comment-score">1</div><div class="comment-text"><p>Yep, although you'll have to work a little harder in tshark to control the field output.</p></div><div id="comment-37589-info" class="comment-info"><span class="comment-age">(05 Nov '14, 06:54)</span> grahamb ♦</div></div><span id="37590"></span><div id="comment-37590" class="comment"><div id="post-37590-score" class="comment-score"></div><div class="comment-text"><p>That's my next task. Figuring out capture and display filtering.</p><p>Thanks again</p></div><div id="comment-37590-info" class="comment-info"><span class="comment-age">(05 Nov '14, 06:57)</span> EdDickens</div></div><span id="37591"></span><div id="comment-37591" class="comment"><div id="post-37591-score" class="comment-score"></div><div class="comment-text"><p>Filtering syntax is the same for both applications (noting that capture and display filters do have a different syntax), although tshark has two display filter options; -R and -Y.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-37591-info" class="comment-info"><span class="comment-age">(05 Nov '14, 07:11)</span> grahamb ♦</div></div></div><div id="comment-tools-37586" class="comment-tools"></div><div class="clear"></div><div id="comment-37586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

