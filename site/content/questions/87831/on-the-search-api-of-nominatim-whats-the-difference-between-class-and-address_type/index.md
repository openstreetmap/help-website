+++
type = "question"
title = "On the search API of Nominatim, what&#x27;s the difference between class and address_type"
description = '''Hi, so far, every query I did always returned the same value for the field &quot;class&quot; vs the field &quot;addresstype&quot; in the Json Response. Are they the same and for historical reason they are both present of there&#x27;s any difference I should be aware of? By the way, I&#x27;m in the process of documenting with Ope...'''
date = "2023-09-11T15:22:00Z"
lastmod = "2023-09-20T22:49:00Z"
weight = 87831
keywords = [ "api", "nominatim", "class" ]
aliases = [ "/questions/87831" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [On the search API of Nominatim, what's the difference between class and address_type](/questions/87831/on-the-search-api-of-nominatim-whats-the-difference-between-class-and-address_type)

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
<span id="post-87831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87831-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, so far, every query I did always returned the same value for the field "class" vs the field "addresstype" in the Json Response. Are they the same and for historical reason they are both present of there's any difference I should be aware of?</p>
<p>By the way, I'm in the process of documenting with OpenAPI the Nominatim endpoints, so the kind of answer I'm looking for is what I can actually put on the addresstype. For the class field I've written: "Key of the principal tag defining the object type"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-class" rel="tag" title="see questions tagged &#39;class&#39;">class</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '23, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0900332f0ef93125d5acc2bf12fbae47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattCon&#39;s gravatar image" />
<p><span>MattCon</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattCon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87831" class="comments-container">
&#10;</div>
<div id="comment-tools-87831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87831-form-container" class="comment-form-container">
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

<span id="87833"></span>

<div id="answer-container-87833" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87833-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>[edited to include information from the disucssion that followed]</p>
<p>Some fields are documented at <a href="https://nominatim.org/release-docs/latest/api/Output/">https://nominatim.org/release-docs/latest/api/Output/</a></p>
<p>For a point-of-internet like a bank, restaurant, office or an address the values of the 'class' and 'addresstype' are indeed the same. For places in the hierarchy, e.g. the village, city, county, state the 'addresstype' gets derived from the type and the rank (country=4, city=16, suburb=18 etc).</p>
<p>The logic can be found in the method 'get_label_tag' in <a href="https://github.com/osm-search/Nominatim/blob/master/nominatim/api/v1/classtypes.py">https://github.com/osm-search/Nominatim/blob/master/nominatim/api/v1/classtypes.py</a> (Python) Nominatim 3.x used PHP language so look for a 'ClassTypes.php' file. Nominatim 4.x has both Python and PHP so it depends on the server installation which language is used. If in doubt look at Python.</p>
<p>You should coordinate the effort on <a href="https://github.com/osm-search/Nominatim/issues/1697">https://github.com/osm-search/Nominatim/issues/1697</a> where two other users started in the past. Not sure why nobody finished.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '23, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '23, 22:48</strong> </span></p>
</div>
</div>
<div id="comments-container-87833" class="comments-container">
<span id="87834"></span>
<div id="comment-87834" class="comment">
<div id="post-87834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>please correct me if I'm wrong, but I don't see the address_type field neither in JSON nor in JSONv2. For the field missing I went to the database schema, but I could not find anything about address_type.</p>
</div>
<div id="comment-87834-info" class="comment-info">
<span class="comment-age">(11 Sep '23, 20:16)</span> <span class="comment-user userinfo">MattCon</span>
</div>
</div>
<span id="87835"></span>
<div id="comment-87835" class="comment">
<div id="post-87835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You wrote "value for the field "class" vs the field "addresstype" in the Json Response" Can you give an example where addresstype is returned? What version of Nominatim are you using or have you used?</p>
</div>
<div id="comment-87835-info" class="comment-info">
<span class="comment-age">(11 Sep '23, 21:02)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="87840"></span>
<div id="comment-87840" class="comment">
<div id="post-87840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please check this: curl --request GET \ --url 'https://nominatim.openstreetmap.org/?q=135%20pilkington%20avenue%2C%20birmingham&amp;format=json'</p>
</div>
<div id="comment-87840-info" class="comment-info">
<span class="comment-age">(13 Sep '23, 13:22)</span> <span class="comment-user userinfo">MattCon</span>
</div>
</div>
<span id="87841"></span>
<div id="comment-87841" class="comment">
<div id="post-87841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is the result (for other readers)</p>
<p>[ { "place_id": 272820811, "licence": "Data © OpenStreetMap contributors, ODbL 1.0. <a href="http://osm.org/copyright">http://osm.org/copyright",</a> "osm_type": "way", "osm_id": 90394480, "lat": "52.5487921", "lon": "-1.8164308339635031", "class": "building", "type": "residential", "place_rank": 30, "importance": 9.99999999995449e-06, "addresstype": "building", "name": "", "display_name": "135, Pilkington Avenue, Maney, Sutton Coldfield, Wylde Green, Birmingham, West Midlands Combined Authority, England, B72 1LH, United Kingdom", "boundingbox": [ "52.5487473", "52.5488481", "-1.8165130", "-1.8163464" ] } ]</p>
</div>
<div id="comment-87841-info" class="comment-info">
<span class="comment-age">(13 Sep '23, 13:24)</span> <span class="comment-user userinfo">MattCon</span>
</div>
</div>
<span id="87842"></span>
<div id="comment-87842" class="comment not_top_scorer">
<div id="post-87842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For a place_rank=30, e.g. shop, restaurant, bank it would indeed be the same. The logic is in get_label_tag in <a href="https://github.com/osm-search/Nominatim/blob/master/nominatim/api/v1/classtypes.py">https://github.com/osm-search/Nominatim/blob/master/nominatim/api/v1/classtypes.py</a> That's Python, Nominatim used to be written in PHP and there's a similar ClassTypes.php. nominatim.openstreetmap.org uses Python frontend, while other local installed servers might still use the PHP frontend (<a href="https://nominatim.org/2023/08/13/going-live.html).">https://nominatim.org/2023/08/13/going-live.html).</a></p>
</div>
<div id="comment-87842-info" class="comment-info">
<span class="comment-age">(13 Sep '23, 15:52)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="87843"></span>
<div id="comment-87843" class="comment not_top_scorer">
<div id="post-87843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the future you should use <a href="https://nominatim.openstreetmap.org/search?q=an-address">https://nominatim.openstreetmap.org/search?q=an-address</a> instead of <a href="https://nominatim.openstreetmap.org/?q=an-address">https://nominatim.openstreetmap.org/?q=an-address</a> The former is legacy and might be removed in the future. format=jsonv2 is also usually better than format=json</p>
</div>
<div id="comment-87843-info" class="comment-info">
<span class="comment-age">(13 Sep '23, 15:53)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="87844"></span>
<div id="comment-87844" class="comment not_top_scorer">
<div id="post-87844-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now it's clear at least where the value comes from. Not so easy to explain in the documentation, tough. Thanks for the tip on the right url to use.</p>
<p>would you mind editing your answer for the future readers?</p>
</div>
<div id="comment-87844-info" class="comment-info">
<span class="comment-age">(13 Sep '23, 16:19)</span> <span class="comment-user userinfo">MattCon</span>
</div>
</div>
<span id="87863"></span>
<div id="comment-87863" class="comment">
<div id="post-87863-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good idea since only the first 5 comments are shown by default. I edited the answer now.</p>
</div>
<div id="comment-87863-info" class="comment-info">
<span class="comment-age">(20 Sep '23, 22:49)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-87833" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-87833-form-container" class="comment-form-container">
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

