+++
type = "question"
title = "How to create a maxspeed zone?"
description = '''I&#x27;ve read here -- http://wiki.openstreetmap.org/wiki/Key:zone:maxspeed -- that the max speed zones should be marked with a special tag rather than with the generic maxspeed. It makes perfect sense. However I wonder: isn&#x27;t there a way to actually create such zone as an area (polygon)? Or is there a r...'''
date = "2014-08-14T10:52:00Z"
lastmod = "2014-09-05T05:39:00Z"
weight = 35817
keywords = [ "maxspeed", "zone", "tagging" ]
aliases = [ "/questions/35817" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to create a maxspeed zone?](/questions/35817/how-to-create-a-maxspeed-zone)

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
<span id="post-35817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35817-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've read here -- <a href="http://wiki.openstreetmap.org/wiki/Key:zone:maxspeed">http://wiki.openstreetmap.org/wiki/Key:zone:maxspeed</a> -- that the max speed zones should be marked with a special tag rather than with the generic <code>maxspeed</code>. It makes perfect sense. However I wonder: isn't there a way to actually create such zone as an area (polygon)? Or is there a reason not to do it that way?</p>
<p>And also: should I then apply two tags to each street, <code>maxspeed=*</code> and <code>zone:maxspeed=*</code>? As explained in the wiki, “in Germany maxspeed-zones apply to all vehicles while maxspeed-signs only apply to motorized-vehicles”. I think it is true at least also for the Netherlands. So the zone is “stronger” than the speed limit. Why set both tags then?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-zone" rel="tag" title="see questions tagged &#39;zone&#39;">zone</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '14, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/7f75b476d4984deb5e4c83d276b9c22b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kotya&#39;s gravatar image" />
<p><span>Kotya</span><br />
<span class="score" title="631 reputation points">631</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kotya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '14, 13:12</strong> </span></p>
</div>
</div>
<div id="comments-container-35817" class="comments-container">
<span id="35845"></span>
<div id="comment-35845" class="comment">
<div id="post-35845-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Kotya, a bicycle without any power source other than human can exceed the speeds inside a zone in the Netherlands. All other vehicles have to obey to they’re specific rules. So your argument pro or contra a zone is not correct. The zones in the Netherlands were made to avoid many traffic signs, because they did not place a sign after every crossroad, but every now and then a zone sign. With one exception the living street were pedestrians have special privileges, any vehicle has to prove that an accident was not his/here doing.</p>
</div>
<div id="comment-35845-info" class="comment-info">
<span class="comment-age">(14 Aug '14, 21:54)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-35817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35817-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="35831"></span>

<div id="answer-container-35831" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35831-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kotya has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO you set it on the ways, because that is easier for the consumers to find. Otherwise they have to find the area to which the street belongs. Also zones can be rather small. I know a 30-zone in Belgium with only 1 street in it. It would be an overkill to create a zone for that.</p>
<p>I also thought the current way of tagging is more towards maxspeed=70, source:maxspeed=BE:zone70 (or BE:zone or BE:zone:70), see <a href="http://wiki.openstreetmap.org/wiki/Key:source:maxspeed">http://wiki.openstreetmap.org/wiki/Key:source:maxspeed</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '14, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-35831" class="comments-container">
<span id="36625"></span>
<div id="comment-36625" class="comment">
<div id="post-36625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree. I looked at the zone proposal (since this is a <em>very</em> common situation in Oklahoma) and decided trying to get adoption for 77 different speed zones, not counting hundreds to possibly thousands more speed zones for each little town that posts it, would be impossible.</p>
<p>You're better off (CAREFULLY and judiciously!!) tagging ways that aren't yet maxspeed tagged with maxspeed and maxspeed:source, since this obviates issues in case a way that wasn't already tagged but has a speed limit other than the zone limit, can be found.</p>
</div>
<div id="comment-36625-info" class="comment-info">
<span class="comment-age">(05 Sep '14, 05:39)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-35831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35831-form-container" class="comment-form-container">
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

