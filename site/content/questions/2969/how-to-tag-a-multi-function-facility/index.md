+++
type = "question"
title = "How to tag a multi-function facility?"
description = '''How do you tag a multi-function facility? Examples of multi-use facilities include, cafes that become nightclubs, resorts that include restaurants and book stores that include coffee shops.  A detailed example is included below. I don&#x27;t know how unique this particular establishment&#x27;s concept is, but...'''
date = "2011-02-11T22:59:00Z"
lastmod = "2011-02-14T17:49:00Z"
weight = 2969
keywords = [ "multi-use", "tagging" ]
aliases = [ "/questions/2969" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a multi-function facility?](/questions/2969/how-to-tag-a-multi-function-facility)

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
<span id="post-2969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2969-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-2969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do you tag a multi-function facility? Examples of multi-use facilities include, cafes that become nightclubs, resorts that include restaurants and book stores that include coffee shops.<br />
</p>
<p>A detailed example is included below.</p>
<p>I don't know how unique this particular establishment's concept is, but I am using it to get my thoughts in order when it comes to a single physical building containing two (or more) POIs.</p>
<p>Here's the place in question: <a href="http://www.renaissanceclubsport.com/home.do">Renaissance ClubSport</a>. They bill themselves as a "contemporary boutique hotel, an impressive full-service sports club, a vibrant bar &amp; restaurant, and a rejuvenating day spa all under one roof...creating a one-of-a-kind experience." I would not worry about the spa, bar and restaurant, though they are certainly rejuvenating and vibrant, respectively. But one can belong to the sports club without staying at the hotel (I do), and one can stay at the hotel without setting a foot in the gym. Thinking from the standpoint of POIs on a map, I would like the place to show up as both a hotel and a sports club.</p>
<p>What I did for now (<a href="https://www.openstreetmap.org/?lat=33.582325&amp;lon=-117.729298&amp;zoom=18&amp;layers=M">map</a>) was split the building outline roughly where the gym (plus spa, bar and restaurant) ends and the hotel begins, even though they are under the same roof. One is tagged as a <strong>tourism</strong>=hotel with applicable hotel schema tags, the other as <strong>leisure</strong>=sports_centre with an opportunity to add other tags from the schema (have not done that yet).</p>
<p>The problem I am having with this solution is that on a map both might show up as two separate, though extremely close, POIs with the same rather longish name. That would be ugly. More likely, because they are so close, only one will show up at most scale levels - either as a result of the decision by the smart renderer, or as a result of overlap by a "dumb" renderer. Also, I had to list the same address on both objects, and that does not feel right at all.</p>
<p>There is an additional (though not as crucial) challenge of tagging the spa and the eateries. Again, from the standpoint of someone driving in the neighborhood looking for a place to eat or drink, they might want to visit the restaurant or the bar inside the hotel/club, which are open to the public.</p>
<p>I dealt with that issue by dropping three POI nodes (there is also a coffee bar) approximately where they are located inside the building. (The spa could be the fourth, although there should probably be a spa=yes key on the hotel or the sports club.)</p>
<p>And, for good measure, I added a relationship of <strong>type</strong>=site, to which I added both parts of the building and the two pools I outlined.</p>
<p>I ended up with a mixed solution of outlines and points. The Mapnik rendering looks quite intriguing, though not unreasonable. At zoom 17 it shows the icon and the name of the hotel and the outline and shading, though not the name or the icon, for the the gym. It also shows the icon and the name for the restaurant, which is fine. but it appears that all of the gym is the restaurant - confusing. At zoom=18, it also shows the icon for the coffee bar, though no name (which is fine), but no icon for the bar (and in all fairness, I did not have to add it since most restaurants can be assumed to have a bar; also, unlike the coffee bar, this bar does not have its own name).</p>
<p>All I want is to capture the data properly while keeping the needs of the renderers and POI searchers in mind. Am I way off? Is there a best practice for this sort of a situation? How would you have mapped/tagged this place?</p>
<p>One last question: what would happen - from the standpoint of data integrity and the rendered look - if I kept it as one building, but tagged it as <em>both</em> <strong>tourism</strong>=hotel and <strong>leisure</strong>=sports_centre? It's tempting, but somehow that does not feel right.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multi-use" rel="tag" title="see questions tagged &#39;multi-use&#39;">multi-use</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '11, 22:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '11, 21:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span></p>
</div>
</div>
<div id="comments-container-2969" class="comments-container">
<span id="3002"></span>
<div id="comment-3002" class="comment">
<div id="post-3002-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My first suggestion would be to find a way to ask the question using fewer words.</p>
</div>
<div id="comment-3002-info" class="comment-info">
<span class="comment-age">(13 Feb '11, 12:45)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="3010"></span>
<div id="comment-3010" class="comment">
<div id="post-3010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I asked the question in 10 words, didn't I?</p>
</div>
<div id="comment-3010-info" class="comment-info">
<span class="comment-age">(13 Feb '11, 14:58)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3015"></span>
<div id="comment-3015" class="comment">
<div id="post-3015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This could be quite a useful question, but it really is much too long to read.</p>
</div>
<div id="comment-3015-info" class="comment-info">
<span class="comment-age">(13 Feb '11, 16:41)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="3022"></span>
<div id="comment-3022" class="comment">
<div id="post-3022-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The way the question is written probably lends itself better to the forum. But the forum appears a little dead. It IS a useful question. Would it be helpful if I asked it in two lines and moved the context and the nuances to a comment? More people might read it and more people might attempt to answer it using their own assumptions. But unless they read the comment, I doubt it will lead to a useful answer. I am hoping that sooner or later someone will show up who hates unanswered questions more than reading.</p>
</div>
<div id="comment-3022-info" class="comment-info">
<span class="comment-age">(13 Feb '11, 18:53)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3023"></span>
<div id="comment-3023" class="comment">
<div id="post-3023-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd suggest you summarise the problem and the question in one paragraph (as a "tl;dr" summary), then put the rest below for people who are really interested.</p>
</div>
<div id="comment-3023-info" class="comment-info">
<span class="comment-age">(13 Feb '11, 21:06)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-2969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2969-form-container" class="comment-form-container">
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

<span id="3025"></span>

<div id="answer-container-3025" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3025-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-3025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question addresses one of the key tensions in OpenStreetMap; How much detail is Just Right. How do we know when we have mapped too little, with just enough detail, or provided too much information?<br />
</p>
<p>Typical mapping of multi-function facilities is to map the largest, or most-significant object as an area and the lesser objects as nodes. This gives us a shopping mall building with individual store nodes; enough detail to find the individual shops without the additional detail of the exact size of each suite within the shopping mall.<br />
</p>
<p>In the case of a book store that contains a coffee shop, it would be typical to map the building as shop=books and include a node within for the coffee shop, tagged amenity=cafe. It would be unusual to then subdivide the book shop into fiction, non-fiction, biography and other sections.<br />
</p>
<p>Where there are only a few objects, of similar importance one might choose to map each object as areas / buildings or each as nodes, either with or without an un-differentiated building. Consider a building that houses a grade-school and a public day care facility. It would be a matter for the mapper to choose either building with nodes or joined buildings for these features.<br />
</p>
<p>Differentiate this from an office building with a non-public day care, for families of employees only. I'd would argue that the private day care would not be included in the OSM database as a general case. Of course an OSM contributor who is also an employee might have the access and interest in mapping that extra detail even if a general audience might not be interested.<br />
</p>
<p>In the case of the resort in the original question, I would want to base any mapping decision on a site survey to understand the context of the place. Then I would be inclined to tag only the public-facing amenities. Without that local context, I'm inclined to say, tag the building as tourism=hotel, and then add a node for each public-facing amenity, like the spa, restaurant or gym. If there is no public sign for an internal amenity, I'd be inclined to leave it out.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '11, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-3025" class="comments-container">
<span id="3040"></span>
<div id="comment-3040" class="comment">
<div id="post-3040-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. It makes sense, and adding nodes for lesser objects (like a coffee shop inside of a book store) is what I would do - and have done in the case of the facility described above. As far as approaching this unique case - and it may be truly unique, so I may just make a decision and move on, rather tan trying to build any kind of knowledge base around it - the place truly is two things in one. And the sports club is the more prominent part of it. To be honest, I'm happy with the way it came out looking in Mapnik, see link above.</p>
</div>
<div id="comment-3040-info" class="comment-info">
<span class="comment-age">(14 Feb '11, 17:49)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3025-form-container" class="comment-form-container">
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

