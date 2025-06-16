+++
type = "question"
title = "Restricted lanes with &quot;lanes&quot; tag?"
description = '''When using the lanes tag to indicate lane count, do we count only lanes open to all traffic, or do we include restricted lanes such as bus, taxi, carpool and bicycle lanes?'''
date = "2011-01-21T05:46:00Z"
lastmod = "2012-02-13T10:29:00Z"
weight = 2339
keywords = [ "psv", "bicycle", "hov", "lanes", "tagging" ]
aliases = [ "/questions/2339" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Restricted lanes with "lanes" tag?](/questions/2339/restricted-lanes-with-lanes-tag)

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
<span id="post-2339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2339-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using the lanes tag to indicate lane count, do we count only lanes open to all traffic, or do we include restricted lanes such as bus, taxi, carpool and bicycle lanes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-psv" rel="tag" title="see questions tagged &#39;psv&#39;">psv</span> <span class="post-tag tag-link-bicycle" rel="tag" title="see questions tagged &#39;bicycle&#39;">bicycle</span> <span class="post-tag tag-link-hov" rel="tag" title="see questions tagged &#39;hov&#39;">hov</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '11, 05:46</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-2339" class="comments-container">
&#10;</div>
<div id="comment-tools-2339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2339-form-container" class="comment-form-container">
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

<span id="2381"></span>

<div id="answer-container-2381" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2381-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Baloo Uriza has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all the <code>lanes=*</code> tag was not ment to handle every case. A <code>lanes=*</code> tag on highway=residential would include all motorized lanes, but not bike lanes, mostly since bike lanes tend to be so much smaller.</p>
<p><strong>Example:</strong> <a href="https://www.openstreetmap.org/browse/way/31719658">Bahnhofsplatz</a> and a <a href="http://www.panoramio.com/photo/23677275">picture of it</a>, where you can almost see 4 car lanes + cycle lane + bus lane. tagged as lanes=5</p>
<p><strong>Verbose lane tagging</strong> is AFAIK not solved, but you are not alone wanting to do that, but <code>lanes=*</code> is not the place for that. There are several proposals hidden on the wiki, on some link from the <a href="https://wiki.openstreetmap.org/wiki/Key:lanes">key:lanes=* page</a> they all lack an easy to access documentation with examples. You are free to document your findings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '11, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '11, 23:16</strong> </span></p>
</div>
</div>
<div id="comments-container-2381" class="comments-container">
<span id="2393"></span>
<div id="comment-2393" class="comment">
<div id="post-2393-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The reason I ask is because in some places (like Vancouver, BC and Portland, OR) there's a propensity for streets having a bus and taxi lane right of the bicycle lane (like on Robson in Vancouver), or multiple bicycle lanes going in the same direction (like on several central Portland streets, where common configurations are to have one bike lane on each side of a one-way so cyclists can merge to whichever one is on the side with their next turn, or two bicycle lanes adjacent on high volume, steep routes so faster cyclists don't have to use a general traffic lane to pass slower cyclists).</p>
</div>
<div id="comment-2393-info" class="comment-info">
<span class="comment-age">(23 Jan '11, 19:31)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="2401"></span>
<div id="comment-2401" class="comment">
<div id="post-2401-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well lanes was never a very good approximation of street width.</p>
</div>
<div id="comment-2401-info" class="comment-info">
<span class="comment-age">(23 Jan '11, 22:59)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="2402"></span>
<div id="comment-2402" class="comment">
<div id="post-2402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, the lanes tag is a pretty poor way to determine street width, tagging the right of way with an area as landuse=highway would give a better indication of that. However, knowing how many lanes may be useful to some routing engines to make a guess about which lane you should be in in advance.</p>
</div>
<div id="comment-2402-info" class="comment-info">
<span class="comment-age">(23 Jan '11, 23:11)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="2403"></span>
<div id="comment-2403" class="comment">
<div id="post-2403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes but the lanes tag is completely unable to handle that. You need something else. Just look at the lanes wiki page the second picture example of lanes=2, but it really looks like lanes=1.5 right? lanes is very broken..</p>
</div>
<div id="comment-2403-info" class="comment-info">
<span class="comment-age">(23 Jan '11, 23:17)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="2775"></span>
<div id="comment-2775" class="comment not_top_scorer">
<div id="post-2775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wonder if it's time to retire the lanes key at this point given it's severe shortcomings.</p>
</div>
<div id="comment-2775-info" class="comment-info">
<span class="comment-age">(08 Feb '11, 01:16)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="2787"></span>
<div id="comment-2787" class="comment not_top_scorer">
<div id="post-2787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well someone have to come up with a better one.. :-)</p>
</div>
<div id="comment-2787-info" class="comment-info">
<span class="comment-age">(08 Feb '11, 12:34)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="2796"></span>
<div id="comment-2796" class="comment">
<div id="post-2796-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unless we do not have something better it is not time to retire the lanes tag. I still think that it is usefull but only if the lane number refers to normal motor vehicle lanes.</p>
</div>
<div id="comment-2796-info" class="comment-info">
<span class="comment-age">(08 Feb '11, 15:40)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
</div>
<div id="comment-tools-2381" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-2381-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10565"></span>

<div id="answer-container-10565" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10565-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If there is one globally agreed definition of what a "lane" is, it's this: quote UN Vienna Convention on road signs and signals:</p>
<p>"Lane" means any one of the longitudinal strips into which the carriageway is divisible, whether or not defined by longitudinal road markings, which is wide enough for one moving line of motor vehicles other than motor cycles;"</p>
<p>That's what people have been told to tag with the lanes=* tag all the way from 2006. All motorcar-wide lanes count.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '12, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/54b673553098748d5c57bd19ae4157dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alv&#39;s gravatar image" />
<p><span>alv</span><br />
<span class="score" title="180 reputation points">180</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10565" class="comments-container">
&#10;</div>
<div id="comment-tools-10565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10565-form-container" class="comment-form-container">
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

