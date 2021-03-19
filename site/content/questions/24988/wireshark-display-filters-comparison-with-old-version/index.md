+++
type = "question"
title = "Wireshark display filters comparison with old version"
description = '''Hi, We have current automation framework that uses wireshark version 1.2. We would like to use wireshark version 1.6.7. But the problem is, there are some display filters that are changed from 1.2.x to 1.6.7. I would like to get list of filters that are changed so that I can just change those in my ...'''
date = "2013-09-20T01:49:00Z"
lastmod = "2013-09-20T07:35:00Z"
weight = 24988
keywords = [ "display", "filters" ]
aliases = [ "/questions/24988" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark display filters comparison with old version](/questions/24988/wireshark-display-filters-comparison-with-old-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have current automation framework that uses wireshark version 1.2. We would like to use wireshark version 1.6.7. But the problem is, there are some display filters that are changed from 1.2.x to 1.6.7. I would like to get list of filters that are changed so that I can just change those in my automation framework. With out this data, I'll need to check all current display filters to see whether they are valid or not, which will be tedious!</p><p>Any help will be really helpful!</p></div><div id="question-tags" class="tags-container tags">display filters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '13, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/5c59321a66976ba615e1a50b46a4d209?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramprasad&#39;s gravatar image" /><p>Ramprasad<br />
<span class="score" title="20 reputation points">20</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramprasad has no accepted answers">0%</span></p></div></div><div id="comments-container-24988" class="comments-container"></div><div id="comment-tools-24988" class="comment-tools"></div><div class="clear"></div><div id="comment-24988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24989"></span>

<div id="answer-container-24989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24989-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no list of changed filters, at least I don't know one.</p><p>You can print the list of fields (usable in the filters) with tshark and run a diff on the output.</p><blockquote><p>tshark -G fields</p></blockquote><p>However, I don't know if tshark 1.2 has this feature. Just try it and you'll see.</p><p>If that does not work, you can still run a diff on the source code to see what fields have changed.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Sep '13, 02:03</p></div></div><div id="comments-container-24989" class="comments-container"><span id="24990"></span><div id="comment-24990" class="comment"><div id="post-24990-score" class="comment-score"></div><div class="comment-text"><p>That approach was my idea, too, but I didn't remember how to list all the fields. I don't use tshark enough, it seems :-)</p></div><div id="comment-24990-info" class="comment-info"><span class="comment-age">(20 Sep '13, 02:28)</span> Jasper ♦♦</div></div><span id="24993"></span><div id="comment-24993" class="comment"><div id="post-24993-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I don't use tshark enough, it seems :-)</p></blockquote><p>well, I'm a lot into automation in my projects and tshark is quite useful for some tasks.</p><p>But, it's never too late ;-) And you are probably spending some of time on <a href="http://www.tracewrangler.com/">tracewrangler</a> :-)</p></div><div id="comment-24993-info" class="comment-info"><span class="comment-age">(20 Sep '13, 03:59)</span> Kurt Knochner ♦</div></div><span id="25041"></span><div id="comment-25041" class="comment"><div id="post-25041-score" class="comment-score"></div><div class="comment-text"><p>yup, whenever there is time I'm wrangling code :-)</p></div><div id="comment-25041-info" class="comment-info"><span class="comment-age">(20 Sep '13, 07:44)</span> Jasper ♦♦</div></div></div><div id="comment-tools-24989" class="comment-tools"></div><div class="clear"></div><div id="comment-24989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25035"></span>

<div id="answer-container-25035" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25035-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark <a href="http://www.wireshark.org/docs/dfref/">Display Filter Reference</a> page lists all fields and their applicable versions.</p><p>And besides <code>tshark -G fields</code> that Kurt mentioned, you can also get that information from Wireshark via: <code>Internals -&gt; Supported Protocols (slow!) -&gt; Display Filter Fields</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25035" class="comments-container"><span id="25038"></span><div id="comment-25038" class="comment"><div id="post-25038-score" class="comment-score"></div><div class="comment-text"><blockquote><p>lists all fields <strong>and their applicable versions</strong>.</p></blockquote><p>that would be a nice extension for tshark.</p></div><div id="comment-25038-info" class="comment-info"><span class="comment-age">(20 Sep '13, 07:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25035" class="comment-tools"></div><div class="clear"></div><div id="comment-25035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

