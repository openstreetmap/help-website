+++
type = "question"
title = "Changing the TVB in a dissector"
description = '''Is it advisable to change the tvb from a dissector. Say I have some encrypted data which I recieve in a tvb. I do the necessary decryption now I want to store it. Can I store this in the exsisitng tvb by using something like a tvb_get_pointer() and others and doing a memcpy instead of a creating new...'''
date = "2016-10-23T23:13:00Z"
lastmod = "2016-10-24T02:18:00Z"
weight = 56598
keywords = [ "dissector", "dissection", "tvb" ]
aliases = [ "/questions/56598" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Changing the TVB in a dissector](/questions/56598/changing-the-tvb-in-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56598-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it advisable to change the tvb from a dissector. Say I have some encrypted data which I recieve in a tvb. I do the necessary decryption now I want to store it.</p><p>Can I store this in the exsisitng tvb by using something like a tvb_get_pointer() and others and doing a memcpy instead of a creating new tvb using tvb_new_child_real_data() and others then passing it on for further dissection?<br />
</p><p>Please advise on which is the preferred way.</p><p>Thanks, Koundi</p></div><div id="question-tags" class="tags-container tags">dissector dissection tvb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '16, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '16, 06:50</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-56598" class="comments-container"></div><div id="comment-tools-56598" class="comment-tools"></div><div class="clear"></div><div id="comment-56598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56600"></span>

<div id="answer-container-56600" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56600-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should never go and write to the backing store of the TVB, simply because you don't know how it is composed. The only valid way to get decrypted data into a TVB is to use the <code>tvb_new_child_real_data()</code> function you found.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '16, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '16, 06:00</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-56600" class="comments-container"><span id="56603"></span><div id="comment-56603" class="comment"><div id="post-56603-score" class="comment-score"></div><div class="comment-text"><p>Those were my first instincts too :) So basically I will create a new tvbuff and pass it on for further dissection. Thanks @Jaap.</p></div><div id="comment-56603-info" class="comment-info"><span class="comment-age">(24 Oct '16, 04:40)</span> koundi</div></div></div><div id="comment-tools-56600" class="comment-tools"></div><div class="clear"></div><div id="comment-56600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

