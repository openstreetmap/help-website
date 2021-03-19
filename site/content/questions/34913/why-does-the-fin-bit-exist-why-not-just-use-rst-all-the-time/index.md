+++
type = "question"
title = "Why does the FIN bit exist? Why not just use RST all the time?"
description = '''Can someone give me a reason the FIN bit exists, or a use case where it would be used to &quot;terminate&quot; a connection instead of using the RST bit? I ask this because I&#x27;ve been watching a bunch of Laura&#x27;s training videos. She continually mentions that when a connection is terminated using the FIN bit, t...'''
date = "2014-07-25T13:09:00Z"
lastmod = "2014-08-02T02:30:00Z"
weight = 34913
keywords = [ "tcp" ]
aliases = [ "/questions/34913" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does the FIN bit exist? Why not just use RST all the time?](/questions/34913/why-does-the-fin-bit-exist-why-not-just-use-rst-all-the-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34913-score" class="post-score" title="current number of votes">0</div><span id="post-34913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone give me a reason the FIN bit exists, or a use case where it would be used to "terminate" a connection instead of using the RST bit?</p><p>I ask this because I've been watching a bunch of Laura's training videos. She continually mentions that when a connection is terminated using the FIN bit, the other side doesn't actually tear down the connection. It then allows someone else to hijack the connection...</p><p>So, could the FIN bit be considered legacy, or is there a real reason to use it instead of RST?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '14, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/4a4df10c701372e5dbbb8015a1d6b67b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_harrold&#39;s gravatar image" /><p><span>patrick_harrold</span><br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_harrold has no accepted answers">0%</span></p></div></div><div id="comments-container-34913" class="comments-container"></div><div id="comment-tools-34913" class="comment-tools"></div><div class="clear"></div><div id="comment-34913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34914"></span>

<div id="answer-container-34914" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34914-score" class="post-score" title="current number of votes">1</div><span id="post-34914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="patrick_harrold has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The RST bit was historically designed to signal fatal connection problems, while FIN was designed to signal graceful shutdown. FIN also allows late packet arrivals and one sided connection tear down without the other party being forbidden to send more data.</p><p>I'm not sure why Laura says that with FIN the other side does not tear down the connection, because in most cases it does. It just does not HAVE to right away.</p><p>FIN is not (yet) legacy, it's still used quite often. RST is just quicker and releases resources right away, so it is slowly replacing the use of FIN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '14, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34914" class="comments-container"><span id="35078"></span><div id="comment-35078" class="comment"><div id="post-35078-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the prompt reply and apologies for my late reply. I figured I would get a notification email by default when someone answered my question but I guess not.</p><p>Can you think of any reason a node would choose to not tear down a connection when it receives a FIN? I mean... if you hear that someone isn't listening to you anymore, why wouldn't you tear down the connection? I know you say they don't HAVE to, but why shouldn't they be forced?</p><p>I'm just trying to think of a valid, real-world use case that FIN would be used instead of RST (assuming one exists).</p></div><div id="comment-35078-info" class="comment-info"><span class="comment-age">(01 Aug '14, 15:56)</span> <span class="comment-user userinfo">patrick_harrold</span></div></div><span id="35081"></span><div id="comment-35081" class="comment"><div id="post-35081-score" class="comment-score"></div><div class="comment-text"><p>A node would not tear down the connection immediately if it still had data to send. FIN does not mean "I'm not listening any more," it means "I have no more data to send." It's unusual, but the other host is allowed to continue sending. RST, on the other hand, does mean "I'm not listening any more."</p></div><div id="comment-35081-info" class="comment-info"><span class="comment-age">(01 Aug '14, 20:49)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="35084"></span><div id="comment-35084" class="comment"><div id="post-35084-score" class="comment-score"></div><div class="comment-text"><p>You see that kind of one sided teardown for some web based services, e.g. a client sending "hey server, I need this XML, btw, that's all I need" by sending a GET request with a FIN following it right away. The server can then prepare the XML and send it, already knowing that that was all the client wants. So it usually sends the content and a FIN of its own to signal that it has finished the job as well.</p></div><div id="comment-35084-info" class="comment-info"><span class="comment-age">(02 Aug '14, 02:30)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-34914" class="comment-tools"></div><div class="clear"></div><div id="comment-34914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

