+++
type = "question"
title = "Filter FTP"
description = '''Hi, I have been asked to run Wireshark on a server using an FTP filter but can&#x27;t seem to find the right way to do this....can anyone assist?'''
date = "2013-06-05T08:18:00Z"
lastmod = "2013-06-05T08:30:00Z"
weight = 21765
keywords = [ "ftp", "server", "wireshark" ]
aliases = [ "/questions/21765" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter FTP](/questions/21765/filter-ftp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21765-score" class="post-score" title="current number of votes">0</div><span id="post-21765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have been asked to run Wireshark on a server using an FTP filter but can't seem to find the right way to do this....can anyone assist?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '13, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/908dce768dea1d7941aabe5e077e2748?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharwal&#39;s gravatar image" /><p><span>sharwal</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharwal has no accepted answers">0%</span></p></div></div><div id="comments-container-21765" class="comments-container"></div><div id="comment-tools-21765" class="comment-tools"></div><div class="clear"></div><div id="comment-21765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21767"></span>

<div id="answer-container-21767" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21767-score" class="post-score" title="current number of votes">0</div><span id="post-21767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On display filter For FTP Control connection do tcp.port==21 and For FTP Data connection do tcp.port==20 For both(tcp.port==21 || tcp.port==20) If you type ft in display filter box that will show you all display filters starting with ft..You can make use of that too.I am seeing ftp and ftp-data.</p><p>On capture filter port 21 or port 20</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '13, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '13, 08:31</strong> </span></p></div></div><div id="comments-container-21767" class="comments-container"><span id="21768"></span><div id="comment-21768" class="comment"><div id="post-21768-score" class="comment-score"></div><div class="comment-text"><p>Thats what I saw only as well....thanks</p></div><div id="comment-21768-info" class="comment-info"><span class="comment-age">(05 Jun '13, 08:30)</span> <span class="comment-user userinfo">sharwal</span></div></div></div><div id="comment-tools-21767" class="comment-tools"></div><div class="clear"></div><div id="comment-21767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

