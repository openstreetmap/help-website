+++
type = "question"
title = "How to do capture on Cisco switch with Wireshark"
description = '''How do you do a capture on Cisco switch that is connected to a server that is remotely connected to PC using Wireshark? I cannot put Wireshark on the server but would like to (if possible) do the capture from a PC remotely connected to that server instead. I&#x27;m new to this. Bear with me.'''
date = "2014-11-24T18:05:00Z"
lastmod = "2014-11-26T07:55:00Z"
weight = 38114
keywords = [ "switch", "remote" ]
aliases = [ "/questions/38114" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to do capture on Cisco switch with Wireshark](/questions/38114/how-to-do-capture-on-cisco-switch-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38114-score" class="post-score" title="current number of votes">0</div><span id="post-38114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do you do a capture on Cisco switch that is connected to a server that is remotely connected to PC using Wireshark? I cannot put Wireshark on the server but would like to (if possible) do the capture from a PC remotely connected to that server instead. I'm new to this. Bear with me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '14, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/004381850ed115e9ba83dfaae4f3fccc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="holtsclaw74&#39;s gravatar image" /><p><span>holtsclaw74</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="holtsclaw74 has no accepted answers">0%</span></p></div></div><div id="comments-container-38114" class="comments-container"></div><div id="comment-tools-38114" class="comment-tools"></div><div class="clear"></div><div id="comment-38114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38126"></span>

<div id="answer-container-38126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38126-score" class="post-score" title="current number of votes">0</div><span id="post-38126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may want to read <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a> for starters to see how capture setups are usually set up.</p><p>What you can do additionally is to use RSPAN/ERSPAN to configure remote SPANning solutions, but they have a lot of drawbacks, e.g. timings that aren't exact, and the transport of additional capture load over the backbone. <a href="http://wiki.wireshark.org/SwitchReference/CiscoSystems">See</a> <a href="http://wiki.wireshark.org/SwitchReference/CiscoSystems">http://wiki.wireshark.org/SwitchReference/CiscoSystems</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '14, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38126" class="comments-container"><span id="38175"></span><div id="comment-38175" class="comment"><div id="post-38175-score" class="comment-score"></div><div class="comment-text"><p>Jasper. Thank you for the helpful advice. Regards.</p></div><div id="comment-38175-info" class="comment-info"><span class="comment-age">(26 Nov '14, 07:55)</span> <span class="comment-user userinfo">holtsclaw74</span></div></div></div><div id="comment-tools-38126" class="comment-tools"></div><div class="clear"></div><div id="comment-38126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

