+++
type = "question"
title = "how to tag non-public governmental campus areas"
description = '''I live in a capital city where there are lots of non-public governmental areas such as the presidency palace and ministries. These places not only contains only a single governmental building but also span huge territories similar to military areas. The areas are usually surrounded by some kind fenc...'''
date = "2012-11-28T08:53:00Z"
lastmod = "2012-11-28T20:43:00Z"
weight = 18048
keywords = [ "landuse", "government" ]
aliases = [ "/questions/18048" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to tag non-public governmental campus areas](/questions/18048/how-to-tag-non-public-governmental-campus-areas)

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
<span id="post-18048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18048-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live in a capital city where there are lots of non-public governmental areas such as the presidency palace and ministries. These places not only contains only a single governmental building but also span huge territories similar to military areas. The areas are usually surrounded by some kind fence or wall so that no one (other than the civil servants) can enter. From outside they look like small leisure forest parks with a couple of governmental building scattered around the territory. (Therefore, it is best that these areas are rendered with green on the maps.)</p>
<p>Which kind of tag should I use for such places? I saw people complaining about similar issues in the "talk" page of "landuse" tag. Has any consensus been reached on this issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-government" rel="tag" title="see questions tagged &#39;government&#39;">government</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '12, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/b357be198f4d267d029942e5135da35b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yigiter&#39;s gravatar image" />
<p><span>yigiter</span><br />
<span class="score" title="96 reputation points">96</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yigiter has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '12, 15:01</strong> </span></p>
</div>
</div>
<div id="comments-container-18048" class="comments-container">
&#10;</div>
<div id="comment-tools-18048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18048-form-container" class="comment-form-container">
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

<span id="18054"></span>

<div id="answer-container-18054" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18054-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yigiter has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you are just asking about the "area" access restriction here. Because OSM has a well established convention to specify access restrictions on roads (see the <a href="https://wiki.openstreetmap.org/wiki/Access">key access on the wiki</a>) and you should use them for all highways inside the restricted access areas (if any).</p>
<p>I see two options in your case. You can combine them.</p>
<ul>
<li>create a specific "<a href="https://wiki.openstreetmap.org/wiki/Key:landuse">landuse</a>" polygon (e.g. "landuse=government" ? not documented currently on the wiki) and add an "access=private" or "access=no" or "access=destination" depending on the degree of accessibility. But I'm not sure that any current software will try to interpret access tags on a landuse polygon. This landuse should not overlap with other landuse polygones othewise it could create some ambiguity.</li>
<li>draw the surrounding fences/walls and tag them with the key "<a href="https://wiki.openstreetmap.org/wiki/Barrier">barrier</a>". This should prevent any routing software to cross the area by foot.</li>
</ul>
<p>The advantage of the landuse polygon is that you can name it (e.g. "landuse=government" + "access=private" + "name=Ministry of Interior").</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '12, 11:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-18054" class="comments-container">
<span id="18083"></span>
<div id="comment-18083" class="comment">
<div id="post-18083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i would prefer "landuse=government" + "access=private" + "name=Ministry of Interior" + "barrier=fence" , if the whole area is surrounded by a fence.</p>
</div>
<div id="comment-18083-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 20:43)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-18054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18054-form-container" class="comment-form-container">
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

