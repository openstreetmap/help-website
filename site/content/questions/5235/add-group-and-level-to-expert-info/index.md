+++
type = "question"
title = "Add group and level to expert info?"
description = '''hello, you can add a level of security and group for the coloring of the node. And how? Below an example of using: expert_add_info_format(pinfo, flags_item, MY_PI_XXX, MY_PI_XXX, &quot;Descrition&quot;); Thanks.'''
date = "2011-07-25T15:49:00Z"
lastmod = "2011-07-26T10:09:00Z"
weight = 5235
keywords = [ "expert-info" ]
aliases = [ "/questions/5235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Add group and level to expert info?](/questions/5235/add-group-and-level-to-expert-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, you can add a level of security and group for the coloring of the node. And how?</p><p>Below an example of using: expert_add_info_format(pinfo, flags_item, MY_PI_XXX, MY_PI_XXX, "Descrition");</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">expert-info</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '11, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/5905f96c1d7b3e960e209fd33429dfa4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ignacio%20Rivera&#39;s gravatar image" /><p>Ignacio Rivera<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ignacio Rivera has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '11, 16:52</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5235" class="comments-container"><span id="5255"></span><div id="comment-5255" class="comment"><div id="post-5255-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I'm not sure what the question is here.</p><p>You've quoted how to do it, for example:</p><p>expert_add_info_format(pinfo, flags_item, PI_WARN, PI_SECURITY, "Description");</p><p>See epan/proto.h for the defined PI_ values.</p></div><div id="comment-5255-info" class="comment-info"><span class="comment-age">(26 Jul '11, 06:57)</span> JeffMorriss ♦</div></div><span id="5256"></span><div id="comment-5256" class="comment"><div id="post-5256-score" class="comment-score"></div><div class="comment-text"><p>Are you asking how to apply an expert level (in order to colorize a packet/node)? Or are you asking how to define a custom expert-info level? I don't believe custom expert levels are allowed.</p></div><div id="comment-5256-info" class="comment-info"><span class="comment-age">(26 Jul '11, 07:02)</span> bstn</div></div><span id="5264"></span><div id="comment-5264" class="comment"><div id="post-5264-score" class="comment-score"></div><div class="comment-text"><p>Sorry, i am asking hoy define my new expert-info level and group. For example, PI_MY_LEVEL, and GROUP: MYGROUP.</p></div><div id="comment-5264-info" class="comment-info"><span class="comment-age">(26 Jul '11, 09:11)</span> Ignacio Rivera</div></div></div><div id="comment-tools-5235" class="comment-tools"></div><div class="clear"></div><div id="comment-5235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5267"></span>

<div id="answer-container-5267" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5267-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>(BTW, your answer should probably be converted to a comment.)</p><p>To create new expert-info levels and groups you'll have to modify Wireshark's source code. At least (and possibly only, but I haven't fully researched it) epan/proto.h and epan/expert.c .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5267" class="comments-container"><span id="5272"></span><div id="comment-5272" class="comment"><div id="post-5272-score" class="comment-score"></div><div class="comment-text"><p>Ok. Thanks. Know when you are going to make configuration?</p></div><div id="comment-5272-info" class="comment-info"><span class="comment-age">(26 Jul '11, 11:46)</span> Ignacio Rivera</div></div><span id="5273"></span><div id="comment-5273" class="comment"><div id="post-5273-score" class="comment-score"></div><div class="comment-text"><p>Sorry, what's the question?</p></div><div id="comment-5273-info" class="comment-info"><span class="comment-age">(26 Jul '11, 12:06)</span> JeffMorriss ♦</div></div><span id="5275"></span><div id="comment-5275" class="comment"><div id="post-5275-score" class="comment-score"></div><div class="comment-text"><p>I think Jeff was suggesting that <strong>you</strong> make the change in your own sandbox to allow custom expert-info.</p></div><div id="comment-5275-info" class="comment-info"><span class="comment-age">(26 Jul '11, 12:25)</span> bstn</div></div><span id="5276"></span><div id="comment-5276" class="comment"><div id="post-5276-score" class="comment-score"></div><div class="comment-text"><p>But I don't understand the advantage of adding a new expert-info. Is your primary goal to change the color of a packet/node? You can do that without a custom expert-info (the source already supports <a href="http://anonsvn.wireshark.org/viewvc/trunk/color_filters.c?revision=37859&amp;view=markup#l147">temp color filters</a>).</p></div><div id="comment-5276-info" class="comment-info"><span class="comment-age">(26 Jul '11, 12:26)</span> bstn</div></div><span id="5282"></span><div id="comment-5282" class="comment"><div id="post-5282-score" class="comment-score"></div><div class="comment-text"><p>Hmm, I don't know. There's no specific values requested here [to add to Wireshark]. And it does not make sense to have dynamic (run time) values because you have to COMPILE your dissector or plugin against whatever values you put in epan/proto.h .</p><p>You're right, maybe we need to back up and find out what the primary goal is here...</p></div><div id="comment-5282-info" class="comment-info"><span class="comment-age">(26 Jul '11, 13:17)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-5267" class="comment-tools"></div><div class="clear"></div><div id="comment-5267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

