+++
type = "question"
title = "US State/Interstate highways, noname &amp; the &#x27;on the ground rule&#x27;"
description = '''If a state highway has no street signs, does the &#x27;on the ground rule&#x27; dictate that it has no name? What if official government data lists the name on both the road itself and all of the addresses along it as &quot;Highway XYZ&quot;? From the wiki: Some examples of incorrect usage: &quot;Interstate 5&quot;: When a name ...'''
date = "2020-09-18T02:13:00Z"
lastmod = "2020-09-18T06:57:00Z"
weight = 76690
keywords = [ "noname", "highway" ]
aliases = [ "/questions/76690" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [US State/Interstate highways, noname & the 'on the ground rule'](/questions/76690/us-stateinterstate-highways-noname-the-on-the-ground-rule)

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
<span id="post-76690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76690-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If a state highway has no street signs, does the 'on the ground rule' dictate that it has no name? What if official government data lists the name on both the road itself and all of the addresses along it as "Highway XYZ"?</p>
<p>From the wiki: <a href="https://wiki.openstreetmap.org/wiki/Names#Name_is_the_name_only">Some examples of incorrect usage: "Interstate 5": When a name would only be duplicating the information in the ref=* tag, then the ref and noname=yes is almost always more appropriate.</a></p>
<p>This makes sense, but I don't know if this is something that was decided by the community or if someone just made this up and added it to the wiki. Whoever added this must not have noticed that the entire Interstate system and most US/state highways do not follow this rule.</p>
<p>I'd imagine that to data consumers, consistency is more important than technicalities like what constitutes a name. What if the software doesn't read the network/ref tags? The road would just be called 'unnamed road'? One could argue this is a software bug and not a data issue, but I don't see any harm in adding a name to avoid it.</p>
<p>Should the route relation and/or road segments be tagged with a name?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-noname" rel="tag" title="see questions tagged &#39;noname&#39;">noname</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '20, 02:13</strong></p>
<img src="https://secure.gravatar.com/avatar/6203fe5d1e41fd2c3f1c1354049b3efc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tguen&#39;s gravatar image" />
<p><span>tguen</span><br />
<span class="score" title="141 reputation points">141</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tguen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76690" class="comments-container">
&#10;</div>
<div id="comment-tools-76690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76690-form-container" class="comment-form-container">
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

<span id="76691"></span>

<div id="answer-container-76691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76691-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should only ask one question at a time, thanks.</p>
<p>The on the ground rule just requires something to be reasonably verifiable for an OSM contributor, on the ground at the location. That could easily be by determining the name of a road by asking locals, or deriving it from an address on the road, a street sign is simply the easiest way of determining a name.</p>
<p>It is not clear what your other questions are, but yes simply duplicating the ref to the name field is not really necessary and all reasonable applications will check both, particularly for major roads that might not have a "name".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '20, 06:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-76691" class="comments-container">
&#10;</div>
<div id="comment-tools-76691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76691-form-container" class="comment-form-container">
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

