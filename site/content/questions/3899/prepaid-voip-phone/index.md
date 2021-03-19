+++
type = "question"
title = "Prepaid VoIP phone?"
description = '''Can VoIP phone use prepaid card? I&#x27;m asking because, in my case, from request INVITE, it looks like a call was established with subscription (billed) number. And, as my cooworker said, calling part was prepaid...hmmm...'''
date = "2011-05-03T06:37:00Z"
lastmod = "2011-05-04T05:01:00Z"
weight = 3899
keywords = [ "phone", "prepaid", "voip", "card", "sim" ]
aliases = [ "/questions/3899" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Prepaid VoIP phone?](/questions/3899/prepaid-voip-phone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3899-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can VoIP phone use prepaid card?</p><p>I'm asking because, in my case, from request INVITE, it looks like a call was established with subscription (billed) number. And, as my cooworker said, calling part was prepaid...hmmm...</p></div><div id="question-tags" class="tags-container tags">phone prepaid voip card sim</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p>wired<br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '11, 11:17</p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-3899" class="comments-container"><span id="3901"></span><div id="comment-3901" class="comment"><div id="post-3901-score" class="comment-score"></div><div class="comment-text"><p>Sorry to be "that guy", but someone has to.</p><p>This is not an appropriate question for this forum, as it has nothing to do with Wireshark or network analysis. You need to take this up with your provider or post a question to a general VoIP forum.</p></div><div id="comment-3901-info" class="comment-info"><span class="comment-age">(03 May '11, 07:56)</span> grossman</div></div><span id="3902"></span><div id="comment-3902" class="comment"><div id="post-3902-score" class="comment-score"></div><div class="comment-text"><p>It is appropriate because I have a trace of prepaid call, but I'm not sure if it a calling or called party. But nevermind, I'll get the answer.</p></div><div id="comment-3902-info" class="comment-info"><span class="comment-age">(03 May '11, 08:32)</span> wired</div></div></div><div id="comment-tools-3899" class="comment-tools"></div><div class="clear"></div><div id="comment-3899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3911"></span>

<div id="answer-container-3911" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3911-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found it out. SIP call goes from [email protected] to "mobile_number_in_local_format"@simobil.net Si.mobil is mine provider of mobile telecommunications. So, calling party is prepaid.</p><p>For seeig that I used Telephony =&gt; VoIP Calls in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p>wired<br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3911" class="comments-container"></div><div id="comment-tools-3911" class="comment-tools"></div><div class="clear"></div><div id="comment-3911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

