+++
type = "question"
title = "Graphing Using TShark"
description = '''Hello. I want to be able to generate an xml graph output like that generated in Wireshark using TShark. I don&#x27;t need any filters for the moment, just the basic output. However I do need the graph to show time of day, and be in bits/second. Can anyone offer any help?'''
date = "2012-11-29T07:02:00Z"
lastmod = "2012-11-29T07:39:00Z"
weight = 16422
keywords = [ "graph", "tshark" ]
aliases = [ "/questions/16422" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Graphing Using TShark](/questions/16422/graphing-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16422-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I want to be able to generate an xml graph output like that generated in Wireshark using TShark. I don't need any filters for the moment, just the basic output. However I do need the graph to show time of day, and be in bits/second.</p><p>Can anyone offer any help?</p></div><div id="question-tags" class="tags-container tags">graph tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/95c900b24e31e3c7623eeaaca40cbed5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chazzquire&#39;s gravatar image" /><p>chazzquire<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chazzquire has no accepted answers">0%</span></p></div></div><div id="comments-container-16422" class="comments-container"><span id="16423"></span><div id="comment-16423" class="comment"><div id="post-16423-score" class="comment-score"></div><div class="comment-text"><p>can you please add some information about the xml graph output you are talking about (how do you generate it in Wireshark)?</p></div><div id="comment-16423-info" class="comment-info"><span class="comment-age">(29 Nov '12, 07:04)</span> Kurt Knochner ♦</div></div><span id="16425"></span><div id="comment-16425" class="comment"><div id="post-16425-score" class="comment-score"></div><div class="comment-text"><p>I want an IO Graph, and in Wireshark I simply click copy to get the xml.</p><p>The format is:</p><p>"Interval start","Graph 1" "15:32:51","2259" "15:33:01","2926" "15:33:11","1756" "15:33:21","1655"</p></div><div id="comment-16425-info" class="comment-info"><span class="comment-age">(29 Nov '12, 07:08)</span> chazzquire</div></div><span id="16426"></span><div id="comment-16426" class="comment"><div id="post-16426-score" class="comment-score"></div><div class="comment-text"><p>My sticking point is getting the output to show Time of day, rather than time since the start of capture.</p></div><div id="comment-16426-info" class="comment-info"><span class="comment-age">(29 Nov '12, 07:17)</span> chazzquire</div></div></div><div id="comment-tools-16422" class="comment-tools"></div><div class="clear"></div><div id="comment-16422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16427"></span>

<div id="answer-container-16427" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16427-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My sticking point is getting the output to show Time of day, rather than time since the start of capture.</p></blockquote><p>There is an option 'View as time of day' in the IO graphs. Did you try that?</p><p><strong>UPDATE:</strong></p><p>Sample with tshark:</p><blockquote><p><code>tshark -q -nr input.cap</code> <strong><code>-t ad</code></strong> <code>-z io,stat,1,"AVG(frame.len)frame.len"</code><br />
</p></blockquote><p>See the tshark man page for more information about <strong>io,stat</strong></p><blockquote><p><code>http://www.wireshark.org/docs/man-pages/tshark.html</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '12, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Nov '12, 08:07</p></div></div><div id="comments-container-16427" class="comments-container"><span id="16428"></span><div id="comment-16428" class="comment"><div id="post-16428-score" class="comment-score"></div><div class="comment-text"><p>I am running this in tshark not wireshark</p></div><div id="comment-16428-info" class="comment-info"><span class="comment-age">(29 Nov '12, 07:42)</span> chazzquire</div></div><span id="16430"></span><div id="comment-16430" class="comment"><div id="post-16430-score" class="comment-score"></div><div class="comment-text"><p>ah, right. Add the option <strong><code>-t ad</code></strong> to tshark. This works in the current version 1.8.x (possibly also with older versions). See UPDATE in my answer.</p></div><div id="comment-16430-info" class="comment-info"><span class="comment-age">(29 Nov '12, 08:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16427" class="comment-tools"></div><div class="clear"></div><div id="comment-16427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

