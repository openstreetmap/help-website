+++
type = "question"
title = "How to download a particular wireshark revision?"
description = '''I would like to download only the wireshark 1.6.1 version, 38101 revision. Today&#x27;s Revision number of 1.6.1 is 39457. How can i Download 38101?'''
date = "2011-10-18T02:57:00Z"
lastmod = "2011-10-18T03:17:00Z"
weight = 6946
keywords = [ "wireshark" ]
aliases = [ "/questions/6946" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to download a particular wireshark revision?](/questions/6946/how-to-download-a-particular-wireshark-revision)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6946-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to download only the wireshark 1.6.1 version, 38101 revision. Today's Revision number of 1.6.1 is 39457. How can i Download 38101?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '11, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div></div><div id="comments-container-6946" class="comments-container"></div><div id="comment-tools-6946" class="comment-tools"></div><div class="clear"></div><div id="comment-6946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6947"></span>

<div id="answer-container-6947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6947-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think there are tar-balls of specific svn revisions (other than releases) available except for the trunk (1.7 currently) Look in the <a href="http://www.wireshark.org/download/automated/">automated downloads</a> section for those.</p><p>I think you'll have to use your svn client of choice to get that specific revision, simply use the update command to update to your target revision.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '11, 03:18</p></div></div><div id="comments-container-6947" class="comments-container"><span id="6948"></span><div id="comment-6948" class="comment"><div id="post-6948-score" class="comment-score"></div><div class="comment-text"><p>I use tortoise svn. I've tried with it but failed to do so.</p></div><div id="comment-6948-info" class="comment-info"><span class="comment-age">(18 Oct '11, 03:49)</span> Terrestrial ...</div></div><span id="6949"></span><div id="comment-6949" class="comment"><div id="post-6949-score" class="comment-score"></div><div class="comment-text"><p>How can i know the list of updates done to 39457 right from 38101?</p></div><div id="comment-6949-info" class="comment-info"><span class="comment-age">(18 Oct '11, 03:50)</span> Terrestrial ...</div></div><span id="6950"></span><div id="comment-6950" class="comment"><div id="post-6950-score" class="comment-score"></div><div class="comment-text"><p>Assuming your working copy is connected to wireshark/trunk-1.6, from the menu select <code>TortoiseSVN | Update to revision...</code> and enter the appropriate rev number.</p><p>To see the differences between revisions either use the viewvc interface on the server, e.g. <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.6/?view=log">here</a>, or using TSVN again, use <code>TortoiseSVN | Show Log</code> to view the log of the part of the repo you are interested in, e.g. trunk-1.6, multiple select the two revisions of interest and then right click one of them and select <code>Compare revisions</code></p></div><div id="comment-6950-info" class="comment-info"><span class="comment-age">(18 Oct '11, 04:03)</span> grahamb ♦</div></div><span id="6951"></span><div id="comment-6951" class="comment"><div id="post-6951-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This answer would help me in Comparing revisions. Could you please tell me one thing? Finally, Can i download that revision? Is that possible?</p></div><div id="comment-6951-info" class="comment-info"><span class="comment-age">(18 Oct '11, 04:06)</span> Terrestrial ...</div></div><span id="6952"></span><div id="comment-6952" class="comment"><div id="post-6952-score" class="comment-score"></div><div class="comment-text"><p>As per my previous answer, I don't think that specific rev is available as a direct download, only by using an svn client.</p><p>I forgot to mention before that you can also just <code>checkout</code> a new working copy of a specific revision as well as updating an existing working copy. In the Checkout dialog there is a field to enter the required revision.</p></div><div id="comment-6952-info" class="comment-info"><span class="comment-age">(18 Oct '11, 04:33)</span> grahamb ♦</div></div><span id="6980"></span><div id="comment-6980" class="comment not_top_scorer"><div id="post-6980-score" class="comment-score"></div><div class="comment-text"><p>I've tried using SWVN Checkout and revision number=38101 but after compiling and running; I cannot see Revision Number in About Wireshark Dialog Box. It shows "SVN Rev Unknown from Unknown".</p></div><div id="comment-6980-info" class="comment-info"><span class="comment-age">(18 Oct '11, 22:20)</span> Terrestrial ...</div></div><span id="6985"></span><div id="comment-6985" class="comment not_top_scorer"><div id="post-6985-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure about building from an "alternate" trunk such as trunk-1.6, but when building the main trunk, the makefile calls a perl script <code>make-version.pl</code> that adds the svn revision info to the build by creating <code>svnversion.h</code>. This script uses the contents of <code>version.conf</code> if present to control the output.</p><p>I don't know why this isn't working for you, and can only suggest that you firstly ensure your working copy is absolutely clean, i.e. no modifications are shown in the wc by TSVN, and that you are building in your working copy and not exporting the files elsewhere for a build.</p></div><div id="comment-6985-info" class="comment-info"><span class="comment-age">(19 Oct '11, 02:39)</span> grahamb ♦</div></div></div><div id="comment-tools-6947" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-6947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

