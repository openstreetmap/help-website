+++
type = "question"
title = "How to circumvent Lua limitation for 200 local variables when machine-generating a dissector from XML description of protocol"
description = '''I&#x27;ve used Matlab (this is the easiest language for me) to generate a Lua dissector from an XML file describing a protocol. The issue right now, is that it is generating too many local (global) variables and I&#x27;m getting the `too many local variables (limit is 200) in main function near &#x27;=&#x27;`  error. M...'''
date = "2017-08-10T01:27:00Z"
lastmod = "2018-07-31T09:15:00Z"
weight = 63458
keywords = [ "lua", "limitation" ]
aliases = [ "/questions/63458" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to circumvent Lua limitation for 200 local variables when machine-generating a dissector from XML description of protocol](/questions/63458/how-to-circumvent-lua-limitation-for-200-local-variables-when-machine-generating-a-dissector-from-xml-description-of-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63458-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've used Matlab (this is the easiest language for me) to generate a Lua dissector from an XML file describing a protocol.</p><p>The issue right now, is that it is generating too many local (global) variables and I'm getting the</p><pre><code>`too many local variables (limit is 200) in main function near &#39;=&#39;`</code></pre><p>error.</p><p>Many of the variables (~150) are due to some enumeration.</p><p>Any suggestion how to solve it?</p></div><div id="question-tags" class="tags-container tags">lua limitation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '17, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p>BMWE<br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '17, 01:39</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-63458" class="comments-container"><span id="63459"></span><div id="comment-63459" class="comment"><div id="post-63459-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/7415/bmwe">@BMWE</a>, I've converted your post to a new Question as this way it better fits this site's purpose.</p></div><div id="comment-63459-info" class="comment-info"><span class="comment-age">(10 Aug '17, 01:39)</span> sindy</div></div><span id="63460"></span><div id="comment-63460" class="comment"><div id="post-63460-score" class="comment-score"></div><div class="comment-text"><p>To the subject, what means "some enumeration"? If your protocol has 150 distinct fields, there is no surprise that 150 variables get created. If that is not the case, please provide some more details.</p></div><div id="comment-63460-info" class="comment-info"><span class="comment-age">(10 Aug '17, 01:40)</span> sindy</div></div></div><div id="comment-tools-63458" class="comment-tools"></div><div class="clear"></div><div id="comment-63458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64340"></span>

<div id="answer-container-64340" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64340-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I realize this is an old question on a now-obsolete Q&amp;A site, but in case anyone finds themselves in this situation, one solution is to group variables together into a Lua table.</p><p>For example, instead of:</p><pre><code>local variableA = 1
local variableB = 2
...
local variableZ = 26</code></pre><p>use something like:</p><pre><code>local variables = {
    A = 1,
    B = 2,
    ...,
    Z = 26
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '18, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-64340" class="comments-container"></div><div id="comment-tools-64340" class="comment-tools"></div><div class="clear"></div><div id="comment-64340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

