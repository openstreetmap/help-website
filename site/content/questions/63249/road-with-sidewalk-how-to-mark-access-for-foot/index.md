+++
type = "question"
title = "Road with sidewalk, how to mark access for foot"
description = '''I have a highway:service sidewalk:right I wonder what would be the proper way to mark access for foot. I&#x27;m thinking either foot:designed because sidewalk is designed for foot, or foot:yes because while sidewalk is for foot, the road is not and that&#x27;s the part that is being mapped here. Alternatively...'''
date = "2018-05-01T09:58:00Z"
lastmod = "2018-05-01T10:50:00Z"
weight = 63249
keywords = [ "foot", "access", "sidewalks" ]
aliases = [ "/questions/63249" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Road with sidewalk, how to mark access for foot](/questions/63249/road-with-sidewalk-how-to-mark-access-for-foot)

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
<span id="post-63249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63249-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a</p>
<p><code>highway:service sidewalk:right</code></p>
<p>I wonder what would be the proper way to mark access for <code>foot</code>. I'm thinking either <code>foot:designed</code> because sidewalk is designed for foot, or <code>foot:yes</code> because while sidewalk is for foot, the road is not and that's the part that is being mapped here.</p>
<p>Alternatively I might map sidewalk separately, which makes sense too, because other sidewalks in that area are mapped that way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-foot" rel="tag" title="see questions tagged &#39;foot&#39;">foot</span> <span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-sidewalks" rel="tag" title="see questions tagged &#39;sidewalks&#39;">sidewalks</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '18, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9f399cd11754dee90b48d8ee30e13e69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HalfTough&#39;s gravatar image" />
<p><span>HalfTough</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HalfTough has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63249" class="comments-container">
&#10;</div>
<div id="comment-tools-63249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63249-form-container" class="comment-form-container">
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

<span id="63251"></span>

<div id="answer-container-63251" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63251-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="HalfTough has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd use "<code>foot=yes</code>" if there is a public right of way to walk there, or "<code>foot=permissive</code>" if there isn't a public right of way, but the people who own the service road let people walk down it.</p>
<p>If they only let people walk down it if they're accessing something down the service road, then "<code>foot=destination</code>" may be appropriate.</p>
<p>However, if the same rules apply to all modes of transport I probably wouldn't tag "foot" at all but instead use "<code>access=destination</code>" (or whatever).</p>
<p>This <a href="https://wiki.openstreetmap.org/wiki/Key:access">wiki page</a> has lots more details.</p>
<p>(this is leaving the "separate sidewalk" issue to one side, which is of course a whole other issue, and there's lots of discussion on that elsewhere).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '18, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63251" class="comments-container">
&#10;</div>
<div id="comment-tools-63251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63251-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63253"></span>

<div id="answer-container-63253" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63253-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>highway=service implies foot=yes and when you have a sidewalk=right/left/both tag that in it itself implies foot=yes too. So, do you really need to add extra tags?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '18, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-63253" class="comments-container">
<span id="63255"></span>
<div id="comment-63255" class="comment">
<div id="post-63255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wouldn't make that assumption everywhere - actually not in most places I've ever been. The exception might be where there's Allemansrätten-style access (Scandinavia, Scotland).</p>
<p>There's further discussion at <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions</a> , but to say that "highway=service implies foot=yes" is far too simplistic. In the case of the UK the example table is unclear partly because the <em>law</em> is unclear (about cycle access on designated footpaths, for example).</p>
</div>
<div id="comment-63255-info" class="comment-info">
<span class="comment-age">(01 May '18, 10:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63256"></span>
<div id="comment-63256" class="comment">
<div id="post-63256-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh, I'm in Scandinavia :-)</p>
</div>
<div id="comment-63256-info" class="comment-info">
<span class="comment-age">(01 May '18, 10:50)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
</div>
<div id="comment-tools-63253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63253-form-container" class="comment-form-container">
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

