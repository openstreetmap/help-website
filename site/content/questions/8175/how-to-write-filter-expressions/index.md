+++
type = "question"
title = "How to write filter expressions??"
description = '''Hi I&#x27;m trying to figure out the generic logic of writing filter expression to be able to write them easily. I found a link that shows its syntax. The link is that : http://openmaniak.com/wireshark_filters.php It shows that expressions always start with protocol name, then (.) dot and one of that pro...'''
date = "2012-01-01T18:24:00Z"
lastmod = "2012-01-01T19:43:00Z"
weight = 8175
keywords = [ "filter", "expression" ]
aliases = [ "/questions/8175" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to write filter expressions??](/questions/8175/how-to-write-filter-expressions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8175-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm trying to figure out the generic logic of writing filter expression to be able to write them easily. I found a link that shows its syntax. The link is that : http://openmaniak.com/wireshark_filters.php</p><p>It shows that expressions always start with protocol name, then (.) dot and one of that protocol's substructure follows.</p><p>Is it always like this? Are there any more rules to write filter expression that must be followed?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">filter expression</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '12, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/f28df4e1d1ceb6f6a38657888457a740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sawque&#39;s gravatar image" /><p>sawque<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sawque has no accepted answers">0%</span></p></div></div><div id="comments-container-8175" class="comments-container"></div><div id="comment-tools-8175" class="comment-tools"></div><div class="clear"></div><div id="comment-8175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8176"></span>

<div id="answer-container-8176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8176-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, it's not quite that simple. The first thing to understand is that there are two kinds of filters in Wireshark: Capture filters and display filters, and they use different syntax. Here's a reference on <a href="http://wiki.wireshark.org/CaptureFilters">capture filters</a> from the Wireshark wiki, and another one on <a href="http://wiki.wireshark.org/DisplayFilters">display filters</a>.</p><p>Creating filters in Wireshark is a "learn by doing" thing. I recommend you just jump in and try to create different filters, and then come back here with any specific questions if you have difficulty.</p><p>I'd start with display filters first, and tackle capture filters second. You really need display filters in order to do meaningful analysis in Wireshark, but you can do without capture filters at first.</p><p>Also, Google is your friend. There is a lot of information about Wireshark filters on the web.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '12, 19:43</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-8176" class="comments-container"><span id="8177"></span><div id="comment-8177" class="comment"><div id="post-8177-score" class="comment-score">2</div><div class="comment-text"><p>Other useful links:<br />
<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDefineFilterSection.html">display filters</a><br />
<a href="http://www.wireshark.org/docs/dfref/">display filter Reference</a><br />
<a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html">capture filters</a><br />
Or watch some <a href="http://www.youtube.com/watch?v=__SR6JO6l-A">videos</a> at YouTube.</p></div><div id="comment-8177-info" class="comment-info"><span class="comment-age">(02 Jan '12, 00:19)</span> joke</div></div></div><div id="comment-tools-8176" class="comment-tools"></div><div class="clear"></div><div id="comment-8176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

