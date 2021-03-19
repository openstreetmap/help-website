+++
type = "question"
title = "No interface can be used"
description = '''Couldn&#x27;t run /usr/sbin/dumpcap  I added my account as a member to the wireshark group.'''
date = "2014-02-08T09:51:00Z"
lastmod = "2015-10-13T14:04:00Z"
weight = 29555
keywords = [ "interfaces", "dumpcap" ]
aliases = [ "/questions/29555" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [No interface can be used](/questions/29555/no-interface-can-be-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29555-score" class="post-score" title="current number of votes">0</div><span id="post-29555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Couldn't run /usr/sbin/dumpcap</p><p>I added my account as a member to the wireshark group.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '14, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/6b1b9ebf822e46308059d8dc01a4f8ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theking2&#39;s gravatar image" /><p><span>theking2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theking2 has no accepted answers">0%</span></p></div></div><div id="comments-container-29555" class="comments-container"><span id="29557"></span><div id="comment-29557" class="comment"><div id="post-29557-score" class="comment-score"></div><div class="comment-text"><p>OS, dumpcap version?</p></div><div id="comment-29557-info" class="comment-info"><span class="comment-age">(08 Feb '14, 13:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="29584"></span><div id="comment-29584" class="comment"><div id="post-29584-score" class="comment-score"></div><div class="comment-text"><p>For Ubuntu (and derivatives), see <a href="http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed">http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed</a></p></div><div id="comment-29584-info" class="comment-info"><span class="comment-age">(09 Feb '14, 12:32)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="46521"></span><div id="comment-46521" class="comment"><div id="post-46521-score" class="comment-score"></div><div class="comment-text"><p>how to add an account as a member to the wireshark group</p></div><div id="comment-46521-info" class="comment-info"><span class="comment-age">(13 Oct '15, 14:04)</span> <span class="comment-user userinfo">agwmar</span></div></div></div><div id="comment-tools-29555" class="comment-tools"></div><div class="clear"></div><div id="comment-29555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29583"></span>

<div id="answer-container-29583" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29583-score" class="post-score" title="current number of votes">0</div><span id="post-29583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>dumpcap is usually installed in /usr/<strong>bin</strong> not /usr/<strong>sbin</strong>. Can you please check that?</p><p>Then run the following commands</p><blockquote><p>sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap<br />
chgrp wireshark /usr/bin/dumpcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '14, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '14, 12:28</strong> </span></p></div></div><div id="comments-container-29583" class="comments-container"><span id="44281"></span><div id="comment-44281" class="comment"><div id="post-44281-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt, it helps me on LMDE.</p></div><div id="comment-44281-info" class="comment-info"><span class="comment-age">(18 Jul '15, 04:02)</span> <span class="comment-user userinfo">Chewits</span></div></div></div><div id="comment-tools-29583" class="comment-tools"></div><div class="clear"></div><div id="comment-29583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29779"></span>

<div id="answer-container-29779" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29779-score" class="post-score" title="current number of votes">0</div><span id="post-29779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently a reboot was required.</p><p>After a reboot wireshark did find the interfaces.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/6b1b9ebf822e46308059d8dc01a4f8ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="theking2&#39;s gravatar image" /><p><span>theking2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="theking2 has no accepted answers">0%</span></p></div></div><div id="comments-container-29779" class="comments-container"></div><div id="comment-tools-29779" class="comment-tools"></div><div class="clear"></div><div id="comment-29779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

