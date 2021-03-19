+++
type = "question"
title = "Default profile"
description = '''Is there a way to set the Wireshark default profile back to its defaults? Thanks. Owen'''
date = "2013-03-16T15:50:00Z"
lastmod = "2013-03-16T17:07:00Z"
weight = 19575
keywords = [ "default", "profile" ]
aliases = [ "/questions/19575" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Default profile](/questions/19575/default-profile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19575-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to set the Wireshark default profile back to its defaults?</p><p>Thanks.</p><p>Owen</p></div><div id="question-tags" class="tags-container tags">default profile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '13, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/e12b8d5f904f018189f5cf3c69cbe5f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Owen&#39;s gravatar image" /><p>Owen<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Owen has no accepted answers">0%</span></p></div></div><div id="comments-container-19575" class="comments-container"><span id="59421"></span><div id="comment-59421" class="comment"><div id="post-59421-score" class="comment-score"></div><div class="comment-text"><p>In the upcoming version 2.4 it's possible to reset the Default profile by "Removing" the profile in the "Configuration Profiles" dialog.</p></div><div id="comment-59421-info" class="comment-info"><span class="comment-age">(14 Feb '17, 12:44)</span> stig ♦</div></div></div><div id="comment-tools-19575" class="comment-tools"></div><div class="clear"></div><div id="comment-19575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19581"></span>

<div id="answer-container-19581" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19581-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>The preferences that constitute your default profile consist of a series of files, as do all profiles. You can reset your default profile to the default values by deleting these files.</p><p>In the Windows version of Wireshark, go to Help &gt; About and click on the Folders tab. Double-click the link labeled "Personal Configuration." This will take you to the folder that contains the various preference files. Make a backup of this folder before you delete anything, but almost all of the files in this folder can be safely deleted. If there is a <strong>profiles</strong> folder, don't delete it. The <strong>profiles</strong> folder contains your other profiles.</p><p>These are some of the more common files that can be safely deleted:</p><ul><li>colorfilters - contains the coloring rules for your default profile</li><li>dfilters - contains saved display filters for your default profile</li><li>cfilters - contains saved capture filters for your default profile</li><li>recent - contains some preference settings for your default profile, mostly related to how things are displayed</li><li>preferences - contains most other preference settings for your default profile</li></ul><p>There can be other files, depending on how much you've changed Wireshark's settings.</p><p>The following files apply to <em>all</em> profiles. You can safely delete them if you don't have any other profiles.</p><ul><li>preferences_common</li><li>geoip_db_paths</li></ul><p>If you do have other profiles, you may want to keep these files, but even if you do delete them, the important files for your other profiles are saved in the individual profile directories under the <strong>profiles</strong> folder.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 17:07</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19581" class="comments-container"><span id="19582"></span><div id="comment-19582" class="comment"><div id="post-19582-score" class="comment-score"></div><div class="comment-text"><p>Jim,</p><p>That did it! Thank you for your quick response.</p><p>Owen.</p></div><div id="comment-19582-info" class="comment-info"><span class="comment-age">(16 Mar '13, 17:22)</span> Owen</div></div></div><div id="comment-tools-19581" class="comment-tools"></div><div class="clear"></div><div id="comment-19581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

