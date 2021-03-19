+++
type = "question"
title = "Extracting Objects"
description = '''Hi so i have been working with stream flows and its just not working i am not smart enough to grasp Hex editing and why my extracted data is not working  But i discovered the Extract Object button that works great under the file menu But some http objects are not displayed i would just like to know ...'''
date = "2016-07-28T09:19:00Z"
lastmod = "2016-07-28T10:21:00Z"
weight = 54405
keywords = [ "extraction", "object" ]
aliases = [ "/questions/54405" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting Objects](/questions/54405/extracting-objects)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54405-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi so i have been working with stream flows and its just not working i am not smart enough to grasp Hex editing and why my extracted data is not working</p><p>But i discovered the Extract Object button that works great under the file menu But some http objects are not displayed i would just like to know why and what the limits of this easy to use item is so i can know where i can use it and where not</p><p>i have tested downloading exe from a website works great but once i try and download a sample capture it does not see the object why would this be is it just that .pcap/.cap/.pcapng files are not in the data base or is there just a limited use for this feature</p></div><div id="question-tags" class="tags-container tags">extraction object</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/98ae0bbe126e829e5ab083d3d40bd1c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reynhard%20Wouda&#39;s gravatar image" /><p>Reynhard Wouda<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reynhard Wouda has no accepted answers">0%</span></p></div></div><div id="comments-container-54405" class="comments-container"></div><div id="comment-tools-54405" class="comment-tools"></div><div class="clear"></div><div id="comment-54405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54409"></span>

<div id="answer-container-54409" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54409-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It may be that there are missing packets from the capture file so the object is incomplete and thus can't be exported. But it's hard to say for sure without a capture file to look at. Coincidentally, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12588">bug 12588</a> was recently opened regarding this very topic.</p><p><em>(The bug has since been closed because it wasn't actually a bug at all but merely that packets were missing from the capture file.)</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '16, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54409" class="comments-container"><span id="54438"></span><div id="comment-54438" class="comment"><div id="post-54438-score" class="comment-score"></div><div class="comment-text"><p>Thanks Helps allot</p><p>But now all a need to know is will this work as an alternative to following a packet stream and saving the raw data and then compiling the file</p><p>it seems allot easier but will this be sufficient for all data in most cases or does the feature have a limitation to its use in the sense of garbing data from a packet capture and opening the file content downloaded by the user</p></div><div id="comment-54438-info" class="comment-info"><span class="comment-age">(29 Jul '16, 03:37)</span> Reynhard Wouda</div></div><span id="54440"></span><div id="comment-54440" class="comment"><div id="post-54440-score" class="comment-score"></div><div class="comment-text"><p>For forensic purposes it would be beneficial if the object (with holes) could be exported. Same is done for RTP streams, where artificial silence is inserted on time stamp jumps.</p></div><div id="comment-54440-info" class="comment-info"><span class="comment-age">(29 Jul '16, 04:48)</span> Jaap ♦</div></div></div><div id="comment-tools-54409" class="comment-tools"></div><div class="clear"></div><div id="comment-54409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

