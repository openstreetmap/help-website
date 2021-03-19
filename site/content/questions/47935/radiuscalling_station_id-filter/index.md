+++
type = "question"
title = "radius.calling_station_id filter"
description = '''Guys, Could you give me an example of how use this filter? radius.calling_station_id I have tried with colon (:), with hyphen (-), all together and none of these gives any info. radius.calling_station_id eq AA:BB:CC:DD:EE:FF radius.calling_station_id eq aa:bb:cc:dd:ee:ff radius.calling_station_id eq...'''
date = "2015-11-24T11:39:00Z"
lastmod = "2015-11-24T12:25:00Z"
weight = 47935
keywords = [ "station", "calling" ]
aliases = [ "/questions/47935" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [radius.calling\_station\_id filter](/questions/47935/radiuscalling_station_id-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Guys,</p><p>Could you give me an example of how use this filter? radius.calling_station_id</p><p>I have tried with colon (:), with hyphen (-), all together and none of these gives any info.</p><p>radius.calling_station_id eq AA:BB:CC:DD:EE:FF radius.calling_station_id eq aa:bb:cc:dd:ee:ff radius.calling_station_id eq aa-bb-cc-dd-ee-ff radius.calling_station_id eq AA-BB-CC-DD-EE-FF radius.calling_station_id eq aabbccddeeff radius.calling_station_id eq AABBCCDDEEFF</p><p>none of them works. but if I look directly I can see the MAC address is there.</p><p>Thanks for your help.</p><p>Cheers.</p></div><div id="question-tags" class="tags-container tags">station calling</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '15, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/ddacc770b7955273148a9a77eb71c762?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Victor%20Tort&#39;s gravatar image" /><p>Victor Tort<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Victor Tort has no accepted answers">0%</span></p></div></div><div id="comments-container-47935" class="comments-container"></div><div id="comment-tools-47935" class="comment-tools"></div><div class="clear"></div><div id="comment-47935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47937"></span>

<div id="answer-container-47937" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47937-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't have a radius capture with Calling station ID AVP handy, but a general hint:</p><p>go to the packet dissection pane, select the detail of the element you are interested in, right-click to open a context menu for it and use "Apply as Filter -&gt; Selected" (or "Prepare Filter -&gt; selected").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '15, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-47937" class="comments-container"><span id="47938"></span><div id="comment-47938" class="comment"><div id="post-47938-score" class="comment-score"></div><div class="comment-text"><p>Pretty good Sindy,</p><p>how it works is by using " " example</p><p>radius.Calling_Station_Id == "AA-BB-CC-DD-EE-FF"</p><p>cheers.</p></div><div id="comment-47938-info" class="comment-info"><span class="comment-age">(24 Nov '15, 12:37)</span> Victor Tort</div></div></div><div id="comment-tools-47937" class="comment-tools"></div><div class="clear"></div><div id="comment-47937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

