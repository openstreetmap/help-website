+++
type = "question"
title = "Is there a tag to store bus intervals?"
description = '''Is there an OSM tag to store bus intervals at different times of the day?'''
date = "2015-01-15T10:55:00Z"
lastmod = "2015-01-15T17:03:00Z"
weight = 40390
keywords = [ "tagging" ]
aliases = [ "/questions/40390" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a tag to store bus intervals?](/questions/40390/is-there-a-tag-to-store-bus-intervals)

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
<span id="post-40390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40390-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there an OSM tag to store bus intervals at different times of the day?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '15, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e0304055ba107b43dc134e4a9e5a955c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wasus&#39;s gravatar image" />
<p><span>Wasus</span><br />
<span class="score" title="346 reputation points">346</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wasus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '15, 10:56</strong> </span></p>
</div>
</div>
<div id="comments-container-40390" class="comments-container">
&#10;</div>
<div id="comment-tools-40390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40390-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="40396"></span>

<div id="answer-container-40396" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40396-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-40396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Wasus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe the most widely used tag is <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Headway">headway</a>, but this is a) not <a href="http://taginfo.openstreetmap.org/keys/headway">used very much</a>, b) a somewhat obscure term. It is also mainly used with a single value, presumable the typical service interval during the day.</p>
<p>It is not something I have tagged myself, and I certainly agree with others that in many cases trying to enter such a tag on OSM is not useful. That being said, there is clearly some utility in being able to discriminate on something like the Public Transport layer between services based on frequency of service. (And although such information can be gathered from things like GTFS it is often non-trivial to provide a concise summary).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '15, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-40396" class="comments-container">
<span id="40399"></span>
<div id="comment-40399" class="comment">
<div id="post-40399-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>And the wiki page for the headway tag then refers to a later proposal for an "interval" tag: <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Interval">https://wiki.openstreetmap.org/wiki/Proposed_features/Interval</a> It's still not used very much though: <a href="http://taginfo.openstreetmap.org/keys/interval#overview">http://taginfo.openstreetmap.org/keys/interval#overview</a></p>
</div>
<div id="comment-40399-info" class="comment-info">
<span class="comment-age">(15 Jan '15, 17:03)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-40396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40396-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40393"></span>

<div id="answer-container-40393" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40393-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-40393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not that I know of, and I'm doubtful there would be, because:</p>
<ol>
<li>that would be a really complex tagging scheme, probably using some variant on the <a href="http://wiki.openstreetmap.org/wiki/Key:opening_hours">opening hours</a> scheme</li>
<li>it could potentially change so much it would be difficult to keep updated in OSM</li>
<li>it might make more sense to use something like the <a href="https://developers.google.com/transit/gtfs/">Google Transit Feed Specification</a>, which is specifically tailored to distribute this kind of information</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '15, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '15, 16:14</strong> </span></p>
</div>
</div>
<div id="comments-container-40393" class="comments-container">
&#10;</div>
<div id="comment-tools-40393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40393-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40394"></span>

<div id="answer-container-40394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40394-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello !</p>
<p>I'm not sure that this kind of tagging will help many people. Bus frequencies often change every year. Are you willing to change these ? If you don't people will complain OSM information is not accurate.</p>
<p>I would link the the website of the bus operator with the tag</p>
<p>website=http://...</p>
<p>best regards,</p>
<p>DF45</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '15, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/669afc5a0f42b94aec8450a16a53696a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DF45&#39;s gravatar image" />
<p><span>DF45</span><br />
<span class="score" title="196 reputation points">196</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DF45 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40394" class="comments-container">
&#10;</div>
<div id="comment-tools-40394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40394-form-container" class="comment-form-container">
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

