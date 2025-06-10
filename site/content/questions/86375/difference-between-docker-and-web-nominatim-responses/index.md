+++
type = "question"
title = "Difference between docker and web nominatim responses"
description = '''Hi everyone,  I installed locally nominatim via docker image, using the following docker-compose services:  nominatim:  container_name: nominatim  image: mediagis/nominatim:4.2  volumes:  - ./volumes/sources:/nominatim/sources  - nominatim-data:/var/lib/postgresql/14/main  environment:  - PBF_PATH=/...'''
date = "2022-12-22T16:15:00Z"
lastmod = "2022-12-23T11:16:00Z"
weight = 86375
keywords = [ "docker", "reversegeocoding", "nominatim" ]
aliases = [ "/questions/86375" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between docker and web nominatim responses](/questions/86375/difference-between-docker-and-web-nominatim-responses)

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
<span id="post-86375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86375-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I installed locally nominatim via docker image, using the following docker-compose</p>
<pre><code>services:
  nominatim:
    container_name: nominatim
    image: mediagis/nominatim:4.2
    volumes:
      - ./volumes/sources:/nominatim/sources
      - nominatim-data:/var/lib/postgresql/14/main
    environment:
      - PBF_PATH=/nominatim/sources/freiburg-regbez-latest.osm.pbf
      - REVERSE_ONLY=true
    ports:
      - &quot;8080:8080&quot;
    restart: always
    shm_size: 4gb</code></pre>
<p>the image is the latest available and the pbf file is fresh new.</p>
<p>I realized that the query <a href="https://nominatim.openstreetmap.org/reverse?lat=48.45851286058211&amp;lon=7.885465667596962&amp;format=json&amp;accept-language=en&amp;addressdetails=1">https://nominatim.openstreetmap.org/reverse?lat=48.45851286058211&amp;lon=7.885465667596962&amp;format=json&amp;accept-language=en</a> online shows the field "address.state" and enriches also the "display_name" with the same information, while the local one doesn't.</p>
<p>Online response:</p>
<pre><code>{
  &quot;place_id&quot;: 181685288,
  &quot;licence&quot;: &quot;Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright&quot;,
  &quot;osm_type&quot;: &quot;way&quot;,
  &quot;osm_id&quot;: 318873074,
  &quot;lat&quot;: &quot;48.45858375&quot;,
  &quot;lon&quot;: &quot;7.8852782999999995&quot;,
  &quot;display_name&quot;: &quot;12, Vogesenstraße, Schutterwald, Verwaltungsgemeinschaft Offenburg, Ortenaukreis, Baden-Württemberg, 77746, Germany&quot;,
  &quot;address&quot;: {
    &quot;house_number&quot;: &quot;12&quot;,
    &quot;road&quot;: &quot;Vogesenstraße&quot;,
    &quot;village&quot;: &quot;Schutterwald&quot;,
    &quot;municipality&quot;: &quot;Verwaltungsgemeinschaft Offenburg&quot;,
    &quot;county&quot;: &quot;Ortenaukreis&quot;,
    &quot;state&quot;: &quot;Baden-Württemberg&quot;,
    &quot;ISO3166-2-lvl4&quot;: &quot;DE-BW&quot;,
    &quot;postcode&quot;: &quot;77746&quot;,
    &quot;country&quot;: &quot;Germany&quot;,
    &quot;country_code&quot;: &quot;de&quot;
  },
  &quot;boundingbox&quot;: [
    &quot;48.4585076&quot;,
    &quot;48.4586599&quot;,
    &quot;7.8851729&quot;,
    &quot;7.8853837&quot;
  ]
}</code></pre>
<p>Local response:</p>
<pre><code>{
  &quot;place_id&quot;: 814300,
  &quot;licence&quot;: &quot;Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright&quot;,
  &quot;osm_type&quot;: &quot;way&quot;,
  &quot;osm_id&quot;: 318873074,
  &quot;lat&quot;: &quot;48.45858375&quot;,
  &quot;lon&quot;: &quot;7.8852782999999995&quot;,
  &quot;display_name&quot;: &quot;12, Vogesenstraße, Schutterwald, Verwaltungsgemeinschaft Offenburg, Ortenaukreis, 77746, Germany&quot;,
  &quot;address&quot;: {
    &quot;house_number&quot;: &quot;12&quot;,
    &quot;road&quot;: &quot;Vogesenstraße&quot;,
    &quot;village&quot;: &quot;Schutterwald&quot;,
    &quot;municipality&quot;: &quot;Verwaltungsgemeinschaft Offenburg&quot;,
    &quot;county&quot;: &quot;Ortenaukreis&quot;,
    &quot;postcode&quot;: &quot;77746&quot;,
    &quot;country&quot;: &quot;Germany&quot;,
    &quot;country_code&quot;: &quot;de&quot;
  },
  &quot;boundingbox&quot;: [
    &quot;48.4585076&quot;,
    &quot;48.4586599&quot;,
    &quot;7.8851729&quot;,
    &quot;7.8853837&quot;
  ]
}</code></pre>
<p>Does anybody know why I'm missing the "state" information locally? I double-checked on the general configuration of the docker image, but I couldn't find anything relevant related to Germany addresses.</p>
<p>Thanks for your help! Roberto</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '22, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/304b4b251431e96939ec717f352b42a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RMeloni00&#39;s gravatar image" />
<p><span>RMeloni00</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RMeloni00 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Dec '22, 16:15</strong> </span></p>
</div>
</div>
<div id="comments-container-86375" class="comments-container">
&#10;</div>
<div id="comment-tools-86375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86375-form-container" class="comment-form-container">
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

<span id="86377"></span>

<div id="answer-container-86377" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86377-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RMeloni00 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The extract you are using doesn't have the full state boundary of Baden-Würtemberg. That is why it doesn't show up in the result. Use <a href="http://download.geofabrik.de/europe/germany/baden-wuerttemberg-latest.osm.pbf">http://download.geofabrik.de/europe/germany/baden-wuerttemberg-latest.osm.pbf</a> and you should be fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '22, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-86377" class="comments-container">
<span id="86387"></span>
<div id="comment-86387" class="comment">
<div id="post-86387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi lonvia,</p>
<p>thank you very much for your answer, indeed it was that.</p>
<p>Out of curiosity, where can I find some doc to better understand how it works? I mean...that extract doesn't have the full boundary of Germany either, but the country is displayed anyway. Of course, it's the country, so that might be differently handled but still I'm curious of how it works!</p>
<p>Thanks again for your help!</p>
</div>
<div id="comment-86387-info" class="comment-info">
<span class="comment-age">(23 Dec '22, 10:18)</span> <span class="comment-user userinfo">RMeloni00</span>
</div>
</div>
<span id="86388"></span>
<div id="comment-86388" class="comment">
<div id="post-86388-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nominatim has a fallback for countries but that's all. For any other boundaries, you either need to make sure your extract covers all of it or manually add the boundaries to the extract before import. Sadly, the latter requires some level of insight into how OSM works. I can't offer a simple solution.</p>
</div>
<div id="comment-86388-info" class="comment-info">
<span class="comment-age">(23 Dec '22, 11:16)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-86377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86377-form-container" class="comment-form-container">
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

