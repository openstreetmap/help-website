+++
type = "question"
title = "Tshark storing only a piece of data.data field"
description = '''Looking for a way to store a portion of the data.data field. I&#x27;ve tried things like data.data[0:10] or data[0:10] but in those cases nothing gets stored.  Thanks in advance!'''
date = "2013-05-28T15:34:00Z"
lastmod = "2013-05-29T14:13:00Z"
weight = 21542
keywords = [ "tshark", "data.data" ]
aliases = [ "/questions/21542" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark storing only a piece of data.data field](/questions/21542/tshark-storing-only-a-piece-of-datadata-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21542-score" class="post-score" title="current number of votes">0</div><span id="post-21542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Looking for a way to store a portion of the data.data field. I've tried things like data.data[0:10] or data[0:10] but in those cases nothing gets stored.<br />
</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-data.data" rel="tag" title="see questions tagged &#39;data.data&#39;">data.data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '13, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/8aac550c1fb20062738a7da1e4d00ade?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hsingh419&#39;s gravatar image" /><p><span>hsingh419</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hsingh419 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-21542" class="comments-container"></div><div id="comment-tools-21542" class="comment-tools"></div><div class="clear"></div><div id="comment-21542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21547"></span>

<div id="answer-container-21547" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21547-score" class="post-score" title="current number of votes">1</div><span id="post-21547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can look at editcap with the -s &lt;snaplength&gt; option to cut a given number of bytes.</p><p>If you want to snip just a specific field value in a protocol, the best way to export that value is probably going to be with the '-T fields' option in tshark, with an '-e {display filter}' option to present as output the value of that particular field in the packet.</p><p>Depending on what you're trying to do, another option is to export the packet as plain text, write a script to grab the trace into a "packet array", and run that array through a loop to parse and manipulate the bytes of each packet however you see fit. I've done this a few times with perl for some small projects.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '13, 20:23</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21547" class="comments-container"><span id="21585"></span><div id="comment-21585" class="comment"><div id="post-21585-score" class="comment-score"></div><div class="comment-text"><p>Used the -s &lt;snaplength&gt; in tshark while doing a live capture. Works great. Thanks!</p></div><div id="comment-21585-info" class="comment-info"><span class="comment-age">(29 May '13, 14:13)</span> <span class="comment-user userinfo">hsingh419</span></div></div></div><div id="comment-tools-21547" class="comment-tools"></div><div class="clear"></div><div id="comment-21547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21543"></span>

<div id="answer-container-21543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21543-score" class="post-score" title="current number of votes">0</div><span id="post-21543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What do you mean, store a portion of the data.data field? You can't change bytes in a packet with tShark, it is a "read only" tool (at least at the moment), same as Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '13, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21543" class="comments-container"><span id="21544"></span><div id="comment-21544" class="comment"><div id="post-21544-score" class="comment-score"></div><div class="comment-text"><p>I only need to capture a portion of the payload.</p></div><div id="comment-21544-info" class="comment-info"><span class="comment-age">(28 May '13, 15:47)</span> <span class="comment-user userinfo">hsingh419</span></div></div><span id="21545"></span><div id="comment-21545" class="comment"><div id="post-21545-score" class="comment-score"></div><div class="comment-text"><p>I'm not really sure you can do this either. As far as I know you always need to have all the layers up to the bytes you want to keep because otherwise Wireshark cannot later decode it again.</p></div><div id="comment-21545-info" class="comment-info"><span class="comment-age">(28 May '13, 15:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="21546"></span><div id="comment-21546" class="comment"><div id="post-21546-score" class="comment-score"></div><div class="comment-text"><p>Looks like the SnapLen function could work. Not exactly what I'm looking for but might be my only choice.</p></div><div id="comment-21546-info" class="comment-info"><span class="comment-age">(28 May '13, 20:06)</span> <span class="comment-user userinfo">hsingh419</span></div></div></div><div id="comment-tools-21543" class="comment-tools"></div><div class="clear"></div><div id="comment-21543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

