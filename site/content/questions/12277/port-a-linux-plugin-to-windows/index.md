+++
type = "question"
title = "Port a linux plugin to windows"
description = '''Is there any easy way for me to make the .dll file from what i already have in linux? From what I read, I&#x27;d have to build wireshark in windows but it&#x27;d take me a while to get all the necessary tools and set up the environment. Is there an easier method to get a plugin working on a windows platform? ...'''
date = "2012-06-28T09:23:00Z"
lastmod = "2012-06-28T09:55:00Z"
weight = 12277
keywords = [ "windows", "linux", "so", "dll" ]
aliases = [ "/questions/12277" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Port a linux plugin to windows](/questions/12277/port-a-linux-plugin-to-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12277-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any easy way for me to make the .dll file from what i already have in linux? From what I read, I'd have to build wireshark in windows but it'd take me a while to get all the necessary tools and set up the environment. Is there an easier method to get a plugin working on a windows platform? And yes my plugin works fine and I was able to use the .so file to work on other computers with linux.</p></div><div id="question-tags" class="tags-container tags">windows linux so dll</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '12, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/9370e965a8cb362339126710f94fd714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rewindmad&#39;s gravatar image" /><p>rewindmad<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rewindmad has no accepted answers">0%</span></p></div></div><div id="comments-container-12277" class="comments-container"></div><div id="comment-tools-12277" class="comment-tools"></div><div class="clear"></div><div id="comment-12277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12278"></span>

<div id="answer-container-12278" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12278-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The easy answer is to submit the plugin to the Wireshark developers and put it in the core. The devs will then maintain it for you and the Wireshark build ecosystem will produce all the various builds.</p><p>If you must keep the plugin private, then your only option is to set up a Windows build environment. Follow the instructions in the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> to the letter and you'll be fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '12, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-12278" class="comments-container"></div><div id="comment-tools-12278" class="comment-tools"></div><div class="clear"></div><div id="comment-12278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

