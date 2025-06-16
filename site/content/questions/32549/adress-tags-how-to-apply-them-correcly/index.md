+++
type = "question"
title = "[closed] adress tags - how to apply them correcly"
description = '''i wanted to run a osmconvert &amp;amp; filter with the following goal - to get the following tags out of the datas: addr:street addr:housenumber addr:city so i decided to do the following command ./osmconvert hamburg-latest.osm.pbf --all-to-nodes -o=hamburgrestaurants_2.o5m ./osmfilter hamburgrestaurant...'''
date = "2014-04-23T09:00:00Z"
lastmod = "2014-04-23T21:11:00Z"
weight = 32549
keywords = [ "osmconvert", "geocoding" ]
aliases = [ "/questions/32549" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] adress tags - how to apply them correcly](/questions/32549/adress-tags-how-to-apply-them-correcly)

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
<span id="post-32549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i wanted to run a osmconvert &amp; filter with the following goal - to get the following tags out of the datas:</p>
<p>addr:street addr:housenumber addr:city</p>
<p>so i decided to do the following command</p>
<pre><code>./osmconvert hamburg-latest.osm.pbf --all-to-nodes -o=hamburgrestaurants_2.o5m
./osmfilter hamburgrestaurants_2.o5m --keep=&quot;amenity=restaurant&quot; -o=restaurant_2.o5m
./osmconvert restaurant_2.o5m --csv=&quot;@id @lon @lat shop name  addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=restaurant_2.csv</code></pre>
<p>but i failed - there were no streets no housenumbers and cities. Now i decidet to use overpass-API which seems to be less complicated. Can someone advice me here to go the first step.</p>
<p>how to apply the correct adress tags for getting</p>
<ul>
<li>adress like</li>
<li>street , housnomber and .... eg. mailadress and website....</li>
</ul>
<p>update;</p>
<p>what i want to get is this following result:</p>
<pre><code>/tmp$ osmconvert my_gooddata_.o5m --csv=&quot;@id @lon @lat shop name addr:street addr:housenumber addr:city website email&quot; --csv-headline | more
@id     @lon    @lat    shop    name    addr:street     addr:housenumber        addr:city       website email
29950894        11.7415509      48.3978074              Parkcafe        Am Wörth        23      Freising        http://www.parkcafe-freising.de
32559987        11.7841034      47.8785126              Waldrestaurant Maxlmühle        Maxlmühle       2       Valley  http://www.maxlmuehle.de/
33047448        11.1863664      47.9072486              Hirschberg-Alm
34034075        11.6704030      48.1169551              Zum Goldenen Stern      Gartenstadtstraße       6       München
34072038        11.6707224      48.1093154              Franziskaner Garten     Friedenspromenade       45      München http://www.franziskanergarten.de/</code></pre>
<p>hmm i guess that i have made something wrong in the applcation of the tags!? What !?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '14, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>24 Apr '14, 15:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-32549" class="comments-container">
<span id="32552"></span>
<div id="comment-32552" class="comment">
<div id="post-32552-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>When you failed did you perhaps not see <a href="/questions/32434/address-tags-in-a-very-simple-osmconvert-filter-task/32479">this answer</a> to your previous question that said "<code>Issue: there's an extra space between "name" and "addr:street" in your osmconvert csv string</code>".</p>
</div>
<div id="comment-32552-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 10:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32586"></span>
<div id="comment-32586" class="comment">
<div id="post-32586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thx alot - guess that you hit the point - btw. see the update above, i will try out your solution - thx alaot</p>
</div>
<div id="comment-32586-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 21:11)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-32549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32549-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by SimonPoole 24 Apr '14, 15:20

</div>

</div>

</div>

