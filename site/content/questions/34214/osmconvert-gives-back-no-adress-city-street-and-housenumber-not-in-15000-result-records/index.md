+++
type = "question"
title = "osmconvert gives back no adress: city, street and housenumber - not in 15000 result-records"
description = '''hello dear osm-experts with an update: scroll down the key question is, how can we write the request: that takes up the adress-tags correctly: http://wiki.openstreetmap.org/wiki/Key:addr while trying to gather information about european schools - note i try it with different approaches  with the tar...'''
date = "2014-06-21T12:10:00Z"
lastmod = "2014-06-22T07:13:00Z"
weight = 34214
keywords = [ "overpass", "osmconvert", "osm", "tagging" ]
aliases = [ "/questions/34214" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmconvert gives back no adress: city, street and housenumber - not in 15000 result-records](/questions/34214/osmconvert-gives-back-no-adress-city-street-and-housenumber-not-in-15000-result-records)

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
<span id="post-34214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34214-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello dear osm-experts</p>
<p>with <strong>an update: scroll down</strong> the key question is, how can we write the request: that takes up the adress-tags correctly: <a href="http://wiki.openstreetmap.org/wiki/Key:addr">http://wiki.openstreetmap.org/wiki/Key:addr</a></p>
<p>while trying to gather information about european schools - note i try it with different approaches with the target-goal to gather</p>
<pre><code>name
adress
long
lat
and town, street, housenumber information
and then - if possible website -adress</code></pre>
<p><strong>spain:</strong> 10000 Records</p>
<pre><code>wget http://download.geofabrik.de/europe/spain-latest.osm.pbf
./osmconvert spain-latest.osm.pbf -o=spain.o5m
./osmfilter spain.o5m --keep=&quot;amenity=school&quot; -o=spain-schools.o5m
./osmconvert spain-schools.o5m --all-to-nodes -o=spain-schools_nodes.o5m
./osmfilter spain-schools_nodes.o5m --keep=&quot;amenity=school&quot; -o=spain-schools-results.o5m
./osmconvert spain-schools-results.o5m --csv=&quot;name addr:city website&quot; -o=spain-schools-results.csv</code></pre>
<p><strong>netherlands</strong> 3000 Records</p>
<pre><code>wget http://download.geofabrik.de/europe/netherlands-latest.osm.pbf
./osmconvert netherlands-latest.osm.pbf -o=dutch.o5m
./osmfilter dutch.o5m --keep=&quot;amenity=school&quot; -o=dutch-schools.o5m
./osmconvert dutch-schools.o5m --all-to-nodes -o=dutch-schools_nodes.o5m
./osmfilter dutch-schools_nodes.o5m --keep=&quot;amenity=school&quot; -o=dutch-schools-results.o5m
./osmconvert dutch-schools-results.o5m --csv=&quot;name addr:city website&quot; -o=dutch-schools-results.csv</code></pre>
<p>interesting: i can get the name of the school, and sometimes the website - but never a street ...what goes wrong here.</p>
<p>besides the missing street i also miss the long and lat information</p>
<p>can any body help out here. thanks in advance</p>
<p>by the way - any chance to store the data in a db!?</p>
<p><strong>update</strong> <span><span>@mmd</span></span>: let us compare the lines: - see this thread - with the code:<br />
</p>
<pre><code>./osmconvert dutch-schools-results.o5m --csv=&quot;name addr:city website&quot; -o=dutch-schools-results.csv</code></pre>
<p>and see the code you mentioend - in the formerly thread</p>
<pre><code>./osmconvert restaurant_2.o5m --csv=&quot;@id @lon @lat shop name  addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=restaurant_2.csv</code></pre>
<p>comment: sure thing, this so called "restaurant" -code has an <strong>extra</strong> space - subsequently it had to fail - there were no streets no housenumbers and cities thread: <a href="https://help.openstreetmap.org/questions/32434/address-tags-in-a-very-simple-osmconvert-filter-task">https://help.openstreetmap.org/questions/32434/address-tags-in-a-very-simple-osmconvert-filter-task</a></p>
<p>so - i am not convinced - since i do not see an similar error!?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '14, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jun '14, 22:37</strong> </span></p>
</div>
</div>
<div id="comments-container-34214" class="comments-container">
<span id="34218"></span>
<div id="comment-34218" class="comment">
<div id="post-34218-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>When you don't provide addr:street in your osmconvert "--csv" string, why would you expect it to show up in your result?</p>
<p>Your --csv="name addr:city website" does not match your requirements. Please revisit some of your previous posts, you've already got that right at some point in time.</p>
<p>BTW: cross posted here: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=430746#p430746">http://forum.openstreetmap.org/viewtopic.php?pid=430746#p430746</a></p>
</div>
<div id="comment-34218-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 12:50)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="34230"></span>
<div id="comment-34230" class="comment">
<div id="post-34230-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thx for the hints - i appreciate any and all help. btw: regarding the crosspost: the other thread is an answer (!!) in a THREAD (!) - somewhat self-reliying... - this thread. so - i am sorry for this! and now i try to figure out how to solve the issues. Again thanks</p>
</div>
<div id="comment-34230-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 17:32)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34231"></span>
<div id="comment-34231" class="comment">
<div id="post-34231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i try to find the thread where i gladly was able to hit the point and was able to provide all what is needed to get the full -dataset.</p>
</div>
<div id="comment-34231-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 17:34)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34235"></span>
<div id="comment-34235" class="comment">
<div id="post-34235-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear mmd - thank your for the reply, the hints and the offered help,. At the moment i do not see the significant parts that interlink the two threads. in other words if we compare the code - you mention then we can see in the so called restaurant-request (formerly request) a space near name. but in this thread - the school-thread i cannot see such a space. Subsequently i cannot see where you find the link between the both issues. But perhaps i hae to rethink all and to look at the code again - i will come back tomorrow. Meanwhwile many thaks for all you do and did. thx</p>
</div>
<div id="comment-34235-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 22:23)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34236"></span>
<div id="comment-34236" class="comment not_top_scorer">
<div id="post-34236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>see the update in the threadstart - there i have a synopsis of both lines - the formerly written restaurant-request and the actual school-request. they are not similar. but - i think i have to look at all tomorrow. - i come back tomorrow... greetings sayhello</p>
</div>
<div id="comment-34236-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 22:25)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34237"></span>
<div id="comment-34237" class="comment">
<div id="post-34237-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You complain that your dutch-schools query never returns a street. So why don't you add "addr:street" to your --csv string, as you did for your restaurant query. It's really not that difficult, is it?</p>
</div>
<div id="comment-34237-info" class="comment-info">
<span class="comment-age">(21 Jun '14, 22:39)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="34240"></span>
<div id="comment-34240" class="comment not_top_scorer">
<div id="post-34240-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello mmd - thanks for revisiting this thread - and for your continued help. i will rework the dutch-schools-request with the renewed request-line. pps i come back and will let you know the results- have a great day. ;-)</p>
</div>
<div id="comment-34240-info" class="comment-info">
<span class="comment-age">(22 Jun '14, 07:13)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-34214" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-34214-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

