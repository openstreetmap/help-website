+++
type = "question"
title = "displaying last N frames of all TCP streams"
description = '''I&#x27;d like to write a filter that shows last 5 frames from all TCP streams in the capture (5 last frames from stream #1, 5 last frames from stream #2, ...). Is it possible? Thanks in advance!'''
date = "2014-06-20T18:58:00Z"
lastmod = "2014-06-24T07:06:00Z"
weight = 34010
keywords = [ "display-filter" ]
aliases = [ "/questions/34010" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [displaying last N frames of all TCP streams](/questions/34010/displaying-last-n-frames-of-all-tcp-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34010-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to write a filter that shows last 5 frames from all TCP streams in the capture (5 last frames from stream #1, 5 last frames from stream #2, ...). Is it possible? Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '14, 18:58</strong></p><img src="https://secure.gravatar.com/avatar/3b45a5cf8cd1ab3fabb3de8a80fbc1a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sjlee&#39;s gravatar image" /><p>sjlee<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sjlee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jun '14, 19:40</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34010" class="comments-container"><span id="34020"></span><div id="comment-34020" class="comment"><div id="post-34020-score" class="comment-score"></div><div class="comment-text"><p>are you asking for a method during the <strong>capturing</strong> phase (question title) or during the <strong>analysis</strong> phase (question text, as I understand it)?</p><p>What exactly are you trying to do with those last 5 frames?</p></div><div id="comment-34020-info" class="comment-info"><span class="comment-age">(21 Jun '14, 16:28)</span> Kurt Knochner ♦</div></div><span id="34028"></span><div id="comment-34028" class="comment"><div id="post-34028-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment. I'm asking for a method during the analysis phase. I'd like to look at all the frames just prior to connections being closed.</p></div><div id="comment-34028-info" class="comment-info"><span class="comment-age">(21 Jun '14, 17:47)</span> sjlee</div></div></div><div id="comment-tools-34010" class="comment-tools"></div><div class="clear"></div><div id="comment-34010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34119"></span>

<div id="answer-container-34119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34119-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could write <a href="http://wiki.wireshark.org/Lua">a Lua script</a> to do this, if you want to automate it. You could either (1) write a Lua script to automatically build the appropriate display filter (i.e., a huge display filter of the correct frame numbers to display) and have the script also apply the filter, or (2) write a Lua script to create a new temporary pcap file of only the appropriate packets and have the script also load that temp file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-34119" class="comments-container"></div><div id="comment-tools-34119" class="comment-tools"></div><div class="clear"></div><div id="comment-34119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34033"></span>

<div id="answer-container-34033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34033-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a manual way to do it, but it will only work for a few connections. So, how many of those connections do you have to look at?</p><p>Unfortunately, there is no automatic way in the current code, so you'll either have to implement that yourself or use external tools.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '14, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34033" class="comments-container"><span id="34081"></span><div id="comment-34081" class="comment"><div id="post-34081-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer! In this particular case we're talking about hundreds of connections (otherwise I would have just looked at the conversations one by one).</p></div><div id="comment-34081-info" class="comment-info"><span class="comment-age">(23 Jun '14, 08:15)</span> sjlee</div></div><span id="34118"></span><div id="comment-34118" class="comment"><div id="post-34118-score" class="comment-score">1</div><div class="comment-text"><p>Since you have hundreds of connections you obviously need to automate this. If you are looking for an external tool that allows this kind of scripting, check out Unsniff. This blog post should help with your particular case <a href="http://www.unleashnetworks.com/blog/?p=627">http://www.unleashnetworks.com/blog/?p=627</a></p><p>Hope this helps.</p></div><div id="comment-34118-info" class="comment-info"><span class="comment-age">(24 Jun '14, 06:17)</span> VIVEKRJG</div></div><span id="34128"></span><div id="comment-34128" class="comment"><div id="post-34128-score" class="comment-score"></div><div class="comment-text"><p>Unsniff sounds real interesting. I'll check it out. Thanks!</p></div><div id="comment-34128-info" class="comment-info"><span class="comment-age">(24 Jun '14, 08:28)</span> sjlee</div></div></div><div id="comment-tools-34033" class="comment-tools"></div><div class="clear"></div><div id="comment-34033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

