+++
type = "question"
title = "how to find out passwords in continuation or non- http traffic?"
description = '''in my college i can&#x27;t find out any post(password finding method) for http protocols it shows &quot;continuation or non-http traffic&quot; for http protocols always. im so much confused.pls help me..if im filter out the tcp stream means all the datas are in encoded format(non human understandable(in raw)). any...'''
date = "2012-01-23T10:12:00Z"
lastmod = "2012-01-23T11:00:00Z"
weight = 8565
keywords = [ "continuation", "post", "nonhttp" ]
aliases = [ "/questions/8565" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to find out passwords in continuation or non- http traffic?](/questions/8565/how-to-find-out-passwords-in-continuation-or-non-http-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8565-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in my college i can't find out any post(password finding method) for http protocols it shows "continuation or non-http traffic" for http protocols always. im so much confused.pls help me..if im filter out the tcp stream means all the datas are in encoded format(non human understandable(in raw)). any alternative ways to detect passwords? pls help me.</p></div><div id="question-tags" class="tags-container tags">continuation post nonhttp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '12, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/bc78c927dc9edffbfa1942f94d18d0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akbarsha&#39;s gravatar image" /><p>akbarsha<br />
<span class="score" title="5 reputation points">5</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akbarsha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 20:48</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-8565" class="comments-container"><span id="8569"></span><div id="comment-8569" class="comment"><div id="post-8569-score" class="comment-score"></div><div class="comment-text"><p>you can try looking for the Credentials field. I did a quick video if it helps http://tinyurl.com/3wrwk45</p></div><div id="comment-8569-info" class="comment-info"><span class="comment-age">(23 Jan '12, 11:34)</span> thetechfirm</div></div></div><div id="comment-tools-8565" class="comment-tools"></div><div class="clear"></div><div id="comment-8565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8566"></span>

<div id="answer-container-8566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8566-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In brief, no. Passwords sent over the Internet intelligently are encrypted before transmission so that unauthorized eavesdroppers cannot obtain them in this manner. That being the case, you will not see any passwords at all, except for those that are transmitted in the clear (<code>ftp</code> passwords, for example). Are you sure that the passwords you are trying to see are actually transmitted in cleartext in an <code>http</code>-protocol packet? My guess is that they are not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '12, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8566" class="comments-container"></div><div id="comment-tools-8566" class="comment-tools"></div><div class="clear"></div><div id="comment-8566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

