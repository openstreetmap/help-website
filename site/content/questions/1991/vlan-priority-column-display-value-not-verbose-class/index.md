+++
type = "question"
title = "VLAN Priority Column Display Value not Verbose Class"
description = '''Is there a way to create a column for Ethernet VLAN priority that displays the value (e.g. 0-7 decimal or 000-111 binary) instead of the verbose traffic class? I am capturing traffic and exporting to CSV for Excel analysis and graphing. I can export the verbose and then do a search and replace, or f...'''
date = "2011-01-28T09:31:00Z"
lastmod = "2011-01-28T09:41:00Z"
weight = 1991
keywords = [ "priority", "vlan" ]
aliases = [ "/questions/1991" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VLAN Priority Column Display Value not Verbose Class](/questions/1991/vlan-priority-column-display-value-not-verbose-class)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1991-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to create a column for Ethernet VLAN priority that displays the value (e.g. 0-7 decimal or 000-111 binary) instead of the verbose traffic class?</p><p>I am capturing traffic and exporting to CSV for Excel analysis and graphing. I can export the verbose and then do a search and replace, or formula to glean the value, but that adds a significant amount of post-processing work that could be avoided if Wireshark just displayed the binary or decimal PCP value.</p></div><div id="question-tags" class="tags-container tags">priority vlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '11, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/6d94c0537e1678875e63a431b1fd1c90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nick%20Del%20Regno&#39;s gravatar image" /><p>Nick Del Regno<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nick Del Regno has no accepted answers">0%</span></p></div></div><div id="comments-container-1991" class="comments-container"></div><div id="comment-tools-1991" class="comment-tools"></div><div class="clear"></div><div id="comment-1991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1992"></span>

<div id="answer-container-1992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right-click on the column-title and de-select "Show Resolved" (not sure if this is available in 1.4.x though, you might need to install 1.5.0 for it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '11, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1992" class="comments-container"><span id="1995"></span><div id="comment-1995" class="comment"><div id="post-1995-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply. I am using a Spirent modified version of 1.4.2 (for their signature decodes) and no "Show Resolved" option exists... Oh well.</p></div><div id="comment-1995-info" class="comment-info"><span class="comment-age">(28 Jan '11, 10:53)</span> Nick Del Regno</div></div><span id="1998"></span><div id="comment-1998" class="comment"><div id="post-1998-score" class="comment-score"></div><div class="comment-text"><p>The "Show Unresolved" option has only been in development versions at the moment. It will apparently be included in the official releas of V1.6.0.</p></div><div id="comment-1998-info" class="comment-info"><span class="comment-age">(28 Jan '11, 11:11)</span> KeithFrench</div></div><span id="1999"></span><div id="comment-1999" class="comment"><div id="post-1999-score" class="comment-score"></div><div class="comment-text"><p>If you can't run 1.5.0, you might be able to use tshark to get what you need.</p><p>Try something like:</p><p>tshark -r &lt;file&gt; -T fields -e frame.number -e frame.time -e vlan.id -e vlan.priority -e ip.src -e ip.dst -e ... &gt; out.txt</p><p>All fields are by default separated by a TAB character which makes importing in Excel pretty easy.</p></div><div id="comment-1999-info" class="comment-info"><span class="comment-age">(28 Jan '11, 11:58)</span> SYN-bit ♦♦</div></div><span id="2008"></span><div id="comment-2008" class="comment"><div id="post-2008-score" class="comment-score"></div><div class="comment-text"><p>Thanks folks for the info. SYNbit, I tried that and it will do the job until "Show Unresolved" is added to an official release. Thanks!</p></div><div id="comment-2008-info" class="comment-info"><span class="comment-age">(29 Jan '11, 08:42)</span> Nick Del Regno</div></div></div><div id="comment-tools-1992" class="comment-tools"></div><div class="clear"></div><div id="comment-1992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

