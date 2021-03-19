+++
type = "question"
title = "Does Wireshark have an API?"
description = '''Hi everyone, I am a MSc. student, and I want to use Wireshark to analyze packets and import this result to Java. Anyone know whether Wireshark has an API? Sarwar U1076875@unimail.hud.ac.uk'''
date = "2012-05-20T06:27:00Z"
lastmod = "2012-05-23T04:03:00Z"
weight = 11153
keywords = [ "java" ]
aliases = [ "/questions/11153" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark have an API?](/questions/11153/does-wireshark-have-an-api)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11153-score" class="post-score" title="current number of votes">0</div><span id="post-11153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I am a MSc. student, and I want to use Wireshark to analyze packets and import this result to Java. Anyone know whether Wireshark has an API?</p><p>Sarwar<br />
<span class="__cf_email__" data-cfemail="2d781c1d1a1b151a186d">[email protected]</span><a href="http://unimail.hud.ac.uk">unimail.hud.ac.uk</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '12, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/625f3d20662b77a0133a8791e0110e5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sarwar&#39;s gravatar image" /><p><span>sarwar</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sarwar has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 May '12, 14:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11153" class="comments-container"><span id="11247"></span><div id="comment-11247" class="comment"><div id="post-11247-score" class="comment-score"></div><div class="comment-text"><p>Dear All,</p><p>Have anyone information about library to analysis packets in Java.</p></div><div id="comment-11247-info" class="comment-info"><span class="comment-age">(23 May '12, 03:22)</span> <span class="comment-user userinfo">sarwar</span></div></div><span id="11248"></span><div id="comment-11248" class="comment"><div id="post-11248-score" class="comment-score"></div><div class="comment-text"><p>did you read my answer, posted 2 days ago?</p></div><div id="comment-11248-info" class="comment-info"><span class="comment-age">(23 May '12, 04:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11153" class="comment-tools"></div><div class="clear"></div><div id="comment-11153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11154"></span>

<div id="answer-container-11154" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11154-score" class="post-score" title="current number of votes">1</div><span id="post-11154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have these options:</p><ol><li>run tshark (possibly with option -V) and then parse the text output with Java</li><li><p>If you want to use Java anyway, use one of these PCAP Java libraries/bindings:</p><ul><li>jNetPcap - <a href="http://jnetpcap.com/">http://jnetpcap.com/</a></li><li>Jpcap - <a href="http://netresearch.ics.uci.edu/kfujii/Jpcap/doc/">http://netresearch.ics.uci.edu/kfujii/Jpcap/doc/</a></li></ul></li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '12, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11154" class="comments-container"></div><div id="comment-tools-11154" class="comment-tools"></div><div class="clear"></div><div id="comment-11154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

