+++
type = "question"
title = "How to find TCP version"
description = '''How to find TCP version (TCP congestion avoidance algorithms) like TCP TAHOE,TCP VEGAS,TCP NEW RENO IN wireshark FILES '''
date = "2011-06-10T03:47:00Z"
lastmod = "2011-06-14T12:19:00Z"
weight = 4491
keywords = [ "tcp", "versions" ]
aliases = [ "/questions/4491" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find TCP version](/questions/4491/how-to-find-tcp-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4491-score" class="post-score" title="current number of votes">0</div><span id="post-4491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to find TCP version (TCP congestion avoidance algorithms) like TCP TAHOE,TCP VEGAS,TCP NEW RENO IN wireshark FILES</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-versions" rel="tag" title="see questions tagged &#39;versions&#39;">versions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '11, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/7ee3c4f6c2555921f08b9220251c5e71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kumar86&#39;s gravatar image" /><p><span>kumar86</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kumar86 has no accepted answers">0%</span></p></div></div><div id="comments-container-4491" class="comments-container"></div><div id="comment-tools-4491" class="comment-tools"></div><div class="clear"></div><div id="comment-4491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4493"></span>

<div id="answer-container-4493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4493-score" class="post-score" title="current number of votes">5</div><span id="post-4493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Its not a value in the tcp headers, you can only tell by how the stack behaves. Watch for things like how the stack retransmits lost packets (Retransmission, Fast Retransmission, Selective Acknowledgement), how sessions are setup (with Window Scaling, Timestamps, MSS value etc.) and so on. For that you need to have a documentation which feature was introduced in which version, and you might be able to tell.</p><p>Or, if you see HTTP requests you can usually tell the OS from the HTTP headers (User Agent string), and lookup what stack that OS was built with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4493" class="comments-container"><span id="4494"></span><div id="comment-4494" class="comment"><div id="post-4494-score" class="comment-score"></div><div class="comment-text"><p>hello jasper thank you for your reply</p><p>is there any procedure to find which type of TCP version used in windows xp , smart phones</p><p>or</p><p>do i need to observe the TCP flow.</p></div><div id="comment-4494-info" class="comment-info"><span class="comment-age">(10 Jun '11, 04:19)</span> <span class="comment-user userinfo">kumar86</span></div></div><span id="4495"></span><div id="comment-4495" class="comment"><div id="post-4495-score" class="comment-score">2</div><div class="comment-text"><p>Windows XP uses the New Reno stack according to http://www.math.tau.ac.il/~mansour/students/Ceskis-MSc-thesis.pdf.</p><p>"Smart Phones" is a bit too generic to tell, but if you know the OS (iOS, Android, etc.) you might find something by googling for it.</p></div><div id="comment-4495-info" class="comment-info"><span class="comment-age">(10 Jun '11, 05:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="4527"></span><div id="comment-4527" class="comment"><div id="post-4527-score" class="comment-score"></div><div class="comment-text"><p>hello Jasper</p><p>help me where can I find information regarding versions of smart phone {android ,windows mobile,iOS,Symbian .</p></div><div id="comment-4527-info" class="comment-info"><span class="comment-age">(12 Jun '11, 05:39)</span> <span class="comment-user userinfo">kumar86</span></div></div><span id="4565"></span><div id="comment-4565" class="comment"><div id="post-4565-score" class="comment-score"></div><div class="comment-text"><p>Not sure, I'd google for it and see if I can find anything. Android is linux based, so you might be able to deduct it (my Android has Kernel 2.6.35, just to give you a hint). The new Windows mobile might be build on Compound TCP but I have never checked. iOS is based on MacOS as far as I know, which is some kind of unix OS, but this is where you have to use the power of Google on your own :-)</p></div><div id="comment-4565-info" class="comment-info"><span class="comment-age">(14 Jun '11, 12:19)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-4493" class="comment-tools"></div><div class="clear"></div><div id="comment-4493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

