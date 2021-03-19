+++
type = "question"
title = "NIC Component Bindings During Capture"
description = '''I&#x27;m a relative novice with Wireshark and network analysis in general and my question is regarding unbinding NIC components on the NIC I use to perform captures with. I normally install/insert a dedicated NIC in the Windows computer I&#x27;m going to capture from and unbind all components from the NIC bef...'''
date = "2011-03-24T16:18:00Z"
lastmod = "2011-03-24T16:32:00Z"
weight = 3094
keywords = [ "capture", "method" ]
aliases = [ "/questions/3094" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [NIC Component Bindings During Capture](/questions/3094/nic-component-bindings-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3094-score" class="post-score" title="current number of votes">0</div><span id="post-3094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a relative novice with Wireshark and network analysis in general and my question is regarding unbinding NIC components on the NIC I use to perform captures with.</p><p>I normally install/insert a dedicated NIC in the Windows computer I'm going to capture from and unbind all components from the NIC before starting a capture (Client for Microsoft Networks, File and Printer Sharing, TCP/IP). I do this under the pretense that this eliminates the possibility that my capture host will "inject" traffic into the network I'm analyzing and skew the capture results. I've noticed that some capture programs (ColaSoft Capsa) will allow me to select this adapter for my capture while other programs won't (Wireshark, Microsoft Network Monitor).</p><p>Am I barking up the wrong tree regarding my assumption that my method ensures that my capture host won't influence the network I'm analyzing and possibly skew the capture? If so, does it not make sense for Wireshark to allow me to capture from a NIC with no components bound to it?</p><p>When I run a capture with ColaSoft Capsa with no bound components I believe I'm seeing the same results I see when using Wireshark with bound components so I don't believe I'm missing anything in the capture results using my method.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-method" rel="tag" title="see questions tagged &#39;method&#39;">method</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '11, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/bbb8df45b4d304408e6a3cea6cac2233?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joeqwerty&#39;s gravatar image" /><p><span>joeqwerty</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joeqwerty has no accepted answers">0%</span></p></div></div><div id="comments-container-3094" class="comments-container"></div><div id="comment-tools-3094" class="comment-tools"></div><div class="clear"></div><div id="comment-3094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3095"></span>

<div id="answer-container-3095" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3095-score" class="post-score" title="current number of votes">0</div><span id="post-3095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joeqwerty has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I do what you do too, unbinding all protocols from the gigabit NIC of my notebook when I capture with it for exactly the same reason: to avoid my card trying to get an IP via DHCP or do anything else in the network like reverse DNS lookups (especially if it is a customer network where I am not allowed to communicate with non-company equipment).</p><p>I think it is a network card issue if Wireshark can't use it to capture from your card, because it is absolutely no problem for mine. The card doesn't show an IP in the NIC selection dialog, but I can still start a capture with it.</p><p>Try a different card or a different PC, I think it should work. Maybe you should also try reinstalling WinPCAP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '11, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3095" class="comments-container"><span id="3096"></span><div id="comment-3096" class="comment"><div id="post-3096-score" class="comment-score"></div><div class="comment-text"><p>OK, my method isn't flawed. That's good to know. I'll try a different NIC and see what happens. Thanks much for the prompt answer.</p></div><div id="comment-3096-info" class="comment-info"><span class="comment-age">(24 Mar '11, 16:32)</span> <span class="comment-user userinfo">joeqwerty</span></div></div></div><div id="comment-tools-3095" class="comment-tools"></div><div class="clear"></div><div id="comment-3095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

