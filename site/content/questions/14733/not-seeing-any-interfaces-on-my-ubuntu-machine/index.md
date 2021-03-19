+++
type = "question"
title = "Not seeing any interfaces on my Ubuntu machine"
description = '''Hello, I am using wireshark on a laptop do I need to install anything extra to get it to capture packets going through my wireless network card? When I go to intrefaces it says there is no interfaces. I am running wiresahrk 1.8.2 on Ubuntu. Thanks,'''
date = "2012-10-05T06:58:00Z"
lastmod = "2012-10-05T12:12:00Z"
weight = 14733
keywords = [ "wireless", "network" ]
aliases = [ "/questions/14733" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Not seeing any interfaces on my Ubuntu machine](/questions/14733/not-seeing-any-interfaces-on-my-ubuntu-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14733-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am using wireshark on a laptop do I need to install anything extra to get it to capture packets going through my wireless network card?</p><p>When I go to intrefaces it says there is no interfaces.</p><p>I am running wiresahrk 1.8.2 on Ubuntu.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">wireless network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '12, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/865c8ff61c8626647de2b885a59567e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rob123&#39;s gravatar image" /><p>rob123<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rob123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Oct '12, 11:31</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-14733" class="comments-container"></div><div id="comment-tools-14733" class="comment-tools"></div><div class="clear"></div><div id="comment-14733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14734"></span>

<div id="answer-container-14734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14734-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should either run Wireshark as root, or have a look on document <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a> for other ways to capture packets as non-root user.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '12, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/477ab2a2074857c0bb7d051f3c49f676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jurij%20Sikorsky&#39;s gravatar image" /><p>Jurij Sikorsky<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jurij Sikorsky has no accepted answers">0%</span></p></div></div><div id="comments-container-14734" class="comments-container"><span id="14739"></span><div id="comment-14739" class="comment"><div id="post-14739-score" class="comment-score"></div><div class="comment-text"><p>Note that running as root is not recommended, hence the warnings that Wireshark issues when you do so.</p></div><div id="comment-14739-info" class="comment-info"><span class="comment-age">(05 Oct '12, 12:11)</span> grahamb ♦</div></div><span id="14742"></span><div id="comment-14742" class="comment"><div id="post-14742-score" class="comment-score"></div><div class="comment-text"><p>&lt;rant&gt;And it would be great if the distribtion packagers would provide the means to easily setup these privileges...&lt;/rant&gt; Thanks Balint for the Debian package.</p></div><div id="comment-14742-info" class="comment-info"><span class="comment-age">(05 Oct '12, 14:35)</span> Jaap ♦</div></div></div><div id="comment-tools-14734" class="comment-tools"></div><div class="clear"></div><div id="comment-14734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14740"></span>

<div id="answer-container-14740" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14740-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See this similar question: <a href="http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed">ubuntu machine no interfaces listed</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '12, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-14740" class="comments-container"></div><div id="comment-tools-14740" class="comment-tools"></div><div class="clear"></div><div id="comment-14740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

