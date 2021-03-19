+++
type = "question"
title = "Debug console won&#x27;t show up when opened through python"
description = '''I&#x27;m using a python program to open wireshark to use a plugin I wrote. However, the debug console won&#x27;t show up when my python program opens wireshark. If I open wireshark normally, the debug console works fine, but I need the console to open when my python program opens wireshark. Any ideas?'''
date = "2015-10-21T09:54:00Z"
lastmod = "2015-10-21T09:54:00Z"
weight = 46807
keywords = [ "debug_console" ]
aliases = [ "/questions/46807" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Debug console won't show up when opened through python](/questions/46807/debug-console-wont-show-up-when-opened-through-python)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46807-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using a python program to open wireshark to use a plugin I wrote. However, the debug console won't show up when my python program opens wireshark. If I open wireshark normally, the debug console works fine, but I need the console to open when my python program opens wireshark. Any ideas?</p></div><div id="question-tags" class="tags-container tags">debug_console</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '15, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/110b64762d70c6642030fe842d013497?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swelna&#39;s gravatar image" /><p>swelna<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swelna has no accepted answers">0%</span></p></div></div><div id="comments-container-46807" class="comments-container"><span id="46816"></span><div id="comment-46816" class="comment"><div id="post-46816-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any ideas?</p></blockquote><p>Maybe.</p><p>Some questions first:</p><ul><li>what is your OS and OS version?</li><li>what is your Wireshark version?</li><li>how do you start wireshark from your Python code?</li><li>how do you start wireshark "normally" if you see the debug console?</li></ul></div><div id="comment-46816-info" class="comment-info"><span class="comment-age">(21 Oct '15, 13:01)</span> Kurt Knochner ♦</div></div><span id="46936"></span><div id="comment-46936" class="comment"><div id="post-46936-score" class="comment-score"></div><div class="comment-text"><p>I am running Windows 7 Enterprise SP1. My Wireshark version is 1.12.0. I'm using a python subprocess with the function Popen(), however, I can't currently post my code. Finally, When I say start wireshark "normally", I mean double clicking the shortcut on my desktop.</p></div><div id="comment-46936-info" class="comment-info"><span class="comment-age">(26 Oct '15, 07:25)</span> swelna</div></div><span id="46955"></span><div id="comment-46955" class="comment"><div id="post-46955-score" class="comment-score"></div><div class="comment-text"><p>The debug console will only apprear if you start Wireshark from the GUI, as there would be no console to print messages to STDOUT and STDERR. If you call Wireshark from Python with popen(), you should be able to read STDOUT and STDERR directly (<a href="https://www.google.com/?q=python%20popen%20stdout">https://www.google.com/?q=python%20popen%20stdout</a> ). If you don't know how to do that, please ask in a Python forum, as this is more a Python question than a Wireshark question.</p></div><div id="comment-46955-info" class="comment-info"><span class="comment-age">(26 Oct '15, 13:24)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46807" class="comment-tools"></div><div class="clear"></div><div id="comment-46807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

