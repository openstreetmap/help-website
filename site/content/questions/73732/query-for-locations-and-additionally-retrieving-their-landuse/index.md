+++
type = "question"
title = "query for locations and additionally retrieving their landuse"
description = '''Hello all,  I need to analyse the locations of electric vehicle charging points for university. I plan on doing that with R and so far I have been successful to get the locations for Germany, France and Italy through a csv export. I would now like to know if it&#x27;s possible to attach another column wi...'''
date = "2020-03-24T17:17:00Z"
lastmod = "2020-03-30T14:56:00Z"
weight = 73732
keywords = [ "charging_station", "landuse", "export", "csv" ]
aliases = [ "/questions/73732" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [query for locations and additionally retrieving their landuse](/questions/73732/query-for-locations-and-additionally-retrieving-their-landuse)

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
<span id="post-73732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73732-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I need to analyse the locations of electric vehicle charging points for university. I plan on doing that with R and so far I have been successful to get the locations for Germany, France and Italy through a csv export. I would now like to know if it's possible to attach another column with the "landuse" data. It would be very helpful for my analysis to be able to know whether a charging station is in a residential area, commercial area, etc.</p>
<p>Is that at all possible? Thank you for your time.</p>
<p>My query so far:</p>
<pre><code>/*
This is an example Overpass query.
Try it out by pressing the Run button above!
You can find more examples with the Load tool.
*/
[out:csv(::id,::type,&quot;name&quot;,&quot;addr:postcode&quot;,&quot;addr:city&quot;,&quot;addr:street&quot;,&quot;addr:housenumber&quot;,
&quot;authentication.nfc&quot;,&quot;authentication.none&quot;,&quot;authentication.membership_card&quot;,&quot;brand&quot;,&quot;capacity&quot;,&quot;car&quot;,&quot;fee&quot;,&quot;network&quot;,&quot;note&quot;,&quot;opening_hours&quot;,&quot;operator&quot;,&quot;socket=*&quot;,&quot;voltage&quot;,::lat,::lon,::timestamp;
    true; &quot;|&quot;)][timeout:50];
 area[&quot;ISO3166-1&quot;=&quot;DE&quot;]-&gt;.a;
( node(area.a)[amenity=charging_station];
  way(area.a)[amenity=charging_station];
  rel(area.a)[amenity=charging_station];);
out meta;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-charging_station" rel="tag" title="see questions tagged &#39;charging_station&#39;">charging_station</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '20, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d38b3239c81d2ca8e5c6d67d726b81dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerd_Lauer&#39;s gravatar image" />
<p><span>Gerd_Lauer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerd_Lauer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '20, 21:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-73732" class="comments-container">
<span id="73737"></span>
<div id="comment-73737" class="comment">
<div id="post-73737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would not expect any of the addr:* tags on a amenity=charging_station, especially not an addr:housenumber</p>
<p>You cannot simply add another field to retrieve the landuse. You will have to make additional queries for that.</p>
</div>
<div id="comment-73737-info" class="comment-info">
<span class="comment-age">(25 Mar '20, 06:49)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="73797"></span>
<div id="comment-73797" class="comment">
<div id="post-73797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>. I'm trying to set up queries per landuse type now. Adding the additional column should be very easy in R later-on once I have all the data ready.</p>
<p>If you have a minute, could you help me with the following query? I modeled it after one that I found online that also queried for multiple conditions: <a href="https://wiki.openstreetmap.org/wiki/User:Tagtheworld/CSV-Export">https://wiki.openstreetmap.org/wiki/User:Tagtheworld/CSV-Export</a></p>
<p>The thing is that I don't get any output with this query. Also not with other landuse types so there has to be sth wrong with the query. The output just shows the column headers without content. Do you have an idea for that?</p>
<p>Query: <a href="https://pastebin.com/skRgCG8G">https://pastebin.com/skRgCG8G</a></p>
</div>
<div id="comment-73797-info" class="comment-info">
<span class="comment-age">(27 Mar '20, 15:00)</span> <span class="comment-user userinfo">Gerd_Lauer</span>
</div>
</div>
<span id="73806"></span>
<div id="comment-73806" class="comment">
<div id="post-73806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi there,</p>
<p>As I was told that I cannot retrieve the landuse as another field, I'm trying to create different queries per landuse and then merge them later-on in R.</p>
<p>I have tried to model my query after different variations I found online, namely <a href="https://wiki.openstreetmap.org/wiki/User:Tagtheworld/CSV-Export">this one</a> and <a href="https://help.openstreetmap.org/questions/73145/overpass-query-for-a-name-with-different-possible-keystagsfeatures">that one</a>. The problem is that the results of the query are empty fields and I don't know what is going on. I'm very new to the OSM and Overpass Turbo syntax.</p>
<p>My resulting query attempts look like <a href="https://pastebin.com/v7rHzkBp">this</a> and <a href="https://pastebin.com/skRgCG8G">that</a> and both produce empty fields.</p>
<p>What I would like to achieve is the following: I want to retrieve the location of all charging stations in Germany, Italy and France. I also need to know what kind of area they are located in. For example I would like to know how many public charging stations are within residential areas of cities, how many are at rest stops on highways, etc.</p>
<p>Can anyone give me a hint as to how I can achieve this? Thank you all for your time.</p>
</div>
<div id="comment-73806-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 11:02)</span> <span class="comment-user userinfo">Gerd_Lauer</span>
</div>
</div>
<span id="73863"></span>
<div id="comment-73863" class="comment">
<div id="post-73863-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can nobody help me with this problem? Whatever I do I can't seem to be able to retrieve the information about the environment of the charging stations. <a href="https://pastebin.com/YCa4ACVq">This</a> is the query that I'm using now. That way it returns all charging stations, but as soon as I try to specify the landuse type from <code>["landuse" = ""]</code> to eg this <code>["landuse" = "residential"]</code> it returns empty fields. Does anyone have an idea how I could go about somehow adding that information to my csv export or just in general to my query?</p>
</div>
<div id="comment-73863-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 14:56)</span> <span class="comment-user userinfo">Gerd_Lauer</span>
</div>
</div>
</div>
<div id="comment-tools-73732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73732-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

