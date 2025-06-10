+++
type = "question"
title = "query with region"
description = '''I have the following code: with only city name it works good. (&quot;Кировск&quot;) But when I try to do it with region, i get zero import overpy city_name = &quot;Кировск, Мурманская область&quot;  api = overpy.Overpass() query = f&quot;&quot;&quot;  area[&quot;name&quot;=&quot;{city_name}&quot;];  node(area)[&quot;tourism&quot;];  out; &quot;&quot;&quot;  result = api.query(q...'''
date = "2023-12-28T18:38:00Z"
lastmod = "2023-12-28T18:38:00Z"
weight = 88094
keywords = [ "city", "region" ]
aliases = [ "/questions/88094" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [query with region](/questions/88094/query-with-region)

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
<span id="post-88094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88094-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the following code: with only city name it works good. ("Кировск") But when I try to do it with region, i get zero</p>
<pre><code>import overpy
city_name = &quot;Кировск, Мурманская область&quot;
&#10;api = overpy.Overpass()
query = f&quot;&quot;&quot;
    area[&quot;name&quot;=&quot;{city_name}&quot;];
    node(area)[&quot;tourism&quot;];
    out;
&quot;&quot;&quot;
&#10;result = api.query(query)
poi_count = len(result.nodes)
&#10;print(f&quot;{city_name}: {poi_count}&quot;)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '23, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/8690c64395d865a6915aed5d898d6f59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dthedog&#39;s gravatar image" />
<p><span>dthedog</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dthedog has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88094" class="comments-container">
&#10;</div>
<div id="comment-tools-88094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88094-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

