+++
type = "question"
title = "pcap: network type 538976257"
description = '''Hi, i tried to open a pcap-file with an unsuccessful SIP-registration, but i get the following error message: The file &quot;hpbx_reg.pcap&quot; is a capture for a network type that Wireshark doesn&#x27;t support. (pcap: network type 538976257 unknown or unsupported) My Wireshark version is Version 1.10.6 (v1.10.6...'''
date = "2015-08-11T02:51:00Z"
lastmod = "2015-08-11T15:22:00Z"
weight = 44958
keywords = [ "538976257", "version", "type", "network" ]
aliases = [ "/questions/44958" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pcap: network type 538976257](/questions/44958/pcap-network-type-538976257)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44958-score" class="post-score" title="current number of votes">0</div><span id="post-44958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i tried to open a pcap-file with an unsuccessful SIP-registration, but i get the following error message: The file "hpbx_reg.pcap" is a capture for a network type that Wireshark doesn't support. (pcap: network type 538976257 unknown or unsupported)</p><p>My Wireshark version is Version 1.10.6 (v1.10.6 from master-1.10)</p><p>Regards Martin H.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-538976257" rel="tag" title="see questions tagged &#39;538976257&#39;">538976257</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/2c6b26dbae29a5a0155dcbe3371a473a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaHa86&#39;s gravatar image" /><p><span>MaHa86</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaHa86 has no accepted answers">0%</span></p></div></div><div id="comments-container-44958" class="comments-container"><span id="44960"></span><div id="comment-44960" class="comment"><div id="post-44960-score" class="comment-score"></div><div class="comment-text"><p>The file may be broken, it wasn't ftp:d with ASCII rather than BIN by any chance?</p></div><div id="comment-44960-info" class="comment-info"><span class="comment-age">(11 Aug '15, 06:42)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-44958" class="comment-tools"></div><div class="clear"></div><div id="comment-44958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44971"></span>

<div id="answer-container-44971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44971-score" class="post-score" title="current number of votes">0</div><span id="post-44971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>538976257 decimal is 20202001 hex, which has 3 blanks and a control-A, so this <em>definitely</em> looks as if the file was somehow damaged.</p><p>What program produced the file, and what programs, if any, were used to transfer the file from the machine that produced it to the machine on which you read it? As Anders said, it might, for example, have been FTPed between a Windows machine and a UN*X machine in ASCII mode; that will probably damage any non-plain-text file, although whether it will produce that <em>particular</em> form of damage is another matter (it would convert hex 0A to hex 0D 0A when transferring from UN*X to Windows, transfer hex 0D 0A to hex 0A when transferring Windows to UN*X, and might do other things as well).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44971" class="comments-container"></div><div id="comment-tools-44971" class="comment-tools"></div><div class="clear"></div><div id="comment-44971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

