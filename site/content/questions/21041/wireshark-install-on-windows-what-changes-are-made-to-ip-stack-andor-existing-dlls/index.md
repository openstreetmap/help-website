+++
type = "question"
title = "Wireshark install on WIndows - what changes are made to IP Stack and/or existing .dlls?"
description = '''In trying to track down HTTP protocol errors, we installed Wireshark on 3 Windows 2008 R2 servers. Prior to installing Wireshark, specific HTTP traffic would fail. Immediately upon installing Wireshark, the problematic HTTP traffic worked as expected. Even after uninstalling Wireshark, the initially...'''
date = "2013-05-08T14:53:00Z"
lastmod = "2013-05-08T17:26:00Z"
weight = 21041
keywords = [ "ip", ".dll", "stack" ]
aliases = [ "/questions/21041" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark install on WIndows - what changes are made to IP Stack and/or existing .dlls?](/questions/21041/wireshark-install-on-windows-what-changes-are-made-to-ip-stack-andor-existing-dlls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21041-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In trying to track down HTTP protocol errors, we installed Wireshark on 3 Windows 2008 R2 servers. Prior to installing Wireshark, specific HTTP traffic would fail. Immediately upon installing Wireshark, the problematic HTTP traffic worked as expected. Even after uninstalling Wireshark, the initially problematic HTTP traffic continued to work.</p><p>I'm wondering if the Wireshark installation makes changes to the IP stack or any existing .dlls. I'd like to compare against the 2008 R2 servers that continue to have HTTP issues. It could just be a coincidence, but I want to confirm.</p></div><div id="question-tags" class="tags-container tags">ip .dll stack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '13, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/4472e87244bb75c67eaf24bdd270563f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbright&#39;s gravatar image" /><p>jbright<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbright has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '13, 17:27</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-21041" class="comments-container"><span id="21043"></span><div id="comment-21043" class="comment"><div id="post-21043-score" class="comment-score"></div><div class="comment-text"><blockquote><p>HTTP protocol errors,<br />
specific HTTP traffic would fail.</p></blockquote><p>what is the nature of those protocol errors and what kind of HTTP traffic failed (how did it fail)?</p></div><div id="comment-21043-info" class="comment-info"><span class="comment-age">(08 May '13, 17:42)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-21041" class="comment-tools"></div><div class="clear"></div><div id="comment-21041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21042"></span>

<div id="answer-container-21042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21042-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Windows Wireshark installer runs the <a href="http://www.winpcap.org">WinPcap</a> installer; WinPcap installs a transport driver (which <em>shouldn't</em> affect other parts of the networking stack) and its own DLLs, but doesn't modify any existing DLLs. Wireshark <em>itself</em> does nothing to the networking stack or any system DLLs.</p><p>When you uninstalled Wireshark, did you also uninstall WinPcap? (Check whether "WinPcap 4.1.2" is installed.)</p><p>Perhaps something about WinPcap is making the problem go away. You could try downloading and installing WinPcap on the servers that are still having issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '13, 17:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-21042" class="comments-container"><span id="21058"></span><div id="comment-21058" class="comment"><div id="post-21058-score" class="comment-score"></div><div class="comment-text"><p>I uninstalled both Wireshark and WinPcap, so in theory, if either of those magically resolved the issue, the issue would return once they were uninstalled.</p></div><div id="comment-21058-info" class="comment-info"><span class="comment-age">(09 May '13, 08:37)</span> jbright</div></div></div><div id="comment-tools-21042" class="comment-tools"></div><div class="clear"></div><div id="comment-21042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

