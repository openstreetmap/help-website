+++
type = "question"
title = "I get wrong OSM id after osmconvert and osmfilter"
description = '''I need to get all addresses and appropriate coordinates from NYC. I use Osmconvert and osm filter. I took a NY .pbf file from Geofabrik. After some filters, I did this to select buildings only: osmfilter.exe 1_to-node.o5m --keep=&quot;building AND addr*&quot; --drop-author --drop-version -o=2.building-addr.o5...'''
date = "2019-08-21T13:19:00Z"
lastmod = "2019-08-22T11:40:00Z"
weight = 70450
keywords = [ "osm", "osmconvert", "osmfilter", "geofabrik", "coordinates" ]
aliases = [ "/questions/70450" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I get wrong OSM id after osmconvert and osmfilter](/questions/70450/i-get-wrong-osm-id-after-osmconvert-and-osmfilter)

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
<span id="post-70450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70450-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to get all addresses and appropriate coordinates from NYC.</p>
<p>I use Osmconvert and osm filter.</p>
<p>I took a NY .pbf file from Geofabrik.</p>
<p>After some filters, I did this to select buildings only:</p>
<pre><code>osmfilter.exe 1_to-node.o5m --keep=&quot;building AND addr*&quot; --drop-author --drop-version -o=2.building-addr.o5m</code></pre>
<p>Then, I did this for an output:</p>
<pre><code>osmconvert.exe 2.building-addr.o5m -o=3.addr.csv --csv-headline --csv-separator=; --csv=&quot;@id addr:street addr:housenumber @lat @lon&quot;</code></pre>
<p><strong>But the problem is that it gives me the wrong <a href="https://help.openstreetmap.org/users/260/idoneus"></a><a href="https://help.openstreetmap.org/users/260/idoneus">@id</a></a>. It gives some of the addresses with normal id and then - with 1000000000000000 id only. What can I do?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '19, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/d107175b90214ff725c8ad69153427e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skrypch&#39;s gravatar image" />
<p><span>Skrypch</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skrypch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70450" class="comments-container">
&#10;</div>
<div id="comment-tools-70450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70450-form-container" class="comment-form-container">
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

<span id="70452"></span>

<div id="answer-container-70452" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70452-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The convert to node feature of osmconvert adds an offset (configurable) to ways, as described in the <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Dispose_of_Ways_and_Relations_and_Convert_them_to_Nodes">documentation</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '19, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-70452" class="comments-container">
<span id="70453"></span>
<div id="comment-70453" class="comment">
<div id="post-70453-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot. Could you please describe how to make IDs to be counted from 0? --object-type-offset=0?</p>
</div>
<div id="comment-70453-info" class="comment-info">
<span class="comment-age">(21 Aug '19, 15:20)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70454"></span>
<div id="comment-70454" class="comment">
<div id="post-70454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also don't understand why some coordinates are false? I aimed to get coordinates of all buidlings in NYC but I got { "<a href="https://help.openstreetmap.org/users/260/idoneus">@id</a>;addr:street;addr:housenumber;<a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a>;<a href="https://help.openstreetmap.org/users/1350/longestaugust">@lon</a>": "2322155479;10th Avenue;192;40.7467964;-74.0048356" },</p>
<p>And these coordinates show just the road.</p>
<p>It's also rather strange that NYC has more than 1 mil of buidlings but I got the list of 700k+</p>
</div>
<div id="comment-70454-info" class="comment-info">
<span class="comment-age">(21 Aug '19, 15:24)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70457"></span>
<div id="comment-70457" class="comment">
<div id="post-70457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That node is mapped as being out in the road, so the coordinates you have are correct (in as far as they match what's in the database). <a href="https://www.openstreetmap.org/node/2322155479">2322155479</a></p>
<p>As for not getting all of the buildings, you're only filtering for buildings that have an address tagged on them. There are probably lots of buildings that don't have an address tagged at all or have the contained addresses tagged separately on nodes within the building area. You can see examples of this on West 26th between 9th and 10th, where the addresses are on separate nodes (<a href="https://www.openstreetmap.org/node/2703182012">example node</a>).</p>
</div>
<div id="comment-70457-info" class="comment-info">
<span class="comment-age">(21 Aug '19, 16:57)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="70458"></span>
<div id="comment-70458" class="comment">
<div id="post-70458-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see. Thanks, I was thinking about almost the same. So it means OSM has still a lot of mistakes to deal with. However, could you please explain your example more clearly? I couldn't get it. I understand that some buildings don't have an address tagged (and that's a pity) but I can't get the meaning of "have the contained addresses tagged separately on nodes within the building area".</p>
<p>May be it is worth saying that my idea is that I will have data scraped every several hours from Rental websites and I will get ~40k of address of NYC buildings (actually, I will take coordinates only). As far as I use OSM polygons for NYC buildings, I need to check if these coordinates are within any of these polygons. So I decided that using a function in Python or other language may do the work more difficuly and I realised I needed a database of all NYC polygons and of coordinates of all NYC polygons. After I check what coordinate is inside which polygon and save this data into a database (mysql) it would be easier to check new coordinates after scraping because I will just need to check if this coordinate is in my base and what is the corresponding polygon.</p>
</div>
<div id="comment-70458-info" class="comment-info">
<span class="comment-age">(21 Aug '19, 17:21)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70459"></span>
<div id="comment-70459" class="comment not_top_scorer">
<div id="post-70459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hope It's clear. So the more coordinates of NYC buildings I have - the better. That's why I also need to deal with an IDs problem.</p>
</div>
<div id="comment-70459-info" class="comment-info">
<span class="comment-age">(21 Aug '19, 17:21)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
<span id="70460"></span>
<div id="comment-70460" class="comment">
<div id="post-70460-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Explaining the example, consider the case where one building may have multiple addresses, such as when there are multiple businesses in it. In such a case, the address tags would typically be on separate nodes for each of the businesses, not on the building object itself. If you look at the example node I linked to, you can see that it only has address information and no building tag. Therefore, your filter wouldn't find it. The same can be seen with the "Avenues" building across 10th, which isn't tagged with an address but has three nodes with addresses located within it.</p>
<p>As for your goal, I don't completely understand what it is you're trying to do. If you want to get data for all of the buildings, you could just filter for that tag and ignore addresses. If you also need address information for all of the buildings, it becomes much more complicated due to the cases I described, as well as alternate addressing schemes, mis-tagging, etc.</p>
</div>
<div id="comment-70460-info" class="comment-info">
<span class="comment-age">(21 Aug '19, 18:15)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="70471"></span>
<div id="comment-70471" class="comment not_top_scorer">
<div id="post-70471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the great explanation! I guess I will need to get these "multiple addresses" too because I may be in a situation when I want to check if a specific address is within a specific building (polygon) but my database doesn't contain the polygons with addresses needed.</p>
</div>
<div id="comment-70471-info" class="comment-info">
<span class="comment-age">(22 Aug '19, 11:40)</span> <span class="comment-user userinfo">Skrypch</span>
</div>
</div>
</div>
<div id="comment-tools-70452" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-70452-form-container" class="comment-form-container">
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

