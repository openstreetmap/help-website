+++
type = "question"
title = "listening twice ( lua) to the same log on tshark"
description = '''hi, i&#x27;m writing a lua script for tshark that has to run (using a listener) on a whole log once (or until it finds a specific packet) and then run on the log again and verifies it with the previously found data.  i have managed to do so in wireshark using tap:remove() and then calling a function that...'''
date = "2014-07-15T06:51:00Z"
lastmod = "2014-07-15T14:13:00Z"
weight = 34663
keywords = [ "listener", "lua", "tap", "tshark", "wireshark" ]
aliases = [ "/questions/34663" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [listening twice ( lua) to the same log on tshark](/questions/34663/listening-twice-lua-to-the-same-log-on-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34663-score" class="post-score" title="current number of votes">0</div><span id="post-34663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i'm writing a lua script for tshark that has to run (using a listener) on a whole log once (or until it finds a specific packet) and then run on the log again and verifies it with the previously found data. i have managed to do so in wireshark using tap:remove() and then calling a function that opens a new listener. however, on tshark, the new listener doesnt start from the begining of the log but from where i stopped the first tap. thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-listener" rel="tag" title="see questions tagged &#39;listener&#39;">listener</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/3fc979a5020fe344a18686c03f083147?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orenn&#39;s gravatar image" /><p><span>orenn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orenn has no accepted answers">0%</span></p></div></div><div id="comments-container-34663" class="comments-container"></div><div id="comment-tools-34663" class="comment-tools"></div><div class="clear"></div><div id="comment-34663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34693"></span>

<div id="answer-container-34693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34693-score" class="post-score" title="current number of votes">0</div><span id="post-34693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Tshark doesn't work the same way as Wireshark in terms of reading capture files. By default tshark only reads a capture file once and only dissects+taps each frame once, whereas wireshark reads it multiple times and even lets Lua force a re-read using the <code>reload()</code> function, but that won't work in tshark. There is a command switch to make tshark process a capture file twice (using the "-2" command option switch), but I'm not sure it will help you at all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '14, 14:13</strong> </span></p></div></div><div id="comments-container-34693" class="comments-container"></div><div id="comment-tools-34693" class="comment-tools"></div><div class="clear"></div><div id="comment-34693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

