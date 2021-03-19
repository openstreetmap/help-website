+++
type = "question"
title = "Does Wireshark Calculate Application Turns?"
description = '''Hi all...  I&#x27;m analyzing a home-grown application that uses SSL. I do not have the Private Key, so there is no way to isolate requests and responses, except for identifying where the &quot;Application Data&quot; changes direction. I can do that manually, and I often do for small-ish captures. But I&#x27;m now look...'''
date = "2017-02-01T13:07:00Z"
lastmod = "2017-02-04T23:08:00Z"
weight = 59230
keywords = [ "application_turns" ]
aliases = [ "/questions/59230" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark Calculate Application Turns?](/questions/59230/does-wireshark-calculate-application-turns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59230-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all...<br />
</p><p>I'm analyzing a home-grown application that uses SSL. I do not have the Private Key, so there is no way to isolate requests and responses, except for identifying where the "Application Data" changes direction. I can do that manually, and I often do for small-ish captures.</p><p>But I'm now looking at a ~1600-packet capture (1 TCP connection), and it would be helpful if I could determine how many application turns occur in this connection.</p><p>I <em>thought</em> I saw some Wireshark screen, at some point, that tallied Application Turns. For the life of me, I cannot find such a screen now.</p><p>Was I dreaming? Or, does Wireshark calculate App Turns and make it available somewhere.</p><p>Thx!!</p><p>feenyman99</p></div><div id="question-tags" class="tags-container tags">application_turns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '17, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span> </br></p></div></div><div id="comments-container-59230" class="comments-container"></div><div id="comment-tools-59230" class="comment-tools"></div><div class="clear"></div><div id="comment-59230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59251"></span>

<div id="answer-container-59251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59251-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at a plugin called TRANSUM. See <a href="https://community.tribelab.com/course/view.php?id=9">https://community.tribelab.com/course/view.php?id=9</a></p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '17, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-59251" class="comments-container"><span id="59253"></span><div id="comment-59253" class="comment"><div id="post-59253-score" class="comment-score"></div><div class="comment-text"><p>If you are referring to the code than this <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=plugins/transum;hb=HEAD">open link to the Wireshark code</a> would be more appropriate than a login required site.</p></div><div id="comment-59253-info" class="comment-info"><span class="comment-age">(05 Feb '17, 00:50)</span> Jaap ♦</div></div><span id="59254"></span><div id="comment-59254" class="comment"><div id="post-59254-score" class="comment-score"></div><div class="comment-text"><p>@Jaap Good point re the Wireshark code. The only problem is that feenyman99 would have to run a dev version of Wireshark to get TRANSUM. Whichever way he goes, the documentation on TribeLab accurately describes TRANSUM and is accessible without login.</p><p>Registering on TribeLab for access to the transum.dll or transum.lue plugin is completely free.</p></div><div id="comment-59254-info" class="comment-info"><span class="comment-age">(05 Feb '17, 01:11)</span> PaulOfford</div></div></div><div id="comment-tools-59251" class="comment-tools"></div><div class="clear"></div><div id="comment-59251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

