+++
type = "question"
title = "Is someone willing to take a look at a capture of mine?"
description = '''Hi, some users on my website are experiencing problems while uploading a file. The problem is that the uploading is extremely slowed down. Taking hours for a simple 2MB file upload. I haven&#x27;t been able to reproduce the problem on my end. Someone recommended me to use Wireshark to trace the packets. ...'''
date = "2014-11-26T04:22:00Z"
lastmod = "2014-12-06T16:54:00Z"
weight = 38162
keywords = [ "capture", "examine", "slow", "help", "upload" ]
aliases = [ "/questions/38162" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is someone willing to take a look at a capture of mine?](/questions/38162/is-someone-willing-to-take-a-look-at-a-capture-of-mine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38162-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, some users on my website are experiencing problems while uploading a file. The problem is that the uploading is extremely slowed down. Taking hours for a simple 2MB file upload. I haven't been able to reproduce the problem on my end.</p><p>Someone recommended me to use Wireshark to trace the packets. I installed it on my computer and made a capture of a upload that went pretty normal. When I review the capture I see quite a lot of black lines which I believe to be problem marked packets. This is all new to me and actually not making a lot of sense.</p><p>So my questions is: Is someone willing to take a look to see if something is really out of the ordinary? This capture is not from a session with extremely slow upload, but maybe issues can be extracted from it anyway?</p></div><div id="question-tags" class="tags-container tags">capture examine slow help upload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '14, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/d9a37b055f7854897aa4659145fa9680?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lwvvliet&#39;s gravatar image" /><p>lwvvliet<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lwvvliet has no accepted answers">0%</span></p></div></div><div id="comments-container-38162" class="comments-container"><span id="38163"></span><div id="comment-38163" class="comment"><div id="post-38163-score" class="comment-score"></div><div class="comment-text"><p>If the capture doesn't contain sensitive information you could upload it to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the link here. Otherwise sanitize your file with TraceWrangler first: <a href="http://www.tracewrangler.com">http://www.tracewrangler.com</a></p></div><div id="comment-38163-info" class="comment-info"><span class="comment-age">(26 Nov '14, 04:42)</span> Jasper ♦♦</div></div><span id="38172"></span><div id="comment-38172" class="comment"><div id="post-38172-score" class="comment-score"></div><div class="comment-text"><p>Jasper, thanks for your response. I did what you suggested and uploaded the sanitized version. <a href="https://www.cloudshark.org/captures/b571559db283">https://www.cloudshark.org/captures/b571559db283</a></p><p>I hope you can take a look! Thanks.</p></div><div id="comment-38172-info" class="comment-info"><span class="comment-age">(26 Nov '14, 06:53)</span> lwvvliet</div></div></div><div id="comment-tools-38162" class="comment-tools"></div><div class="clear"></div><div id="comment-38162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38402"></span>

<div id="answer-container-38402" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38402-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry, I didn't have time to take a look earlier. From what I see you have packet loss on the server side, which can delay the upload process quite a bit. Your trace is not really that bad, but it takes about 1 second in some cases to get the retransmission trough (e.g. packet 1932, retransmited in 2035). This happens a couple of times during the capture, so if other uploads experience more packet loss it could get a lot worse.</p><p>Next step should be to capture at the server to see if it even gets the original packets, or if they're lost (and how many of them). In your trace we see original and retransmission, so the loss is somewhere further up on the path to the server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '14, 16:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38402" class="comments-container"></div><div id="comment-tools-38402" class="comment-tools"></div><div class="clear"></div><div id="comment-38402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

