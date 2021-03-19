+++
type = "question"
title = "Parsing Pcap summary"
description = '''Is it possible to output the pcap summary (using -z in tshark) in a specific format like csv/xml'''
date = "2014-12-05T13:44:00Z"
lastmod = "2014-12-06T17:07:00Z"
weight = 38375
keywords = [ "summary", "tshark", "parsing" ]
aliases = [ "/questions/38375" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Parsing Pcap summary](/questions/38375/parsing-pcap-summary)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38375-score" class="post-score" title="current number of votes">0</div><span id="post-38375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to output the pcap summary (using -z in tshark) in a specific format like csv/xml</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-summary" rel="tag" title="see questions tagged &#39;summary&#39;">summary</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '14, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/b50929bbf0ce05d5c8984dc841f2a449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nightwatcher&#39;s gravatar image" /><p><span>nightwatcher</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nightwatcher has no accepted answers">0%</span></p></div></div><div id="comments-container-38375" class="comments-container"></div><div id="comment-tools-38375" class="comment-tools"></div><div class="clear"></div><div id="comment-38375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38378"></span>

<div id="answer-container-38378" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38378-score" class="post-score" title="current number of votes">1</div><span id="post-38378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not within tshark -z io,stat (though I wish it could). It's doable with a script though.</p><p>The -z io,stat output will put all the capture file's statistics you're looking for into a single very long line and a "|" delimiter. There are a couple tricks to it though:</p><ol><li><p>The output line changes depending on how many statistics you are querying. Every new metric adds one more line, so I just have a script use the number of metrics to predict the "stats line" that contains all the actual data you want.</p></li><li><p>The number of columns per metric you're trying to calculate is variable (eg: you'll get frame and byte counts with separate | delimiters if you query a normal display filter count, but you'll get a single field returned within one delimited cell if you query a function such as SUM or AVG. I actually solved this by always assuming there will be two field outputs per metric in the -z query, where a 'filler' metric will be added to my query just to make sure the "take every second field returned" rule in the script holds true.</p></li></ol><p>I really do wish -z would just give a .csv output, though. People who forego the GUI to write out a longhand -z query are likely not the sort who would want pretty ASCII text output. Likely, they're using tshark because they want to automate it and the output makes it inherently more difficult for it to be used for that purpose.</p><p>Edit: For reference, at least for the -z io,stat to be an option here I've submitted bug/feature request 10759. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10759">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10759</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '14, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '14, 15:36</strong> </span></p></div></div><div id="comments-container-38378" class="comments-container"><span id="38403"></span><div id="comment-38403" class="comment"><div id="post-38403-score" class="comment-score"></div><div class="comment-text"><p>I just wanted the summary for rtp streams and sip stats to be put in variables but now I see that there is no other way other than doing regex and other non elegant file parsing to achieve the purpose.</p></div><div id="comment-38403-info" class="comment-info"><span class="comment-age">(06 Dec '14, 17:07)</span> <span class="comment-user userinfo">nightwatcher</span></div></div></div><div id="comment-tools-38378" class="comment-tools"></div><div class="clear"></div><div id="comment-38378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

