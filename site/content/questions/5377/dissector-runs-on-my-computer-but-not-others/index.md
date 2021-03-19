+++
type = "question"
title = "Dissector Runs on My computer, but not others"
description = '''I compiled the AMIN dissector as given at: http://www.codeproject.com/KB/IP/custom_dissector.aspx The dissector dll runs fine on both my compiled version and the binary version posted on The wireshark website under the downloads section (both are on the same computer). When I copy the amin.dll over ...'''
date = "2011-08-01T09:41:00Z"
lastmod = "2011-08-01T13:42:00Z"
weight = 5377
keywords = [ "windows", "dissector", "amin" ]
aliases = [ "/questions/5377" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector Runs on My computer, but not others](/questions/5377/dissector-runs-on-my-computer-but-not-others)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5377-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I compiled the AMIN dissector as given at:</p><p>http://www.codeproject.com/KB/IP/custom_dissector.aspx</p><p>The dissector dll runs fine on both my compiled version and the binary version posted on The wireshark website under the downloads section (both are on the same computer). When I copy the amin.dll over to my coworkers computer, and place it under</p><p>"C:Document and SettingsJohn SmithApplication DataWiresharkpluginsamin.dll"</p><p>and then run Wireshark, it tells me</p><p>"Couldn't load module C:Dou...pluginsamin.dll... The specified module could not be found."</p><p>I have tried compiling the dissector with both VC++ 2005, and VC++ 2010EE and neither work on his computer. The one compiled with VC++ 2005 will not work on my computer either unless I use the version of Wireshark that I compiled, which is fine, and to be expected.</p><p>Thank you for your time,</p><p>Brandon</p></div><div id="question-tags" class="tags-container tags">windows dissector amin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '11, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p>officialhopsof<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '11, 16:06</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5377" class="comments-container"></div><div id="comment-tools-5377" class="comment-tools"></div><div class="clear"></div><div id="comment-5377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5381"></span>

<div id="answer-container-5381" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5381-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The VC++ Redistributable package was not installed on that computer. Once it was installed the Dissector ran properly.</p><p>Thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '11, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p>officialhopsof<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span></p></div></div><div id="comments-container-5381" class="comments-container"></div><div id="comment-tools-5381" class="comment-tools"></div><div class="clear"></div><div id="comment-5381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5378"></span>

<div id="answer-container-5378" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5378-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does the DLL as copied to your coworkers computer have "reasonable" permissions ?</p><p>The error message indicates that the DLL name was found in the directory but attempting to load the DLL failed ("... could not be found").</p><p>(I'm not exactly sure what "reasonable permissions" would be, i.e., what is required for Wireshark to be able to load the DLL, but certainly the DLL must at least be readable for the account on your coworkers computer).</p><p>On a separate note:</p><p>Is your coworker running a 1.6 version of Wireshark ? (I'm assuming that you built your dissector from SVN).</p><p>In general, plugins are not guaranteed to run properly if not compiled with the sources for the same major version of Wireshark as the version of the binary Wireshark being used. (I think using SVN, i.e., 1.7 to build the plugin and using the plugin on 1.6 should be OK).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '11, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '11, 11:50</p></div></div><div id="comments-container-5378" class="comments-container"></div><div id="comment-tools-5378" class="comment-tools"></div><div class="clear"></div><div id="comment-5378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

