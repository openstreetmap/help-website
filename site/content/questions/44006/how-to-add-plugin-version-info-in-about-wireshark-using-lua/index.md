+++
type = "question"
title = "How to add plugin version info in &quot;About Wireshark&quot; Using Lua"
description = ''' As mentioned in above figure If i want to display my lua scipt&#x27;s version in About Wireshark. How can i do that? Is there any LUA API Available for this?'''
date = "2015-07-09T04:11:00Z"
lastmod = "2016-05-03T03:46:00Z"
weight = 44006
keywords = [ "ui_about_wireshark", "lua", "plugin" ]
aliases = [ "/questions/44006" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to add plugin version info in "About Wireshark" Using Lua](/questions/44006/how-to-add-plugin-version-info-in-about-wireshark-using-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44006-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/about_wireshark.png" alt="alt text" /></p><p>As mentioned in above figure If i want to display my lua scipt's version in About Wireshark. How can i do that? Is there any LUA API Available for this?</p></div><div id="question-tags" class="tags-container tags">ui_about_wireshark lua plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '15, 15:32</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-44006" class="comments-container"></div><div id="comment-tools-44006" class="comment-tools"></div><div class="clear"></div><div id="comment-44006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44008"></span>

<div id="answer-container-44008" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44008-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No not yet. There's an open enhancement request in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11315">bugs.wireshark.org, as bug 11315</a>. It won't be available until version 2.0, however.</p><p>And it's not guaranteed to work the way it is suggested to in that enhancement request - it might just be implemented as a Lua function call instead of table attribute.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '15, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44008" class="comments-container"><span id="44012"></span><div id="comment-44012" class="comment"><div id="post-44012-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks for info @hadriel But If my plugin is developed let's say using C language then how to set version of my own added plugin into this?</p></div><div id="comment-44012-info" class="comment-info"><span class="comment-age">(09 Jul '15, 08:21)</span> ankit</div></div><span id="44017"></span><div id="comment-44017" class="comment"><div id="post-44017-score" class="comment-score"></div><div class="comment-text"><p>It's in the moduleinfo.h file for each plugin</p></div><div id="comment-44017-info" class="comment-info"><span class="comment-age">(09 Jul '15, 09:28)</span> grahamb ♦</div></div><span id="44026"></span><div id="comment-44026" class="comment"><div id="post-44026-score" class="comment-score"></div><div class="comment-text"><p>Thanks @grahamb I got it now.</p></div><div id="comment-44026-info" class="comment-info"><span class="comment-age">(09 Jul '15, 19:56)</span> ankit</div></div></div><div id="comment-tools-44008" class="comment-tools"></div><div class="clear"></div><div id="comment-44008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52171"></span>

<div id="answer-container-52171" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52171-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>see: <a href="https://ask.wireshark.org/questions/43375/display-a-version-number-for-lua-dissector">https://ask.wireshark.org/questions/43375/display-a-version-number-for-lua-dissector</a></p><p>short version: Example Lua code:</p><pre><code>local my_info = 
{
    version = &quot;1.0.1&quot;,
    author = &quot;Jane Doe&quot;,
    description = &quot;this plugin parses rainbows&quot;,
    repository = &quot;https://github.com/octocat/Spoon-Knife&quot;
}

set_plugin_info(my_info)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/28d0f2e999fefc0514aee9223bc9fa83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KamratKalasson&#39;s gravatar image" /><p>KamratKalasson<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KamratKalasson has no accepted answers">0%</span></p></div></div><div id="comments-container-52171" class="comments-container"></div><div id="comment-tools-52171" class="comment-tools"></div><div class="clear"></div><div id="comment-52171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

