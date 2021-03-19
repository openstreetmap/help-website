+++
type = "question"
title = "filtering on SMPP gives no result"
description = '''A colleague of mine wants to investigate a problem related to SMPP, and he took a snoop on the node, and when opening it with wireshark, he can see plenty of packets, then filtering on SMPP, there is nothing anymore. If I take that same snoop, load it in Wireshark, use the same filter, I can see all...'''
date = "2013-06-12T10:36:00Z"
lastmod = "2014-09-09T02:16:00Z"
weight = 21965
keywords = [ "smpp", "filtering", "result", "no" ]
aliases = [ "/questions/21965" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [filtering on SMPP gives no result](/questions/21965/filtering-on-smpp-gives-no-result)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21965-score" class="post-score" title="current number of votes">0</div><span id="post-21965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A colleague of mine wants to investigate a problem related to SMPP, and he took a snoop on the node, and when opening it with wireshark, he can see plenty of packets, then filtering on SMPP, there is nothing anymore. If I take that same snoop, load it in Wireshark, use the same filter, I can see all SMPP related packets, including bind, submit_SM that was used for his test, etc.</p><p>We have the same version of Wireshark by the way...</p><p>Do you have any idea why he can't see the SMPP packets????</p><p>Thanks,</p><p>Charles</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smpp" rel="tag" title="see questions tagged &#39;smpp&#39;">smpp</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-result" rel="tag" title="see questions tagged &#39;result&#39;">result</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '13, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/0846f67c9d8960698937e9b66ee95d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lmcchju&#39;s gravatar image" /><p><span>lmcchju</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lmcchju has no accepted answers">0%</span></p></div></div><div id="comments-container-21965" class="comments-container"><span id="36015"></span><div id="comment-36015" class="comment"><div id="post-36015-score" class="comment-score"></div><div class="comment-text"><p>I am facing same issue, filtering SMPP on Wireshark gives no result. Manual decode also not working. Any specific version to try ?</p><p>Thanks, Steve</p></div><div id="comment-36015-info" class="comment-info"><span class="comment-age">(04 Sep '14, 22:19)</span> <span class="comment-user userinfo">steve8</span></div></div><span id="36020"></span><div id="comment-36020" class="comment"><div id="post-36020-score" class="comment-score"></div><div class="comment-text"><p>Did you try Kurt's version as described below? <code>Analyze -&gt; Enabled Protocols -&gt; SMPP</code></p></div><div id="comment-36020-info" class="comment-info"><span class="comment-age">(05 Sep '14, 03:56)</span> <span class="comment-user userinfo">Edmond</span></div></div><span id="36098"></span><div id="comment-36098" class="comment"><div id="post-36098-score" class="comment-score"></div><div class="comment-text"><p>yes.It is enabled.</p></div><div id="comment-36098-info" class="comment-info"><span class="comment-age">(09 Sep '14, 02:16)</span> <span class="comment-user userinfo">steve8</span></div></div></div><div id="comment-tools-21965" class="comment-tools"></div><div class="clear"></div><div id="comment-21965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="21967"></span>

<div id="answer-container-21967" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21967-score" class="post-score" title="current number of votes">0</div><span id="post-21967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe the SMPP dissector is disabled on his machine.</p><blockquote><p><code>Analyze -&gt; Enabled Protocols -&gt; SMPP</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21967" class="comments-container"></div><div id="comment-tools-21967" class="comment-tools"></div><div class="clear"></div><div id="comment-21967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21978"></span>

<div id="answer-container-21978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21978-score" class="post-score" title="current number of votes">0</div><span id="post-21978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It also maybe that your friend has tried to decode that specific traffic (SMPP) in some other protocol and when he tries to filter now with SMPP normally he will not see anything.</p><p>Right-click to the <code>SMPP packet -&gt; Decode As</code> , than there are two options:</p><ol><li>Click on <code>Clear</code></li><li>Go to <code>Transport tab</code> and chose your <code>TCP ports</code> and select <code>SMPP</code> and <code>Apply</code></li></ol><p>Regards, Edmond.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '13, 10:18</strong> </span></p></div></div><div id="comments-container-21978" class="comments-container"></div><div id="comment-tools-21978" class="comment-tools"></div><div class="clear"></div><div id="comment-21978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21983"></span>

<div id="answer-container-21983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21983-score" class="post-score" title="current number of votes">0</div><span id="post-21983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I suggest you have the blank trace use a display filter for the TCP port number you're using (assuming this is over TCP), then do as others have suggested and do a manual right-click "Decode As" operation for SMPP.</p><p>Since SMPP doesn't use a defined port number it might just be some difference in the heuristics logic that Wireshark users between versions, if one version decodes it as SMPP and the other does not. Have you confirmed these are different versions you're using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '13, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21983" class="comments-container"><span id="21986"></span><div id="comment-21986" class="comment"><div id="post-21986-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Have you confirmed these are different versions you're using?</p></blockquote><p>Quote from the question:</p><blockquote><p>We have the <strong>same version</strong> of Wireshark by the way...</p></blockquote></div><div id="comment-21986-info" class="comment-info"><span class="comment-age">(12 Jun '13, 16:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="21989"></span><div id="comment-21989" class="comment"><div id="post-21989-score" class="comment-score"></div><div class="comment-text"><p>touché. :)</p><p>Still right that a manual decode should work though.</p></div><div id="comment-21989-info" class="comment-info"><span class="comment-age">(12 Jun '13, 19:39)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="21998"></span><div id="comment-21998" class="comment"><div id="post-21998-score" class="comment-score"></div><div class="comment-text"><blockquote><p>touché. :)</p></blockquote><p>de rien ;-)</p></div><div id="comment-21998-info" class="comment-info"><span class="comment-age">(13 Jun '13, 03:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21983" class="comment-tools"></div><div class="clear"></div><div id="comment-21983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

