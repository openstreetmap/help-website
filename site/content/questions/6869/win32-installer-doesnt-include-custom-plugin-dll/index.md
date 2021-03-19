+++
type = "question"
title = "win32 Installer doesn&#x27;t include custom plugin dll"
description = '''I created a dissector for my protocol and recompiled wireshark (1.6.2) using VS 2010. Everything works fine except when I try to create an installer. The dll for my custom plugin is not included. I&#x27;ve changed everything in the ...packagingnsis directory to add the plugin (Custom.nmake, custom_plugin...'''
date = "2011-10-12T07:57:00Z"
lastmod = "2011-10-12T19:29:00Z"
weight = 6869
keywords = [ "win32", "installer", "dll", "plugin" ]
aliases = [ "/questions/6869" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [win32 Installer doesn't include custom plugin dll](/questions/6869/win32-installer-doesnt-include-custom-plugin-dll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6869-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created a dissector for my protocol and recompiled wireshark (1.6.2) using VS 2010. Everything works fine except when I try to create an installer. The dll for my custom plugin is not included. I've changed everything in the ...packagingnsis directory to add the plugin (Custom.nmake, custom_plugins, Makefile.nmake, etc). Is there another file that needs modified?</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags">win32 installer dll plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '11, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p>brwiese<br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-6869" class="comments-container"></div><div id="comment-tools-6869" class="comment-tools"></div><div class="clear"></div><div id="comment-6869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6876"></span>

<div id="answer-container-6876" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6876-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Refer to <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.plugins?revision=34921&amp;view=markup">README.plugins</a>, in particular section 3.7.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '11, 19:29</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6876" class="comments-container"></div><div id="comment-tools-6876" class="comment-tools"></div><div class="clear"></div><div id="comment-6876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6870"></span>

<div id="answer-container-6870" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6870-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To include your plugin dll in a custom Wireshark installer, you need to update both <code>Makefile.nmake</code> and <code>wireshark.nsi</code> under <code>packaging/nsis/</code>. Add your dll to the list in <code>Makefile.nmake</code> that starts around line 47, and to the list in <code>wireshark.nsi</code> on about line 900.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '11, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-6870" class="comments-container"></div><div id="comment-tools-6870" class="comment-tools"></div><div class="clear"></div><div id="comment-6870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

