+++
type = "question"
title = "capture filter error"
description = '''I&#x27;m trying to capture SOAP messages from tcp port. If I enter &quot;tcp port 4040&quot; as capture filter, the capture filter bar always stays red and I&#x27;m not able to start capturing messages. What am I doing wrong, any help?'''
date = "2016-05-12T07:57:00Z"
lastmod = "2016-05-13T12:11:00Z"
weight = 52472
keywords = [ "capture-filter", "soap" ]
aliases = [ "/questions/52472" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter error](/questions/52472/capture-filter-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52472-score" class="post-score" title="current number of votes">0</div><span id="post-52472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture SOAP messages from tcp port. If I enter "tcp port 4040" as capture filter, the capture filter bar always stays red and I'm not able to start capturing messages. What am I doing wrong, any help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/80f62caf51db11cd51658278ce56b76f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sivapriya&#39;s gravatar image" /><p><span>Sivapriya</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sivapriya has no accepted answers">0%</span></p></div></div><div id="comments-container-52472" class="comments-container"><span id="52474"></span><div id="comment-52474" class="comment"><div id="post-52474-score" class="comment-score"></div><div class="comment-text"><p>Use tcp.port ==4040 in capture filter and start capture, if you need to capture specific SOAP messages</p></div><div id="comment-52474-info" class="comment-info"><span class="comment-age">(12 May '16, 08:35)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="52478"></span><div id="comment-52478" class="comment"><div id="post-52478-score" class="comment-score"></div><div class="comment-text"><p><span>@Dinesh Babu Sadu</span>, you mix together capture filter and display filter.</p><p>The syntax you've given (<code>tcp.port ==4040</code>) corresponds to display filter.</p></div><div id="comment-52478-info" class="comment-info"><span class="comment-age">(12 May '16, 12:54)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52472" class="comment-tools"></div><div class="clear"></div><div id="comment-52472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52487"></span>

<div id="answer-container-52487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52487-score" class="post-score" title="current number of votes">0</div><span id="post-52487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture filter will turn green when the syntax is valid AND an interface has been selected. If you have not set a default interface, then when you first start Wireshark, no interface is selected, so the capture filter will display in red.</p><p>Simply click first on the interface(s) you want to capture on, and then enter your capture filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '16, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-52487" class="comments-container"><span id="52496"></span><div id="comment-52496" class="comment"><div id="post-52496-score" class="comment-score"></div><div class="comment-text"><p><span>@Jim Aragon</span>, I've withdrawn my answer that the behaviour you describe is a bug, but I still find it counter-intuitive.</p><p>Showing a valid syntax in red is really confusing and doesn't give the user a clue what is actually wrong.</p><p>Especially as there is just a single capture filter field whose contents changes depending on which interface is chosen, and if you choose several interfaces and each of them has a different capture filter setting, an explanatory text occurs in the capture filter field. This behaviour is a proof that doing it in a user-friendly way is possible.</p><p>So instead of the red background appearing as late as when the user actually types into the field, I'd expect another explanatory text, asking to choose an interface first, to be shown in the capture filter field, locked against editing, until an interface is chosen. I'd not object against the field to be red as well, but it'd have to be red already <em>before</em> the user starts to type in.</p><p>Want me to file a bug or is it enough like this?</p></div><div id="comment-52496-info" class="comment-info"><span class="comment-age">(13 May '16, 02:51)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52521"></span><div id="comment-52521" class="comment"><div id="post-52521-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span>, I agree that the current behavior is neither friendly nor intuitive. I'd go ahead and file an enhancement request. I think that the capture filter field should be red or green based solely on whether the text is valid or invalid capture filter syntax. I agree that a separate message should pop up if the user tries to start capturing with no interface selected.</p><p>Note that in the current interface, if you enter the capture filter first and then select the interface, the capture filter will be cleared and you will have to enter it again. I think it would be better if you could select the interface either before or after entering the filter, without losing what was already entered.</p></div><div id="comment-52521-info" class="comment-info"><span class="comment-age">(13 May '16, 09:48)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="52523"></span><div id="comment-52523" class="comment"><div id="post-52523-score" class="comment-score"></div><div class="comment-text"><p>I'd prefer to file a detailed suggestion as an enhancement request rather than a vague "make it better than it is now". So:</p><blockquote><p>I think it would be better if you could select the interface either before or after entering the filter, without losing what was already entered.</p></blockquote><p>I agree with you that it would be the best option (least work lost at user side if they first fill in the filter and then choose an interface), but in this case, the information that capture is not possible until an interface is chosen would have to be rendered in a different way. By starting the capture by double-clicking an interface, you also select it so there is nothing to indicate; if you want to start the capture by pressing the Λ button, do you consider a pop-up window "No interface selected" to fit into the overall design concept of the Qt GUI?</p></div><div id="comment-52523-info" class="comment-info"><span class="comment-age">(13 May '16, 10:29)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52529"></span><div id="comment-52529" class="comment"><div id="post-52529-score" class="comment-score"></div><div class="comment-text"><p>I think a pop-up with "No interface selected" is exactly what we need.</p></div><div id="comment-52529-info" class="comment-info"><span class="comment-age">(13 May '16, 12:11)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-52487" class="comment-tools"></div><div class="clear"></div><div id="comment-52487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

