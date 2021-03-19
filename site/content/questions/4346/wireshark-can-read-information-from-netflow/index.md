+++
type = "question"
title = "Wireshark can read information from netflow ?"
description = '''Hello, i have one PC connected to router interface, and i want see a trafic for other interface in the same router. So, i want use wireshark to snif and read a netflow information from these interfaces, it&#x27;s possible ? need a some modifications or indications in wireshark ?  Thanks.'''
date = "2011-06-02T13:02:00Z"
lastmod = "2011-06-07T18:38:00Z"
weight = 4346
keywords = [ "netflow" ]
aliases = [ "/questions/4346" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark can read information from netflow ?](/questions/4346/wireshark-can-read-information-from-netflow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4346-score" class="post-score" title="current number of votes">0</div><span id="post-4346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i have one PC connected to router interface, and i want see a trafic for other interface in the same router. So, i want use wireshark to snif and read a netflow information from these interfaces, it's possible ? need a some modifications or indications in wireshark ? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netflow" rel="tag" title="see questions tagged &#39;netflow&#39;">netflow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '11, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/189db3db5399fb754985552c5f110783?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adi&#39;s gravatar image" /><p><span>Adi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jun '11, 13:14</strong> </span></p></div></div><div id="comments-container-4346" class="comments-container"></div><div id="comment-tools-4346" class="comment-tools"></div><div class="clear"></div><div id="comment-4346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4351"></span>

<div id="answer-container-4351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4351-score" class="post-score" title="current number of votes">2</div><span id="post-4351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a difference in being able to dissect NetFlow packets and to collect (&amp;report on) NetFlow packets.</p><p>Wireshark can dissect NetFlow traffic as it travels from the NetFlow Agent (your router) to the Collector (absent in your network if I read your question correctly). So, even though Wireshark is capable of interpreting the NetFlow packets, it will not collect them, aggregate them and report (combined) statistics which seems to be what you want.</p><p>You might want to have a look at <a href="http://www.ntop.org/overview.html">NTOP</a>, which is capable of collecting NetFlow packets and might be more the tool you're looking for...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4351" class="comments-container"></div><div id="comment-tools-4351" class="comment-tools"></div><div class="clear"></div><div id="comment-4351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4448"></span>

<div id="answer-container-4448" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4448-score" class="post-score" title="current number of votes">0</div><span id="post-4448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please consider <a href="http://www.plixer.com/products/netflow-sflow/scrutinizer-netflow-sflow.php">Scrutinizer</a> as well for NetFlow Reporting and Analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 18:38</strong></p><img src="https://secure.gravatar.com/avatar/2aa41cab1f69408fe078675ef2868614?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jake%20Wilson&#39;s gravatar image" /><p><span>Jake Wilson</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jake Wilson has no accepted answers">0%</span></p></div></div><div id="comments-container-4448" class="comments-container"></div><div id="comment-tools-4448" class="comment-tools"></div><div class="clear"></div><div id="comment-4448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

