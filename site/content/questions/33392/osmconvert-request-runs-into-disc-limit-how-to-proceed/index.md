+++
type = "question"
title = "osmconvert - request runs into disc limit - how to proceed"
description = '''hello dear osm-experts fairly new to osm - i tried to run the following code  ./osmconvert baden-wuerttemberg-latest.osm.pbf --all-to-nodes -o=baden-wuerttembergrestaurants.o5m ./osmfilter baden-wuerttembergrestaurants.o5m --keep=&quot;amenity=restaurant&quot; -o=baden-wuerttembergrestaurants_2.o5m ./osmconve...'''
date = "2014-05-23T03:56:00Z"
lastmod = "2014-05-27T19:49:00Z"
weight = 33392
keywords = [ "osmconvert", "osm", "linux" ]
aliases = [ "/questions/33392" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osmconvert - request runs into disc limit - how to proceed](/questions/33392/osmconvert-request-runs-into-disc-limit-how-to-proceed)

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
<span id="post-33392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello dear osm-experts</p>
<p>fairly new to osm - i tried to run the following code</p>
<pre><code>./osmconvert baden-wuerttemberg-latest.osm.pbf --all-to-nodes -o=baden-wuerttembergrestaurants.o5m
./osmfilter baden-wuerttembergrestaurants.o5m --keep=&quot;amenity=restaurant&quot; -o=baden-wuerttembergrestaurants_2.o5m
./osmconvert baden-wuerttembergrestaurants_2.o5m --csv=&quot;@id @lon @lat restaurant:name addr:street addr:housenumber addr:city website email&quot; 
--csv-headline -o=badenwuerttembergrestaurant_2.csv</code></pre>
<p>the terminal gave back the following results - see the complain not enough space</p>
<pre><code>martin@linux-70ce:~&gt; cd osmosis/
martin@linux-70ce:~/osmosis&gt; ./osmconvert baden-wuerttemberg-latest.osm.pbf --all-to-nodes -o=baden-wuerttembergrestaurants.o5m
osmconvert Error: not enough space. Increase --max-objects=
martin@linux-70ce:~/osmosis&gt; ./osmfilter baden-wuerttembergrestaurants.o5m --keep=&quot;amenity=restaurant&quot; -o=baden-wuerttembergrestaurants_2.o5m
osmfilter Warning: unexpected end of input file: baden-wuerttembergrestaurants.o5m
martin@linux-70ce:~/osmosis&gt; ./osmconvert baden-wuerttembergrestaurants_2.o5m --csv=&quot;@id @lon @lat restaurant:name addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=badenwuerttembergrestaurant_2.csv
martin@linux-70ce:~/osmosis&gt; cd..
martin@linux-70ce:~&gt; mv *.osm.pbf ~/osmosis</code></pre>
<p>well what can i do - how to limit the request to get results....</p>
<p><strong>update:</strong></p>
<p>well i think i have to try out Parameter --max-objects=50000000 but i am not sure how!?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '14, 03:56</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '14, 14:01</strong> </span></p>
</div>
</div>
<div id="comments-container-33392" class="comments-container">
<span id="33396"></span>
<div id="comment-33396" class="comment">
<div id="post-33396-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Duplicated question: <a href="https://gis.stackexchange.com/questions/97767/osmconvert-gives-back-complains-about-disc-space">https://gis.stackexchange.com/questions/97767/osmconvert-gives-back-complains-about-disc-space</a></p>
</div>
<div id="comment-33396-info" class="comment-info">
<span class="comment-age">(23 May '14, 07:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33392-form-container" class="comment-form-container">
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

<span id="33397"></span>

<div id="answer-container-33397" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33397-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you try increasing max-objects <a href="http://manpages.ubuntu.com/manpages/trusty/man1/osmconvert.1.html">as suggested by the documentation</a>?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '14, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33397" class="comments-container">
<span id="33415"></span>
<div id="comment-33415" class="comment">
<div id="post-33415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>many many thanks <strong>update:</strong></p>
<p>well i think i have to try out Parameter --max-objects=50000000 but i am not sure how!?</p>
</div>
<div id="comment-33415-info" class="comment-info">
<span class="comment-age">(23 May '14, 14:01)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="33474"></span>
<div id="comment-33474" class="comment">
<div id="post-33474-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just append it to your <code>osmconvert</code> call. You already pass various other parameters.</p>
</div>
<div id="comment-33474-info" class="comment-info">
<span class="comment-age">(26 May '14, 09:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33397-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33512"></span>

<div id="answer-container-33512" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33512-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello!</p>
<p>You of course can use --max-objects parameter to increase the number of allowed objects – as suggested previously. Additional help is available via osmconvert's help function: --help</p>
<p>In my opinion, the better way in this case would be to <em>first</em> filter and <em>then</em> convert to .csv. This should work faster and there would be no need for applying any --max-objects parameter:</p>
<ul>
<li>Convert baden-wuerttemberg-latest.osm.pbf to .o5m (osmconvert)</li>
<li>Filter restaurants (osmfilter)</li>
<li>Convert to .csv (osmconvert)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '14, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-33512" class="comments-container">
&#10;</div>
<div id="comment-tools-33512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33512-form-container" class="comment-form-container">
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

