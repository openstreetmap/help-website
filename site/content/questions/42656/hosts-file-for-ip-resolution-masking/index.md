+++
type = "question"
title = "hosts file for IP resolution - masking"
description = '''Hi, Can I use masking in hosts file such as: 1.1.1.1/27 GGSN or do I need to insert it one by one? Diana'''
date = "2015-05-26T01:10:00Z"
lastmod = "2015-05-27T07:50:00Z"
weight = 42656
keywords = [ "hosts" ]
aliases = [ "/questions/42656" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [hosts file for IP resolution - masking](/questions/42656/hosts-file-for-ip-resolution-masking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42656-score" class="post-score" title="current number of votes">1</div><span id="post-42656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Can I use masking in hosts file such as: 1.1.1.1/27 GGSN</p><p>or do I need to insert it one by one?</p><p>Diana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-42656" class="comments-container"></div><div id="comment-tools-42656" class="comment-tools"></div><div class="clear"></div><div id="comment-42656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42681"></span>

<div id="answer-container-42681" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42681-score" class="post-score" title="current number of votes">2</div><span id="post-42681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to the page titled "<a href="https://www.wireshark.org/docs/wsug_html/#ChAppFilesConfigurationSection">Configuration Files and Folders</a>" in Wireshark's help and read about the <em>subnets</em> file. This is similar to a <em>hosts</em> file, but for subnets instead of for individual hosts. You have to manually create the file. Suppose you have this line in the file:</p><p>192.168.1.0/24 MYNETWORK</p><p>If network name resolution is enabled, and if Wireshark is not able to resolve a specific IP address (from the regular hosts file, or from the DNS cache, or from a DNS query), then Wireshark will show the name using the entry from the <em>subnets</em> file.</p><p>So, for example, a destination IP address of 192.168.1.89 would show as:</p><p>MYNETWORK.89</p><p>Wireshark will always use the specific host name instead of the subnets name if Wireshark is able to resolve the address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 15:35</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 May '15, 06:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-42681" class="comments-container"><span id="42694"></span><div id="comment-42694" class="comment"><div id="post-42694-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I will try it!</p></div><div id="comment-42694-info" class="comment-info"><span class="comment-age">(27 May '15, 00:47)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="42700"></span><div id="comment-42700" class="comment"><div id="post-42700-score" class="comment-score"></div><div class="comment-text"><p>Wow, all this time I didn't think this feature was available, but it turns out that it was implemented back in 2008 with the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=a88efc932543d32a668233ad77ad6bdcc2f8f9ac">SVN r24154 commit</a>, which resolved <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1445">Bug 1445</a>. I marked my bug, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7339">Bug 7339</a> as a duplicate of Bug 1445, which closes that bug.</p><p>While the feature does work, there are a couple of issues though:</p><ul><li>The <code>subnets</code> file does not work on a per-profile basis like other files, e.g., the <code>hosts</code> file. For consistency, it probably should.</li><li>While the <code>subnets</code> file is documented in the <a href="https://www.wireshark.org/docs/wsug_html/#ChAppFilesConfigurationSection">User Guide</a>, it is not documented in the <a href="https://www.wireshark.org/docs/man-pages/wireshark.html">Wireshark man page</a> under the <strong>Files</strong> section like the rest of the files are (with the exception of the <code>services</code> file, which is also not documented). I suspect that this may be part of the reason why this file and feature was not known before.</li></ul><p>Anyway, a huge thanks to Jim for pointing it out to the community, and to me personally!</p></div><div id="comment-42700-info" class="comment-info"><span class="comment-age">(27 May '15, 07:18)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="42703"></span><div id="comment-42703" class="comment"><div id="post-42703-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>While the subnets file is documented in the User Guide, it is not documented in the Wireshark man page</p></blockquote><p>Yeah, I noticed that too and just submitted a change for it: <a href="https://code.wireshark.org/review/8662">https://code.wireshark.org/review/8662</a></p><p>I also noticed the 'services' doc problem and will submit another change for it.</p></div><div id="comment-42703-info" class="comment-info"><span class="comment-age">(27 May '15, 07:44)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="42706"></span><div id="comment-42706" class="comment"><div id="post-42706-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff!</p></div><div id="comment-42706-info" class="comment-info"><span class="comment-age">(27 May '15, 07:50)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-42681" class="comment-tools"></div><div class="clear"></div><div id="comment-42681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42661"></span>

<div id="answer-container-42661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42661-score" class="post-score" title="current number of votes">0</div><span id="post-42661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to enter hosts one-by-one in /etc/hosts.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-42661" class="comments-container"><span id="42666"></span><div id="comment-42666" class="comment"><div id="post-42666-score" class="comment-score"></div><div class="comment-text"><p>... at least until <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7339">Bug 7339</a> is resolved, should anyone ever care to implement it.</p></div><div id="comment-42666-info" class="comment-info"><span class="comment-age">(26 May '15, 10:28)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-42661" class="comment-tools"></div><div class="clear"></div><div id="comment-42661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

