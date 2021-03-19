+++
type = "question"
title = "how to log website activity ?"
description = '''Hello all I want to know who browses any website with wireshark? Is it possible to know that address was visited by any computer? Thank you !'''
date = "2014-09-19T11:43:00Z"
lastmod = "2014-09-19T13:40:00Z"
weight = 36463
keywords = [ "logging", "network", "activity" ]
aliases = [ "/questions/36463" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to log website activity ?](/questions/36463/how-to-log-website-activity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36463-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all I want to know who browses any website with wireshark? Is it possible to know that address was visited by any computer?</p><p>Thank you !</p></div><div id="question-tags" class="tags-container tags">logging network activity</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '14, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/f1b6fbdc730ddb2fcaf765a6dceb381a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shawn69&#39;s gravatar image" /><p>shawn69<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shawn69 has no accepted answers">0%</span></p></div></div><div id="comments-container-36463" class="comments-container"></div><div id="comment-tools-36463" class="comment-tools"></div><div class="clear"></div><div id="comment-36463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36471"></span>

<div id="answer-container-36471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36471-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not completely sure what you want. If you want to filter a trace to show all browser requests you can use the filter:</p><p>http.request.method</p><p>To summarize export the Packet Summary Lines to CSV, import into Excel and then create a pivot table using the Source address column (as Row Labels and Sum Values).</p><p>Or you you filter the data with http.request.method, Export Specified Packets to create a filtered file, open the filtered file in Wireshark and then use:</p><p>Statistics -&gt; Conversation List -&gt; IPv4</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '14, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-36471" class="comments-container"></div><div id="comment-tools-36471" class="comment-tools"></div><div class="clear"></div><div id="comment-36471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

