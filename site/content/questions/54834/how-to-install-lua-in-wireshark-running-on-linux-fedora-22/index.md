+++
type = "question"
title = "How to install LUA in Wireshark running on Linux (Fedora 22)?"
description = '''Hi I am running Wireshark 1.12.10 on Fedora 22. I want to use a dissector written by a third party, which requires LUA. Help -&amp;gt; About Wireshark states &quot;without LUA&quot;. I believe I installed Wireshark using yum install. How can I install LUA support for Wireshark? Best regards David'''
date = "2016-08-15T08:57:00Z"
lastmod = "2016-08-15T10:44:00Z"
weight = 54834
keywords = [ "lua", "dissector", "linux" ]
aliases = [ "/questions/54834" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to install LUA in Wireshark running on Linux (Fedora 22)?](/questions/54834/how-to-install-lua-in-wireshark-running-on-linux-fedora-22)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54834-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am running Wireshark 1.12.10 on Fedora 22. I want to use a dissector written by a third party, which requires LUA. Help -&gt; About Wireshark states "without LUA".</p><p>I believe I installed Wireshark using yum install. How can I install LUA support for Wireshark?</p><p>Best regards</p><p>David</p></div><div id="question-tags" class="tags-container tags">lua dissector linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '16, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p>DavidA_2015<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Aug '16, 09:06</p></div></div><div id="comments-container-54834" class="comments-container"></div><div id="comment-tools-54834" class="comment-tools"></div><div class="clear"></div><div id="comment-54834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54842"></span>

<div id="answer-container-54842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54842-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, you'll need an RPM package of Wireshark that was build with LUA support.</p><p>Form the changelog on rpmfind.net</p><ul><li>Mon Feb 02 2015 Peter Hatina [email protected] - 1.12.3-3</li><li>temporary: disable lua</li></ul><p>So that's probably why yours has no LUA support.</p><p>Or you can <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBinary.html">build your own from source</a>, or have someone do it for you..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '16, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54842" class="comments-container"></div><div id="comment-tools-54842" class="comment-tools"></div><div class="clear"></div><div id="comment-54842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

