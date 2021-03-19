+++
type = "question"
title = "display only portion of data field as column"
description = '''hi.. my company is using custom data packets to send info to access points and other devices.  i was wondering is there a way to have only a specific position in the data field byte array that can be displayed as a column (like data[52]), in the table.  alternatively can you create a custom column w...'''
date = "2015-03-03T03:40:00Z"
lastmod = "2015-03-03T10:08:00Z"
weight = 40203
keywords = [ "column", "bytes", "array", "data" ]
aliases = [ "/questions/40203" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [display only portion of data field as column](/questions/40203/display-only-portion-of-data-field-as-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40203-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi..</p><p>my company is using custom data packets to send info to access points and other devices. i was wondering is there a way to have only a specific position in the data field byte array that can be displayed as a column (like data[52]), in the table.</p><p>alternatively can you create a custom column with labels that would display a string if data[52]==3 and another string in case another data[52]==4 , similar to the coloring rules, only with labels (as it is hard to remember which colors belong to each message)</p></div><div id="question-tags" class="tags-container tags">column bytes array data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '15, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/c1ae031356d61509c1e12593563f937d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emaayan&#39;s gravatar image" /><p>emaayan<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emaayan has no accepted answers">0%</span></p></div></div><div id="comments-container-40203" class="comments-container"></div><div id="comment-tools-40203" class="comment-tools"></div><div class="clear"></div><div id="comment-40203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40223"></span>

<div id="answer-container-40223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40223-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a similar questions.</p><blockquote><p><a href="https://ask.wireshark.org/questions/31295/need-part-of-data-only">https://ask.wireshark.org/questions/31295/need-part-of-data-only</a></p></blockquote><p>To sum it up: Wireshark does not offer that functionality by default. You can however write a Post-Dissector (e.g. in Lua) and add your own fields to the frame, which can then be used to show data in a column.</p><p>See also here:</p><blockquote><p><a href="https://ask.wireshark.org/questions/26091/how-to-display-s1apgtp_teid-as-decimal-format">https://ask.wireshark.org/questions/26091/how-to-display-s1apgtp_teid-as-decimal-format</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40223" class="comments-container"><span id="40365"></span><div id="comment-40365" class="comment"><div id="post-40365-score" class="comment-score"></div><div class="comment-text"><p>actually the using color rules and then 'apply as column' on the color is pretty close to what i want, i understand that from 1.9.0 it's considered buggy?</p></div><div id="comment-40365-info" class="comment-info"><span class="comment-age">(08 Mar '15, 08:14)</span> emaayan</div></div><span id="40403"></span><div id="comment-40403" class="comment"><div id="post-40403-score" class="comment-score"></div><div class="comment-text"><p>I think the Lua postdissector code would get you much closer to the desired result than anything of Wiresharks built in functionality.</p></div><div id="comment-40403-info" class="comment-info"><span class="comment-age">(09 Mar '15, 13:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40223" class="comment-tools"></div><div class="clear"></div><div id="comment-40223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

