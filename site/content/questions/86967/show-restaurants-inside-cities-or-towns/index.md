+++
type = "question"
title = "show restaurants inside cities or towns"
description = '''Hey guys, I am trying to find all restaurants inside a city or town like this on overpass turbo: [out:json][timeout:25]; area[&quot;ISO3166-1&quot;=&quot;AM&quot;]; area(area)[&#x27;name:en&#x27;~&quot;^Ararat&quot;][&quot;place&quot;=&quot;town&quot;]-&amp;gt;.a; node(area.a)[&quot;amenity&quot;=&quot;restaurant&quot;]; out qt;  but its result is empty, if I am using the relation ...'''
date = "2023-03-22T08:59:00Z"
lastmod = "2023-04-01T17:37:00Z"
weight = 86967
keywords = [ "overpass-turbo", "osm" ]
aliases = [ "/questions/86967" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [show restaurants inside cities or towns](/questions/86967/show-restaurants-inside-cities-or-towns)

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
<span id="post-86967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys, I am trying to find all restaurants inside a city or town like this on overpass turbo:</p>
<pre><code>[out:json][timeout:25];
area[&quot;ISO3166-1&quot;=&quot;AM&quot;];
area(area)[&#39;name:en&#39;~&quot;^Ararat&quot;][&quot;place&quot;=&quot;town&quot;]-&gt;.a;
node(area.a)[&quot;amenity&quot;=&quot;restaurant&quot;];
out qt;</code></pre>
<p>but its result is empty, if I am using the relation :</p>
<pre><code>[out:json][timeout:25];
area[&quot;ISO3166-1&quot;=&quot;AM&quot;]-&gt;.b;
rel(area.b)[&#39;name:en&#39;~&quot;^Ararat&quot;];
out geom;
{{style: 
  area
  { color:gray; fill-color:DarkGray; }
}}
map_to_area;
node(area)[&quot;amenity&quot;=&quot;restaurant&quot;];
out qt;</code></pre>
<p>there is 1 restaurant inside Ararat town <img src="/upfiles/Screenshot_2023-03-22_at_12.55.02.png" alt="alt text" /></p>
<p>What is the difference between the 2 queries? and how can I show restaurants inside cities or towns? not inside province or state!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '23, 08:59</strong></p>
<img src="https://secure.gravatar.com/avatar/3016a8114f68eb431594ee9ec890c246?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alt2020&#39;s gravatar image" />
<p><span>alt2020</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alt2020 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-86967" class="comments-container">
<span id="86970"></span>
<div id="comment-86970" class="comment">
<div id="post-86970-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which specific area/province do you wish to search? Your search criteria is ambiguous ('name:en'~"^Ararat") The restaurant you highlight isn't in a town try [place~"town|village|city"]</p>
</div>
<div id="comment-86970-info" class="comment-info">
<span class="comment-age">(22 Mar '23, 15:19)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="86972"></span>
<div id="comment-86972" class="comment">
<div id="post-86972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>do I need to search first a province first? and after that, I have to search the town and then In town, I have to search restaurant.Ararat is a town in Ararat province, <a href="https://help.openstreetmap.org/users/1532/davef"></a><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a></p>
</div>
<div id="comment-86972-info" class="comment-info">
<span class="comment-age">(22 Mar '23, 18:51)</span> <span class="comment-user userinfo">alt2020</span>
</div>
</div>
<span id="86973"></span>
<div id="comment-86973" class="comment">
<div id="post-86973-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I chenged query ti this <code>[out:json][timeout:25]; area["ISO3166-1"="AM"]; area(area)[place~"town|village|city"]-&gt;.a; area(area.a)['name:en'~"^Ararat"]-&gt;.b; node(area.b)["amenity"="restaurant"]; out qt;</code> but my query result is all restaurants inside Ararat province, I just want all restaurant inside Ararat town. <a href="https://overpass-turbo.eu/s/1sLq">https://overpass-turbo.eu/s/1sLq</a> <a href="https://help.openstreetmap.org/users/1532/davef"></a><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a></p>
</div>
<div id="comment-86973-info" class="comment-info">
<span class="comment-age">(22 Mar '23, 18:56)</span> <span class="comment-user userinfo">alt2020</span>
</div>
</div>
<span id="86978"></span>
<div id="comment-86978" class="comment">
<div id="post-86978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it depends how the town is defined. If there's a town boundary, then things will be much easier compared to a node. Unless all the restaurants' address have place:city(or town) = ararat specified.</p>
</div>
<div id="comment-86978-info" class="comment-info">
<span class="comment-age">(24 Mar '23, 03:49)</span> <span class="comment-user userinfo">kucai</span>
</div>
</div>
<span id="87041"></span>
<div id="comment-87041" class="comment">
<div id="post-87041-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You will need to include ways and relations as object types too.</p>
</div>
<div id="comment-87041-info" class="comment-info">
<span class="comment-age">(01 Apr '23, 17:37)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86967-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

