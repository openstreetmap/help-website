+++
type = "question"
title = "Can&#x27;t view and write at the same time now?"
description = '''Hello. I used to be able to to the following: tshark -t ad -n -S -w bleh.pcap ip and host whatever is there a way I can do this with the new version of tshark? Thank you. James'''
date = "2012-08-13T14:57:00Z"
lastmod = "2012-08-13T15:01:00Z"
weight = 13595
keywords = [ "and", "capture", "view" ]
aliases = [ "/questions/13595" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't view and write at the same time now?](/questions/13595/cant-view-and-write-at-the-same-time-now)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13595-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I used to be able to to the following:</p><p>tshark -t ad -n -S -w bleh.pcap ip and host whatever</p><p>is there a way I can do this with the new version of tshark? Thank you.</p><p>James</p></div><div id="question-tags" class="tags-container tags">and capture view</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/37898d970fb9980bdd2168e913a50ca2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngel&#39;s gravatar image" /><p>DigiAngel<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngel has no accepted answers">0%</span></p></div></div><div id="comments-container-13595" class="comments-container"></div><div id="comment-tools-13595" class="comment-tools"></div><div class="clear"></div><div id="comment-13595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13596"></span>

<div id="answer-container-13596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13596-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The -S option is now used for something else, you can use the -P option, see "tshark -h":</p><pre><code>  -P        print packets even when writing to a file</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13596" class="comments-container"><span id="13599"></span><div id="comment-13599" class="comment"><div id="post-13599-score" class="comment-score"></div><div class="comment-text"><p>Awesome...just what I needed...thank you!</p></div><div id="comment-13599-info" class="comment-info"><span class="comment-age">(13 Aug '12, 15:42)</span> DigiAngel</div></div></div><div id="comment-tools-13596" class="comment-tools"></div><div class="clear"></div><div id="comment-13596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

