+++
type = "question"
title = "Name resolution in Wireshark 2.2"
description = '''Does Wirehark in version 2.2x still use the PCs system files located in the Folder &#92;etc for name resolution? I had tested it with older Versions (1.8, 1.10) and there I could resolve ip addresses to names via etc&#92;hosts and port number to names via etc&#92;Services. Is this still working for Windows or L...'''
date = "2017-04-07T01:02:00Z"
lastmod = "2017-04-07T02:40:00Z"
weight = 60630
keywords = [ "nameresolution" ]
aliases = [ "/questions/60630" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Name resolution in Wireshark 2.2](/questions/60630/name-resolution-in-wireshark-22)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does Wirehark in version 2.2x still use the PCs system files located in the Folder \etc for name resolution? I had tested it with older Versions (1.8, 1.10) and there I could resolve ip addresses to names via etc\hosts and port number to names via etc\Services. Is this still working for Windows or Linux? Now I can't get it working.</p></div><div id="question-tags" class="tags-container tags">nameresolution</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '17, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/ecc4cabfe484a10c822121c8a38f655a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharky&#39;s gravatar image" /><p>wiresharky<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharky has no accepted answers">0%</span></p></div></div><div id="comments-container-60630" class="comments-container"></div><div id="comment-tools-60630" class="comment-tools"></div><div class="clear"></div><div id="comment-60630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60635"></span>

<div id="answer-container-60635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60635-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is still possible. Under normal circumstances the file in /etc/hosts should be file, UNLESS the "only use the profile 'hosts' file" is checked, or your running in a build directory, or you've set the environment variable WIRESHARK_DATA_DIR. So there are a lot of parameters influencing the actual choice of hosts file to read. And now I'm talking !WIN32 only.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '17, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60635" class="comments-container"></div><div id="comment-tools-60635" class="comment-tools"></div><div class="clear"></div><div id="comment-60635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

