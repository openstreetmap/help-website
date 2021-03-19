+++
type = "question"
title = "easy way to extract websites visited from a capture"
description = '''Hi all, I have always wondered is there an easy way to extract the web pages that have been visited from a capture.  For example let&#x27;s say I have a 30 min capture of all traffic from a user and I want a simple list of the websites he/she has visited i.e. facebook bbc etc. Is there an easy way to do ...'''
date = "2012-06-28T06:08:00Z"
lastmod = "2015-04-07T18:45:00Z"
weight = 12271
keywords = [ "visited", "websites" ]
aliases = [ "/questions/12271" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [easy way to extract websites visited from a capture](/questions/12271/easy-way-to-extract-websites-visited-from-a-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12271-score" class="post-score" title="current number of votes">0</div><span id="post-12271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have always wondered is there an easy way to extract the web pages that have been visited from a capture.<br />
</p><p>For example let's say I have a 30 min capture of all traffic from a user and I want a simple list of the websites he/she has visited i.e. facebook bbc etc. Is there an easy way to do this in wireshark or with another tool (by feeding in the pcap)?</p><p>Regards</p><p>J</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-visited" rel="tag" title="see questions tagged &#39;visited&#39;">visited</span> <span class="post-tag tag-link-websites" rel="tag" title="see questions tagged &#39;websites&#39;">websites</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '12, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/3b26283fc2ea878034c78ed1c2c6d676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-man9&#39;s gravatar image" /><p><span>j-man9</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-man9 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12271" class="comments-container"></div><div id="comment-tools-12271" class="comment-tools"></div><div class="clear"></div><div id="comment-12271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12272"></span>

<div id="answer-container-12272" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12272-score" class="post-score" title="current number of votes">0</div><span id="post-12272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry all - I found the answer here: <a href="http://ask.wireshark.org/questions/7040/how-to-monitor-what-websites-are-visited">http://ask.wireshark.org/questions/7040/how-to-monitor-what-websites-are-visited</a></p><p>Basically: Go to Statistics | HTTP | Load Distribution and type http.host. Now look at the "HTTP Requests by HTTP Hosts". This will show you all the HTTP type traffic coming in and out of your network.</p><p>And it works pretty well too! ta</p><p>J</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '12, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/3b26283fc2ea878034c78ed1c2c6d676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-man9&#39;s gravatar image" /><p><span>j-man9</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-man9 has no accepted answers">0%</span></p></div></div><div id="comments-container-12272" class="comments-container"></div><div id="comment-tools-12272" class="comment-tools"></div><div class="clear"></div><div id="comment-12272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41266"></span>

<div id="answer-container-41266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41266-score" class="post-score" title="current number of votes">0</div><span id="post-41266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This doesn't shows https websites. Is there a way to use Load distribution feature for https traffic</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '15, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/65ee38e2a4b25f780742a641d57a6db4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karan%20kapoor&#39;s gravatar image" /><p><span>karan kapoor</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karan kapoor has no accepted answers">0%</span></p></div></div><div id="comments-container-41266" class="comments-container"></div><div id="comment-tools-41266" class="comment-tools"></div><div class="clear"></div><div id="comment-41266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

