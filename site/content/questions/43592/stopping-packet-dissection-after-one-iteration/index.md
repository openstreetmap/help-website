+++
type = "question"
title = "Stopping  packet dissection after one iteration"
description = '''Hi all, I am working on a dissector for srtp which can decrypt and play audio.So once the dissector runs and processes a packet and then there is a rollover,next time i try to play audio my dissector thinks that the packets belonging to the first cycle are also the packets after rollover so it keeps...'''
date = "2015-06-26T07:30:00Z"
lastmod = "2015-06-29T23:20:00Z"
weight = 43592
keywords = [ "roc", "srtp", "rtp" ]
aliases = [ "/questions/43592" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Stopping packet dissection after one iteration](/questions/43592/stopping-packet-dissection-after-one-iteration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43592-score" class="post-score" title="current number of votes">0</div><span id="post-43592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,<br />
</p><p>I am working on a dissector for srtp which can decrypt and play audio.So once the dissector runs and processes a packet and then there is a rollover,next time i try to play audio my dissector thinks that the packets belonging to the first cycle are also the packets after rollover so it keeps the roc 1 which results in a failure.I really hope I made sense!<br />
</p><p>So can someone help me in figuring out how to either stop the dissector from processing already proccesed packets again or get the correct roc for the current packet! Thanks a lot!</p><p>-koundinya</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-roc" rel="tag" title="see questions tagged &#39;roc&#39;">roc</span> <span class="post-tag tag-link-srtp" rel="tag" title="see questions tagged &#39;srtp&#39;">srtp</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '15, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p><span>koundi</span><br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-43592" class="comments-container"><span id="43605"></span><div id="comment-43605" class="comment"><div id="post-43605-score" class="comment-score"></div><div class="comment-text"><p>Note that <em>dissectors</em> shouldn't play audio themselves; if you can plug into the same mechanism that the existing audio player code does, that would probably work better, and, if you <em>can't</em> plug into that mechanism, that's a deficiency in that mechanism, and you should file an enhancement request on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>.</p></div><div id="comment-43605-info" class="comment-info"><span class="comment-age">(27 Jun '15, 13:19)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="43705"></span><div id="comment-43705" class="comment"><div id="post-43705-score" class="comment-score"></div><div class="comment-text"><p>yes I am taking care of that I pass it on to the rtp tap so that I can use the telephony-&gt;rtp-&gt;analyse option to see srtp streams as well adn play them.</p></div><div id="comment-43705-info" class="comment-info"><span class="comment-age">(29 Jun '15, 23:20)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-43592" class="comment-tools"></div><div class="clear"></div><div id="comment-43592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43594"></span>

<div id="answer-container-43594" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43594-score" class="post-score" title="current number of votes">0</div><span id="post-43594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="koundi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The pinfo-&gt;fd-&gt;flags.visited flag allows you to know when a given packet is seen for the first time. So you can use this to do whatever you want / need to do on first pass, then save the result and retrieve it afterwards (for subsequent passes). That's what is done for request response tracking for example. You can find more info in doc/README.request_response_tracking file for example, or by checking the use of this flag in other dissectors.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '15, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43594" class="comments-container"><span id="43595"></span><div id="comment-43595" class="comment"><div id="post-43595-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the prompt response I will test it tomorrow and let you know how it goes,then i will accept your answer.Thanks so much! you guys rock:)</p></div><div id="comment-43595-info" class="comment-info"><span class="comment-age">(26 Jun '15, 11:14)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="43660"></span><div id="comment-43660" class="comment"><div id="post-43660-score" class="comment-score"></div><div class="comment-text"><p>hi pascal, I did find the flag that you pointed me to,But It doesnot help me because</p><p>1.My packet is first read as rtp(as all srtp packets are just proccesed as rtp packets) and is processed before I pass the key to the rtp dissector.</p><p>2.so when I send it the key it has already been processed by rtp dissector and I cant differentiate between the 2nd and third time when it is being processed. 3.For storing the decrypted data I am using the data sources which I add when it is decrypted the first time.so that I can check if it is already proccesed by srtp then I just give the dissector the decrypted tvb when the rtp dissector is called.</p><p>I am implementing the srtp decryption as part of the rtp dissector.Please suggest an alternative way for the dissector to remember that srtp has not been done even though rtp dissector has proccesed the packet once Thanks a lot! -koundi</p></div><div id="comment-43660-info" class="comment-info"><span class="comment-age">(29 Jun '15, 04:59)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-43594" class="comment-tools"></div><div class="clear"></div><div id="comment-43594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

