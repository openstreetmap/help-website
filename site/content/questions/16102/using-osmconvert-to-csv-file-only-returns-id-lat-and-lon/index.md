+++
type = "question"
title = "Using osmconvert to .csv file only returns id, lat, and lon."
description = '''I want to use osmconvert to .csv to put certain fields into a csv file and I want to keep the relations.  First, I want to run osmfilter to filter data to just street, city, state, lat, long where street, city, and state are all populated for each record. In other words, I don&#x27;t want a bunch of reco...'''
date = "2012-09-14T17:06:00Z"
lastmod = "2014-06-11T12:44:00Z"
weight = 16102
keywords = [ "osmconvert", "csv", "osmfilter" ]
aliases = [ "/questions/16102" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using osmconvert to .csv file only returns id, lat, and lon.](/questions/16102/using-osmconvert-to-csv-file-only-returns-id-lat-and-lon)

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
<span id="post-16102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to use osmconvert to .csv to put certain fields into a csv file and I want to keep the relations.</p>
<p>First, I want to run osmfilter to filter data to just street, city, state, lat, long where street, city, and state are all populated for each record. In other words, I don't want a bunch of records with the state populated but not the city and street.</p>
<p>I created a parameters file with the following -v</p>
<p>-keep= -keep-relations all addr:street!= addr:city!= addr:state!=</p>
<p>Then I run osmconvert like below, but I am getting records where the state is just populated. Also, I see records where the just street and city are populated. ./osmconvert planetfile.osm --csv"addr:street addr:city addr:state" --csv-headline -o=filteredfile.csv.</p>
<p>I also tried @lat and <span>@long</span> in the above statement to filter lat and long for the street as well, but then it didn't report any streets, cities or states, just lat and long.</p>
<p>So, I guess there is two questions? How do I filter the data such that all the fields I need are populated? And how do I tack on lat and long in the convert statement to get it to appear with the addresses in the csv?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '12, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a45de846d76d68849c0e70b6fd21f256?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JMB5&#39;s gravatar image" />
<p><span>JMB5</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JMB5 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16102" class="comments-container">
<span id="33387"></span>
<div id="comment-33387" class="comment">
<div id="post-33387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>many many thanxk you helped me alot</p>
</div>
<div id="comment-33387-info" class="comment-info">
<span class="comment-age">(22 May '14, 21:53)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-16102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16102-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="16246"></span>

<div id="answer-container-16246" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16246-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Jochen is right, Osmium is much more fexible if you want to do special data processing. However, what you want to accomplish can be done with <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>/<a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> too. For example:<br />
<br />
</p>
<p>$ ./osmfilter bremen.o5m --keep="addr:country= and addr:city= and addr:street=" --ignore-dependencies | ./osmconvert - --csv="@oname <span>@id</span> <span>@lon</span> @lat addr:country addr:city addr:street"<br />
<br />
node 103065646 8.7174590 53.1528516 DE Bremen Alwin-Lonke-Straße<br />
node 103075917 8.7113611 53.1501230 DE Bremen Grambker Heerstraße<br />
node 169500351 8.8907070 53.0349470 DE Bremen Europaallee<br />
node 171358853 8.8809487 53.0704234 DE Bremen Hützelstrasse<br />
node 172133861 8.8860047 53.0607349 DE Bremen Hemelinger Bahnhofstraße<br />
node 175673452 8.9541837 53.0338771 DE Achim Uphuser Heerstraße<br />
node 175675316 8.9675299 53.0574772 DE Oyten Oyterdamm<br />
...<br />
<br />
</p>
<p>I am just not sure what you mean with "keeping the relations". If you really want only relations but nothing else, you might want to filter this way:</p>
<p>$ ./osmfilter bremen.o5m --keep="" --keep-relations="addr:country= and ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '12, 23:52</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-16246" class="comments-container">
<span id="33384"></span>
<div id="comment-33384" class="comment">
<div id="post-33384-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>overwhelming - you saved my day: many many thanks for sharing your insights - great!</p>
</div>
<div id="comment-33384-info" class="comment-info">
<span class="comment-age">(22 May '14, 20:26)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="33880"></span>
<div id="comment-33880" class="comment">
<div id="post-33880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi there! could you help out? I am using your osmfilter nodes_hiAgra.osm --keep="addr:street=" --ignore-depemdencies --drop-relations --drop-ways |osmconvert - --csv="<span>@id</span> <span>@lon</span> <span>@lat</span> addr:street " and only got 1 line .... But streets are more in that area What to do? I need only id,lon,lat, street_name</p>
</div>
<div id="comment-33880-info" class="comment-info">
<span class="comment-age">(11 Jun '14, 12:44)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-16246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16246-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16137"></span>

<div id="answer-container-16137" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16137-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure I understand exactly what you want, but if you find that osmconvert doesn't do what you need, you might want to try <a href="https://wiki.openstreetmap.org/wiki/Osmium">Osmium</a>, specifically the "osmjs" utility that comes with it. Osmjs can also create CSV files and you can write small Javascript snippets to define exactly what you need, so it is rather flexible. There are examples in the "osmjs" directory in the distribution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '12, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span> </br></br></p>
</div>
</div>
<div id="comments-container-16137" class="comments-container">
<span id="33383"></span>
<div id="comment-33383" class="comment">
<div id="post-33383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear jochen many many thanks for sharing your insights - great! you helped me alot</p>
</div>
<div id="comment-33383-info" class="comment-info">
<span class="comment-age">(22 May '14, 20:25)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-16137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16137-form-container" class="comment-form-container">
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

