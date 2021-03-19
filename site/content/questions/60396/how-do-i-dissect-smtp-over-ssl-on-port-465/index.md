+++
type = "question"
title = "How do I dissect SMTP over SSL on Port 465"
description = '''Hello! I&#x27;m trying to do same thing under smtp (destination port is 465) under Windows. How can i do that?'''
date = "2017-03-29T02:11:00Z"
lastmod = "2017-03-29T11:40:00Z"
weight = 60396
keywords = [ "ssl", "smtp" ]
aliases = [ "/questions/60396" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I dissect SMTP over SSL on Port 465](/questions/60396/how-do-i-dissect-smtp-over-ssl-on-port-465)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60396-score" class="post-score" title="current number of votes">0</div><span id="post-60396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I'm trying to do same thing under smtp (destination port is 465) under Windows. How can i do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '17, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/a64ec042436d7aee0418f929ef9244c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="icegood&#39;s gravatar image" /><p><span>icegood</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="icegood has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>29 Mar '17, 04:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60396" class="comments-container"><span id="60400"></span><div id="comment-60400" class="comment"><div id="post-60400-score" class="comment-score"></div><div class="comment-text"><p>Converted to a question from an "answer" on <a href="https://ask.wireshark.org/questions/34075/why-wireshark-cannot-display-tlsssl">this</a> question.</p></div><div id="comment-60400-info" class="comment-info"><span class="comment-age">(29 Mar '17, 04:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-60396" class="comment-tools"></div><div class="clear"></div><div id="comment-60396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60417"></span>

<div id="answer-container-60417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60417-score" class="post-score" title="current number of votes">0</div><span id="post-60417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The current Wireshark version (2.2.5) should decode SMTPS (SMTP over SSL) on port 456/TCP as SSL per default.</p><p>When your able to decode the encrypted data (e.g. with the RSA key in use or with the premaster secret) the application data should also be decoded as SMTP by default.</p><p>If your capture has not been decoded as SSL please use the „Analyze“ -&gt; „Decode As“ feature.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '17, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '17, 11:43</strong> </span></p></div></div><div id="comments-container-60417" class="comments-container"></div><div id="comment-tools-60417" class="comment-tools"></div><div class="clear"></div><div id="comment-60417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

