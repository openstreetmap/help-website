+++
type = "question"
title = "Lua script eating memory"
description = '''I have run a Lua script on tshark on many capture files i have, but if i run this files sequentially i see that the number of packets is decreasing means that i am loosing some data. So I had to restart CMD every time to run the Lua script throw tshark.  I asking is this from the memory eating effec...'''
date = "2013-06-10T12:17:00Z"
lastmod = "2013-06-11T05:46:00Z"
weight = 21898
keywords = [ "lua", "eating", "loosedata" ]
aliases = [ "/questions/21898" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua script eating memory](/questions/21898/lua-script-eating-memory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21898-score" class="post-score" title="current number of votes">0</div><span id="post-21898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have run a Lua script on tshark on many capture files i have, but if i run this files sequentially i see that the number of packets is decreasing means that i am loosing some data. So I had to restart CMD every time to run the Lua script throw tshark. I asking is this from the memory eating effect?? if so is there any garbage collection tool for cleaning the memory ??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-eating" rel="tag" title="see questions tagged &#39;eating&#39;">eating</span> <span class="post-tag tag-link-loosedata" rel="tag" title="see questions tagged &#39;loosedata&#39;">loosedata</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '13, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/583b809745fa45690fa8b950c5d28714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashraf&#39;s gravatar image" /><p><span>Ashraf</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashraf has no accepted answers">0%</span></p></div></div><div id="comments-container-21898" class="comments-container"></div><div id="comment-tools-21898" class="comment-tools"></div><div class="clear"></div><div id="comment-21898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21910"></span>

<div id="answer-container-21910" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21910-score" class="post-score" title="current number of votes">0</div><span id="post-21910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I asking is this from the memory eating effect??</p></blockquote><p>hard to tell without information about the nature of your script. Do you generate any data structures yourself?</p><p>Anyway: tshark uses the dissecting engine of Wireshark and it will continuously consume RAM as it builds internal state (growing data structures) about conversations and other things needed to do the dissection. However that should not lead to 'missed packets' in your Lua script.</p><p>Is it possible to post the script somewhere?</p><blockquote><p>if so is there any garbage collection tool for cleaning the memory ??</p></blockquote><p>Currently there is no 'garbage collection' available in tshark/wireshark. Such a thing would be really interesting for a long term monitoring solution with tshark/wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21910" class="comments-container"><span id="21917"></span><div id="comment-21917" class="comment"><div id="post-21917-score" class="comment-score"></div><div class="comment-text"><p>The script is very simple it is a listener just to collect the time stamp and Length of the frame</p></div><div id="comment-21917-info" class="comment-info"><span class="comment-age">(11 Jun '13, 03:27)</span> <span class="comment-user userinfo">Ashraf</span></div></div><span id="21925"></span><div id="comment-21925" class="comment"><div id="post-21925-score" class="comment-score"></div><div class="comment-text"><blockquote><p>i see that the number of packets is decreasing means that i am loosing some data.</p></blockquote><p>well, then I don't see a correlation between the memory consumption and your observed 'data loss'. Either there is a bug in the wireshark code or your listener contains an error. Can you post the code and possibly a sample capture file?</p><p>BTW: How do you recognize the 'data loss'?</p></div><div id="comment-21925-info" class="comment-info"><span class="comment-age">(11 Jun '13, 05:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21910" class="comment-tools"></div><div class="clear"></div><div id="comment-21910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

