+++
type = "question"
title = "what is ardus??"
description = '''At least, I think it&#x27;s called protocol. All I can find is that it stands for Automatic Retrieval Delete Update System. My computer is connecting on Port 1115 and I&#x27;m trying to figure out what program is executing this?'''
date = "2011-05-11T08:15:00Z"
lastmod = "2011-05-11T09:06:00Z"
weight = 4034
keywords = [ "ardus" ]
aliases = [ "/questions/4034" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [what is ardus??](/questions/4034/what-is-ardus)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4034-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At least, I think it's called protocol. All I can find is that it stands for Automatic Retrieval Delete Update System. My computer is connecting on Port 1115 and I'm trying to figure out what program is executing this?</p></div><div id="question-tags" class="tags-container tags">ardus</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '11, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/580aa0ee8838d179c079bd87f15238e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="david&#39;s gravatar image" /><p>david<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="david has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '11, 08:40</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4034" class="comments-container"><span id="4035"></span><div id="comment-4035" class="comment"><div id="post-4035-score" class="comment-score"></div><div class="comment-text"><p>I'm curious: I note that 3 years ago a question with almost exactly the same wording was asked on answers.yahoo.com.</p><p>Any connection ?</p><p>http://answers.yahoo.com/question/index?qid=20080402113115AAc1d7t</p></div><div id="comment-4035-info" class="comment-info"><span class="comment-age">(11 May '11, 08:34)</span> Bill Meier ♦♦</div></div><span id="4037"></span><div id="comment-4037" class="comment"><div id="post-4037-score" class="comment-score"></div><div class="comment-text"><p>seems to be the exact same question... :-)</p></div><div id="comment-4037-info" class="comment-info"><span class="comment-age">(11 May '11, 09:00)</span> Jasper ♦♦</div></div><span id="4039"></span><div id="comment-4039" class="comment"><div id="post-4039-score" class="comment-score"></div><div class="comment-text"><p>Yup. Either @david is the same person as @LadyInvisible, or he/she has the same problem and decided to copy-and-paste.</p></div><div id="comment-4039-info" class="comment-info"><span class="comment-age">(11 May '11, 09:06)</span> bstn</div></div></div><div id="comment-tools-4034" class="comment-tools"></div><div class="clear"></div><div id="comment-4034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4038"></span>

<div id="answer-container-4038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4038-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you're just getting confused by the transport layer name resolution feature that replaced the port 1115 with "ardus". In most cases that port is just an ephemeral port your PC used as a client port. You can disable the transport layer name resolution in the Wireshark preferences or the View Menu.</p><p>If you want to know what program uses the port you could runing <code>netstat -anb</code> (if you're running Windows). I guess there are similar possibilities for Linux/MacOS</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '11, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4038" class="comments-container"></div><div id="comment-tools-4038" class="comment-tools"></div><div class="clear"></div><div id="comment-4038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4036"></span>

<div id="answer-container-4036" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4036-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.ethereal.com/lists/ethereal-users/200506/msg00003.html">ARDUS</a> appears to be an application/DLL that interfaces with Microsoft Access. It uses port <a href="http://www.speedguide.net/port.php?port=1115">1115</a>, <a href="http://www.speedguide.net/port.php?port=1116">1116</a>, and <a href="http://www.speedguide.net/port.php?port=1117">1117</a>, which are shared with <strong>trojans / worms</strong>. The traffic you're seeing might actually be these creatures at work. You should run a virus scanner.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '11, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-4036" class="comments-container"></div><div id="comment-tools-4036" class="comment-tools"></div><div class="clear"></div><div id="comment-4036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

