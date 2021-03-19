+++
type = "question"
title = "Add dissectors inside GSM-MAP protocol dissector"
description = '''Hello, i have some extra tags that i would like to decode inside a GSM-MAP message. So i decided to add my dissector code inside the allready defined code for GSM-MAP (edit /epan/dissector/packet-gsm_map.c file). After adding my impacts inside the existing code i tried to build again the source code...'''
date = "2016-10-06T02:11:00Z"
lastmod = "2016-10-07T04:13:00Z"
weight = 56179
keywords = [ "map", "dissector", "gsm_map" ]
aliases = [ "/questions/56179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Add dissectors inside GSM-MAP protocol dissector](/questions/56179/add-dissectors-inside-gsm-map-protocol-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56179-score" class="post-score" title="current number of votes">0</div><span id="post-56179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i have some extra tags that i would like to decode inside a GSM-MAP message. So i decided to add my dissector code inside the allready defined code for GSM-MAP (edit /epan/dissector/packet-gsm_map.c file). After adding my impacts inside the existing code i tried to build again the source code, after the compilation of the new gsm_map.c file compiler came up with some errors inside gsm_map.cnf file displaying the extra data and structures added. Below you can se some logs of the errors</p><pre><code>&quot;ett_gsm_map_lsc_XXX&quot; undeclared identifier
&quot;dissect_gsm_map_lsc_XXX&quot; undeclared identifier
&quot;initializer is not a contstant&quot;
etc.</code></pre>Inside the error logs the gsm_map.cnf file appears. I think i should edit and update accordingly the gsm_map.cnf file but i dont know how Any idea?</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-gsm_map" rel="tag" title="see questions tagged &#39;gsm_map&#39;">gsm_map</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '16, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/57991ad0d04b3bd4c722c2b266d9494f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vapashos&#39;s gravatar image" /><p><span>vapashos</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vapashos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '16, 02:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-56179" class="comments-container"></div><div id="comment-tools-56179" class="comment-tools"></div><div class="clear"></div><div id="comment-56179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56216"></span>

<div id="answer-container-56216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56216-score" class="post-score" title="current number of votes">0</div><span id="post-56216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The erroneous line indicated by the compiler is somewhat of a red herring as the packet-gsm_map.c is a generated file there is statements like this <code>#line 227 "./asn1/gsm_map/gsm_map.cnf"</code> generated in the code so the compiler will refer to offsets of those. It is possible to edit packet-gsm_map.c and make it compile but "right" way would be to edit the ASN1 files with your new tags and regenerate the file I suppose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '16, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Oct '16, 07:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-56216" class="comments-container"></div><div id="comment-tools-56216" class="comment-tools"></div><div class="clear"></div><div id="comment-56216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

