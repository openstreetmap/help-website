+++
type = "question"
title = "Has anyone got the ethers file to work in version 1.10.5?"
description = '''I am slowly working my way through the Wireshark Network Analysis book. I am trying to replicate the example on page 166 Chapter 5. The example figure 98 shows ethers.txt I created both files one without and one with a file extension. Both in my profiles directory. I have tried restarting Wireshark ...'''
date = "2013-12-22T09:29:00Z"
lastmod = "2013-12-22T10:21:00Z"
weight = 28322
keywords = [ "ethers", "preferences" ]
aliases = [ "/questions/28322" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Has anyone got the ethers file to work in version 1.10.5?](/questions/28322/has-anyone-got-the-ethers-file-to-work-in-version-1105)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28322-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am slowly working my way through the Wireshark Network Analysis book. I am trying to replicate the example on page 166 Chapter 5. The example figure 98 shows ethers.txt I created both files one without and one with a file extension. Both in my profiles directory. I have tried restarting Wireshark but I am unable to get Wireshark to recognize the name of my NIC.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_10.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture1.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ethers preferences</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/5b20990cd21bd091665e684410ebe9fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdJ&#39;s gravatar image" /><p>EdJ<br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdJ has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Dec '13, 10:26</p></div></div><div id="comments-container-28322" class="comments-container"></div><div id="comment-tools-28322" class="comment-tools"></div><div class="clear"></div><div id="comment-28322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28325"></span>

<div id="answer-container-28325" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28325-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Verify that the preference to enable MAC address resolution is enabled in the profile you're using. Do this via: <code>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Resolve MAC addresses</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '13, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></img></div></div><div id="comments-container-28325" class="comments-container"><span id="28326"></span><div id="comment-28326" class="comment"><div id="post-28326-score" class="comment-score"></div><div class="comment-text"><p>It's Checked. Still not working.</p></div><div id="comment-28326-info" class="comment-info"><span class="comment-age">(22 Dec '13, 10:25)</span> EdJ</div></div><span id="28327"></span><div id="comment-28327" class="comment"><div id="post-28327-score" class="comment-score">1</div><div class="comment-text"><p>It doesn't look like the <code>ethers</code> file works in profiles. For now, try placing it in the top-level preferences directory. You may want to file a bug report for allowing separate per-profile <code>ethers</code> files.</p></div><div id="comment-28327-info" class="comment-info"><span class="comment-age">(22 Dec '13, 10:31)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-28325" class="comment-tools"></div><div class="clear"></div><div id="comment-28325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28324"></span>

<div id="answer-container-28324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28324-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not in 1.10.5 - I'm still on 1.10.4 but it works there ...</p><p>Before updating <code>ethers</code> in my personal configuration folder <img src="https://osqa-ask.wireshark.org/upfiles/Selection_024.png" alt="alt text" /></p><p>and after</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_025.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '13, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Dec '13, 10:10</p></div></div><div id="comments-container-28324" class="comments-container"></div><div id="comment-tools-28324" class="comment-tools"></div><div class="clear"></div><div id="comment-28324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

