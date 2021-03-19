+++
type = "question"
title = "expert info"
description = '''Is there a way to use wireshark/tshark with options to generate the &quot;analyze-&amp;gt;expert info&quot; output for an input/existing PCAP file? thanks'''
date = "2013-02-07T16:32:00Z"
lastmod = "2013-02-08T12:05:00Z"
weight = 18428
keywords = [ "info", "expert" ]
aliases = [ "/questions/18428" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [expert info](/questions/18428/expert-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18428-score" class="post-score" title="current number of votes">0</div><span id="post-18428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to use wireshark/tshark with options to generate the "analyze-&gt;expert info" output for an input/existing PCAP file?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-expert" rel="tag" title="see questions tagged &#39;expert&#39;">expert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '13, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/a8ed11193097e6b69df83d0bf5770f82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="donlex&#39;s gravatar image" /><p><span>donlex</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="donlex has no accepted answers">0%</span></p></div></div><div id="comments-container-18428" class="comments-container"></div><div id="comment-tools-18428" class="comment-tools"></div><div class="clear"></div><div id="comment-18428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18431"></span>

<div id="answer-container-18431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18431-score" class="post-score" title="current number of votes">0</div><span id="post-18431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately that functionality is not implemented. The best you can do is this:</p><blockquote><p><code>tshark -nr input.pcap -z expert -q</code><br />
</p></blockquote><p>and/or</p><blockquote><p><code>tshark -nr input.pcap -R "expert" -T fields -e frame.number -e expert -E occurrence=a</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '13, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Feb '13, 02:02</strong> </span></p></div></div><div id="comments-container-18431" class="comments-container"><span id="18441"></span><div id="comment-18441" class="comment"><div id="post-18441-score" class="comment-score"></div><div class="comment-text"><p>The development version does have a tshark tap for this. e.g.</p><p>tshark -2 -r input.pcap -zexpert,&lt;min-severity&gt; -q</p><p>where min-severity can be error error | warn | note | chat</p></div><div id="comment-18441-info" class="comment-info"><span class="comment-age">(08 Feb '13, 01:35)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="18442"></span><div id="comment-18442" class="comment"><div id="post-18442-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The development version does have a tshark tap for this. e.g.</p></blockquote><p>hm.. that option is already in the version 1.8.x. See my first example in the answer. Is the output different in the development version?</p></div><div id="comment-18442-info" class="comment-info"><span class="comment-age">(08 Feb '13, 02:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="18445"></span><div id="comment-18445" class="comment"><div id="post-18445-score" class="comment-score"></div><div class="comment-text"><p>Oops, sorry, I didn't spot that your first example already uses it, and hadn't checked that it was already in 1.8. There have been no changes to the code for this since the 1.8 branch was created, so the form of the output would be the same.</p><p>If the functionality that the question wanted is not implemented, what is it that they are looking for?</p></div><div id="comment-18445-info" class="comment-info"><span class="comment-age">(08 Feb '13, 04:31)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="18448"></span><div id="comment-18448" class="comment"><div id="post-18448-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If the functionality that the question wanted is not implemented, what is it that they are looking for?</p></blockquote><p>good question. Let's wait for an update of the OP.</p></div><div id="comment-18448-info" class="comment-info"><span class="comment-age">(08 Feb '13, 12:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-18431" class="comment-tools"></div><div class="clear"></div><div id="comment-18431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

