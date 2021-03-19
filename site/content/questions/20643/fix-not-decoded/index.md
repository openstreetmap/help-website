+++
type = "question"
title = "Fix not decoded"
description = '''I did a packet capture of FIX traffic. The traffic is from multiple sources. What I noticed unusual is it decoded FIX for half the traffic and not the other half. The only difference is the port the traffic was running on. The port it did not decode was TCP 5000. How do I tell it port 5000 is FIX'''
date = "2013-04-19T14:34:00Z"
lastmod = "2013-04-21T13:55:00Z"
weight = 20643
keywords = [ "fix" ]
aliases = [ "/questions/20643" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fix not decoded](/questions/20643/fix-not-decoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20643-score" class="post-score" title="current number of votes">0</div><span id="post-20643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I did a packet capture of FIX traffic. The traffic is from multiple sources. What I noticed unusual is it decoded FIX for half the traffic and not the other half. The only difference is the port the traffic was running on. The port it did not decode was TCP 5000. How do I tell it port 5000 is FIX</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '13, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/f87db37d7236cbe1e006ab8c561a7399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="plnnightsky&#39;s gravatar image" /><p><span>plnnightsky</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="plnnightsky has no accepted answers">0%</span></p></div></div><div id="comments-container-20643" class="comments-container"></div><div id="comment-tools-20643" class="comment-tools"></div><div class="clear"></div><div id="comment-20643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20653"></span>

<div id="answer-container-20653" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20653-score" class="post-score" title="current number of votes">0</div><span id="post-20653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Right click one of those packets and choose: Decode as -&gt; TCP (both ports), then select the FIX protocol.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '13, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20653" class="comments-container"><span id="20662"></span><div id="comment-20662" class="comment"><div id="post-20662-score" class="comment-score"></div><div class="comment-text"><p>Thanks this worked for most of them. some it made no change too</p></div><div id="comment-20662-info" class="comment-info"><span class="comment-age">(20 Apr '13, 13:25)</span> <span class="comment-user userinfo">plnnightsky</span></div></div><span id="20663"></span><div id="comment-20663" class="comment"><div id="post-20663-score" class="comment-score"></div><div class="comment-text"><p>If those packets that are not decoded use a different port, you'll have to repeat the "decode as" steps.</p></div><div id="comment-20663-info" class="comment-info"><span class="comment-age">(20 Apr '13, 14:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20686"></span><div id="comment-20686" class="comment"><div id="post-20686-score" class="comment-score"></div><div class="comment-text"><p>The first mistake I made was ports for both it was looking for both ports. Once I changed it to just the destination port (5000) it worked most. There are about 8 which it does not work for. I am thinking there is something wrong either with my copy of Wireshark or more likely something strange with the packets thanks again for taking the time to answer</p></div><div id="comment-20686-info" class="comment-info"><span class="comment-age">(21 Apr '13, 12:17)</span> <span class="comment-user userinfo">plnnightsky</span></div></div><span id="20687"></span><div id="comment-20687" class="comment"><div id="post-20687-score" class="comment-score"></div><div class="comment-text"><p>can you post a sample capture file somewhere (google docs, dropbox, etc.)?</p></div><div id="comment-20687-info" class="comment-info"><span class="comment-age">(21 Apr '13, 13:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20653" class="comment-tools"></div><div class="clear"></div><div id="comment-20653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

