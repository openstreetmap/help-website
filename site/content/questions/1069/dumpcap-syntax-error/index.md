+++
type = "question"
title = "Dumpcap syntax error"
description = '''dumpcap -i 1 -f &quot;ip.addr == 192.168.11.61&quot; -b files:500 -b filesize:30000 -w textcap.pcap, error is string is not a valid capture filter. What is wrong with the string?'''
date = "2010-11-22T13:16:00Z"
lastmod = "2010-11-22T13:40:00Z"
weight = 1069
keywords = [ "dumpcap" ]
aliases = [ "/questions/1069" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap syntax error](/questions/1069/dumpcap-syntax-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1069-score" class="post-score" title="current number of votes">0</div><span id="post-1069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>dumpcap -i 1 -f "ip.addr == 192.168.11.61" -b files:500 -b filesize:30000 -w textcap.pcap, error is string is not a valid capture filter. What is wrong with the string?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '10, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/aa827f1bc204a438bdd0aad81d714a21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qs_tech_support&#39;s gravatar image" /><p><span>qs_tech_support</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qs_tech_support has no accepted answers">0%</span></p></div></div><div id="comments-container-1069" class="comments-container"></div><div id="comment-tools-1069" class="comment-tools"></div><div class="clear"></div><div id="comment-1069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1070"></span>

<div id="answer-container-1070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1070-score" class="post-score" title="current number of votes">3</div><span id="post-1070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What's wrong is that it's a display filter, not a capture filter; capture filters are implemented by libpcap/WinPcap, and have a different syntax from display filters. (Display filters require a full-blown Wireshark packet dissection; dumpcap does not include Wireshark dissectors, because it might have to run with special privileges, and the Wireshark dissection code is a <em>lot</em> of code to run with privileges.)</p><p>The equivalent capture filter would be "host 192.168.11.61"; it would also work as a capture filter in Wireshark, TShark, and tcpdump.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '10, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-1070" class="comments-container"></div><div id="comment-tools-1070" class="comment-tools"></div><div class="clear"></div><div id="comment-1070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

