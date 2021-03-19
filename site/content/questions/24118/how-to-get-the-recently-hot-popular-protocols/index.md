+++
type = "question"
title = "How to get the recently hot &amp; popular protocols?"
description = '''Hi folks, I&#x27;m doing a research on the protocol coverage of Wireshark. And I&#x27;d like to ask here, is there any effective way to get the hot and popular protocols up to date? Watching the bugs in Bugzilla may be an approach, but is there any possibility to get data from a widely range? such as the user...'''
date = "2013-08-28T01:57:00Z"
lastmod = "2013-08-28T06:35:00Z"
weight = 24118
keywords = [ "protocol" ]
aliases = [ "/questions/24118" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the recently hot & popular protocols?](/questions/24118/how-to-get-the-recently-hot-popular-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24118-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>I'm doing a research on the protocol coverage of Wireshark. And I'd like to ask here, is there any effective way to get the hot and popular protocols up to date? Watching the bugs in Bugzilla may be an approach, but is there any possibility to get data from a widely range? such as the users who are not so professional to file a bug in Bugzilla. Or is there such a criteria to select high-demanded protocols to develop a dissector for it?</p><p>Thanks in advance, I would really appreciate your answer.</p></div><div id="question-tags" class="tags-container tags">protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '13, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/f93696f1f8cda9ab2c5efc13d5b35625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="polerfox&#39;s gravatar image" /><p>polerfox<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="polerfox has no accepted answers">0%</span></p></div></div><div id="comments-container-24118" class="comments-container"><span id="24122"></span><div id="comment-24122" class="comment"><div id="post-24122-score" class="comment-score"></div><div class="comment-text"><p>Hot and popular to whom? Networking people data storage Telecoms/Mobile car manufacurers Cable TV etc..etc</p></div><div id="comment-24122-info" class="comment-info"><span class="comment-age">(28 Aug '13, 03:42)</span> Anders ♦</div></div><span id="24126"></span><div id="comment-24126" class="comment"><div id="post-24126-score" class="comment-score"></div><div class="comment-text"><p>to add some more:</p><p>Hot and popular protocols, where? local network, internet, corporate environment, private environment, educational environment, etc.</p><blockquote><p>I'm doing a <strong>research on the protocol coverage of Wireshark</strong>.</p></blockquote><p>I would think, that you have a list of protocols you need and then you check if those are covered by Wireshark.</p><p>If you don't have any protocols in mind, what is the purpose (and value) of such a research?</p></div><div id="comment-24126-info" class="comment-info"><span class="comment-age">(28 Aug '13, 06:11)</span> Kurt Knochner ♦</div></div><span id="24128"></span><div id="comment-24128" class="comment"><div id="post-24128-score" class="comment-score"></div><div class="comment-text"><p>Hi, What I mean is, I'd like to know the criteria of selecting high-demanded protocols to develop a dissector for it. I'm trying to do the research acting as a member of Wireshark dev team, not a normal customer. So I am curious that, there must be hundreds of protocols which haven't a dissector, how can you guys collect the data (such as top 20 popular, widely-used protocols) and define the priority in the development planning process?</p></div><div id="comment-24128-info" class="comment-info"><span class="comment-age">(28 Aug '13, 06:20)</span> polerfox</div></div></div><div id="comment-tools-24118" class="comment-tools"></div><div class="clear"></div><div id="comment-24118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24132"></span>

<div id="answer-container-24132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24132-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'd like to know the criteria of selecting high-demanded protocols to develop a dissector for it<br />
... and <strong>define the priority in the development planning process</strong>?</p></blockquote><p>There is no (official) planning process for protocol support. A dissector for a new protocol is implemented</p><ul><li>if somebody (a user of Wireshark) needs that protocol and has the knowledge to develop a dissector</li><li>a core developer has (whatever) interest in the new protocol and decides to implement a dissector for it</li></ul><p>See also the answer to your other question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/24115/how-to-request-a-new-dissector-supporting-a-protocol">http://ask.wireshark.org/questions/24115/how-to-request-a-new-dissector-supporting-a-protocol</a></p></blockquote><p>and these links:</p><blockquote><p><a href="http://wiki.wireshark.org/Development/Roadmap">http://wiki.wireshark.org/Development/Roadmap</a><br />
<a href="http://wiki.wireshark.org/Development/LifeCycle">http://wiki.wireshark.org/Development/LifeCycle</a><br />
</p></blockquote><p>So, to answer your original question:</p><blockquote><p>And I'd like to ask here, is there any effective way to get the hot and popular protocols up to date?</p></blockquote><p>There is no (simple) way to get that information as there is no process in place to collect and rate information about 'new and popular' protocols.</p><p>So your best source of information is <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and the enhancement requests there.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Aug '13, 06:48</p></div></div><div id="comments-container-24132" class="comments-container"></div><div id="comment-tools-24132" class="comment-tools"></div><div class="clear"></div><div id="comment-24132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

