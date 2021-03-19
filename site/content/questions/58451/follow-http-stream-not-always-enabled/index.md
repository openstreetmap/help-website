+++
type = "question"
title = "&#x27;Follow HTTP stream&#x27; not always enabled."
description = '''Following HTTP streams was a great addition, particularly when trying to follow servers which send their HTML content gzip&#x27;ed. Strangely enough, the &#x27;HTTP stream&#x27; in the popup dialog (or the main menu for that matter), isn&#x27;t alwys enabled - even when I am clearly inside a TCP packet. (BTW it worked ...'''
date = "2017-01-01T08:05:00Z"
lastmod = "2017-01-13T13:10:00Z"
weight = 58451
keywords = [ "streams", "http" ]
aliases = [ "/questions/58451" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ['Follow HTTP stream' not always enabled.](/questions/58451/follow-http-stream-not-always-enabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58451-score" class="post-score" title="current number of votes">0</div><span id="post-58451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Following HTTP streams was a great addition, particularly when trying to follow servers which send their HTML content gzip'ed.</p><p>Strangely enough, the 'HTTP stream' in the popup dialog (or the main menu for that matter), isn't alwys enabled - even when I am clearly inside a TCP packet. (BTW it worked yesterday, same session, even the same capture). When does the HTTP stream option get enabled? Do I have to do anything special?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-streams" rel="tag" title="see questions tagged &#39;streams&#39;">streams</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '17, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/1d06c6d3c85351c8d2fa977805621ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcoppens&#39;s gravatar image" /><p><span>jcoppens</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcoppens has no accepted answers">0%</span></p></div></div><div id="comments-container-58451" class="comments-container"><span id="58477"></span><div id="comment-58477" class="comment"><div id="post-58477-score" class="comment-score"></div><div class="comment-text"><p>Have you selected a packet which has the "HTTP" layer?</p></div><div id="comment-58477-info" class="comment-info"><span class="comment-age">(03 Jan '17, 05:25)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div><span id="58552"></span><div id="comment-58552" class="comment"><div id="post-58552-score" class="comment-score"></div><div class="comment-text"><p>can you share your pcap ?</p></div><div id="comment-58552-info" class="comment-info"><span class="comment-age">(05 Jan '17, 23:07)</span> <span class="comment-user userinfo">Alexis La Go...</span></div></div></div><div id="comment-tools-58451" class="comment-tools"></div><div class="clear"></div><div id="comment-58451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58747"></span>

<div id="answer-container-58747" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58747-score" class="post-score" title="current number of votes">0</div><span id="post-58747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello again,</p><p>Thanks for reading the original question, and commenting! I've been suffering the follow-up of an Achilles tendon rupture and haven't really been on the computer much. Sorry for the delay in replying!</p><p>If I'm not mistaken, my complaint originates from the fact that in the actual Wireshark version, it is necessary to click on the first packet of a TCP stream (i.e. GET, POST, etc). I believe that, when following TCP streams was first implemented (in the last instances of the 1.x series), I could click on any packet of a TCP stream and still get the entire thread selected.</p><p>Could that be?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '17, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/1d06c6d3c85351c8d2fa977805621ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcoppens&#39;s gravatar image" /><p><span>jcoppens</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcoppens has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jan '17, 13:12</strong> </span></p></div></div><div id="comments-container-58747" class="comments-container"></div><div id="comment-tools-58747" class="comment-tools"></div><div class="clear"></div><div id="comment-58747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

