+++
type = "question"
title = "[closed] How can I Get The Streets of a specific postcode using OpenStreetMap"
description = '''want to write a code that has the Countrycode and Postcode as an input and the ouput are the streets that are in the given postcode using some apis that use OSM. My tactic is as follows: I need to get the relation Id of the district. For Example 1991416 is the relation id for the third district in V...'''
date = "2014-12-12T17:15:00Z"
lastmod = "2014-12-12T17:48:00Z"
weight = 39242
keywords = [ "overpass", "nominatim", "streetnames", "postcode" ]
aliases = [ "/questions/39242" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How can I Get The Streets of a specific postcode using OpenStreetMap](/questions/39242/how-can-i-get-the-streets-of-a-specific-postcode-using-openstreetmap)

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
<span id="post-39242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39242-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-39242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>want to write a code that has the Countrycode and Postcode as an input and the ouput are the streets that are in the given postcode using some apis that use OSM.</p>
<p>My tactic is as follows:</p>
<p>I need to get the relation Id of the district. For Example 1991416 is the relation id for the third district in Vienna - Austria. It's provided by the nominatim api: <a href="http://nominatim.openstreetmap.org/details.php?place_id=158947085">http://nominatim.openstreetmap.org/details.php?place_id=158947085</a></p>
<p>Put the id in this api url: <a href="http://polygons.openstreetmap.fr/get_wkt.py?id=1991416&amp;params=0">http://polygons.openstreetmap.fr/get_wkt.py?id=1991416&amp;params=0</a></p>
<p>After downloading the polygon I can put the gathered polygon in this query on the overpass api</p>
<p>( way (poly: "polygone data") ["highway"~"^(primary|secondary|tertiary|residential)$"] ["name"];</p>
<p>); out geom;</p>
<p>And this gives me the streets of the searched district. My two problems with this solution are 1. that it takes quite a time, because asking three different APIs per request isn't that easy on ressources and 2. I don't know how to gather the relation Id from step one automatically. When I enter a Nominatim query like <a href="http://nominatim.openstreetmap.org/search?format=json&amp;country=austria&amp;postalcode=1030">http://nominatim.openstreetmap.org/search?format=json&amp;country=austria&amp;postalcode=1030</a> I just get various point in the district, but not the relation id of the searched district in order to get the desired polygone.</p>
<p>So my questions are if someone can tell my how I can get the relation_Id in order to do the mentioned workflow or if there is another, maybe better way to work this issue out.</p>
<p>Thank you for your help!</p>
<p>Best Regards Daniel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '14, 17:15</strong></p>
<img src="https://secure.gravatar.com/avatar/6a3596716f605a1ca0d24f5e7c7091cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shachty&#39;s gravatar image" />
<p><span>Shachty</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shachty has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '14, 11:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-39242" class="comments-container">
<span id="39244"></span>
<div id="comment-39244" class="comment">
<div id="post-39244-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Closing because of cross post.</p>
<p>I just answered this on stackoverflow:</p>
<p><a href="http://stackoverflow.com/questions/27429376/getting-streets-of-a-specific-postcode-using-open-street-maps/27449051">http://stackoverflow.com/questions/27429376/getting-streets-of-a-specific-postcode-using-open-street-maps/27449051</a></p>
</div>
<div id="comment-39244-info" class="comment-info">
<span class="comment-age">(12 Dec '14, 17:48)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-39242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39242-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by mmd 12 Dec '14, 17:48

</div>

</div>

</div>

