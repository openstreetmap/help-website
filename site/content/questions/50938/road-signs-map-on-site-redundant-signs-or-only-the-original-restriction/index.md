+++
type = "question"
title = "Road signs: map on-site redundant signs or only the original restriction?"
description = '''Hello, there. I&#x27;m wondering about mapping restriction road signs: on numerous occasions, these restrictions only repeated other restrictions, clearly in order to highlight them, for example:  a no-turn restriction which prevents entry in a one-way road, or  a no-entry sign with a &quot;but road managemen...'''
date = "2016-07-16T08:46:00Z"
lastmod = "2016-07-16T19:25:00Z"
weight = 50938
keywords = [ "restrictions", "turn_restrictions", "routing", "tagging", "interpretation" ]
aliases = [ "/questions/50938" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Road signs: map on-site redundant signs or only the original restriction?](/questions/50938/road-signs-map-on-site-redundant-signs-or-only-the-original-restriction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50938-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I'm wondering about mapping restriction road signs: on numerous occasions, these restrictions only repeated other restrictions, clearly in order to highlight them, for example:</p>
<ol>
<li>a no-turn restriction which prevents entry in a one-way road, or</li>
<li>a no-entry sign with a "but road management" used to highlight a private access restriction on an access road.</li>
</ol>
<p>In such cases, should I map these restrictions as is, or should I be smart, interpret them and only map the intent behind them, letting the routing engines managing them as they want, i.e. map these examples as:</p>
<ol>
<li>only the <code>oneway=yes</code> road, ignoring the resulting no-turn restrictions, and</li>
<li>mark the road as <code>access=private</code></li>
</ol>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-interpretation" rel="tag" title="see questions tagged &#39;interpretation&#39;">interpretation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '16, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50938" class="comments-container">
&#10;</div>
<div id="comment-tools-50938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50938-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50946"></span>

<div id="answer-container-50946" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50946-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Penegal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Always map the intent of signs. Mapping the signs themselves (and particularly repeater signs) is entirely optional, but ultimately may help fellow mappers in cases where particular restrictions, such as speedlimits, change.</p>
<p>The community of mappers in Helsinki, Finland moved to mapping the signs and their wiki page (<a href="http://wiki.openstreetmap.org/wiki/Finland:Traffic_signs">http://wiki.openstreetmap.org/wiki/Finland:Traffic_signs</a>) provides some good reasons for doing so. Broadly speaking mapping signs assists in verification, and helps spot change &amp; errors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '16, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-50946" class="comments-container">
&#10;</div>
<div id="comment-tools-50946" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50946-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50945"></span>

<div id="answer-container-50945" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50945-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess it comes down to why you are mapping. :)</p>
<p>I have seen areas where a node for each sign it placed adjacent to the highway and, amazingly, the actual information not placed on the ways where it would do routing software any good. I've never understood that as I don't see the use case (no rendering software I am aware of shows those signs and routing software only looks at ways or relations relating to ways).</p>
<p>For highway mapping, I personally don't map signs, I map the intent of the signs on the ways. The reason for this is I am interested in having routing software correctly get people to where they want to go. So I'll map the lane marking (for lane guidance), add maxspeed (for better routing and speed warnings while following router instructions), turn restrictions (for legal routing), destination information (for motorway exit guidance), etc. to the appropriate ways. About the only way you'll figure out where the sign was based on my mapping is because of a change in some value (e.g. maxspeed).</p>
<p>I do map signs along hiking trails as they are shown by at least a few renders that specialize in back country maps and they are often significant landmarks for a person to use to keep oriented.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '16, 16:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-50945" class="comments-container">
&#10;</div>
<div id="comment-tools-50945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50945-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

