+++
type = "question"
title = "How to determine if a node is inside a relation (multipolygon)?"
description = '''For example: Is this place place_id=&quot;68487739&quot; osm_type=&quot;way&quot; osm_id=&quot;21854741&quot; place_rank=&quot;26&quot; boundingbox=&quot;51.7358468,51.7373514,8.7433035,8.7458768&quot; lat=&quot;51.7361866&quot; lon=&quot;8.7446936&quot; display_name=&quot;Meisenweg, Paderborn, Kreis Paderborn, Regierungsbezirk Detmold, Nordrhein-Westfalen, 33102, Deutschl...'''
date = "2017-01-03T17:48:00Z"
lastmod = "2017-01-04T14:13:00Z"
weight = 53836
keywords = [ "node", "relation", "multipolygon" ]
aliases = [ "/questions/53836" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to determine if a node is inside a relation (multipolygon)?](/questions/53836/how-to-determine-if-a-node-is-inside-a-relation-multipolygon)

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
<span id="post-53836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53836-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example:</p>
<p>Is this place</p>
<p>place_id="68487739" osm_type="way" osm_id="21854741" place_rank="26" boundingbox="51.7358468,51.7373514,8.7433035,8.7458768" lat="51.7361866" lon="8.7446936" display_name="Meisenweg, Paderborn, Kreis Paderborn, Regierungsbezirk Detmold, Nordrhein-Westfalen, 33102, Deutschland" class="highway" type="residential" importance="0.32"</p>
<p>inside this relation</p>
<p><a href="https://www.openstreetmap.org/api/0.6/relation/73347">https://www.openstreetmap.org/api/0.6/relation/73347</a> ?</p>
<hr />
<p>Edit:</p>
<p>Precise description of the problem:</p>
<p>How can I determine if a GPS-coordinate (latitude &amp; longtitude) from any node is inside any self-contained relation/area/multipolygon? The area can be an existing boundary like "Regierungsbezirk Detmold" but it can also be a random multipolygon.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '17, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/46f260528fe878a1a9925bfd2149158b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AkeStrop&#39;s gravatar image" />
<p><span>AkeStrop</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AkeStrop has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '17, 14:18</strong> </span></p>
</div>
</div>
<div id="comments-container-53836" class="comments-container">
<span id="53848"></span>
<div id="comment-53848" class="comment">
<div id="post-53848-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>are you looking for a solution for this case only or something automated?</p>
</div>
<div id="comment-53848-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 22:38)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="53856"></span>
<div id="comment-53856" class="comment">
<div id="post-53856-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, nothing automated. Just a solution for this case would be enough ;)</p>
</div>
<div id="comment-53856-info" class="comment-info">
<span class="comment-age">(04 Jan '17, 08:30)</span> <span class="comment-user userinfo">AkeStrop</span>
</div>
</div>
</div>
<div id="comment-tools-53836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53836-form-container" class="comment-form-container">
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

<span id="53857"></span>

<div id="answer-container-53857" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53857-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>[Answer edited, as the question has changed significantly]</p>
<p>If you need to solve the general is a point "in" an OSM "area" for a larger number of points and areas I suspect the simplest way to do this is to import an OSM extract for the area in question in to a Postgis DB with osm2pgsql and then do spatial queries on the data.</p>
<p>Or ... there are many alternatives, but they all (even if you simply roll your own code after reading a corresponding text) will likely require you to first actually create the geometry of the OSM "area" object in question, which in general is not something for the faint hearted so you should simply use something that is known to work.</p>
<p>More details on your application and what you are really trying to do would help with a more specific answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '17, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '17, 21:27</strong> </span></p>
</div>
</div>
<div id="comments-container-53857" class="comments-container">
<span id="53861"></span>
<div id="comment-53861" class="comment">
<div id="post-53861-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's absolutely right and a really simple solution, but that's unfortunately not the solution for my problem. Let me be more precise and rephrase my problem:</p>
<p>How can I determine if a GPS-coordinate (latitude &amp; longtitude) from any node is inside any self-contained relation/area/multipolygon? The area can be an existing boundary like "Regierungsbezirk Detmold" but it can also be a random multipolygon. So your suggested solution don't solve the problem if it's a random multipolygon.</p>
<p>I hope this describes the problem better.</p>
</div>
<div id="comment-53861-info" class="comment-info">
<span class="comment-age">(04 Jan '17, 14:13)</span> <span class="comment-user userinfo">AkeStrop</span>
</div>
</div>
</div>
<div id="comment-tools-53857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53857-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

