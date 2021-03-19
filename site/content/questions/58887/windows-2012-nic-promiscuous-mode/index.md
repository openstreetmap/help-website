+++
type = "question"
title = "Windows 2012 NIC PROMISCUOUS MODE."
description = '''I have installed Wireshark , Wincap and I have my port listening on my switch How do I put my NIC into promiscuous mode. I don&#x27;t know how to do this in window server 2012'''
date = "2017-01-19T08:37:00Z"
lastmod = "2017-01-19T09:01:00Z"
weight = 58887
keywords = [ "windows", "nic", "promiscuous", "server2012" ]
aliases = [ "/questions/58887" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows 2012 NIC PROMISCUOUS MODE.](/questions/58887/windows-2012-nic-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58887-score" class="post-score" title="current number of votes">0</div><span id="post-58887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed Wireshark , Wincap and I have my port listening on my switch How do I put my NIC into promiscuous mode. I don't know how to do this in window server 2012</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-server2012" rel="tag" title="see questions tagged &#39;server2012&#39;">server2012</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '17, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p><span>msmorten</span><br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span></p></div></div><div id="comments-container-58887" class="comments-container"></div><div id="comment-tools-58887" class="comment-tools"></div><div class="clear"></div><div id="comment-58887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58888"></span>

<div id="answer-container-58888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58888-score" class="post-score" title="current number of votes">1</div><span id="post-58888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark, by default, will put a NIC into promiscuous mode when opening it for capture.</p><p>You can disable this by going to the Capture Interfaces dialog (menu Capture -&gt; Options or Ctrl + K) and unchecking the "Promiscuous" checkbox of the required interfaces.</p><p>As Wireshark defaults to promiscuous mode you might also be referring to setting your switch port to such a mode, this is called port mirroring or spanning and you'll have to consult your switch manual for that, Wireshark can't help here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '17, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58888" class="comments-container"></div><div id="comment-tools-58888" class="comment-tools"></div><div class="clear"></div><div id="comment-58888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

