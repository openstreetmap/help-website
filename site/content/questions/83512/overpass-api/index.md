+++
type = "question"
title = "[closed] overpass api"
description = '''Yes, I am using python. I wrote use this code below and it is working fine for me. import overpy import json from copy import deepcopy import haversine as hs import math   api = overpy.Overpass() #generate an intended map boundary for a given coordinates  result = api.query (f&#x27;way(around:100,49.8974...'''
date = "2022-02-17T16:08:00Z"
lastmod = "2022-02-17T16:08:00Z"
weight = 83512
keywords = [ "overpass" ]
aliases = [ "/questions/83512" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] overpass api](/questions/83512/overpass-api)

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
<span id="post-83512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83512-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Yes, I am using python. I wrote use this code below and it is working fine for me.</p>
<pre><code>import overpy
import json
from copy import deepcopy
import haversine as hs
import math
&#10;
api = overpy.Overpass()
#generate an intended map boundary for a given coordinates
&#10;result = api.query (f&#39;way(around:100,49.8974309,-97.2033944 )[&quot;highway&quot;=&quot;footway&quot;];(._;&gt;;);out geom;&#39;)
&#10;where,
radius=100m
latitude =49.8974309
longitude=-97.2033944</code></pre>
<p>But now, i do not want to use radius again, rather i want to use four coordinates like a rectangular bounding box to query osm for highway (e.g. footway in particular, in the specified area) using python.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '22, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>17 Feb '22, 17:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-83512" class="comments-container">
&#10;</div>
<div id="comment-tools-83512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83512-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question of https://help.openstreetmap.org/questions/83509/overpass-query" by TZorn 17 Feb '22, 17:38

</div>

</div>

</div>

