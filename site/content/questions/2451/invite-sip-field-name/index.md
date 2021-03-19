+++
type = "question"
title = "&quot;INVITE sip&quot;:  Field Name?"
description = '''I have a VOIP gateway running in &quot;Debug&quot; mode - so that it throws copies of all it&#x27;s packets to my workstation - and WireShark is showing said packets. The packets I am interested in start with &quot;INVITE sip:&quot; (phone number dialed). Looks like the stuff in the &quot;Info&quot; column is a concatonation of many ...'''
date = "2011-02-21T07:13:00Z"
lastmod = "2011-02-21T07:33:00Z"
weight = 2451
keywords = [ "invitation" ]
aliases = [ "/questions/2451" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["INVITE sip": Field Name?](/questions/2451/invite-sip-field-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2451-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a VOIP gateway running in "Debug" mode - so that it throws copies of all it's packets to my workstation - and WireShark is showing said packets.</p><p>The packets I am interested in start with "INVITE sip:" (phone number dialed).</p><p>Looks like the stuff in the "Info" column is a concatonation of many fields.</p><p>To the end of filtering for the "INVITE: sip" packets, does anybody know the field name for those particular invitations?<br />
</p><p>"aim_invitation" does not seem tb the one.... or is it and I'm missing something?</p></div><div id="question-tags" class="tags-container tags">invitation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '11, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/8bde5a113e61480e8111dcc2e49409f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeteCress&#39;s gravatar image" /><p>PeteCress<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeteCress has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-2451" class="comments-container"></div><div id="comment-tools-2451" class="comment-tools"></div><div class="clear"></div><div id="comment-2451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2452"></span>

<div id="answer-container-2452" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2452-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Display filter:<br />
sip.Method == "INVITE"<br />
<br />
See: <a href="http://www.wireshark.org/docs/dfref/s/sip.html">Display Filter Reference</a>: Session Initiation Protocol</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '11, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-2452" class="comments-container"><span id="2455"></span><div id="comment-2455" class="comment"><div id="post-2455-score" class="comment-score"></div><div class="comment-text"><p>Can anybody suggest what I am doing wrong?</p><p>http://tinyurl.com/4v8usr4</p><p>FWIW, just plain "INVITE" gives the same result.</p></div><div id="comment-2455-info" class="comment-info"><span class="comment-age">(21 Feb '11, 11:33)</span> PeteCress</div></div><span id="2456"></span><div id="comment-2456" class="comment"><div id="post-2456-score" class="comment-score"></div><div class="comment-text"><p>I think I got a valid expression now. Used the expression builder instead of typing it in.</p><p>Sorry for the excess verbage...</p></div><div id="comment-2456-info" class="comment-info"><span class="comment-age">(21 Feb '11, 11:49)</span> PeteCress</div></div><span id="2457"></span><div id="comment-2457" class="comment"><div id="post-2457-score" class="comment-score"></div><div class="comment-text"><p>Just in case some other noob is climbing this little learning curve, the Real Deal is syslog.msg contains "INVITE sip:"</p><p>Reason: Since we are reading packets sent by a VOIP gateway in "Debug" mode, the packets we see are actually Protocol=Syslog instead of Protocol=SIP...</p></div><div id="comment-2457-info" class="comment-info"><span class="comment-age">(21 Feb '11, 11:59)</span> PeteCress</div></div></div><div id="comment-tools-2452" class="comment-tools"></div><div class="clear"></div><div id="comment-2452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

