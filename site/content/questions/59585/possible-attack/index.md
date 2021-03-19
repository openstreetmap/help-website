+++
type = "question"
title = "Possible attack?"
description = '''Hey, i recently encountered internet errors that my provider couldnt fix for more than a month. Sympthoms are a whole lot of FEC and CRC errors, and after a while connection to my dns becomes impossible too. But around 11 pm all these issues suddenly stop, the line becomes crystal clear. It could st...'''
date = "2017-02-21T07:23:00Z"
lastmod = "2017-03-22T08:16:00Z"
weight = 59585
keywords = [ "udp", "sip", "question", "ddos", "voip" ]
aliases = [ "/questions/59585" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Possible attack?](/questions/59585/possible-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59585-score" class="post-score" title="current number of votes">0</div><span id="post-59585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, i recently encountered internet errors that my provider couldnt fix for more than a month. Sympthoms are a whole lot of FEC and CRC errors, and after a while connection to my dns becomes impossible too. But around 11 pm all these issues suddenly stop, the line becomes crystal clear. It could still be a noisy line but all the cables were replaced already, nobody around me reports errors. My modem log displays this often, when the problems happen:</p><p>2017-02-20T23:03:27Z [Warning] IPV4 SIP UDP attack.</p><p>The line is adsl with voip. Could this be a false positive? Could someone please explain how i check this using wireshark? ( Or how can i save logs for someone expert to check) Please note that i am just an end-user, i have no knowledge about networking.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span> <span class="post-tag tag-link-ddos" rel="tag" title="see questions tagged &#39;ddos&#39;">ddos</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '17, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/8592f2b40ca197aa0e3aec9abf2f5383?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Casthaneda&#39;s gravatar image" /><p><span>Casthaneda</span><br />
<span class="score" title="3 reputation points">3</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Casthaneda has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Feb '17, 07:24</strong> </span></p></div></div><div id="comments-container-59585" class="comments-container"></div><div id="comment-tools-59585" class="comment-tools"></div><div class="clear"></div><div id="comment-59585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60214"></span>

<div id="answer-container-60214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60214-score" class="post-score" title="current number of votes">1</div><span id="post-60214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>FEC and CRC errors are usually a Layer 1 or 2 error.</p><p>Possible faulty cabling or bad cable/switch connection. If you've already replaced the cabling, look at the wires on your switch/router which that network cable is plugged into. Perhaps you have one pin partially bent?</p><p>It might also be a faulty\buggy switch/router port driver bug which only occurs when {something or another} gets over a certain level.</p><p>Cheers,</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '17, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-60214" class="comments-container"><span id="60261"></span><div id="comment-60261" class="comment"><div id="post-60261-score" class="comment-score"></div><div class="comment-text"><p>Hey, thanks for the reply, the issue is gone but i actually had to change network provider. But the issue is still a mistery to everyone including the technicians from my old service provider.</p><p>To sum it up: the modem/router was 1 month old functioned perfectly outside of certain timeframes, same for the cables and wires, my old provider had everything replaced, and had me put on a different line even. The issue surely wasnt related to my own network traffic since that was usually higher outside of the problematic tiimeframes.</p><p>Another weird thing i noticed on wireshark is that according to it my pc initiated "open vpn" connection to an unidentified brittish ip, i never had any kind of vpn installed on my current system, should i be worried by that or open vpn is something other applications might use?</p></div><div id="comment-60261-info" class="comment-info"><span class="comment-age">(22 Mar '17, 07:51)</span> <span class="comment-user userinfo">Casthaneda</span></div></div><span id="60263"></span><div id="comment-60263" class="comment"><div id="post-60263-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-60263-info" class="comment-info"><span class="comment-age">(22 Mar '17, 08:16)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-60214" class="comment-tools"></div><div class="clear"></div><div id="comment-60214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

