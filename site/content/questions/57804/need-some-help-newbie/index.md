+++
type = "question"
title = "Need some help - newbie"
description = '''Hi all, I&#x27;m a student at the moment and trying to learn wireshark and can&#x27;t seem to get to grips with it, I have been asked if I can get info off a capture and I&#x27;m struggling to find the filters. Can anyone help me with a link to learn all this. I wouldn&#x27;t normally ask but I&#x27;ve googled this and watc...'''
date = "2016-12-02T15:19:00Z"
lastmod = "2016-12-04T03:42:00Z"
weight = 57804
keywords = [ "ask.wireshark.org" ]
aliases = [ "/questions/57804" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need some help - newbie](/questions/57804/need-some-help-newbie)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57804-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm a student at the moment and trying to learn wireshark and can't seem to get to grips with it, I have been asked if I can get info off a capture and I'm struggling to find the filters. Can anyone help me with a link to learn all this. I wouldn't normally ask but I've googled this and watched you tube videos and the stuff I have to get out of wireshark isn't in it and we never got any lessons on it.</p></div><div id="question-tags" class="tags-container tags">ask.wireshark.org</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '16, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/7ed2f580c89aac937f50758e067442d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Confusedguy&#39;s gravatar image" /><p>Confusedguy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Confusedguy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '16, 03:02</p></div></div><div id="comments-container-57804" class="comments-container"><span id="57819"></span><div id="comment-57819" class="comment"><div id="post-57819-score" class="comment-score"></div><div class="comment-text"><p>You need to be more precise on what the 'stuff you have to get out of wireshark' is.<br />
</p><p>Learning 'wireshark' has some prerequisites: For example having a basic knowledge of the protocols you are interested in seeing.</p><p>As there are thousands that could possibly be present we need to know what you have been asked to get out of the capture in order to provide you some help on filtering.</p></div><div id="comment-57819-info" class="comment-info"><span class="comment-age">(03 Dec '16, 11:28)</span> mrEEde</div></div><span id="57820"></span><div id="comment-57820" class="comment"><div id="post-57820-score" class="comment-score"></div><div class="comment-text"><p>We have to learn to look for configuration of devices, sequence of notable ‘events’.  Incorrect configuratio, Network faults, unusual activity. I don't even know where to start.</p></div><div id="comment-57820-info" class="comment-info"><span class="comment-age">(03 Dec '16, 11:59)</span> Confusedguy</div></div></div><div id="comment-tools-57804" class="comment-tools"></div><div class="clear"></div><div id="comment-57804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57829"></span>

<div id="answer-container-57829" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57829-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"We have to learn to look for configuration of devices, sequence of notable ‘events’. Incorrect configuration, Network faults, unusual activity. I don't even know where to start."</p><p>Well, a good start is probably using the display filter <code>_ws.expert.severity gt "Chat"</code><br />
that gives you all packets that wireshark flagged as suspicious.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '16, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-57829" class="comments-container"><span id="57834"></span><div id="comment-57834" class="comment"><div id="post-57834-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, it has shown 5 and some are black with red writing and some are red with yellow writing and one is blue. How would I be able to see the configuration of the devices?</p></div><div id="comment-57834-info" class="comment-info"><span class="comment-age">(04 Dec '16, 06:09)</span> Confusedguy</div></div><span id="57837"></span><div id="comment-57837" class="comment"><div id="post-57837-score" class="comment-score"></div><div class="comment-text"><p>Well, you certainly will not see the 'configuration' of the 'devices' in the trace. You need to spot what is unusual behaviour, compare it to what you'd expect to see in optimized configurations and draw your conclusions based on what you see in the trace. This requires a lot of experience (years) and is certainly impossible for a newbie to do. . You might get better answers if you provide the capture file in a public space like dropbox etc. But I guess the point of your teacher is not to get this (homework ?) done by others for you .<br />
</p><p>Sorry but this type of education is not something that can be done using this Q&amp;A site Regards Matthias</p></div><div id="comment-57837-info" class="comment-info"><span class="comment-age">(04 Dec '16, 06:54)</span> mrEEde</div></div></div><div id="comment-tools-57829" class="comment-tools"></div><div class="clear"></div><div id="comment-57829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

