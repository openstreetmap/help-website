+++
type = "question"
title = "Best tags for a pedestrian and cycle only &quot;modal filter&quot;"
description = '''In my area, there is a £30 million cycle infrastructure scheme being implemented. In particular, many roads are being closed to vehicular traffic, but remaining open to cyclists and pedestrians.  What is the best way to tag those &quot;modal filters&quot; on the map. I want that routers correctly know that ca...'''
date = "2015-03-21T10:19:00Z"
lastmod = "2015-03-21T11:57:00Z"
weight = 41837
keywords = [ "newbie", "tagging" ]
aliases = [ "/questions/41837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best tags for a pedestrian and cycle only "modal filter"](/questions/41837/best-tags-for-a-pedestrian-and-cycle-only-modal-filter)

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
<span id="post-41837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41837-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my area, there is a £30 million cycle infrastructure scheme being implemented. In particular, many roads are being closed to vehicular traffic, but remaining open to cyclists and pedestrians.</p>
<p>What is the best way to tag those "modal filters" on the map. I want that routers correctly know that cars are not allowed and also that these clearly look like "places you can't drive" on the visual map.</p>
<p>My initial attempts (to change the road type to pedestrian) don't seem to have changed the visuals (although perhaps OSM is just slow to update the tiles.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '15, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/cbd532fbc70628303c6dcb93b338e323?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WalthamCity&#39;s gravatar image" />
<p><span>WalthamCity</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WalthamCity has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Mar '15, 10:21</strong> </span></p>
</div>
</div>
<div id="comments-container-41837" class="comments-container">
&#10;</div>
<div id="comment-tools-41837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41837-form-container" class="comment-form-container">
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

<span id="41838"></span>

<div id="answer-container-41838" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41838-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-41838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please do not even attempt to fiddle with the tagging to acheive any specific visual effect on the standard rendering.</p>
<p>That said, the standard rendering currently only supports a very restricted rendering of access tags, and that is, on top of it, not useful, bordering on wrong. So again please do not try to acheive visual representation of bicycle/pedestrian only access by tag fiddling.</p>
<p>Now back to the underlying question: it really depends what makes most sense, roads that have really changed status from say residential, unclassified or similar to a cycleway with pedestrian access could clearly be tagged as highway=cycleway If access has simply been restricted, for example by allowing only access to residents then that should be tagged.</p>
<p>Further from your question it seems as if you are based in the UK, as a general rule you should not be making widespread tagging changes without at least rough consensus in the respective communities. I would strongly suggest you bringing the matter to the table on the <a href="https://lists.openstreetmap.org/listinfo/talk-gb">GB mailing list</a>.</p>
<p>For more information see: <a href="http://wiki.openstreetmap.org/wiki/Key:access">access tag on the wiki</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '15, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Mar '15, 11:59</strong> </span></p>
</div>
</div>
<div id="comments-container-41838" class="comments-container">
<span id="41839"></span>
<div id="comment-41839" class="comment">
<div id="post-41839-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>So to summarise your answer: "Don't worry about how the visual map looks - just keep the data correct". That makes sense. I think I've done everything right then. Is there any way to test the routing?</p>
</div>
<div id="comment-41839-info" class="comment-info">
<span class="comment-age">(21 Mar '15, 11:55)</span> <span class="comment-user userinfo">WalthamCity</span>
</div>
</div>
<span id="41840"></span>
<div id="comment-41840" class="comment">
<div id="post-41840-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Sure, the routing databases update with some delay, but you can use the routing feature on openstreetmap.org (arrow to the right of the search box) for testing, or use the routing services directly.</p>
<p>Note the routing services will tend to differ on which tags they consider for routing decisions, so you shouldn't forget that there is a certain danger of "tagging for the router" and not just "tagging for the renderer" too.</p>
</div>
<div id="comment-41840-info" class="comment-info">
<span class="comment-age">(21 Mar '15, 11:57)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41838-form-container" class="comment-form-container">
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

