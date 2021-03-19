+++
type = "question"
title = "how to find request based on the http code"
description = '''I have filtered the http 500 code requests using http.response.code == 500. but i would like to see which request got the http 500. how do i filter this. thanks'''
date = "2014-07-15T11:49:00Z"
lastmod = "2014-07-15T13:07:00Z"
weight = 34674
keywords = [ "filter" ]
aliases = [ "/questions/34674" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to find request based on the http code](/questions/34674/how-to-find-request-based-on-the-http-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34674-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have filtered the http 500 code requests using http.response.code == 500. but i would like to see which request got the http 500. how do i filter this.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/be8a9b2e9d87b13606c3b9e75d26e71d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scara&#39;s gravatar image" /><p>scara<br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scara has no accepted answers">0%</span></p></div></div><div id="comments-container-34674" class="comments-container"></div><div id="comment-tools-34674" class="comment-tools"></div><div class="clear"></div><div id="comment-34674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34690"></span>

<div id="answer-container-34690" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34690-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The field <code>http.request_in</code> contains the packet number of the request. If you expand the 'Hypertext Transfer Protocol' node in the packet details pane you should see the field <code>[Request in frame: xxx]</code>, which is double-clickable to take you straight to the request. You can also right-click the field and select <code>Go to Corresponding Packet</code> to do the same.</p><p>The inverse also applies in the request which has the field <code>http.response_in</code>, shown as <code>[Response in frame: xxx]</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34690" class="comments-container"><span id="34696"></span><div id="comment-34696" class="comment"><div id="post-34696-score" class="comment-score"></div><div class="comment-text"><p>Thanks it was useful but for some http 500 requests i only see next request in frame and next response in frame. Some have Prev response in frame,Request in frame , Next request in frame, Next response in frame. why is it like this?</p></div><div id="comment-34696-info" class="comment-info"><span class="comment-age">(15 Jul '14, 19:18)</span> scara</div></div></div><div id="comment-tools-34690" class="comment-tools"></div><div class="clear"></div><div id="comment-34690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34683"></span>

<div id="answer-container-34683" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34683-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>right click the '500' frame and select 'Follow TCP Stream'. That should work in most cases.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34683" class="comments-container"></div><div id="comment-tools-34683" class="comment-tools"></div><div class="clear"></div><div id="comment-34683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

