+++
type = "question"
title = "wireshark decode  element in classmark3 information"
description = '''wireshark decode &amp;lt; 8-PSK Struct&amp;gt;element in classmark3 information as fixed 5bits. but, is it right ?from 3GPP24.008 the structure of this element is  &amp;lt; 8-PSK Struct&amp;gt; : :=  &amp;lt; Modulation Capability : bit &amp;gt;  { 0 | 1 &amp;lt; 8-PSK RF Power Capability 1: bit(2) &amp;gt; }  { 0 | 1 &amp;lt; 8-PSK R...'''
date = "2012-07-24T00:04:00Z"
lastmod = "2012-07-26T04:59:00Z"
weight = 12940
keywords = [ "decode", "abis", "wireshark" ]
aliases = [ "/questions/12940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark decode element in classmark3 information](/questions/12940/wireshark-decode-element-in-classmark3-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12940-score" class="post-score" title="current number of votes">0</div><span id="post-12940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>wireshark decode &lt; 8-PSK Struct&gt;element in classmark3 information as fixed 5bits. but, is it right ?from 3GPP24.008 the structure of this element is</p><pre><code> &lt; 8-PSK Struct&gt; : :=
    &lt; Modulation Capability : bit &gt;
    { 0 | 1 &lt; 8-PSK RF Power Capability 1: bit(2) &gt; }
    { 0 | 1 &lt; 8-PSK RF Power Capability 2: bit(2) &gt; }</code></pre><p>that means if &lt;8-PSK Struct&gt;=1，the following data length will be from 3 to 7 bis？</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-abis" rel="tag" title="see questions tagged &#39;abis&#39;">abis</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '12, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/bb7817a44f6d4d6b044657d48b0a7b82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="61413769&#39;s gravatar image" /><p><span>61413769</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="61413769 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jul '12, 05:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-12940" class="comments-container"></div><div id="comment-tools-12940" class="comment-tools"></div><div class="clear"></div><div id="comment-12940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13015"></span>

<div id="answer-container-13015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13015-score" class="post-score" title="current number of votes">0</div><span id="post-13015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For the record this was fixed in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=44008">http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=44008</a> Bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7524">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7524</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-13015" class="comments-container"></div><div id="comment-tools-13015" class="comment-tools"></div><div class="clear"></div><div id="comment-13015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

