+++
type = "question"
title = "How to use osmapi.WayGet ?"
description = '''I would like to get the way information for https://www.openstreetmap.org/way/300589944 and another way with the python osmapi library. This is my source code so far (3600148838 is the area id for &quot;United States&quot;): import overpy import osmapi api = osmapi.OsmApi(api=&quot;https://api.openstreetmap.org/ap...'''
date = "2019-02-12T03:31:00Z"
lastmod = "2019-02-13T17:41:00Z"
weight = 67972
keywords = [ "python", "overpy", "osmapi_python", "api" ]
aliases = [ "/questions/67972" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use osmapi.WayGet ?](/questions/67972/how-to-use-osmapiwayget)

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
<span id="post-67972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67972-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to get the way information for <a href="https://www.openstreetmap.org/way/300589944">https://www.openstreetmap.org/way/300589944</a> and another way with the python <a href="https://github.com/metaodi/osmapi">osmapi</a> library.</p>
<p>This is my source code so far (3600148838 is the area id for "United States"):</p>
<pre><code>import overpy
import osmapi
api = osmapi.OsmApi(api=&quot;https://api.openstreetmap.org/api&quot;, username = &quot;me&quot;, password = &quot;*&quot;)
&#10;api = overpy.Overpass()
result = api.query(&quot;&quot;&quot;
    area(3600148838)-&gt;.searchArea;
    (
      way[&quot;addr&quot;](area.searchArea);
    );
    out body;
    &quot;&quot;&quot;)
&#10;for way in result.ways:
    print(api.WayGet(way))</code></pre>
<p>I'm getting <code>(overpy.Way id=300589944 nodes=[3046663136, 3046663138, 3046663129, 3046663123, 3046663136])</code> in Python. How can I extract just the way from the overpy.Way class?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpy" rel="tag" title="see questions tagged &#39;overpy&#39;">overpy</span> <span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '19, 03:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0dd38728dd1aa85ca045b06a4273a37f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="norcross&#39;s gravatar image" />
<p><span>norcross</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="norcross has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67972" class="comments-container">
<span id="68000"></span>
<div id="comment-68000" class="comment">
<div id="post-68000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No responses so far?</p>
</div>
<div id="comment-68000-info" class="comment-info">
<span class="comment-age">(13 Feb '19, 17:19)</span> <span class="comment-user userinfo">norcross</span>
</div>
</div>
<span id="68001"></span>
<div id="comment-68001" class="comment">
<div id="post-68001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Impatient much?</p>
</div>
<div id="comment-68001-info" class="comment-info">
<span class="comment-age">(13 Feb '19, 17:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68002"></span>
<div id="comment-68002" class="comment">
<div id="post-68002-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You might get more responses if you provide more detail about what you're trying to do. Exactly what "way information" are you looking to get and what will you be doing with the result? How does an address search of the entire US relate to your first sentence about retrieving information about a specific way? Why are you connecting to the OSM editing API and then querying the Overpass API?</p>
</div>
<div id="comment-68002-info" class="comment-info">
<span class="comment-age">(13 Feb '19, 17:41)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-67972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67972-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

