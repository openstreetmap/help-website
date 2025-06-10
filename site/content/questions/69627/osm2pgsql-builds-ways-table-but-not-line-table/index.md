+++
type = "question"
title = "osm2pgsql builds ways table but not line table"
description = '''I&#x27;m trying to import xml data from an overpass query into postgres. Using the latest windows build on appveyor, &quot;osm2pgsql -c -d postgis_25_sample -U postgres -H localhost -P 5432 -S default.style &quot;myData.osm&quot; -W -s&quot; completes successfully. While it builds the osm_nodes, osm_point, and osm_ways tabl...'''
date = "2019-06-15T02:48:00Z"
lastmod = "2019-06-18T14:17:00Z"
weight = 69627
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/69627" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pgsql builds ways table but not line table](/questions/69627/osm2pgsql-builds-ways-table-but-not-line-table)

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
<span id="post-69627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69627-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to import xml data from an overpass query into postgres. Using the latest windows build on appveyor, "osm2pgsql -c -d postgis_25_sample -U postgres -H localhost -P 5432 -S default.style "myData.osm" -W -s" completes successfully. While it builds the osm_nodes, osm_point, and osm_ways tables correctly, the osm_line table is empty.</p>
<p>The data looks something like this: <a href="https://paste.ee/p/iUUdg">https://paste.ee/p/iUUdg</a> Is something wrong with the data or is it something else?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '19, 02:48</strong></p>
<img src="https://secure.gravatar.com/avatar/5e4011adcdb356367cb9fc693994422e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shinyburger&#39;s gravatar image" />
<p><span>shinyburger</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shinyburger has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jun '19, 02:59</strong> </span></p>
</div>
</div>
<div id="comments-container-69627" class="comments-container">
<span id="69628"></span>
<div id="comment-69628" class="comment">
<div id="post-69628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does your data actually contain anything that would be imported in to osm_line? For example non-closed ways that are not part of a MP?</p>
</div>
<div id="comment-69628-info" class="comment-info">
<span class="comment-age">(15 Jun '19, 11:26)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="69637"></span>
<div id="comment-69637" class="comment">
<div id="post-69637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. I'm sure. The polygon table is empty as well.</p>
</div>
<div id="comment-69637-info" class="comment-info">
<span class="comment-age">(17 Jun '19, 02:06)</span> <span class="comment-user userinfo">shinyburger</span>
</div>
</div>
</div>
<div id="comment-tools-69627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69627-form-container" class="comment-form-container">
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

<span id="69652"></span>

<div id="answer-container-69652" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69652-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shinyburger has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your data is not NWR (Nodes, Ways, Relations) ordered, I don't believe you will get any kind of consistent results without doing that (I'm actually surprised that it imports at all).</p>
<p>PS: I discussed this with the osm2pgsql maintainers, and to be exact: osm2pgsql doesn't require overall nwr ordering, but it does require nodes referenced by ways to be before the ways that reference them (in practical terms this naturally doesn't really make a difference).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '19, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '19, 08:48</strong> </span></p>
</div>
</div>
<div id="comments-container-69652" class="comments-container">
&#10;</div>
<div id="comment-tools-69652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69652-form-container" class="comment-form-container">
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

