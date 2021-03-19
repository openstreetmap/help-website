+++
type = "question"
title = "Wireshark error wslua_count_plugins"
description = '''Each time I try to run wireshark I get this error  wireshark: symbol lookup error: wireshark: undefined symbol: wslua_count_plugins Is there any way to make it work? If you need more info ask me.'''
date = "2016-07-17T15:57:00Z"
lastmod = "2016-07-17T19:54:00Z"
weight = 54116
keywords = [ "symbol", "linux", "lookup", "error" ]
aliases = [ "/questions/54116" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark error wslua\_count\_plugins](/questions/54116/wireshark-error-wslua_count_plugins)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54116-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Each time I try to run wireshark I get this error</p><p><code>wireshark: symbol lookup error: wireshark: undefined symbol: wslua_count_plugins</code></p><p>Is there any way to make it work? If you need more info ask me.</p></div><div id="question-tags" class="tags-container tags">symbol linux lookup error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '16, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/5145cbb8d5c30d6afc96c967c8ce9fb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cloppy21&#39;s gravatar image" /><p>cloppy21<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cloppy21 has no accepted answers">0%</span></p></div></div><div id="comments-container-54116" class="comments-container"><span id="54117"></span><div id="comment-54117" class="comment"><div id="post-54117-score" class="comment-score"></div><div class="comment-text"><p>Have you built this version of Wireshark from source yourself, or is it a Wireshark binary provided by your Linux distribution or by some third party?</p></div><div id="comment-54117-info" class="comment-info"><span class="comment-age">(17 Jul '16, 17:09)</span> Guy Harris ♦♦</div></div><span id="54118"></span><div id="comment-54118" class="comment"><div id="post-54118-score" class="comment-score"></div><div class="comment-text"><p>It's provided by my Linux distribution</p></div><div id="comment-54118-info" class="comment-info"><span class="comment-age">(17 Jul '16, 18:57)</span> cloppy21</div></div></div><div id="comment-tools-54116" class="comment-tools"></div><div class="clear"></div><div id="comment-54116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54119"></span>

<div id="answer-container-54119" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54119-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Then the makers of the Linux distribution probably didn't set up their Linux build of Wireshark correctly.</p><p>That function is called if, and only if, Wireshark was built with Lua support. If it's built with Lua support, then it should 1) be linked with the Lua library and 2) have Lua as a dependency, so that when Wireshark is installed, the Lua run-time support is installed.</p><p>You should report this problem to the distribution's maintainers, and then look for your distribution's package for Lua and install that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '16, 19:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-54119" class="comments-container"><span id="54120"></span><div id="comment-54120" class="comment"><div id="post-54120-score" class="comment-score"></div><div class="comment-text"><p>Well it work now I was going to install a new Linux distribution and no problem on the new one. Thanks for answering.</p></div><div id="comment-54120-info" class="comment-info"><span class="comment-age">(17 Jul '16, 22:23)</span> cloppy21</div></div><span id="54124"></span><div id="comment-54124" class="comment"><div id="post-54124-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-54124-info" class="comment-info"><span class="comment-age">(18 Jul '16, 01:38)</span> Jaap ♦</div></div></div><div id="comment-tools-54119" class="comment-tools"></div><div class="clear"></div><div id="comment-54119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

