+++
type = "question"
title = "highway=ford symbol shows car even on highway=path"
description = '''Is there a way to stop the ford symbol showing up like this: http://osm.org/go/eui0axNC3--'''
date = "2012-07-20T09:51:00Z"
lastmod = "2012-07-20T17:02:00Z"
weight = 14415
keywords = [ "rendering", "highway", "ford" ]
aliases = [ "/questions/14415" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [highway=ford symbol shows car even on highway=path](/questions/14415/highwayford-symbol-shows-car-even-on-highwaypath)

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
<span id="post-14415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14415-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to stop the ford symbol showing up like this:</p>
<p><a href="http://osm.org/go/eui0axNC3--">http://osm.org/go/eui0axNC3--</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-ford" rel="tag" title="see questions tagged &#39;ford&#39;">ford</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '12, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/62ccd2dd6096296adfb03b71675f6b00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="njd27&#39;s gravatar image" />
<p><span>njd27</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="njd27 has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '12, 09:57</strong> </span></p>
</div>
</div>
<div id="comments-container-14415" class="comments-container">
&#10;</div>
<div id="comment-tools-14415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14415-form-container" class="comment-form-container">
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

<span id="14416"></span>

<div id="answer-container-14416" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14416-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="njd27 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Instead of using highway=ford use ford=yes</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '12, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-14416" class="comments-container">
<span id="14423"></span>
<div id="comment-14423" class="comment">
<div id="post-14423-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As an explanation, highway=ford is the deprecated tag while ford=yes is the now preferred one. This means, however, that at some point in the future Mapnik will also render ford=yes with a car symbol unless someone submits a better icon for it :).</p>
</div>
<div id="comment-14423-info" class="comment-info">
<span class="comment-age">(20 Jul '12, 11:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14416-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14443"></span>

<div id="answer-container-14443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14443-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-14443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a couple of bits to this question - how best to map fords and how the "standard" map chooses to display them.</p>
<p>On the "how best to map fords" question, historically "<span>highway=ford</span>" was used on both nodes and ways. This was problematical on ways because what sort of highway it was (tertiary? footway?) was lost for the "ford" part. The solution to this problem was to tag a ford way in the same manner as a bridge, using highway=blah, <span>ford=yes</span>.</p>
<p>The second issue is that the "standard" map renders "highway=ford" with a symbol containing a car, for example <span>here</span>, and doesn't render "ford=yes" at all. The reason for that is that no-one's yet made it do any different. Requests for changes to OSM components are made via <a href="https://trac.openstreetmap.org/">trac</a>, or in the case of the OSM "standard" style <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/118">Github</a>, and there are at least a couple of relevant old trac issues - <a href="https://trac.openstreetmap.org/ticket/2944">2944</a> and <a href="https://trac.openstreetmap.org/ticket/3007">3007</a>. Unfortunately the database that the "standard" map is created from is optimised for rendering and doesn't contain all data, so requests of the type "can't it just display X?" are not as simple as they might seem.</p>
<p>Finally, where we're just talking about nodes where a highway intersects a waterway, I'd disagree with the "highway=ford" wiki page where it says "This tag is deprecated". There are almost no deprecated tags in OSM, because <span>you can use any tags you like</span>. Certainly, data consumers looking for fords will need to look for both "highway=ford" and "ford=yes" - according to <span>taginfo</span> there are around <span>9000</span> of <span>each</span> currently. Changing all of one type to the other overnight isn't practical for a couple of reasons:</p>
<ol>
<li>because there isn't currently an effective way of telling all data consumers to stop looking for the "old" tagging and start looking for the "new".</li>
<li>in the case of "highway=ford", a survey would be needed in some cases to determine the highway tag.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '12, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '15, 21:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-14443" class="comments-container">
&#10;</div>
<div id="comment-tools-14443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14443-form-container" class="comment-form-container">
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

