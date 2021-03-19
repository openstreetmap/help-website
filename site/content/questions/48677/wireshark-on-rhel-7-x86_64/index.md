+++
type = "question"
title = "Wireshark on RHEL 7 (x86_64)"
description = '''Hi, Want to install &quot;Wireshark&quot; on RHEL 7 (x86_64), please let me know where to find this. Also can I see the capture in Windows. Thanks, Nambiar.'''
date = "2015-12-22T23:08:00Z"
lastmod = "2015-12-24T14:24:00Z"
weight = 48677
keywords = [ "rhel7", "rpm", "install" ]
aliases = [ "/questions/48677" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on RHEL 7 (x86\_64)](/questions/48677/wireshark-on-rhel-7-x86_64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48677-score" class="post-score" title="current number of votes">0</div><span id="post-48677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Want to install "Wireshark" on RHEL 7 (x86_64), please let me know where to find this. Also can I see the capture in Windows.</p><p>Thanks, Nambiar.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rhel7" rel="tag" title="see questions tagged &#39;rhel7&#39;">rhel7</span> <span class="post-tag tag-link-rpm" rel="tag" title="see questions tagged &#39;rpm&#39;">rpm</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '15, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/ec04c1ba9b98b4559465fcb610973d52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nambiar&#39;s gravatar image" /><p><span>Nambiar</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nambiar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Dec '15, 06:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-48677" class="comments-container"></div><div id="comment-tools-48677" class="comment-tools"></div><div class="clear"></div><div id="comment-48677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48685"></span>

<div id="answer-container-48685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48685-score" class="post-score" title="current number of votes">0</div><span id="post-48685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With RHEL 7 you have 2 options to get Wireshark; it really depends on how modern a version you want and how much work you're up for. Either:</p><ol><li>yum install wireshark wireshark-gnome</li><li>(or) download the <a href="https://wireshark.org/download/src/">source</a>, install all the necessary build dependencies, and build your own (basically: ./configure [possibly with some options]; make rpm-package), and then install the resulting RPMs.</li></ol><p>(1) is obviously a lot easier but the version you get will be older than you'd get with (2).</p><hr /><p>Yes, whatever you capture with Wireshark (or tcpdump or dumpcap) on Linux will be readable with Wireshark on Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '15, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-48685" class="comments-container"><span id="48709"></span><div id="comment-48709" class="comment"><div id="post-48709-score" class="comment-score"></div><div class="comment-text"><p>(So if all you want to do is <em>capture</em> traffic on RHEL 7, and <em>read</em> the captures on Windows, you don't need Wireshark on RHEL 7 - you could use tcpdump.)</p></div><div id="comment-48709-info" class="comment-info"><span class="comment-age">(24 Dec '15, 14:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-48685" class="comment-tools"></div><div class="clear"></div><div id="comment-48685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

