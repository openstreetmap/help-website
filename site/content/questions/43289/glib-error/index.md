+++
type = "question"
title = "Glib-ERROR"
description = '''Good evening Wireshark users, I&#x27;m getting the following error after trying to open any trace file from the terminal and the GUI. I&#x27;m able to capture traffic but not to open them as mentioned. I&#x27;m running Kali, any solutions? (wireshark:10571): GLib-ERROR **: creating thread &#x27;Recent item status&#x27;: Err...'''
date = "2015-06-17T16:04:00Z"
lastmod = "2015-06-17T23:09:00Z"
weight = 43289
keywords = [ "glib-error" ]
aliases = [ "/questions/43289" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Glib-ERROR](/questions/43289/glib-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43289-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good evening Wireshark users,</p><p>I'm getting the following error after trying to open any trace file from the terminal and the GUI. I'm able to capture traffic but not to open them as mentioned. I'm running Kali, any solutions?</p><p>(wireshark:10571): GLib-ERROR **: creating thread 'Recent item status': Error creating thread: Resource temporarily unavailable Trace/breakpoint trap</p><p>Regards, Cyverzek</p></div><div id="question-tags" class="tags-container tags">glib-error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/9ee914a9fba57513c2612c9d2735a862?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyverzek&#39;s gravatar image" /><p>cyverzek<br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyverzek has no accepted answers">0%</span></p></div></div><div id="comments-container-43289" class="comments-container"></div><div id="comment-tools-43289" class="comment-tools"></div><div class="clear"></div><div id="comment-43289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43301"></span>

<div id="answer-container-43301" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43301-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Error creating thread: Resource temporarily unavailable Trace/breakpoint trap</p></blockquote><p>According to what I found online, that could be a sign that you ran out of memory for some reason.</p><p>How much memory do you have on your Kali box and how large are the capture files you are trying to open?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43301" class="comments-container"><span id="43575"></span><div id="comment-43575" class="comment"><div id="post-43575-score" class="comment-score"></div><div class="comment-text"><p>60G. My /boot partition is at 92%, could that be the reason? All other partitions are &lt; 30%. Trace files &lt; 100MB.</p><p>Sorry for the delayed reply.</p></div><div id="comment-43575-info" class="comment-info"><span class="comment-age">(25 Jun '15, 15:56)</span> cyverzek</div></div></div><div id="comment-tools-43301" class="comment-tools"></div><div class="clear"></div><div id="comment-43301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

