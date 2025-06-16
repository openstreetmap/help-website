+++
type = "question"
title = "How to find cities and states using OSM overpass API?"
description = '''I want to generate the lists of states and cities (state wise cities) of Germany using overpass XAPI of OSM.  In wiki I can see this list http://en.wikipedia.org/wiki/States_of_Germany and http://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population  So according to wiki Germany has 16 state...'''
date = "2012-06-28T10:39:00Z"
lastmod = "2012-06-29T16:25:00Z"
weight = 13877
keywords = [ "openstreetmap", "overpass", "state", "cities", "xapi" ]
aliases = [ "/questions/13877" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to find cities and states using OSM overpass API?](/questions/13877/how-to-find-cities-and-states-using-osm-overpass-api)

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
<span id="post-13877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13877-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to generate the lists of states and cities (state wise cities) of Germany using overpass XAPI of OSM.</p>
<p>In wiki I can see this list <a href="http://en.wikipedia.org/wiki/States_of_Germany">http://en.wikipedia.org/wiki/States_of_Germany</a> and <a href="http://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population">http://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population</a></p>
<p>So according to wiki Germany has 16 states and 80 cities.</p>
<p>Now, to fetch the list of states in Germany I am using this query: <a href="http://www.overpass-api.de/api/xapi?node%5Bbbox=5.87,47.27,15.04,55.12%5D%5Btype=administrative%5D">http://www.overpass-api.de/api/xapi?node[bbox=5.87,47.27,15.04,55.12][type=administrative]</a></p>
<p>To fetch list of cities in Germany I am using this query: <a href="http://www.overpass-api.de/api/xapi?node%5Bbbox=5.87,47.27,15.04,55.12%5D%5Bplace=city%5D">http://www.overpass-api.de/api/xapi?node[bbox=5.87,47.27,15.04,55.12][place=city]</a></p>
<p>So from my above queries I am getting 0 states and 114 cities. Which is absolutely wrong according to wiki. Please guide me if I am writing wrong query? Or suggest me some another way to fetch the list of states and cities from OSM.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-state" rel="tag" title="see questions tagged &#39;state&#39;">state</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '12, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/b3013a84207a32bed7ddfad7004100f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi%20Kotwani&#39;s gravatar image" />
<p><span>Ravi Kotwani</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi Kotwani has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13877" class="comments-container">
&#10;</div>
<div id="comment-tools-13877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13877-form-container" class="comment-form-container">
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

<span id="13911"></span>

<div id="answer-container-13911" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13911-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The states of Germany are all modeled as relations. You can get them (and a lot more) with a call like</p>
<p><a href="http://overpass-api.de/api/interpreter?data=(rel%5Badmin_level=%224%22%5D(47,6,55,15););out;"></a><a href="http://overpass-api.de/api/interpreter?data=(rel%5Badmin_level="><code>http://overpass-api.de/api/interpreter?data=(rel[admin_level="4"](47,6,55,15););out;</code></a></p>
<p>Unfortunately, Germany doesn't fit very well into a single bounding box. For that reason you get a lot of other states into the result.</p>
<p>The cities are more difficult. There is no reliable tagging of the number of inhabitants. It is a number that changes anyway every day, and tends to g. For example, the number of cities with more than 100,000 inhabitants is now probably closer to 90 than to 80.</p>
<p>A more stable criterion are the "Kreisfreie Städte": these are cities big enough to have the administrative rank of a county. You can find them with</p>
<p><a href="http://overpass-api.de/api/interpreter?data=(rel%5Badmin_level=%226%22%5D%5B%22de:place%22=%22city%22%5D;);out;"></a><a href="http://overpass-api.de/api/interpreter?data=(rel%5Badmin_level="><code>http://overpass-api.de/api/interpreter?data=(rel[admin_level="6"]["de:place"="city"];);out;</code></a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '12, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '12, 16:26</strong> </span></p>
</div>
</div>
<div id="comments-container-13911" class="comments-container">
&#10;</div>
<div id="comment-tools-13911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13911-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13880"></span>

<div id="answer-container-13880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13880-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>About the states:<br />
- a state can be modeled in OSM by its boundaries (a way tagged with boundary=administrative + a relation of type=multipolygon (or type=boundary in other countries) + admin_level=4. Or it can be represented by a node of the state capital. You can have both which is the case for German states. See for instance the state "Baden-Wuerttemberg" <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Germany/Grenzen/Baden-Wuerttemberg">in the OSM wiki</a>, its <a href="https://www.openstreetmap.org/browse/relation/62611">relation</a> and its capital "<a href="https://www.openstreetmap.org/browse/node/1674026139">Stuttgart as a node tagged place=city + capital=4</a>". Note that the capital node belongs to the state relation with the role "admin_centre". So, check the type of objects representing features (nodes or ways or relations) and the tagging practices in OSM BEFORE you think about building a query string to Overpass_API.</p>
<p>About the cities:<br />
- the categorization of a place, between "city" or "town", can be country specific. The <a href="https://wiki.openstreetmap.org/wiki/DE:Key:place">wiki about German cities</a> suggests that places with more than 100.000 inhabitants has to be classified as "city". Then the question now is to verify if the 144 German cities in OSM are really &gt;100.000 hab. or if the wikipedia definition of a "city" is different than the OSM definition (the population threshold might be different or other criterium might be involved).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '12, 16:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '12, 16:27</strong> </span></p>
</div>
</div>
<div id="comments-container-13880" class="comments-container">
&#10;</div>
<div id="comment-tools-13880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13880-form-container" class="comment-form-container">
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

