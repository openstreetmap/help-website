+++
type = "question"
title = "Debug console not working"
description = '''I&#x27;m working on a plugin and want to display debug data. I&#x27;ve done this before with another plugin I built a couple of years ago, but now I can&#x27;t even get the debug console to display! I&#x27;ve got the preference set correctly (&quot;always&quot;), but the only time a debug console is displayed is the first time a...'''
date = "2012-07-23T11:57:00Z"
lastmod = "2012-07-23T12:33:00Z"
weight = 12928
keywords = [ "debug", "console" ]
aliases = [ "/questions/12928" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Debug console not working](/questions/12928/debug-console-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12928-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on a plugin and want to display debug data. I've done this before with another plugin I built a couple of years ago, but now I can't even get the debug console to display! I've got the preference set correctly ("always"), but the only time a debug console is displayed is the first time after I install Wireshark. When I close WS and open it again there's no debug console. I've done everything I can thing of and can't get it to work. I'm currently using 1.8.0, but had the same problem in 1.6.7. I'm guessing the problem is peculiar to my installation because I just tried 1.6.7 on another PC I use WS on (but don't develop on it). Any ideas?</p></div><div id="question-tags" class="tags-container tags">debug console</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '12, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/cb936d309bcc49f1d4fb3bfd0b9f5f69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddwashbu&#39;s gravatar image" /><p>ddwashbu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddwashbu has no accepted answers">0%</span></p></div></div><div id="comments-container-12928" class="comments-container"></div><div id="comment-tools-12928" class="comment-tools"></div><div class="clear"></div><div id="comment-12928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12930"></span>

<div id="answer-container-12930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12930-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I do get the debug console every time when I open Wireshark (1.8.0) on Windows 7.</p><blockquote><p>I'm guessing the problem is peculiar to my installation because</p></blockquote><p>I agree. Is there any <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> (AV, Desktop Firewall, Endpoint Protection, IDS, etc.) installed on your computer? If so, please uninstall it and try again. Maybe one of those tools blocks the debug console.</p><p>BTW: What is your OS?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12930" class="comments-container"><span id="12931"></span><div id="comment-12931" class="comment"><div id="post-12931-score" class="comment-score"></div><div class="comment-text"><p>Windows XP in a corporate environment, so lots of stuff like McAfee that I can't remove.</p><p>Would you happen to know which source code module WS uses to launch the debug console. I may have to poke around a build WS with some added debug statements.</p></div><div id="comment-12931-info" class="comment-info"><span class="comment-age">(23 Jul '12, 13:42)</span> ddwashbu</div></div><span id="12968"></span><div id="comment-12968" class="comment"><div id="post-12968-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Would you happen to know which source code module WS uses to launch the debug console.</p></blockquote><p>Please see here:<br />
</p><blockquote><p><code>http://anonsvn.wireshark.org/wireshark/trunk/ui/gtk/main.c</code><br />
<code>void create_console(void)</code></p></blockquote></div><div id="comment-12968-info" class="comment-info"><span class="comment-age">(24 Jul '12, 12:21)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12930" class="comment-tools"></div><div class="clear"></div><div id="comment-12930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

