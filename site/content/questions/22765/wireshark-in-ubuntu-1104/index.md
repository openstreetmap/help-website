+++
type = "question"
title = "wireshark in ubuntu 11.04"
description = '''I have tried to install Wireshark in the usual way: #sudo apt-get install wireshark. It didn&#x27;t work. I think that&#x27;s because Ubuntu 11.04 is not supported anymore. But I need to use it, because my VM with Ubuntu 11.04 is customized to my application. What should I do? Please, I need a step to step pr...'''
date = "2013-07-09T13:09:00Z"
lastmod = "2013-07-10T01:01:00Z"
weight = 22765
keywords = [ "ubuntu1104", "wireshark" ]
aliases = [ "/questions/22765" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark in ubuntu 11.04](/questions/22765/wireshark-in-ubuntu-1104)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22765-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried to install Wireshark in the usual way: #sudo apt-get install wireshark. It didn't work. I think that's because Ubuntu 11.04 is not supported anymore. But I need to use it, because my VM with Ubuntu 11.04 is customized to my application. What should I do? Please, I need a step to step procedure, because I`m a dumb user in Ubuntu. Thanks a lot. Luiz Carlos, Brazil.</p></div><div id="question-tags" class="tags-container tags">ubuntu1104 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/e004cdffc9b69132a406f846064ba13c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lobato&#39;s gravatar image" /><p>lobato<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lobato has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '13, 13:49</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22765" class="comments-container"><span id="22774"></span><div id="comment-22774" class="comment"><div id="post-22774-score" class="comment-score"></div><div class="comment-text"><p>How did it look like when you say "it didn't work"? Does APT say that Wireshark doesn't exist, or what is the error message? Have you verified that the Wireshark package is available in the repository at all (using "sudo apt-cache search wireshark")?</p></div><div id="comment-22774-info" class="comment-info"><span class="comment-age">(09 Jul '13, 16:47)</span> Jasper ♦♦</div></div></div><div id="comment-tools-22765" class="comment-tools"></div><div class="clear"></div><div id="comment-22765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22786"></span>

<div id="answer-container-22786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22786-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><h1 id="sudo-apt-get-install-wireshark.-it-didnt-work.">sudo apt-get install wireshark. It didn't work.</h1></blockquote><p>I guess, by "It didn't work" you mean the command returned with an error. If yes, please, add the error message. If no, please tell us what the problem is?</p><blockquote><p>because my VM with Ubuntu 11.04 is customized to my application.</p></blockquote><p>If it's a customized system, maybe somebody changed the install servers in /etc/apt/sources.list. Please check if that file is identical with the file in a plain Ubuntu 11.04 installation.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22786" class="comments-container"></div><div id="comment-tools-22786" class="comment-tools"></div><div class="clear"></div><div id="comment-22786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

