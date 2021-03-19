+++
type = "question"
title = "HELP! Capturing an entire e-mail using Wireshark"
description = '''Hi all! I created an e-mail anti spam system and I need to test it against an anti spam product that I hired. I duplicated the port from where my e-mail&#x27;s packages comes, so now my homemade system and the oficial product receive both the same packages. My system needs to &quot;see&quot; the entire e-mail in o...'''
date = "2013-05-23T09:48:00Z"
lastmod = "2013-05-23T11:27:00Z"
weight = 21418
keywords = [ "e-mail", "packages", "question", "wireshark" ]
aliases = [ "/questions/21418" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HELP! Capturing an entire e-mail using Wireshark](/questions/21418/help-capturing-an-entire-e-mail-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21418-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all! I created an e-mail anti spam system and I need to test it against an anti spam product that I hired. I duplicated the port from where my e-mail's packages comes, so now my homemade system and the oficial product receive both the same packages. My system needs to "see" the entire e-mail in order to classify it. Now I'm running an offline test, so I captured all packages from this port with Wireshark. I used the filter tcp.srcport == 25 and exported to a txt file every package from this port. Now I have to make a program with some logic that group by sequencially all packages with text from an e-mail and recreate everyone of it manually. How can I make it easier with Wireshark? I mean, is there a way that I can get a complete e-mail without having to process the txt file in order to recreate package by package? I'm open to new ideas even if I'm using the wrong product to capture the packages. Thanks a lot! Kind Regards!</p></div><div id="question-tags" class="tags-container tags">e-mail packages question wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/c513da56ad110ff14347d854ae771bcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anthony&#39;s gravatar image" /><p>Anthony<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anthony has no accepted answers">0%</span></p></div></div><div id="comments-container-21418" class="comments-container"><span id="21550"></span><div id="comment-21550" class="comment"><div id="post-21550-score" class="comment-score"></div><div class="comment-text"><p>That's exactly I'm looking for. Just one more doubt. I collected all packages during 10 minutes. The "Follow TCP Stream" allows me to reassembly email by email. How can I do that for like 100 000 packages and reassembly all emails at once?</p><p>Many thanks!</p></div><div id="comment-21550-info" class="comment-info"><span class="comment-age">(28 May '13, 20:28)</span> Anthony</div></div></div><div id="comment-tools-21418" class="comment-tools"></div><div class="clear"></div><div id="comment-21418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21420"></span>

<div id="answer-container-21420" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21420-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try using the "Follow TCP Stream" option from the popup menu? It should display the reassembly email content in readable format unless it is encrypted or packets are missing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21420" class="comments-container"><span id="21548"></span><div id="comment-21548" class="comment"><div id="post-21548-score" class="comment-score"></div><div class="comment-text"><p>That's exactly I'm looking for. Just one more doubt. I collected all packages during 10 minutes. The "Follow TCP Stream" allows me to reassembly email by email. How can I do that for like 100 000 packages and reassembly all emails at once?</p><p>Many thanks!</p></div><div id="comment-21548-info" class="comment-info"><span class="comment-age">(28 May '13, 20:28)</span> Anthony</div></div><span id="21552"></span><div id="comment-21552" class="comment"><div id="post-21552-score" class="comment-score"></div><div class="comment-text"><p>with a tool like xplico (<a href="http://www.xplico.org/">http://www.xplico.org/</a> )</p></div><div id="comment-21552-info" class="comment-info"><span class="comment-age">(28 May '13, 23:17)</span> Kurt Knochner ♦</div></div><span id="21629"></span><div id="comment-21629" class="comment"><div id="post-21629-score" class="comment-score"></div><div class="comment-text"><p>Ok,but can I reassembly all email at once with WireShark?</p></div><div id="comment-21629-info" class="comment-info"><span class="comment-age">(30 May '13, 20:16)</span> Anthony</div></div></div><div id="comment-tools-21420" class="comment-tools"></div><div class="clear"></div><div id="comment-21420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

