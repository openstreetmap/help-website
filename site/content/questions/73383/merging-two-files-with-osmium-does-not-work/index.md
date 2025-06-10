+++
type = "question"
title = "[closed] Merging two files with osmium does not work"
description = '''So as adviced, I merged several files with osmium, to update the whole database together, instead of doing --append, and after I tried to import the resulting file into the database, I got this error: Processing: Node(1255048k 1457.7k/s) Way(156069k 11.50k/s) Relation(0 0.00/s)result COPY END for pl...'''
date = "2020-03-05T07:57:00Z"
lastmod = "2020-03-05T23:05:00Z"
weight = 73383
keywords = [ "osmium", "merge", "osm2pgsql", "error" ]
aliases = [ "/questions/73383" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Merging two files with osmium does not work](/questions/73383/merging-two-files-with-osmium-does-not-work)

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
<span id="post-73383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73383-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-73383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So as adviced, I merged several files with osmium, to update the whole database together, instead of doing --append, and after I tried to import the resulting file into the database, I got this error:</p>
<p>Processing: Node(1255048k 1457.7k/s) Way(156069k 11.50k/s) Relation(0 0.00/s)result COPY END for planet_osm_ways failed: ERROR: duplicate key value violates unique constraint "planet_osm_ways_pkey" DETAIL: Key (id)=(23535867) already exists. CONTEXT: COPY planet_osm_ways, line 119375 DB copy thread failed: Ending COPY mode</p>
<p>It appears that osmium can't handle overlapping nodes. The worst part of this is that I had to wait 4 hours to discover this.</p>
<p>The question is, how to merge several pbf files so that overlapping tiles are correctly handled? So that I can finally load the map?</p>
<p>AND WHY RUSSIA IN THE COMPLETE ASIA MAPS IS MISSING HALF ITS TERRITORY (THOUGH IF YOU OPOEN ASIA LISTING ALL ITS TERRITORY IS SHOWED AS BEING INCLUDED)?</p>
<p>P.S. @(6 mins ago)SK53</p>
<p>I have no doubt that there must be some magical incantation to make osmosis work. Like in all things.</p>
<p>It's just that a straightforward "osmium merge ./asia-latest.osm.pbf ./northwestern-fed-district-latest.osm.pbf ./central-fed-district-latest.osm.pbf -o merged.pbf" yielded and invalid result.</p>
<p>The whole point of question is to find somebody knowledgable enough to identify the issue. It sucks though that people got so sensitive, like it is not the internet anymore.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '20, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/7d9dea8db6c9981b45d28f28bb29f49d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kartman1&#39;s gravatar image" />
<p><span>kartman1</span><br />
<span class="score" title="38 reputation points">38</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kartman1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '20, 11:56</strong> </span></p>
</div>
</div>
<div id="comments-container-73383" class="comments-container">
<span id="73386"></span>
<div id="comment-73386" class="comment">
<div id="post-73386-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, nice minuses. Good thing you can just crap on somebody and walk away feeling smart.+ Guess you are too chicken to at least show your name.</p>
</div>
<div id="comment-73386-info" class="comment-info">
<span class="comment-age">(05 Mar '20, 09:03)</span> <span class="comment-user userinfo">kartman1</span>
</div>
</div>
<span id="73390"></span>
<div id="comment-73390" class="comment">
<div id="post-73390-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>People here are helpful but they're not going to help someone who keeps shouting and yelling. If you can ask your questions calmly and without pejorative language like "the worst part is", then you're more likely to get answers and not downvotes.</p>
</div>
<div id="comment-73390-info" class="comment-info">
<span class="comment-age">(05 Mar '20, 10:17)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="73391"></span>
<div id="comment-73391" class="comment">
<div id="post-73391-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I can only advise re-evaluating the attitude which you are expressing in your text. I think you have been hinted this before in one of your previous questions. If you like people taking their time for you and getting serious responses it does not help to shout (text in capitals), demand, use words like wtf and OMG, or make totally unrelated and accusing comments to other peoples' questions. There are a lot of folks here who are eager to help and promote the use of OSM but they are doing that for their own good and in their spare time. Stick to the rules/etiquette and you get helped.</p>
<p>And btw: nobody is hiding anything. You can see the votes in your profile.</p>
</div>
<div id="comment-73391-info" class="comment-info">
<span class="comment-age">(05 Mar '20, 10:25)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73392"></span>
<div id="comment-73392" class="comment">
<div id="post-73392-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17942/kartman1">@kartman1</a> : your general tone is not suitable for this forum. Consider that osmosis has been in use for well over a decade for this very purpose: it just might be you that are in error not the programme.</p>
</div>
<div id="comment-73392-info" class="comment-info">
<span class="comment-age">(05 Mar '20, 11:41)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="73403"></span>
<div id="comment-73403" class="comment">
<div id="post-73403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(to second what SK53 said earlier about osmosis) <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh">https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh</a> is the script that I use to load data for <a href="https://map.atownsend.org.uk/">https://map.atownsend.org.uk/</a> and similar sites. I've just tested that it doesn't have a problem by using it to load both ends of the ferry route that ends at <a href="https://www.openstreetmap.org/node/4342493001">https://www.openstreetmap.org/node/4342493001</a> together. That node is in both files, and no error occurs/</p>
</div>
<div id="comment-73403-info" class="comment-info">
<span class="comment-age">(05 Mar '20, 23:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-73383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73383-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Too subjective and argumentative" by SK53 05 Mar '20, 11:42

</div>

</div>

</div>

