+++
type = "question"
title = "Issues in capturing Wireshark filters"
description = '''I am trying to launch wireshark from the cli with the following options... wireshark -k -i eth2 -a filesize:1000000 -f &amp;lt;capture filter=&quot;&quot;&amp;gt; The issue I have is that I want to use a pre-defined wireshark filter... when I run the above with the actual filter in the cli cmd it works, when I use a ...'''
date = "2012-12-13T09:22:00Z"
lastmod = "2012-12-17T16:18:00Z"
weight = 16843
keywords = [ "capture", "cli", "wireshark" ]
aliases = [ "/questions/16843" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Issues in capturing Wireshark filters](/questions/16843/issues-in-capturing-wireshark-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16843-score" class="post-score" title="current number of votes">0</div><span id="post-16843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to launch wireshark from the cli with the following options...</p><p>wireshark -k -i eth2 -a filesize:1000000 -f &lt;capture filter=""&gt; The issue I have is that I want to use a pre-defined wireshark filter... when I run the above with the actual filter in the cli cmd it works, when I use a pre-defined one it fails..</p><p>Working example:</p><p>wireshark -k -i eth2 -a filesize:1000000 -f "host 40.40.41.42" Failure example (the one I am trying to use):</p><p>wireshark -k -i eth2 -a filesize:1000000 -f pre-defined-capture1 Where pre-defined-capture1 filter does show up under "Capture -&gt; Options -&gt; Capture Filter" list...</p><p>The error i get is that the filter is not valid, I would like to specify the filter I saved in the capture filters list if thats possible...</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-cli" rel="tag" title="see questions tagged &#39;cli&#39;">cli</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/d2f70ff89f7658e1d5aa17bf89bd5b48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gates2010&#39;s gravatar image" /><p><span>gates2010</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gates2010 has no accepted answers">0%</span></p></div></div><div id="comments-container-16843" class="comments-container"></div><div id="comment-tools-16843" class="comment-tools"></div><div class="clear"></div><div id="comment-16843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16886"></span>

<div id="answer-container-16886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16886-score" class="post-score" title="current number of votes">0</div><span id="post-16886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, what you are asking for is not yet implemented. The option '-f' accepts only filters in the libpcap syntax. Please file and enhancement bug at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16886" class="comments-container"><span id="16998"></span><div id="comment-16998" class="comment"><div id="post-16998-score" class="comment-score"></div><div class="comment-text"><p>filed a bug.. thank you</p></div><div id="comment-16998-info" class="comment-info"><span class="comment-age">(17 Dec '12, 16:18)</span> <span class="comment-user userinfo">gates2010</span></div></div></div><div id="comment-tools-16886" class="comment-tools"></div><div class="clear"></div><div id="comment-16886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

