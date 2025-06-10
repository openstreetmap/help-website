+++
type = "question"
title = "How to fetch house details with a common regex addr:street value"
description = '''I&#x27;m trying to fetch house locations from streets that match a query search: {{value=&quot;Sancti&quot;}} &amp;lt;osm-script output=&quot;json&quot;&amp;gt;  &amp;lt;query type=&quot;relation&quot;&amp;gt;  &amp;lt;around lat=&quot;40.96515&quot; lon=&quot;-5.664&quot; radius=&quot;1000&quot;/&amp;gt;  &amp;lt;has-kv k=&quot;addr:street&quot; regv={{value}}/&amp;gt;  &amp;lt;/query&amp;gt;  &amp;lt;union&amp;gt;  &amp;l...'''
date = "2013-06-02T17:30:00Z"
lastmod = "2013-06-04T13:55:00Z"
weight = 22956
keywords = [ "overpass" ]
aliases = [ "/questions/22956" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to fetch house details with a common regex addr:street value](/questions/22956/how-to-fetch-house-details-with-a-common-regex-addrstreet-value)

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
<span id="post-22956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22956-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to fetch house locations from streets that match a query search:</p>
<pre><code>{{value=&quot;Sancti&quot;}}
&lt;osm-script output=&quot;json&quot;&gt;
  &lt;query type=&quot;relation&quot;&gt;
    &lt;around lat=&quot;40.96515&quot; lon=&quot;-5.664&quot; radius=&quot;1000&quot;/&gt;
    &lt;has-kv k=&quot;addr:street&quot; regv={{value}}/&gt;
  &lt;/query&gt;
  &lt;union&gt;
    &lt;item/&gt;
    &lt;recurse type=&quot;down&quot;/&gt;
  &lt;/union&gt;
  &lt;print/&gt;
&lt;/osm-script&gt;</code></pre>
<p>At this point, I would love to be able to get the same amount of information that can be retrived by nominatim when query for a 'ways' that match addr:street 'relation' value like <a href="http://nominatim.openstreetmap.org/details.php?place_id=50241282">this</a></p>
<p>So, question is, How can I extend query to retrieve info about buildings on the same street ?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '13, 17:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f06f5e1e5c88a1b4a36263e193b5fae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inean&#39;s gravatar image" />
<p><span>inean</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inean has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '13, 23:01</strong> </span></p>
</div>
</div>
<div id="comments-container-22956" class="comments-container">
<span id="22958"></span>
<div id="comment-22958" class="comment">
<div id="post-22958-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please explain what you mean by "fetch relations of which matched ways are parent of". I suspect that you may have a misconception here about how buildings are mapped; they do not usually have a direct relationship to a nearby street, but instead they just carry the street name in their <code>addr:street</code> tag. There is an "associatedStreet" relation but it is not widely used.</p>
</div>
<div id="comment-22958-info" class="comment-info">
<span class="comment-age">(02 Jun '13, 18:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="22960"></span>
<div id="comment-22960" class="comment">
<div id="post-22960-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I've rewritten question a bit, hope this helps. Said that, Nominatim says that there's some kind of parent-child relation between 'relations' with 'tags' 'type' = 'place:house' and 'ways'. What I want is to get that info with overpass.</p>
<p>I'm trying to implement some kind of adapatative search with overpass to retrieve streets that matchs an user query. At some point, it would be interesting that, with house number info, get coordinates of that building. The main reason to not use Nominating is that I need all available candidates around user coordinates and within a radius.</p>
</div>
<div id="comment-22960-info" class="comment-info">
<span class="comment-age">(02 Jun '13, 19:56)</span> <span class="comment-user userinfo">inean</span>
</div>
</div>
<span id="23002"></span>
<div id="comment-23002" class="comment">
<div id="post-23002-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nominatim does the "parent-child relation" via the name of the street, it's a <a href="http://overpass-turbo.eu/s/ib">simple overpass query</a> you almost did already.</p>
<p>And getting a coordinate for a building is getting the geometry and calculation some middle point.</p>
<p>I agree with Frederik, I can't guess what you really want to do.</p>
</div>
<div id="comment-23002-info" class="comment-info">
<span class="comment-age">(04 Jun '13, 13:55)</span> <span class="comment-user userinfo">_al</span>
</div>
</div>
</div>
<div id="comment-tools-22956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22956-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

