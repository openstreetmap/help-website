+++
type = "question"
title = "unable to add semi-colon to filter for tshark"
description = '''Hello, I also have some troubles to use diameter.Session-Id filters. For my part the semi-colon is not allowed by tshark in the command line. -R diameter.Subsession-Id==&quot;65847;53642;517-02&quot; returns : tshark: &quot;;&quot; was unexpected in this context. REGEXs, contains, matches, don&#x27;t seem to be allowed as w...'''
date = "2013-11-19T03:31:00Z"
lastmod = "2013-11-19T07:47:00Z"
weight = 27095
keywords = [ "filter", "semi-colon", "tshark" ]
aliases = [ "/questions/27095" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unable to add semi-colon to filter for tshark](/questions/27095/unable-to-add-semi-colon-to-filter-for-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27095-score" class="post-score" title="current number of votes">0</div><span id="post-27095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I also have some troubles to use diameter.Session-Id filters. For my part the semi-colon is not allowed by tshark in the command line.</p><p>-R diameter.Subsession-Id=="65847;53642;517-02" returns : tshark: ";" was unexpected in this context.</p><p>REGEXs, contains, matches, don't seem to be allowed as well ...</p><p>Any idea to filter this AVP value ??</p><p>Thx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-semi-colon" rel="tag" title="see questions tagged &#39;semi-colon&#39;">semi-colon</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/030f7b7c77d275b741367841083fb530?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AIex&#39;s gravatar image" /><p><span>AIex</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AIex has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>19 Nov '13, 03:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-27095" class="comments-container"></div><div id="comment-tools-27095" class="comment-tools"></div><div class="clear"></div><div id="comment-27095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27100"></span>

<div id="answer-container-27100" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27100-score" class="post-score" title="current number of votes">1</div><span id="post-27100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows, if I use proper quoting, I get:</p><pre><code>tshark -Y &quot;diameter.Subsession-Id==\&quot;65847;53642;517-02\&quot;&quot;
tshark: &quot;65847;53642;517-02&quot; cannot be converted to Unsigned integer, 4 bytes.</code></pre><p>From the <a href="http://www.wireshark.org/docs/dfref/d/diameter.html">diameter display filter reference page</a>:</p><pre><code>diameter.Subsession-Id  Subsession-Id   Unsigned integer, 4 bytes   1.8.0 to 1.10.3</code></pre><p>This means that the <code>';'</code> character is invalid for this field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '13, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27100" class="comments-container"><span id="27101"></span><div id="comment-27101" class="comment"><div id="post-27101-score" class="comment-score"></div><div class="comment-text"><p>My mistake, I didn't paste the right AVP, I actually tried to filter the "diameter.Session-Id". Unfortunately the matter is still the same for this "Character string" AVP.</p><blockquote><p>diameter.Session-Id Session-Id Character string 1.0.0 to 1.2.0, 1.2.2 to 1.10.3</p></blockquote><p>-R diameter.Session-Id=="65847;53642;517-02" tshark: ";" was unexpected in this context.</p></div><div id="comment-27101-info" class="comment-info"><span class="comment-age">(19 Nov '13, 07:11)</span> <span class="comment-user userinfo">AIex</span></div></div><span id="27102"></span><div id="comment-27102" class="comment"><div id="post-27102-score" class="comment-score">1</div><div class="comment-text"><p>Try using proper quoting:</p><ul><li>Windows: <code>tshark.exe -Y "diameter.Session-Id==\"65847;53642;517-02\""</code></li><li>*Nix: <code>tshark -Y 'diameter.Session-Id=="65847;53642;517-02"'</code></li></ul></div><div id="comment-27102-info" class="comment-info"><span class="comment-age">(19 Nov '13, 07:26)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="27103"></span><div id="comment-27103" class="comment"><div id="post-27103-score" class="comment-score"></div><div class="comment-text"><p>It works with this quoting format</p><p>'diameter.Session-Id=="65847;53642;517-02"'</p><p>Thanks a lot !!!</p></div><div id="comment-27103-info" class="comment-info"><span class="comment-age">(19 Nov '13, 07:47)</span> <span class="comment-user userinfo">AIex</span></div></div></div><div id="comment-tools-27100" class="comment-tools"></div><div class="clear"></div><div id="comment-27100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

