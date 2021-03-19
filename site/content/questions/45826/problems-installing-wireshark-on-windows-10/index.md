+++
type = "question"
title = "Problems installing Wireshark on Windows 10"
description = '''When attempting to install Wireshark 1.12.7 on Windows 10 x64 I am getting an error when the program attempts to begin installing a box pops up that says there is an error reading &quot;Error opening file for writing: C:&#92;Program FIles&#92;Wireshark&#92;uninstall.exe Click abort to stop installation, retry to try...'''
date = "2015-09-14T06:45:00Z"
lastmod = "2015-09-14T10:52:00Z"
weight = 45826
keywords = [ "installation", "windows10", "x64" ]
aliases = [ "/questions/45826" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problems installing Wireshark on Windows 10](/questions/45826/problems-installing-wireshark-on-windows-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45826-score" class="post-score" title="current number of votes">0</div><span id="post-45826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When attempting to install Wireshark 1.12.7 on Windows 10 x64 I am getting an error when the program attempts to begin installing a box pops up that says there is an error reading "Error opening file for writing: C:\Program FIles\Wireshark\uninstall.exe Click abort to stop installation, retry to try again, or ignore to skip this file."</p><p>When I click abort the installation stops, when I click retry the window just pops up again and when I click ignore the exact same window pops up except with the name of the next file the installer is trying to write.</p><p>Please help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-windows10" rel="tag" title="see questions tagged &#39;windows10&#39;">windows10</span> <span class="post-tag tag-link-x64" rel="tag" title="see questions tagged &#39;x64&#39;">x64</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/8a98fe5f2d8eb1f8c6249fa82732317a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bentoj&#39;s gravatar image" /><p><span>bentoj</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bentoj has no accepted answers">0%</span></p></div></div><div id="comments-container-45826" class="comments-container"></div><div id="comment-tools-45826" class="comment-tools"></div><div class="clear"></div><div id="comment-45826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45829"></span>

<div id="answer-container-45829" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45829-score" class="post-score" title="current number of votes">0</div><span id="post-45829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a process is interfering. Did you try to install it with your antivirus / security software deactivated? because fore installing, do you confirm that you do not have any Program Files\Wireshark folder (that could remain from a previous installation attempt)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '15, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '15, 10:25</strong> </span></p></div></div><div id="comments-container-45829" class="comments-container"><span id="45830"></span><div id="comment-45830" class="comment"><div id="post-45830-score" class="comment-score"></div><div class="comment-text"><p>I tried that and it didn't work, but that's OK because it led me to the solution. I just had to run the installer as administrator, which I guess exactly what you suggested. Bypass firewalls and anti-virus.</p><p>Thanks for your suggestion!</p></div><div id="comment-45830-info" class="comment-info"><span class="comment-age">(14 Sep '15, 10:52)</span> <span class="comment-user userinfo">bentoj</span></div></div></div><div id="comment-tools-45829" class="comment-tools"></div><div class="clear"></div><div id="comment-45829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

