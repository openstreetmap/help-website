+++
type = "question"
title = "What is the tshark equivalent of the wireshark -P command line option ?"
description = '''How can I set the path setting for the preferences file on tshark as can be done with the -P wireshark flag ? I want to be able to specify on a tshark command line which preferences file to use.'''
date = "2013-08-01T07:00:00Z"
lastmod = "2013-08-08T07:02:00Z"
weight = 23500
keywords = [ "preferences" ]
aliases = [ "/questions/23500" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the tshark equivalent of the wireshark -P command line option ?](/questions/23500/what-is-the-tshark-equivalent-of-the-wireshark-p-command-line-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23500-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I set the path setting for the preferences file on tshark as can be done with the -P wireshark flag ? I want to be able to specify on a tshark command line which preferences file to use.</p></div><div id="question-tags" class="tags-container tags">preferences</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/ca82a3a735b887d010ade8e30e6ecd54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrylHymel&#39;s gravatar image" /><p>DarrylHymel<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrylHymel has no accepted answers">0%</span></p></div></div><div id="comments-container-23500" class="comments-container"></div><div id="comment-tools-23500" class="comment-tools"></div><div class="clear"></div><div id="comment-23500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23646"></span>

<div id="answer-container-23646" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23646-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I set the path setting for the preferences file on tshark as can be done with the -P wireshark flag ?</p></blockquote><p>You cannot, as that functionality is not implemented in tshark. If you want to have that functionality, please file an enhancement request.</p><blockquote><p><a href="http://wiki.wireshark.org/ReportingBugs">http://wiki.wireshark.org/ReportingBugs</a></p></blockquote><p>In the meantime, you can only copy the personal profile directories from your personal path to the global profile directory of the user (%APPDATA%\Wireshark\profiles) and then select that profile with tshark option -C. However, that will only affect the <strong>profiles</strong>, not the preferences :-(</p><p>Or you create several batch files (as I did) for this purpose and you switch everything you need with those batch files, by copying everything to the user Wireshark directory, or by creating a junction (see mklink on Windows) for the global preferences directory (%APPDATA%\Wireshark).</p><blockquote><p>rmdir %APPDATA%\Wireshark<br />
mklink c:\wireshark\template_1 %APPDATA%\Wireshark</p></blockquote><p>while c:\wireshark\template_1 contains your preferences, profiles, etc.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23646" class="comments-container"></div><div id="comment-tools-23646" class="comment-tools"></div><div class="clear"></div><div id="comment-23646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

