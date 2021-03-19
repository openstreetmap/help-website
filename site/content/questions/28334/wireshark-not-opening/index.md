+++
type = "question"
title = "Wireshark not opening?"
description = '''Hello i am using MAC Mavericks system.i have installed wireshark .dmg and x11 .dmg .but in Xterm when I&#x27;m trying to open wireshark ,using the command  bash-3.2$ open/Applications/Wireshark.app/ i get the following message. bash: open/Applications/Wireshark.app/: No such file or directory. I am a new...'''
date = "2013-12-22T22:44:00Z"
lastmod = "2013-12-23T15:31:00Z"
weight = 28334
keywords = [ "osx", "wireshark" ]
aliases = [ "/questions/28334" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark not opening?](/questions/28334/wireshark-not-opening)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28334-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello i am using MAC Mavericks system.i have installed wireshark .dmg and x11 .dmg .but in Xterm when I'm trying to open wireshark ,using the command<br />
bash-3.2$ open/Applications/Wireshark.app/ i get the following message. bash: open/Applications/Wireshark.app/: No such file or directory.</p><p>I am a newbie in wireshark.please help me .I am trying to open wireshark actually</p></div><div id="question-tags" class="tags-container tags">osx wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '13, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/f8567d265d3a5aca94d6f8922ce91303?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="surajkthomas&#39;s gravatar image" /><p>surajkthomas<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="surajkthomas has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-28334" class="comments-container"></div><div id="comment-tools-28334" class="comment-tools"></div><div class="clear"></div><div id="comment-28334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28350"></span>

<div id="answer-container-28350" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28350-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try</p><pre><code>open /Applications/Wireshark.app</code></pre><p>instead.</p><p>At the command line (UN*X, like OS X, or Windows), spaces are significant; they separate the command from its arguments and separate the arguments from one another. The command is <code>open</code>, and the argument is <code>/Applications/Wireshark.app</code> (the trailing slash isn't necessary).</p><p>(The same answer was given <a href="http://stackoverflow.com/questions/20738416/wireshark-not-opening-in-x11-terminal/20738721">when you asked on Stack Overflow</a>.)</p><p>This is not a Wireshark question, it's a "how do I use the <code>open</code> command" question; the same answer would apply to trying to open anything <em>else</em> with the <code>open</code> command. You can also open it, of course, by double-clicking on the Wireshark icon in the /Applications folder.</p><p>You also don't need to use xterm; OS X has its own command-window program, Terminal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '13, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-28350" class="comments-container"></div><div id="comment-tools-28350" class="comment-tools"></div><div class="clear"></div><div id="comment-28350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

