+++
type = "question"
title = "Removed fields"
description = '''What happens with removed fields? Such as ipv6.traffic_class.dscp which is no longer present in Wireshark 2.0? Any replacements or something? Are these changes documented somewhere?'''
date = "2016-02-23T05:34:00Z"
lastmod = "2016-02-23T06:48:00Z"
weight = 50431
keywords = [ "fields", "filtering" ]
aliases = [ "/questions/50431" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Removed fields](/questions/50431/removed-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50431-score" class="post-score" title="current number of votes">0</div><span id="post-50431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What happens with removed fields? Such as <strong>ipv6.traffic_class.dscp</strong> which is no longer present in Wireshark 2.0? Any replacements or something? Are these changes documented somewhere?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '16, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/a03fa5b340afab78d2e44b63e8dcf3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aliniel&#39;s gravatar image" /><p><span>Aliniel</span><br />
<span class="score" title="30 reputation points">30</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aliniel has 2 accepted answers">100%</span></p></div></div><div id="comments-container-50431" class="comments-container"></div><div id="comment-tools-50431" class="comment-tools"></div><div class="clear"></div><div id="comment-50431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50432"></span>

<div id="answer-container-50432" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50432-score" class="post-score" title="current number of votes">1</div><span id="post-50432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aliniel has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately not really, except via the git commit messages, and even then it may not be spelt out in detail.</p><p>Arguably there should be a list of fields that have changed between releases, the command <code>tshark -G fields</code> will list all the fields in the version of tshark being run, this could be used as a basis of a diff, but that may not really be sufficient to indicate why a field was removed (or what it was renamed to).</p><p>In the case of the field you mention, that was replaced by <code>ipv6.tclass.dscp</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50432" class="comments-container"></div><div id="comment-tools-50432" class="comment-tools"></div><div class="clear"></div><div id="comment-50432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50435"></span>

<div id="answer-container-50435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50435-score" class="post-score" title="current number of votes">0</div><span id="post-50435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>All display filter fields for all Wireshark releases since 1.0.0 are documented online at <a href="https://www.wireshark.org/docs/dfref/">https://www.wireshark.org/docs/dfref/</a>. For <strong>ipv6.traffic_class.dscp</strong> specifically, refer to <a href="https://www.wireshark.org/docs/dfref/i/ipv6.html">https://www.wireshark.org/docs/dfref/i/ipv6.html</a> where you find the following:</p><pre><code>Field name                  Description                 Type                  Versions
ipv6.traffic_class.dscp     Differentiated Services     Unsigned integer,     1.4.0 to 1.12.9
                            Field                       4 bytes</code></pre><p>As Graham mentioned, the field was replaced with <strong>ipv6.tclass.dscp</strong>, documented as:</p><pre><code>ipv6.tclass.dscp            Differentiated Services     Unsigned integer,     2.0.0 to 2.0.1
                            Codepoint                   4 bytes</code></pre><p>Here is the specific commit where the change was made and the reason for it: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=9162177db968f1310d867c32d2920298302f01b5">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=9162177db968f1310d867c32d2920298302f01b5</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-50435" class="comments-container"><span id="50437"></span><div id="comment-50437" class="comment"><div id="post-50437-score" class="comment-score"></div><div class="comment-text"><p>Yeah, I know about the list. Still, there should be a note or a reference for the fields that got replaced, in my opinion.</p></div><div id="comment-50437-info" class="comment-info"><span class="comment-age">(23 Feb '16, 06:48)</span> <span class="comment-user userinfo">Aliniel</span></div></div></div><div id="comment-tools-50435" class="comment-tools"></div><div class="clear"></div><div id="comment-50435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

