+++
type = "question"
title = "Given a set of GPS coordinates, how do I find the closest freeway name?"
description = '''I have been given 100&#x27;s of GPS coordinates for points along the freeway. These points are actually freeway exit GPS coordinates. I need to run a query that just provides the name of the freeway or highway closest to the coordinates. I will than parse this data into Excel where I can display the name...'''
date = "2013-08-05T23:13:00Z"
lastmod = "2013-08-05T23:13:00Z"
weight = 24945
keywords = [ "reversegeocoding", "excel", "highway" ]
aliases = [ "/questions/24945" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Given a set of GPS coordinates, how do I find the closest freeway name?](/questions/24945/given-a-set-of-gps-coordinates-how-do-i-find-the-closest-freeway-name)

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
<span id="post-24945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24945-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been given 100's of GPS coordinates for points along the freeway. These points are actually freeway exit GPS coordinates. I need to run a query that just provides the name of the freeway or highway closest to the coordinates. I will than parse this data into Excel where I can display the name. I have the Excel portion resolved, I just need to reduce the query to just the closest freeway. I am new to this type of query so I really need some help.<br />
</p>
<p>If nothing else just provide a query so I can get the closest freeway!</p>
<p>Sample Data</p>
<pre><code>PRIMM                       1       35.612419   -115.389038 
SR161-JEAN-GOODSPRINGS      1       35.780735   -115.328254 
SLOAN                       0       35.930599   -115.193115 
HENDERSON-LAKE MEAD         0       35.961925   -115.18177
SEACHLIGHT-NEEDLES          1       35.967418   -114.894599</code></pre>
<p>Sample Query: <a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=35.612419%20&amp;lon=-115.389038&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=35.612419%20&amp;lon=-115.389038&amp;zoom=18&amp;addressdetails=1</a></p>
<pre><code>XML Output:
&#10;&lt;reversegeocode timestamp=&quot;Mon, 05 Aug 13 22:08:40 +0000&quot; attribution=&quot;Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright&quot; querystring=&quot;format=xml&amp;lat=35.612419%20&amp;lon=-115.389038&amp;zoom=18&amp;addressdetails=1&quot;&gt;
    &lt;result place_id=&quot;5999235837&quot; osm_type=&quot;way&quot; osm_id=&quot;148728272&quot; ref=&quot;East Primm Boulevard&quot; lat=&quot;35.6125513&quot; lon=&quot;-115.3843467&quot;&gt;
    East Primm Boulevard, Primm, Clark, Nevada, United States of America
    &lt;/result&gt;
    &lt;addressparts&gt;
    &lt;road&gt;East Primm Boulevard&lt;/road&gt;
    &lt;village&gt;Primm&lt;/village&gt;
    &lt;county&gt;Clark&lt;/county&gt;
    &lt;state&gt;Nevada&lt;/state&gt;
    &lt;country&gt;United States of America&lt;/country&gt;
    &lt;country_code&gt;us&lt;/country_code&gt;
    &lt;/addressparts&gt;
    &lt;/reversegeocode&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-excel" rel="tag" title="see questions tagged &#39;excel&#39;">excel</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '13, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/5e5a8c89caac04019351513e5b6728ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="israellopez215&#39;s gravatar image" />
<p><span>israellopez215</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="israellopez215 has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '13, 15:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24945" class="comments-container">
&#10;</div>
<div id="comment-tools-24945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24945-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

