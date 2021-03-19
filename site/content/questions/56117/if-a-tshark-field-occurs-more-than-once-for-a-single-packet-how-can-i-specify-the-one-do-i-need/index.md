+++
type = "question"
title = "If a Tshark field occurs more than once for a single packet, how can I specify the one do I need?"
description = '''In Wireshark, in packet details, sometimes a field occurs more than once, i.e. sometimes it is nested inside more than one nodes. If I want to read the .pcap file in tshark and filter a particular field which occurs more than once under different nodes, can I specify which one I want? For example, i...'''
date = "2016-10-04T00:09:00Z"
lastmod = "2016-10-04T02:47:00Z"
weight = 56117
keywords = [ "filter", "field", "display-filter", "tshark", "wireshark" ]
aliases = [ "/questions/56117" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [If a Tshark field occurs more than once for a single packet, how can I specify the one do I need?](/questions/56117/if-a-tshark-field-occurs-more-than-once-for-a-single-packet-how-can-i-specify-the-one-do-i-need)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56117-score" class="post-score" title="current number of votes">0</div><span id="post-56117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark, in packet <em>details</em>, sometimes a field occurs more than once, i.e. sometimes it is nested inside more than one nodes. If I want to read the .pcap file in tshark and filter a particular field which occurs more than once under different nodes, can I specify which one I want?</p><p>For example, in the following screenshot, there is a field called <code>Good Checksum</code> nested under a node called <code>Checksum</code>. <strong><em>JUST SUPPOSE</em> that <code>Good Checksum</code> also occurred at another place under another node, for the same node, say <code>theOtherNode</code>.</strong> The Tshark field for <code>Good Checksum</code> is <code>tcp.checksum_good</code>. So the normal Tshark command that I know of is</p><pre><code>tshark -r filename.pcap -T fields -e tcp.checksum_good</code></pre><p><strong>The question is, that in Tshark, can I specify that I want the <code>tcp.checksum_good</code> nested under <code>Checksum</code>, and not the one nested under <code>theOtherNode</code>?</strong></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2_m8ZiA6b.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '16, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p><span>Jesss</span><br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></img></div></div><div id="comments-container-56117" class="comments-container"></div><div id="comment-tools-56117" class="comment-tools"></div><div class="clear"></div><div id="comment-56117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56118"></span>

<div id="answer-container-56118" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56118-score" class="post-score" title="current number of votes">1</div><span id="post-56118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jesss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, currently there is no way to do so for fields which occur at the same encapsulation level. For your particular case where the two identically named fields exist at different encapsulation levels, you could possibly "misuse" <a href="https://wiki.wireshark.org/Mate">MATE</a>, which allows to specify the list of transport layers below which no extraction is performed, to extract your desired field into a new one like <code>mate.mypdu.myfield</code> which you would then refer to using <code>-e</code>. But the possibility would still depend on the particular arrangement of the protocols in the frame, and the <a href="https://wiki.wireshark.org/Mate">MATE</a> fields are always ASCII regardless what the source fields' format was.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '16, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56118" class="comments-container"></div><div id="comment-tools-56118" class="comment-tools"></div><div class="clear"></div><div id="comment-56118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56119"></span>

<div id="answer-container-56119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56119-score" class="post-score" title="current number of votes">1</div><span id="post-56119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The tshark <code>-E occurrence=f|l|a</code> option allows you to specify the first, last or all occurrences of each field. This setting is for all specified fields, not on a per field basis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '16, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56119" class="comments-container"><span id="56121"></span><div id="comment-56121" class="comment"><div id="post-56121-score" class="comment-score"></div><div class="comment-text"><p>True, but the OP wanted to <strong>filter</strong> on a particular occurrence, while <code>-E occurrence</code> only controls what the <code>-e</code> <strong>shows</strong>.</p></div><div id="comment-56121-info" class="comment-info"><span class="comment-age">(04 Oct '16, 02:29)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56122"></span><div id="comment-56122" class="comment"><div id="post-56122-score" class="comment-score"></div><div class="comment-text"><p>It wasn't clear to me if the OP did want to filter as in display or capture filter or filter the output to restrict the occurrence of a repeated field. Unfortunately the term filter is used (and misused) in many ways by Wireshark folks.</p><p>If the occurrence the OP wants displayed is the first (or last) then the issue is resolved :-)</p></div><div id="comment-56122-info" class="comment-info"><span class="comment-age">(04 Oct '16, 02:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56119" class="comment-tools"></div><div class="clear"></div><div id="comment-56119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

