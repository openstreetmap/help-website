+++
type = "question"
title = "How to stop wireshark using command line interface in centos 6.3?"
description = '''I have a script that I run to perform some testing and while I start that script I want to issue a command to start wireshark which I have.  Now I want to add a line at the end of the script to STOP wireshark. Can anyone guide me on how to stop wireshark in cli? My script executes sometimes in 1 hou...'''
date = "2013-02-28T07:17:00Z"
lastmod = "2013-02-28T09:51:00Z"
weight = 18978
keywords = [ "capture", "stopwireshark", "stop" ]
aliases = [ "/questions/18978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to stop wireshark using command line interface in centos 6.3?](/questions/18978/how-to-stop-wireshark-using-command-line-interface-in-centos-63)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a script that I run to perform some testing and while I start that script I want to issue a command to start wireshark which I have.</p><p>Now I want to add a line at the end of the script to STOP wireshark. Can anyone guide me on how to stop wireshark in cli?</p><p>My script executes sometimes in 1 hour and sometimes in 20min so my time is not definitive.</p><p>Hope some one could help me!</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture stopwireshark stop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/5345ae9bc5c87550aacda525d9e7d608?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sipguy&#39;s gravatar image" /><p>sipguy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sipguy has no accepted answers">0%</span></p></div></div><div id="comments-container-18978" class="comments-container"></div><div id="comment-tools-18978" class="comment-tools"></div><div class="clear"></div><div id="comment-18978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18984"></span>

<div id="answer-container-18984" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18984-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Now I want to add a line at the end of the script to STOP wireshark.</p></blockquote><p>try this: <code>killall wireshark</code><br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18984" class="comments-container"><span id="18988"></span><div id="comment-18988" class="comment"><div id="post-18988-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt,</p><p>But I have other users who run in the root mode so I have multiple wireshark pids which get killed by this.</p><p>IS there an alternative to it?</p></div><div id="comment-18988-info" class="comment-info"><span class="comment-age">(28 Feb '13, 10:33)</span> sipguy</div></div><span id="18989"></span><div id="comment-18989" class="comment"><div id="post-18989-score" class="comment-score"></div><div class="comment-text"><p>how do you start Wireshark in your script? Can you please post that part of the script?</p></div><div id="comment-18989-info" class="comment-info"><span class="comment-age">(28 Feb '13, 11:28)</span> Kurt Knochner ♦</div></div><span id="18993"></span><div id="comment-18993" class="comment"><div id="post-18993-score" class="comment-score"></div><div class="comment-text"><p>"But I have other users who run in the root mode..."</p><p><a href="https://blog.wireshark.org/2010/02/running-wireshark-as-you/">Haven't you heard</a> you should not do that?</p></div><div id="comment-18993-info" class="comment-info"><span class="comment-age">(28 Feb '13, 14:21)</span> Jaap ♦</div></div></div><div id="comment-tools-18984" class="comment-tools"></div><div class="clear"></div><div id="comment-18984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

