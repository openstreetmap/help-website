+++
type = "question"
title = "Can I pass arguments to a sub-dissector?"
description = '''I&#x27;ve written a dissector that takes various UDP ports and dissects their packets. Now I&#x27;m writting a subdissector that my dissector calls based on an id value that it decodes. I have the subdissector registering for a range of ids (ex 600-700), however, I&#x27;m not sure of the best way to pass that id v...'''
date = "2012-01-26T11:26:00Z"
lastmod = "2014-11-18T03:25:00Z"
weight = 8627
keywords = [ "development", "dissector" ]
aliases = [ "/questions/8627" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I pass arguments to a sub-dissector?](/questions/8627/can-i-pass-arguments-to-a-sub-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8627-score" class="post-score" title="current number of votes">0</div><span id="post-8627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written a dissector that takes various UDP ports and dissects their packets. Now I'm writting a subdissector that my dissector calls based on an id value that it decodes. I have the subdissector registering for a range of ids (ex 600-700), however, I'm not sure of the best way to pass that id value to the subdissector. Any suggestions?</p><p>Additional information: I parse about 4 different items in the dissector before I pass to the sub. if the id was last I would just move my offset back when I make this call</p><pre><code>next_tvb = tvb_new_subset_remaining(tvb, offset);</code></pre><p>however the id is the first of the 4 values and I don't want the subdissector to have to grab the id and then cleanup the other values on its own. I'm looking for a cleaner way to do this.</p><p>A similar but related problem would be how my top dissector could figure out which of the several udp ports it's registered for was actually the reason it was called.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '12, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/76cdf137f5239bfbe6e10e28b7f3b56c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simply_blue&#39;s gravatar image" /><p><span>simply_blue</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simply_blue has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jan '12, 13:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8627" class="comments-container"><span id="8632"></span><div id="comment-8632" class="comment"><div id="post-8632-score" class="comment-score"></div><div class="comment-text"><p>Possibly related: <a href="/questions/5867">What is the best way to track information between packets during dissection?</a></p></div><div id="comment-8632-info" class="comment-info"><span class="comment-age">(26 Jan '12, 13:18)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="8634"></span><div id="comment-8634" class="comment"><div id="post-8634-score" class="comment-score"></div><div class="comment-text"><p>I don't think conversations will help because I only want to pass this data per packet.</p></div><div id="comment-8634-info" class="comment-info"><span class="comment-age">(26 Jan '12, 13:42)</span> <span class="comment-user userinfo">simply_blue</span></div></div></div><div id="comment-tools-8627" class="comment-tools"></div><div class="clear"></div><div id="comment-8627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8635"></span>

<div id="answer-container-8635" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8635-score" class="post-score" title="current number of votes">0</div><span id="post-8635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="simply_blue has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think I have found a solution that will solve my problem.</p><p>A lot of grepping and a re-read of the README.developer led me to the private-data field of the packet-info struct. Since I already pass pinfo to the sub-dissector, this method should store my id value per packet. If I end up with more arguments that I want to keep with the packet I'll just define my own struct in a header and include it in the dissector and sub-dissector and cast the void pointer properly on either side.</p><p>The code builds but I haven't had a chance to test it yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '12, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/76cdf137f5239bfbe6e10e28b7f3b56c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simply_blue&#39;s gravatar image" /><p><span>simply_blue</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simply_blue has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jan '12, 13:47</strong> </span></p></div></div><div id="comments-container-8635" class="comments-container"></div><div id="comment-tools-8635" class="comment-tools"></div><div class="clear"></div><div id="comment-8635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37942"></span>

<div id="answer-container-37942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37942-score" class="post-score" title="current number of votes">0</div><span id="post-37942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found it here <a href="https://www.wireshark.org/lists/wireshark-dev/200911/msg00203.html">https://www.wireshark.org/lists/wireshark-dev/200911/msg00203.html</a></p><pre><code>newtvb = tvbuffer(50):tvb()
next_dissector:call( newtvb, pinfo, treeitem )</code></pre><p>Sorry, It is not an answer to your question. This lua snippet describes sub-dissector calling.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '14, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/08e43ae5ec60b7eaf8ec9076f639e182?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hexum&#39;s gravatar image" /><p><span>hexum</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hexum has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Nov '14, 03:29</strong> </span></p></div></div><div id="comments-container-37942" class="comments-container"></div><div id="comment-tools-37942" class="comment-tools"></div><div class="clear"></div><div id="comment-37942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

