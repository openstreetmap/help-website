+++
type = "question"
title = "Capturing VBScript traffic"
description = '''We have many vbscripts that run on our network and we are trying to identify the source of a vbscript that is starting any service on a server that is stopped at the top of the hour. So I stopped the Print Spooler service on a random server, started the capture a minute before the top of the hour an...'''
date = "2011-02-01T11:30:00Z"
lastmod = "2011-02-01T12:34:00Z"
weight = 2080
keywords = [ "finding", "vbscript", "traffic" ]
aliases = [ "/questions/2080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing VBScript traffic](/questions/2080/capturing-vbscript-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2080-score" class="post-score" title="current number of votes">0</div><span id="post-2080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have many vbscripts that run on our network and we are trying to identify the source of a vbscript that is starting any service on a server that is stopped at the top of the hour. So I stopped the Print Spooler service on a random server, started the capture a minute before the top of the hour and then waited until the service started again. I then stopped the capture and saved it to a file. How would I go about filtering this capture file now for vbscript traffic? I don't even know if it's tcp or udp or what else?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-finding" rel="tag" title="see questions tagged &#39;finding&#39;">finding</span> <span class="post-tag tag-link-vbscript" rel="tag" title="see questions tagged &#39;vbscript&#39;">vbscript</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '11, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/976cc35e8a79dbf1a19ef63a5839ea45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vegas588&#39;s gravatar image" /><p><span>vegas588</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vegas588 has no accepted answers">0%</span></p></div></div><div id="comments-container-2080" class="comments-container"></div><div id="comment-tools-2080" class="comment-tools"></div><div class="clear"></div><div id="comment-2080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2083"></span>

<div id="answer-container-2083" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2083-score" class="post-score" title="current number of votes">0</div><span id="post-2083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure there isn't an automated script running on the server itself that's automatically restarting the processes?</p><p>If it's truly being pushed from a remote source I imagine it'll appear to be some kind of SMS/WMI/MOM/SMB deal. You can just go looking through all of the conversations labeled SMB. You can try searching through the packets for strings like "service" (Edit-&gt;Find Packet). Unless your programmers went all out and built a complete socket based application from the ground up I doubt you'll see a dedicated stream just for this script. Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '11, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-2083" class="comments-container"></div><div id="comment-tools-2083" class="comment-tools"></div><div class="clear"></div><div id="comment-2083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

